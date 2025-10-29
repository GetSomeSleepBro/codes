import os
from flask import Flask
from .config import Config
from .extensions import db

# Optional .env support for easy local configuration
try:
    from dotenv import load_dotenv  # type: ignore
except Exception:  # pragma: no cover
    def load_dotenv(*_args, **_kwargs):
        return None


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # Ensure instance folder exists for SQLite default
    try:
        os.makedirs(app.instance_path, exist_ok=True)
    except OSError:
        pass

    # Load env from .env if present
    load_dotenv()

    app.config.from_object(Config())

    # Default DB: SQLite under instance/ unless DATABASE_URL or MySQL env set
    database_url = os.getenv("DATABASE_URL")
    if database_url:
        app.config["SQLALCHEMY_DATABASE_URI"] = database_url
    else:
        dialect = os.getenv("DB_DIALECT", "sqlite").lower()
        if dialect == "mysql":
            host = os.getenv("MYSQL_HOST", "127.0.0.1")
            port = os.getenv("MYSQL_PORT", "3306")
            user = os.getenv("MYSQL_USER", "root")
            password = os.getenv("MYSQL_PASSWORD", "")
            dbname = os.getenv("MYSQL_DB", "bloodbank")
            app.config["SQLALCHEMY_DATABASE_URI"] = (
                f"mysql+pymysql://{user}:{password}@{host}:{port}/{dbname}?charset=utf8mb4"
            )
        else:
            sqlite_path = os.getenv("SQLITE_PATH") or os.path.join(app.instance_path, "bloodbank.sqlite3")
            app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{sqlite_path}"

    # Fallback to SQLite if the configured DB is unavailable
    try:
        from sqlalchemy import create_engine, text as _text
        uri = app.config.get("SQLALCHEMY_DATABASE_URI", "")
        if not uri.startswith("sqlite"):
            test_engine = create_engine(uri)
            with test_engine.connect() as conn:
                conn.execute(_text("select 1"))
    except Exception as e:
        sqlite_path = os.path.join(app.instance_path, "bloodbank.sqlite3")
        app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{sqlite_path}"
        print(f"[WARN] DB connection failed; falling back to SQLite at {sqlite_path}. Error: {e}")

    # Sensible defaults
    app.config.setdefault("SQLALCHEMY_TRACK_MODIFICATIONS", False)
    app.config.setdefault("SECRET_KEY", os.getenv("SECRET_KEY", "dev-secret-key"))

    # Init extensions
    db.init_app(app)

    # Ensure models are imported before creating tables
    from . import models  # noqa: F401

    # Create tables automatically on startup (idempotent)
    from flask import g, session, has_request_context
    from sqlalchemy import event
    with app.app_context():
        db.create_all()

        # Attach SQL listener within app context to access engine
        if not app.config.get("_SQL_LISTENER_SET") and os.getenv("DISABLE_SQL_LOG", "0") != "1":
            def _log_sql(conn, cursor, statement, parameters, context, executemany):  # noqa: ANN001
                if has_request_context():
                    try:
                        g._sql_log.append((statement, parameters))
                    except Exception:
                        pass

            event.listen(db.engine, "before_cursor_execute", _log_sql)
            app.config["_SQL_LISTENER_SET"] = True

    @app.before_request
    def _sql_log_init():
        g._sql_log = []

    @app.after_request
    def _sql_log_store(response):
        def _fmt_value(v):
            from datetime import date, datetime
            if v is None:
                return "NULL"
            if isinstance(v, (int, float)):
                return str(v)
            if isinstance(v, (date, datetime)):
                return f"'{v.isoformat()}'"
            if isinstance(v, bool):
                return '1' if v else '0'
            # Escape single quotes for SQL display
            s = str(v).replace("'", "''")
            return f"'{s}'"

        def _render_sql(stmt: str, params):
            import re
            s = str(stmt)
            try:
                # Dict param styles: %(name)s or :name
                if isinstance(params, dict) and params:
                    # pyformat: %(name)s
                    def repl_pyformat(m):
                        key = m.group(1)
                        return _fmt_value(params.get(key))
                    s_py = re.sub(r"%\((\w+)\)s", repl_pyformat, s)
                    # named: :name
                    def repl_named(m):
                        key = m.group(1)
                        return _fmt_value(params.get(key))
                    s_named = re.sub(r":(\w+)", repl_named, s_py)
                    return s_named

                # Positional param styles: ? or %s
                if isinstance(params, (list, tuple)) and params:
                    vals = list(params)
                    # First try qmark '?'
                    if '?' in s:
                        out = []
                        it = iter(vals)
                        for ch in s:
                            if ch == '?':
                                try:
                                    out.append(_fmt_value(next(it)))
                                except StopIteration:
                                    out.append('?')
                            else:
                                out.append(ch)
                        return ''.join(out)
                    # Then try %s tokens
                    def repl_s(_m, it=iter(vals)):
                        try:
                            return _fmt_value(next(it))
                        except StopIteration:
                            return '%s'
                    s = re.sub(r"%s", repl_s, s)
                    return s
            except Exception:
                return s
            return s

        try:
            if hasattr(g, "_sql_log") and g._sql_log:
                # Store only the most recent executed statement
                stmt, params = g._sql_log[-1]
                session["last_sql"] = _render_sql(stmt, params)
        except Exception:
            pass
        return response

    @app.context_processor
    def inject_sql_log():
        return {"sql_recent": (session.get("last_sql") or "").strip()}

    # Register blueprints
    from .routes.main import bp as main_bp
    from .routes.donors import bp as donors_bp
    from .routes.donations import bp as donations_bp
    from .routes.inventory import bp as inventory_bp
    from .routes.requests import bp as requests_bp
    from .routes.settings import bp as settings_bp
    from .routes.sql_console import bp as sql_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(donors_bp, url_prefix="/donors")
    app.register_blueprint(donations_bp, url_prefix="/donations")
    app.register_blueprint(inventory_bp, url_prefix="/inventory")
    app.register_blueprint(requests_bp, url_prefix="/requests")
    app.register_blueprint(settings_bp, url_prefix="/settings")
    app.register_blueprint(sql_bp, url_prefix="/sql")

    # CLI commands
    @app.cli.command("init-db")
    def init_db_cmd():
        from .models import Donor, Donation, InventoryUnit, Hospital, Request, Issue  # noqa
        with app.app_context():
            db.create_all()
        print("Initialized the database.")

    @app.cli.command("seed-demo")
    def seed_demo_cmd():
        from datetime import date, timedelta
        from .models import Donor, Donation, InventoryUnit, Hospital
        with app.app_context():
            if not Donor.query.first():
                donors = [
                    Donor(name="Alice", blood_group="A", rh="+"),
                    Donor(name="Bob", blood_group="O", rh="-"),
                    Donor(name="Chitra", blood_group="B", rh="+"),
                    Donor(name="Dev", blood_group="AB", rh="-"),
                ]
                db.session.add_all(donors)
                db.session.commit()

            if not Hospital.query.first():
                db.session.add(Hospital(name="City Hospital", contact="city@example.com"))
                db.session.commit()

            if not Donation.query.first():
                # create some passed donations with inventory
                for donor in Donor.query.all():
                    d = Donation(donor_id=donor.id, date=date.today() - timedelta(days=3), volume_ml=450, test_status="passed")
                    db.session.add(d)
                    db.session.flush()
                    inv = InventoryUnit(
                        donation_id=d.id,
                        blood_group=donor.blood_group,
                        rh=donor.rh,
                        volume_ml=450,
                        expiry_date=date.today() + timedelta(days=39),
                        status="available",
                    )
                    db.session.add(inv)
                db.session.commit()
        print("Seeded demo data.")

    return app

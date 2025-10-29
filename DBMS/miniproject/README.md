# Blood Bank Mini-Project (Flask + SQLAlchemy)

A minimalist Blood Bank management web app that demonstrates core DBMS concepts with a simple, clean UI. The app supports either MySQL or SQLite for quick setup.

## Features (MVP)
- Donor management: Add/list donors with blood type and Rh.
- Donation intake: Record donations, lab test status; auto-add inventory for passed tests.
- Inventory: Per-unit stock with expiry; FEFO used for allocation; auto-mark expired on view.
- Requests: Create hospital requests and allocate compatible units using ABO/Rh compatibility rules.

## Tech
- Backend: Python 3, Flask, SQLAlchemy
- DB: MySQL or SQLite
- No heavy front-end; plain server-rendered templates + minimal CSS

## Run Locally
1) Create a virtual environment and install deps
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2) Choose your database
- Easiest: SQLite (default). No env vars needed.
- MySQL: set env vars or `DATABASE_URL`.

Options:
- Use `DATABASE_URL` directly, e.g. `export DATABASE_URL='mysql+pymysql://user:pass@127.0.0.1:3306/bloodbank?charset=utf8mb4'`
- Or set by parts (driver defaults to PyMySQL):
```
export DB_DIALECT=mysql
export MYSQL_HOST=127.0.0.1
export MYSQL_PORT=3306
export MYSQL_USER=root
export MYSQL_PASSWORD=yourpass
export MYSQL_DB=bloodbank
```
- For SQLite custom path: `export SQLITE_PATH=/absolute/path/to/bloodbank.sqlite3`

3) Initialize the database
```
flask --app run.py init-db
flask --app run.py seed-demo   # optional demo data
```

4) Run the server
```
python run.py
```
Visit http://127.0.0.1:5000

## Key Entities
- Donor(id, name, blood_group[A/B/AB/O], rh[+/-])
- Donation(id, donor_id, date, volume_ml, test_status[pending/passed/failed])
- InventoryUnit(id, donation_id, blood_group, rh, volume_ml, expiry_date, status[available/issued/expired])
- Hospital(id, name, contact)
- Request(id, hospital_id, blood_group, rh, units_needed, status[open/partial/fulfilled/cancelled], created_at)
- Issue(id, request_id, inventory_unit_id, issue_date)

## Allocation Logic (Simple, Safe Defaults)
- ABO/Rh compatibility for RBC transfusion with prioritized choices (same type first).
- Filters out expired units and chooses earliest-expiring units first (FEFO).
- Updates request status: `fulfilled` when enough units issued, else `partial` or remains `open`.

## Minimal SDLC Artifacts (for your report)
- SRS: Problem scope, users (technician, requester), functional requirements (CRUD, allocation), non-functional (simplicity, data integrity), constraints.
- Design: ER diagram for entities above; relational schema in 3NF; simple sequence for request allocation.
- Implementation: Framework choice, configuration for DB swapping, key modules.
- Testing: Manual cases (valid/invalid donor, passed vs failed donation, allocation for each recipient type, expiry filtering); optional Postman collection.
- Conclusion: What works, limits (single-center, no appointments), and possible extensions.

## Notes
- Default SQLite DB file path: `instance/bloodbank.sqlite3` (auto-created).
- If using MySQL, ensure the database exists and user has privileges.
- Keep scope small to avoid errors: single center, simple RBC logic, no transfusion reactions tracking.


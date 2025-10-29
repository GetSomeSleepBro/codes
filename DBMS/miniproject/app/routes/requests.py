from datetime import date
from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..extensions import db
from ..models import Hospital, Request as Req, InventoryUnit, Issue
from ..compatibility import compatible_donors


bp = Blueprint("requests", __name__)


@bp.route("/")
def list_requests():
    requests_ = Req.query.order_by(Req.id.desc()).all()
    hospitals = {h.id: h for h in Hospital.query.all()}
    return render_template("requests_list.html", requests=requests_, hospitals=hospitals)


@bp.route("/new", methods=["GET", "POST"])
def new_request():
    hospitals = Hospital.query.order_by(Hospital.name.asc()).all()
    if request.method == "POST":
        hospital_name = request.form.get("hospital_name", "").strip()
        hospital_id = request.form.get("hospital_id")
        blood_group = request.form.get("blood_group", "").upper()
        rh = request.form.get("rh", "")
        units_needed = int(request.form.get("units_needed", 1))
        next_url = request.form.get("next") or request.args.get("next")

        if hospital_id:
            hospital = Hospital.query.get(int(hospital_id))
        elif hospital_name:
            hospital = Hospital(name=hospital_name)
            db.session.add(hospital)
            db.session.flush()
        else:
            hospital = None

        if not hospital or blood_group not in {"A", "B", "AB", "O"} or rh not in {"+", "-"}:
            flash("Please provide valid request details.")
        else:
            req_ = Req(hospital_id=hospital.id, blood_group=blood_group, rh=rh, units_needed=units_needed, status="open", created_at=date.today())
            db.session.add(req_)
            db.session.commit()
            return redirect(next_url or url_for("requests.view_request", request_id=req_.id))
    return render_template("request_form.html", hospitals=hospitals)


@bp.route("/<int:request_id>")
def view_request(request_id):
    req_ = Req.query.get_or_404(request_id)
    issues = Issue.query.filter_by(request_id=req_.id).all()
    return render_template("request_detail.html", req=req_, issues=issues)


@bp.route("/<int:request_id>/allocate", methods=["POST"])
def allocate_request(request_id):
    req_ = Req.query.get_or_404(request_id)
    next_url = request.form.get("next") or request.args.get("next")
    if req_.status == "fulfilled":
        flash("Request already fulfilled.")
        return redirect(next_url or url_for("requests.view_request", request_id=req_.id))

    needed = req_.units_needed - Issue.query.filter_by(request_id=req_.id).count()
    if needed <= 0:
        req_.status = "fulfilled"
        db.session.commit()
        flash("Request fulfilled.")
        return redirect(url_for("requests.view_request", request_id=req_.id))

    compat = compatible_donors(req_.blood_group, req_.rh)
    allocated = 0
    today = date.today()

    for bg, rh in compat:
        if allocated >= needed:
            break
        q = (
            InventoryUnit.query
            .filter_by(blood_group=bg, rh=rh, status="available")
            .filter(InventoryUnit.expiry_date >= today)
            .order_by(InventoryUnit.expiry_date.asc())
        )
        for unit in q.limit(needed - allocated).all():
            unit.status = "issued"
            db.session.add(Issue(request_id=req_.id, inventory_unit_id=unit.id, issue_date=today))
            allocated += 1
            if allocated >= needed:
                break

    if allocated == 0:
        flash("No compatible units available.")
    else:
        current_total = Issue.query.filter_by(request_id=req_.id).count()
        if current_total >= req_.units_needed:
            req_.status = "fulfilled"
        else:
            req_.status = "partial"
        flash(f"Allocated {allocated} unit(s).")

    db.session.commit()
    return redirect(next_url or url_for("requests.view_request", request_id=req_.id))

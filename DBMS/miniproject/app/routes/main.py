from datetime import date
from flask import Blueprint, render_template
from ..models import Donor, Donation, InventoryUnit, Request, Hospital


bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    # Update expired units
    today = date.today()
    expired = InventoryUnit.query.filter(InventoryUnit.expiry_date < today, InventoryUnit.status == "available").all()
    for item in expired:
        item.status = "expired"
    if expired:
        from ..extensions import db
        db.session.commit()

    donors = Donor.query.order_by(Donor.name.asc()).all()
    donations = Donation.query.order_by(Donation.date.desc()).limit(50).all()
    inventory = InventoryUnit.query.order_by(InventoryUnit.expiry_date.asc()).all()
    requests = Request.query.order_by(Request.id.desc()).all()
    hospitals = Hospital.query.order_by(Hospital.name.asc()).all()

    metrics = {
        "donors_count": len(donors),
        "donations_count": Donation.query.count(),
        "available_units": InventoryUnit.query.filter_by(status="available").count(),
        "open_requests": Request.query.filter(Request.status != "fulfilled").count(),
    }

    donors_map = {d.id: d for d in donors}

    # For each request, compute compatible available units
    from ..compatibility import compatible_donors
    compat_available = {}
    for r in requests:
        total = 0
        for bg, rh in compatible_donors(r.blood_group, r.rh):
            total += (
                InventoryUnit.query
                .filter_by(blood_group=bg, rh=rh, status="available")
                .filter(InventoryUnit.expiry_date >= today)
                .count()
            )
        compat_available[r.id] = total

    return render_template(
        "dashboard.html",
        metrics=metrics,
        donors=donors,
        donations=donations,
        donors_map=donors_map,
        inventory=inventory,
        requests=requests,
        hospitals=hospitals,
        compat_available=compat_available,
    )

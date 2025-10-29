from datetime import timedelta, date
from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..extensions import db
from ..models import Donor, Donation, InventoryUnit


bp = Blueprint("donations", __name__)


@bp.route("/")
def list_donations():
    donations = Donation.query.order_by(Donation.date.desc()).all()
    donors = {d.id: d for d in Donor.query.all()}
    return render_template("donations_list.html", donations=donations, donors=donors)


@bp.route("/new", methods=["GET", "POST"])
def new_donation():
    donors = Donor.query.order_by(Donor.name.asc()).all()
    if not donors:
        flash("Create a donor first.")
    if request.method == "POST":
        donor_id = request.form.get("donor_id")
        date_str = request.form.get("date")
        volume_ml = int(request.form.get("volume_ml", 450))
        test_status = request.form.get("test_status", "pending")
        next_url = request.form.get("next") or request.args.get("next")
        if not donor_id:
            flash("Select a donor.")
        else:
            d_date = date.fromisoformat(date_str) if date_str else date.today()
            donation = Donation(donor_id=int(donor_id), date=d_date, volume_ml=volume_ml, test_status=test_status)
            db.session.add(donation)
            db.session.flush()

            if test_status == "passed":
                donor = Donor.query.get(int(donor_id))
                expiry = d_date + timedelta(days=42)
                unit = InventoryUnit(
                    donation_id=donation.id,
                    blood_group=donor.blood_group,
                    rh=donor.rh,
                    volume_ml=volume_ml,
                    expiry_date=expiry,
                    status="available",
                )
                db.session.add(unit)

            db.session.commit()
            return redirect(next_url or url_for("donations.list_donations"))
    return render_template("donation_form.html", donors=donors)


@bp.route("/<int:donation_id>/update_status", methods=["POST"])
def update_donation_status(donation_id: int):
    next_url = request.form.get("next") or request.args.get("next")
    new_status = (request.form.get("test_status") or "").strip().lower()
    if new_status not in {"pending", "passed", "failed"}:
        flash("Invalid status.")
        return redirect(next_url or url_for("donations.list_donations"))

    donation = Donation.query.get_or_404(donation_id)
    old_status = donation.test_status
    donation.test_status = new_status

    units = InventoryUnit.query.filter_by(donation_id=donation.id).all()

    if new_status == "passed":
        # If no unit exists for this donation, create one
        if not units:
            donor = Donor.query.get(donation.donor_id)
            expiry = donation.date + timedelta(days=42)
            unit = InventoryUnit(
                donation_id=donation.id,
                blood_group=donor.blood_group,
                rh=donor.rh,
                volume_ml=donation.volume_ml,
                expiry_date=expiry,
                status="available",
            )
            db.session.add(unit)
    else:
        # Pending/failed: expire any unissued unit(s) from this donation
        for u in units:
            if u.status in ("available", "reserved"):
                u.status = "expired"

    db.session.commit()
    if old_status != new_status:
        flash(f"Donation status updated: {old_status} → {new_status}")
    return redirect(next_url or url_for("donations.list_donations"))

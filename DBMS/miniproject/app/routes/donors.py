from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..extensions import db
from ..models import Donor


bp = Blueprint("donors", __name__)


@bp.route("/")
def list_donors():
    donors = Donor.query.order_by(Donor.name.asc()).all()
    return render_template("donors_list.html", donors=donors)


@bp.route("/new", methods=["GET", "POST"])
def new_donor():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        blood_group = request.form.get("blood_group", "").upper()
        rh = request.form.get("rh", "")
        next_url = request.form.get("next") or request.args.get("next")
        if not name or blood_group not in {"A", "B", "AB", "O"} or rh not in {"+", "-"}:
            flash("Please provide valid donor details.")
        else:
            donor = Donor(name=name, blood_group=blood_group, rh=rh)
            db.session.add(donor)
            db.session.commit()
            return redirect(next_url or url_for("donors.list_donors"))
    return render_template("donor_form.html")


@bp.route("/<int:donor_id>/delete", methods=["POST"])
def delete_donor(donor_id):
    donor = Donor.query.get_or_404(donor_id)
    db.session.delete(donor)
    db.session.commit()
    next_url = request.form.get("next") or request.args.get("next")
    return redirect(next_url or url_for("donors.list_donors"))

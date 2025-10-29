from datetime import date
from flask import Blueprint, render_template
from ..extensions import db
from ..models import InventoryUnit


bp = Blueprint("inventory", __name__)


@bp.route("/")
def list_inventory():
    # Mark expired items on the fly
    today = date.today()
    expired = InventoryUnit.query.filter(InventoryUnit.expiry_date < today, InventoryUnit.status == "available").all()
    for item in expired:
        item.status = "expired"
    if expired:
        db.session.commit()

    items = InventoryUnit.query.order_by(InventoryUnit.expiry_date.asc()).all()
    return render_template("inventory_list.html", items=items)


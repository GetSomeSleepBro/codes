from datetime import date
from .extensions import db


class Donor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    blood_group = db.Column(db.String(2), nullable=False)  # A, B, AB, O
    rh = db.Column(db.String(1), nullable=False)  # + or -
    last_donation_date = db.Column(db.Date, nullable=True)

    donations = db.relationship("Donation", backref="donor", lazy=True)

    def __repr__(self):
        return f"<Donor {self.name} {self.blood_group}{self.rh}>"


class Donation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    donor_id = db.Column(db.Integer, db.ForeignKey("donor.id"), nullable=False)
    date = db.Column(db.Date, nullable=False, default=date.today)
    volume_ml = db.Column(db.Integer, nullable=False, default=450)
    test_status = db.Column(db.String(20), nullable=False, default="pending")  # pending/passed/failed

    inventory_units = db.relationship("InventoryUnit", backref="donation", lazy=True)


class InventoryUnit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    donation_id = db.Column(db.Integer, db.ForeignKey("donation.id"), nullable=False)
    blood_group = db.Column(db.String(2), nullable=False)
    rh = db.Column(db.String(1), nullable=False)
    volume_ml = db.Column(db.Integer, nullable=False, default=450)
    expiry_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(20), nullable=False, default="available")  # available/issued/expired/reserved


class Hospital(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    contact = db.Column(db.String(200), nullable=True)

    requests = db.relationship("Request", backref="hospital", lazy=True)


class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hospital_id = db.Column(db.Integer, db.ForeignKey("hospital.id"), nullable=False)
    blood_group = db.Column(db.String(2), nullable=False)
    rh = db.Column(db.String(1), nullable=False)
    units_needed = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), nullable=False, default="open")  # open/partial/fulfilled/cancelled
    created_at = db.Column(db.Date, nullable=False, default=date.today)

    issues = db.relationship("Issue", backref="request", lazy=True)


class Issue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    request_id = db.Column(db.Integer, db.ForeignKey("request.id"), nullable=False)
    inventory_unit_id = db.Column(db.Integer, db.ForeignKey("inventory_unit.id"), nullable=False)
    issue_date = db.Column(db.Date, nullable=False, default=date.today)

    inventory_unit = db.relationship("InventoryUnit", backref="issues")


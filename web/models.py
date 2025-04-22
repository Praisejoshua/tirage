from web import db

class Triage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, nullable=False)
    heart_rate = db.Column(db.Float, nullable=False)
    respiratory_rate = db.Column(db.Float, nullable=False)
    temperature = db.Column(db.Float, nullable=False)
    blood_pressure = db.Column(db.String(50), nullable=False)
    oxygen_saturation = db.Column(db.Float, nullable=False)
    symptom = db.Column(db.String(255), nullable=False)
    pre_existing_conditions = db.Column(db.String(255), nullable=True)
    triage_level = db.Column(db.String(50), nullable=False)

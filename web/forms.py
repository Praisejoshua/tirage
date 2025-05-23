from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, FloatField
from wtforms.validators import DataRequired

class TriageForm(FlaskForm):
    age = IntegerField("Age", validators=[DataRequired()])
    heart_rate = IntegerField("Heart Rate", validators=[DataRequired()])
    respiratory_rate = IntegerField("Respiratory Rate", validators=[DataRequired()])
    temperature = FloatField("Temperature (°C)", validators=[DataRequired()])
    blood_pressure = StringField("Blood Pressure", validators=[DataRequired()])
    oxygen_saturation = IntegerField("Oxygen Saturation (%)", validators=[DataRequired()])
    symptom = StringField("Symptom", validators=[DataRequired()], render_kw={"placeholder": "Confusion, Fever, etc."})
    pre_existing_condition = StringField("Pre-Existing Condition", validators=[DataRequired()], render_kw={"placeholder": "Diabetes, Hypertension, etc."})

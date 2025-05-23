# app.py or routes.py

from flask import render_template, Blueprint, request
import joblib
import pandas as pd
from web.forms import TriageForm
from web.models import Triage, db  # Import the Triage model and db object
from web import app

# Load the pre-trained model
model = joblib.load("web/triage_model_with_encoding3.joblib")
print("Loaded model type:", type(model))

# Route to the homepage
@app.route("/", methods=["GET", "POST"])
def index():
    form = TriageForm()

    if form.validate_on_submit():
        # Get user input from the form
        age = form.age.data
        heart_rate = form.heart_rate.data
        respiratory_rate = form.respiratory_rate.data
        temperature = form.temperature.data
        blood_pressure = form.blood_pressure.data
        oxygen_saturation = form.oxygen_saturation.data
        symptom = form.symptom.data
        pre_existing_condition = form.pre_existing_condition.data

        # Prepare input for prediction
        user_data = pd.DataFrame({
            "Age": [age],
            "Heart_Rate": [heart_rate],
            "Respiratory_Rate": [respiratory_rate],
            "Temperature": [temperature],
            "Blood_Pressure": [blood_pressure],
            "Oxygen_Saturation": [oxygen_saturation],
            "Symptom": [symptom],
            "Pre_Existing_Conditions": [pre_existing_condition]
        })

        # Predict using the model
        prediction = model.predict(user_data)[0]

        # Map the prediction to a color
        if prediction == "Red":
            color = "red"
            action = "Seek emergency care immediately!"
            first_aid_steps = "Apply first aid as appropriate and call emergency services."
            care_recommendation = "Immediate care is needed at the nearest emergency department."
        elif prediction == "Yellow":
            color = "yellow"
            action = "Urgent, but not life-threatening. Visit the hospital soon."
            first_aid_steps = "Monitor the condition and apply necessary first aid. Seek medical help as soon as possible."
            care_recommendation = "Visit the hospital within a few hours."
        else:
            color = "green"
            action = "Low urgency. You can wait to visit the clinic."
            first_aid_steps = "Monitor symptoms and rest. Consult a doctor if symptoms persist."
            care_recommendation = "You can wait for a few days to visit a primary care doctor."

        # Save the triage data into the database
        new_triage = Triage(
            age=age,
            heart_rate=heart_rate,
            respiratory_rate=respiratory_rate,
            temperature=temperature,
            blood_pressure=blood_pressure,
            oxygen_saturation=oxygen_saturation,
            symptom=symptom,
            pre_existing_conditions=pre_existing_condition,
            triage_level=prediction
        )
        db.session.add(new_triage)
        db.session.commit()

        # Render the results along with first aid steps and care recommendation
        return render_template("index.html", form=form, color=color, action=action, prediction=prediction, first_aid_steps=first_aid_steps, care_recommendation=care_recommendation)

    return render_template("index.html", form=form, color=None)

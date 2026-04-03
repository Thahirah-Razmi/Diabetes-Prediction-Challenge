from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

model = joblib.load("diapredict_model.pkl")

drop_cols = ['id', 'diagnosed_diabetes']

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    probability = None

    if request.method == "POST":
        input_data = request.form.to_dict()

        yes_no_cols = ['family_history_diabetes', 'hypertension_history', 'cardiovascular_history']
        for col in yes_no_cols:
            input_data[col] = 1 if input_data[col].lower() == 'yes' else 0

        numeric_cols = [
            'age', 'alcohol_consumption_per_week', 'physical_activity_minutes_per_week',
            'diet_score', 'sleep_hours_per_day', 'screen_time_hours_per_day', 'bmi',
            'waist_to_hip_ratio', 'systolic_bp', 'diastolic_bp', 'heart_rate',
            'cholesterol_total', 'hdl_cholesterol', 'ldl_cholesterol', 'triglycerides',
            'family_history_diabetes', 'hypertension_history', 'cardiovascular_history'
        ]
        for col in numeric_cols:
            input_data[col] = float(input_data[col])

        input_df = pd.DataFrame([input_data])

        input_df = input_df.drop(columns=[col for col in drop_cols if col in input_df.columns], errors='ignore')

        prob = model.predict_proba(input_df)[0][1]
        prediction = "Diabetic" if prob >= 0.5 else "Non-Diabetic"
        probability = round(prob * 100, 2)

    return render_template("index.html", prediction=prediction, probability=probability)

if __name__ == "__main__":
    app.run(debug=True)
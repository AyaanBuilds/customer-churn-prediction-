from flask import Flask, render_template, request, jsonify
import os 
import pandas as pd
import pickle 

app = Flask(__name__)


MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "model", "churn_model.pkl")

with open(MODEL_PATH, "rb") as f:
    pipeline = pickle.load(f)



@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        if request.is_json:
            input_data = request.get_json()
        else:
            input_data = request.form.to_dict()

        df = pd.DataFrame([input_data])

        numeric_cols = ["tenure", "MonthlyCharges", "TotalCharges", "SeniorCitizen"]
        for col in numeric_cols:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors="coerce")

        print("DEBUG - Input DataFrame:")
        print(df)
        print("DEBUG - dtypes:")
        print(df.dtypes)
        print("DEBUG - NaN check:")
        print(df.isna().sum())

        prediction = pipeline.predict(df)[0]
        probability = pipeline.predict_proba(df)[0][1]

        print("DEBUG - Raw prediction:", prediction)
        print("DEBUG - Raw probability:", probability)

        result = {
            "prediction": "Yes" if prediction == 1 or prediction == "Yes" else "No",
            "churn_probability": round(float(probability), 4) if not pd.isna(probability) else None
        }

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)



        


   
import warnings
warnings.filterwarnings("ignore")

from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load model
with open("MLR_model_mini_project.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        def get_val(name):
            val = request.form.get(name)
            return float(val) if val not in ["", None] else 0.0

        # 🔥 EXACT SAME ORDER AS MODEL TRAINING (17 FEATURES)
        features = [
            get_val("bedrooms"),
            get_val("bathrooms"),
            get_val("sqft_living"),
            get_val("sqft_lot"),
            get_val("floors"),
            get_val("waterfront"),
            get_val("view"),
            get_val("condition"),
            get_val("sqft_above"),
            get_val("sqft_basement"),
            get_val("yr_built"),
            get_val("yr_renovated"),
            get_val("city"),
            get_val("country"),
            get_val("year"),
            get_val("month"),
            get_val("day"),
        ]

        final_features = np.array(features).reshape(1, -1)
        prediction = model.predict(final_features)[0]

        return render_template(
            "index.html",
            prediction_text=f"₹ {prediction:,.2f}"
        )

    except Exception as e:
        print("ERROR:", e)
        return render_template(
            "index.html",
            prediction_text="Prediction failed – check inputs"
        )

if __name__ == "__main__":
    app.run(debug=True)

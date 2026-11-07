from flask import Flask, request, render_template
from flask_cors import CORS

import bz2
import pickle
import numpy as np


app = Flask(__name__)
CORS(app)

app.config["DEBUG"] = True


# Cargar el escalador
with bz2.BZ2File("Model/standardScalar.pkl", "rb") as scalar_file:
    scaler = pickle.load(scalar_file)


# Cargar el modelo
with bz2.BZ2File("Model/modelForPrediction.pkl", "rb") as model_file:
    model = pickle.load(model_file)


@app.route("/")
def index():
    return render_template("home.html")


@app.route("/predictdata", methods=["GET", "POST"])
def predict_datapoint():
    if request.method == "GET":
        return render_template("home.html")

    try:
        pregnancies = int(request.form.get("Pregnancies"))
        glucose = float(request.form.get("Glucose"))
        blood_pressure = float(
            request.form.get("BloodPressure")
        )
        skin_thickness = float(
            request.form.get("SkinThickness")
        )
        insulin = float(request.form.get("Insulin"))
        bmi = float(request.form.get("BMI"))
        diabetes_pedigree = float(
            request.form.get("DiabetesPedigreeFunction")
        )
        age = float(request.form.get("Age"))

        input_data = np.array([[
            pregnancies,
            glucose,
            blood_pressure,
            skin_thickness,
            insulin,
            bmi,
            diabetes_pedigree,
            age
        ]])

        scaled_data = scaler.transform(input_data)
        prediction = model.predict(scaled_data)[0]

        if int(prediction) == 1:
            result = "Diabetic"
        else:
            result = "Non-Diabetic"

        return render_template(
            "single_prediction.html",
            result=result
        )

    except (TypeError, ValueError) as error:
        return render_template(
            "home.html",
            error=f"Datos inválidos: {error}"
        )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
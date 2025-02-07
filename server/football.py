from flask import Flask, render_template, request
import pickle
import numpy as np

try:
    with open("xgboost_model.pkl", "rb") as file:
        model = pickle.load(file)
        print("Model loaded successfully!")
except FileNotFoundError:
    print("Error: Model file 'xgboost_model.pkl' not found.")
    model = None
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

app = Flask(__name__)

# Root route
@app.route("/", methods=["GET"])
def root():
    return render_template("index.html", background_image="background.jpg")

# Prediction route
@app.route("/predict", methods=["POST"])
def predict_value():
    if model is None:
        return "Model is not available. Please check server logs."

    try:
        position_mapping = {
            "CAM": 0, "CB": 1, "CDM": 2, "CF": 3, "CM": 4, "GK": 5, "LB": 6,
            "LM": 7, "LW": 8, "LWB": 9, "RB": 10, "RM": 11, "RW": 12, "RWB": 13, "ST": 14
        }

        inputs = [
            float(request.form.get("release_clause", 0)) * 1000,  # Convert to €
            int(request.form.get("intl_reputation", 0)),
            float(request.form.get("overall_rating", 0)),
            float(request.form.get("potential", 0)),
            int(request.form.get("playstyles", 0)),
            float(request.form.get("total_stats", 0)),
            float(request.form.get("age", 0)),
            int(request.form.get("year", 0)),
            float(request.form.get("weight", 0)),  # in kg
            int(request.form.get("height", 0)),  # in cm
            position_mapping.get(request.form.get("position", ""), 0),  # Default to "CAM" if invalid
        ]

        input_array = np.array([inputs])

        predicted_value = model.predict(input_array)[0]

        return render_template(
            "output.html",
            predicted_value=f"{predicted_value:,.2f}",
            background_image="background.jpg"
        )
    except ValueError:
        return "Invalid input. Please enter numeric values only."
    except Exception as e:
        return f"An error occurred during prediction: {e}"


# Run the server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

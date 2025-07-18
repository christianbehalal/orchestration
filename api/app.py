from flask import Flask, request, jsonify
import pandas as pd
import mlflow.sklearn

app = Flask(__name__)

# Chemin absolu vers ton modèle MLflow
MODEL_URI = r"C:\Users\utilisateur\Pycharm\orchestration_projet\titanic-pipeline\mlruns\0\models\m-1d2aa83163cc4634982f2575c572f4cd\artifacts"

# Chargement du modèle
model = mlflow.sklearn.load_model(MODEL_URI)

@app.route("/")
def health():
    return "✅ API Titanic en ligne"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        input_data = request.get_json()
        df = pd.DataFrame([input_data])
        prediction = model.predict(df)
        return jsonify({"prediction": int(prediction[0])})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)

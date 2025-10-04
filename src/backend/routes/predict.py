import joblib
import os

from backend.schemas import PredictionRequest, CITY_MAPPING

# Load trained model (update path if needed)
MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "models", "model.pkl")

try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    print(f"⚠️ Model not found: {e}")
    model = None


def predict_price(request: PredictionRequest):
    """Predict house price based on input features."""
    if model is None:
        raise ValueError("Model is not loaded. Ensure 'model.pkl' exists.")

    # Convert city name to corresponding ID
    city_id = CITY_MAPPING.get(request.city, 0)  # Default to 0 if not found

    features = [
        request.surface,
        city_id,  # Use city ID instead of name
        request.rooms,
        request.bathrooms,
        request.parking,
        request.pool,
        request.vue_panoramique,
        request.jardin,
        request.climatisation,
        request.chauffage_central,
        request.ascenseur,
    ]

    prediction = model.predict([features])[0]
    return round(prediction, 2)

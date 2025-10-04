from fastapi import FastAPI
from backend.routes.predict import predict_price
from backend.schemas import PredictionRequest, PredictionResponse

app = FastAPI(title="🏡 House Price Prediction API")


@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    """
    Predicts the house price based on input features.
    """
    price = predict_price(request)
    return {"predicted_price": price}


@app.get("/")
def home():
    return {"message": "Welcome to the House Price Prediction API!"}

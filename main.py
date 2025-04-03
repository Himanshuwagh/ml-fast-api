from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import numpy as np

# --------------------------
# Load the pre-trained model
# --------------------------
MODEL_PATH = "simple_model.pkl"

try:
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
except FileNotFoundError:
    raise RuntimeError(f"Model file not found at '{MODEL_PATH}'.")

# --------------------------
# Initialize the FastAPI app
# --------------------------
app = FastAPI(title="Simple Prediction API", description="A FastAPI service that returns model predictions for a numeric input.")

# --------------------------
# Define input data schema
# --------------------------
class InputData(BaseModel):
    x: float

# --------------------------
# Root endpoint
# --------------------------
@app.get("/", tags=["Health"])
def read_root() -> dict:
    """
    Health check endpoint.
    """
    return {"message": "Welcome to the prediction API!"}

# --------------------------
# GET /predict endpoint
# --------------------------
@app.get("/predict", tags=["Prediction"])
def predict(x: float) -> dict:
    """
    Predict a numeric output based on input x.

    Example:
        /predict?x=5.3
    """
    try:
        # Reshape input to 2D array for scikit-learn
        input_array = np.array([[x]])
        prediction = model.predict(input_array)
        return {"prediction": float(prediction[0])}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle

# Load the model
with open("simple_model.pkl", "rb") as f:
    model = pickle.load(f)

app = FastAPI()

class InputData(BaseModel):
    x: float

@app.get("/")
def root():
    return {"message": "Welcome to the prediction API"}

@app.get("/predict")
def predict_get(x: float):
    try:
        prediction = model.predict([[x]])
        return {"prediction": float(prediction[0])}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

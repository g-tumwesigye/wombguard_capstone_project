from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware

# Initializing the app
app = FastAPI(title="WombGuard Pregnancy Predictive API")

# Allowing all origins 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Loading the model package
try:
    package = joblib.load("wombguard_pregnancy_model.pkl")
    model = package["model"]
    scaler = package["scaler"]
    feature_names = package["feature_names"]
except Exception as e:
    raise RuntimeError(f"Failed to load model package: {e}")

# Input schema
class PatientData(BaseModel):
    Age: float
    Systolic_BP: float
    Diastolic: float
    BS: float
    Body_Temp: float
    BMI: float
    Heart_Rate: float

@app.get("/")
def home():
    return {"message": "WombGuard Pregnancy Predictive API is running successfully!"}

@app.post("/predict")
def predict_pregnancy_risk(features: PatientData):
    try:
        # Converting to DataFrame with correct column order
        patient_df = pd.DataFrame([features.dict()])[feature_names]

        # Scaling data
        patient_scaled = scaler.transform(patient_df)

        # Trying classification prediction
        try:
            probabilities = model.predict_proba(patient_scaled)
            # If model gives 2 probabilities (for 2 classes)
            if probabilities.shape[1] == 2:
                prob_high_risk = probabilities[:, 1]
            else:
                prob_high_risk = probabilities[:, 0]
        except AttributeError:
        
            prob_high_risk = model.predict(patient_scaled)

        # Ensuring numeric output
        prob_high_risk = np.clip(prob_high_risk, 0, 1)

        # Converting to labels
        predictions = (prob_high_risk >= 0.5).astype(int)
        risk_levels = ["Low Risk" if p == 0 else "High Risk" for p in predictions]

        # Confidence
        confidence_scores = np.maximum(prob_high_risk, 1 - prob_high_risk)

        # Preparing response
        response = {
            "prediction": {
                "Predicted_Risk_Level": risk_levels[0],
                "Probability_High_Risk": round(float(prob_high_risk[0]), 4),
                "Confidence_Score": round(float(confidence_scores[0]), 4)
            }
        }

        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


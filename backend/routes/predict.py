from fastapi import APIRouter
from pydantic import BaseModel
import pandas as pd
import joblib

# ==========================
# Router
# ==========================

router = APIRouter()

# ==========================
# Load Model
# ==========================

model = joblib.load("model.pkl")
features = joblib.load("features.pkl")

# ==========================
# Input Schema
# ==========================

class StudentInput(BaseModel):
    age: int
    Medu: int
    Fedu: int
    traveltime: int
    studytime: int
    failures: int
    internet: bool
    health: int
    absences: int
    activities: bool
    gaurdian : bool


# ==========================
# Predict Endpoint
# ==========================

@router.post("/predict")
def predict(student: StudentInput):

    # Create empty dataframe with training columns
    sample = pd.DataFrame(columns=features)

    # Initialize all columns with 0
    sample.loc[0] = 0

    # Fill available features
    if "age" in sample.columns:
        sample.loc[0, "age"] = student.age

    if "absences" in sample.columns:
        sample.loc[0, "absences"] = student.absences

    if "failures" in sample.columns:
        sample.loc[0, "failures"] = student.failures

    if "studytime" in sample.columns:
        sample.loc[0, "studytime"] = student.studytime

    if "G1" in sample.columns:
        sample.loc[0, "G1"] = student.G1

    if "G2" in sample.columns:
        sample.loc[0, "G2"] = student.G2

    # Prediction
    prediction = model.predict(sample)[0]

    probability = float(
        model.predict_proba(sample)[0][1]
    )

    # Risk Label
    if prediction == 1:

        risk = "High Risk"

        recommendations = [
            "Attend remedial classes",
            "Weekly mentoring sessions",
            "Monitor attendance closely",
            "Complete all pending assignments",
            "Meet academic counselor"
        ]

    else:

        risk = "Low Risk"

        recommendations = [
            "Maintain current performance",
            "Continue regular study habits",
            "Participate in academic activities"
        ]

    return {
        "risk": risk,
        "probability": round(probability * 100, 2),
        "recommendations": recommendations
    }
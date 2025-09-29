from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

modelo = joblib.load('modelo_diabetes.pkl')

app = FastAPI()


class DiabetesData(BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int


@app.get("/")
def root():
    return {"message": "API de Previsão de Diabetes"}


@app.post("/predict")
def predict(data: DiabetesData):
    features = np.array([[
        data.Pregnancies,
        data.Glucose,
        data.BloodPressure,
        data.SkinThickness,
        data.Insulin,
        data.BMI,
        data.DiabetesPedigreeFunction,
        data.Age
    ]])

    previsao = modelo.predict(features)
    
    if previsao == 0:
        resultado_str = "Negativo para diabetes"
    else:
        resultado_str = "Positivo para diabetes"    

    return {"Resultado": resultado_str}

@app.get("/predict/{Pregnancies}/{Glucose}/{BloodPressure}/{SkinThickness}/{Insulin}/{BMI}/{DiabetesPedigreeFunction}/{Age}")
def predict_irl( Pregnancies: int, Glucose: int, BloodPressure: int, SkinThickness: int, Insulin: int, BMI: float, DiabetesPedigreeFunction: float, Age: int):
    features = np.array([[]])

    features = np.array([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

    previsao = modelo.predict(features)

    if previsao == 0:
        resultado_str = "Negativo para diabetes"
    else:
        resultado_str = "Positivo para diabetes"    

    return {"Resultado": resultado_str}



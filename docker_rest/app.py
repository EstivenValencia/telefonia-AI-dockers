import sys
import os

from fastapi import FastAPI, HTTPException, Query
from telefonica import TelefonicaAI
import uvicorn
from typing import Dict, Optional

# Inicializar la aplicación FastAPI
app = FastAPI()

# Configuración del modelo de predicción
model_path = 'models/best_random_forest_model.joblib'
scaler_path ='models/scaler.pkl'
significant_columns_path ='models/significant_columns.pkl'
telefonicaAI = TelefonicaAI(model_path, scaler_path, significant_columns_path)

# Ruta raíz para verificar que el servicio está activo
@app.get("/")
def home():
    return {"message": "Modelo de predicción activo. Usa la ruta /predict con los parámetros necesarios."}

# Ruta para realizar predicciones
@app.get("/predict")
async def predict(
    internet_service: Optional[int] = Query(None, description="Internet Service"),
    number_dependents: Optional[int] = Query(None, description="Number of Dependents"),
    number_referrals: Optional[int] = Query(None, description="Number of Referrals"),
    satisfaction_score: Optional[int] = Query(None, description="Satisfaction Score"),
    tenure_in_months: Optional[int] = Query(None, description="Tenure in Months"),
    total_long_distance_charges: Optional[float] = Query(None, description="Total Long Distance Charges"),
    total_revenue: Optional[float] = Query(None, description="Total Revenue"),
    contract: Optional[str] = Query(None, description="Contract"),
    payment_method: Optional[str] = Query(None, description="Payment Method")
) -> Dict[str, str]:
    try:
        # Crear un diccionario con los datos de entrada
        data = {
            "internet_service": internet_service,
            "number_dependents": number_dependents,
            "number_referrals": number_referrals,
            "satisfaction_score": satisfaction_score,
            "tenure_in_months": tenure_in_months,
            "total_long_distance_charges": total_long_distance_charges,
            "total_revenue": total_revenue,
            "contract": contract,
            "payment_method": payment_method
        }

        # Realizar la predicción utilizando el modelo
        pred = telefonicaAI.predict(data)
        return {"prediccion": pred}

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al realizar la predicción: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
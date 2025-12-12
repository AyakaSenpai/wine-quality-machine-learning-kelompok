# FILE: api.py
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import pandas as pd
import numpy as np

app = FastAPI()

# Setup CORS agar script.js bisa mengakses API ini
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- LOAD MODEL WINE KAMU DI SINI ---
# Pastikan nama file .pkl sesuai dengan yang kamu punya
try:
    with open("models/scaler.pkl", "rb") as f:
        scaler = pickle.load(f)
    with open("models/wine_model.pkl", "rb") as f: # Ganti nama file jika beda
        model = pickle.load(f)
except FileNotFoundError:
    print("WARNING: File model .pkl tidak ditemukan di folder models/!")

# Kelas Input sesuai dengan script.js kamu
class WineInput(BaseModel):
    fixed_acidity: float
    volatile_acidity: float
    citric_acid: float
    residual_sugar: float
    chlorides: float
    free_sulfur_dioxide: float
    total_sulfur_dioxide: float
    density: float
    pH: float
    sulphates: float
    alcohol: float

@app.get("/")
def home():
    return {"message": "Wine Quality API Siap! Lakukan POST ke /predict"}

@app.post("/predict")
def predict(data: WineInput):
    try:
        # Urutan kolom harus SAMA PERSIS dengan waktu kamu training model
        input_list = [
            data.fixed_acidity,
            data.volatile_acidity,
            data.citric_acid,
            data.residual_sugar,
            data.chlorides,
            data.free_sulfur_dioxide,
            data.total_sulfur_dioxide,
            data.density,
            data.pH,
            data.sulphates,
            data.alcohol
        ]
        
        # Ubah ke DataFrame atau Numpy Array (tergantung cara training dulu)
        # Disini kita anggap perlu reshape untuk 1 baris data
        features = np.array(input_list).reshape(1, -1)
        
        # Scaling data (jika modelmu butuh scaling)
        scaled_features = scaler.transform(features)
        
        # Prediksi
        prediction = model.predict(scaled_features)
        
        # Kembalikan hasil (float agar bisa dibaca JSON)
        return {"predicted_quality": float(prediction[0])}

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error: {str(e)}")

# Ganti 8000 jadi 7860
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)
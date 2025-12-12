import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import pickle
import os

# 1. Kita buat data pura-pura (Dummy) sesuai format Wine kamu
# Ini supaya modelnya "terbentuk" dan bisa disimpan
print("Sedang membuat data dummy...")
data = {
    'fixed_acidity': np.random.rand(50) * 10,
    'volatile_acidity': np.random.rand(50),
    'citric_acid': np.random.rand(50),
    'residual_sugar': np.random.rand(50) * 5,
    'chlorides': np.random.rand(50),
    'free_sulfur_dioxide': np.random.rand(50) * 50,
    'total_sulfur_dioxide': np.random.rand(50) * 100,
    'density': np.random.rand(50),
    'pH': np.random.rand(50) * 4,
    'sulphates': np.random.rand(50),
    'alcohol': np.random.rand(50) * 15,
    'quality': np.random.randint(3, 9, 50) # Target (Skala 3-8)
}

df = pd.DataFrame(data)

# Pisahkan fitur dan target
X = df.drop('quality', axis=1)
y = df['quality']

# 2. Standarisasi Data (Scaler)
print("Sedang melatih scaler...")
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. Latih Model (Random Forest)
print("Sedang melatih model AI...")
model = RandomForestClassifier(n_estimators=10)
model.fit(X_scaled, y)

# 4. Simpan ke folder 'models'
# Cek kalau folder belum ada, kita buat
if not os.path.exists('models'):
    os.makedirs('models')

print("Menyimpan file .pkl ke folder 'models'...")

# Simpan Scaler
with open('models/scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)

# Simpan Model
with open('models/wine_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("\nBERHASIL! ✅")
print("Cek folder 'models' di laptopmu. Harusnya sekarang sudah ada file:")
print("1. scaler.pkl")
print("2. wine_model.pkl")
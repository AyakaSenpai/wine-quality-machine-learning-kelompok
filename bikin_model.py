import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import pickle
import os

# 1. Buat data dummy
print("Sedang membuat data...")
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
    'quality': np.random.randint(3, 9, 50)
}
df = pd.DataFrame(data)
X = df.drop('quality', axis=1)
y = df['quality']

# 2. Training
print("Sedang training model...")
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
model = RandomForestClassifier(n_estimators=10)
model.fit(X_scaled, y)

# 3. Simpan
if not os.path.exists('models'):
    os.makedirs('models')

print("Menyimpan ke folder models...")
with open('models/scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)
with open('models/wine_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("BERHASIL! Folder 'models' sudah siap.")
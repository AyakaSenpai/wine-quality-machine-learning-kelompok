# Gunakan python versi ringan
FROM python:3.9-slim

# Set folder kerja di dalam VPS/Container
WORKDIR /app

# ... (baris sebelumnya)
COPY requirements.txt .

# Perintah ini akan membaca file requirements.txt yang kamu buat di atas
RUN pip install --no-cache-dir -r requirements.txt


# Copy seluruh kode (api.py dan folder models) ke dalam container
COPY . .

# Ganti 8000 jadi 7860
EXPOSE 7860

# Command jalannya juga ganti portnya
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "7860"]

# Jalankan aplikasi
CMD ["python", "api.py"]
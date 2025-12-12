// GANTI URL INI DENGAN ALAMAT API KAMU YANG ASLI
// Contoh kalau VPS: "http://123.456.78.90/predict"
// Contoh kalau Railway/Render: "https://nama-app.up.railway.app/predict"
const API_URL = "https://ayakasenpai99-wine-prediction.hf.space/predict";

document.getElementById("wineForm").addEventListener("submit", async function(e) {
    e.preventDefault();

    const resultDiv = document.getElementById("result");
    const btnText = document.querySelector(".btn-text");
    const btn = document.getElementById("submitBtn");

    // Efek Loading
    btnText.textContent = "Sedang Menganalisis...";
    btn.disabled = true;
    resultDiv.className = "result hidden";
    resultDiv.innerHTML = "";

    // Ambil Data dari Form
    const data = {
        fixed_acidity: parseFloat(document.getElementById("fixed_acidity").value),
        volatile_acidity: parseFloat(document.getElementById("volatile_acidity").value),
        citric_acid: parseFloat(document.getElementById("citric_acid").value),
        residual_sugar: parseFloat(document.getElementById("residual_sugar").value),
        chlorides: parseFloat(document.getElementById("chlorides").value),
        free_sulfur_dioxide: parseFloat(document.getElementById("free_sulfur_dioxide").value),
        total_sulfur_dioxide: parseFloat(document.getElementById("total_sulfur_dioxide").value),
        density: parseFloat(document.getElementById("density").value),
        pH: parseFloat(document.getElementById("pH").value),
        sulphates: parseFloat(document.getElementById("sulphates").value),
        alcohol: parseFloat(document.getElementById("alcohol").value)
    };

    try {
        console.log("Mengirim data:", data); // Untuk debugging di Console Browser

        const response = await fetch(API_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();
        console.log("Hasil:", result); // Cek hasil di Console

        resultDiv.classList.remove("hidden");
        resultDiv.classList.add("show");

        if (response.ok) {
            resultDiv.innerHTML = `
                <h3>Hasil Prediksi</h3>
                <span class="quality-score">${result.predicted_quality}</span>
                <p>Skala Kualitas (1 - 10)</p>
            `;
            resultDiv.classList.add("success");
        } else {
            throw new Error(result.detail || "Gagal memproses data");
        }

    } catch (error) {
        resultDiv.classList.remove("hidden");
        resultDiv.classList.add("show");
        resultDiv.innerHTML = `<strong>Error:</strong> ${error.message}. <br><small>Pastikan API URL sudah benar dan Server menyala.</small>`;
        resultDiv.classList.add("error");
        console.error("Fetch Error:", error);
    } finally {
        // Kembalikan tombol seperti semula
        btnText.textContent = "Cek Kualitas";
        btn.disabled = false;
    }
});

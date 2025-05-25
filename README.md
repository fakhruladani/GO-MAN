# GO-MAN
Alibaba Hackaton 2025

# GO-MAN 🗺️🤖

**GO-MAN** (short for *Go Meeting Anywhere Now*) adalah aplikasi web berbasis [Streamlit](https://streamlit.io/) yang membantu pengguna menemukan titik tengah pertemuan dari beberapa lokasi dan memberikan rekomendasi tempat terdekat, serta menyediakan chatbot berbasis AI yang dapat menjawab berbagai pertanyaan melalui integrasi dengan webhook [n8n](https://n8n.io/).

## 🚀 Fitur Utama

### 1. 🔍 Cari Titik Tengah Lokasi
Pengguna dapat memasukkan beberapa koordinat lokasi (latitude dan longitude), dan aplikasi akan menghitung titik tengah geografis dari semua lokasi tersebut. Selanjutnya, aplikasi akan mencari dan merekomendasikan kafe terdekat dari titik tengah tersebut (radius 3km) berdasarkan data dummy yang tersedia.

### 2. 🤖 Chat AI
Fitur ini memungkinkan pengguna untuk berinteraksi dengan AI dan mendapatkan jawaban dari pertanyaan apapun. Input pengguna akan dikirim ke endpoint webhook `n8n` yang telah disiapkan, dan respons AI akan ditampilkan di antarmuka aplikasi.

---

## 🧰 Teknologi yang Digunakan

- **Python**
- **Streamlit** — untuk membangun antarmuka pengguna secara cepat dan interaktif
- **Geopy** — untuk menghitung jarak geografis antar titik (dalam meter)
- **Requests** — untuk mengirim permintaan HTTP ke webhook `n8n`
- **n8n** — untuk mengelola dan mengotomatiskan proses alur kerja AI backend

---

## 🖥️ Cara Menjalankan Aplikasi

### 1. Clone repositori ini:
```bash
git clone https://github.com/fakhruladani/GO-MAN.git
cd GO-MAN
````

### 2. Install dependencies:

Pastikan Anda telah mengaktifkan virtual environment (opsional), lalu jalankan:

```bash
pip install -r requirements.txt
```

### 3. Jalankan aplikasi:

```bash
streamlit run app.py
```

---

## 📦 Contoh Format Input Lokasi

Masukkan koordinat dalam format berikut (JSON List of Dicts):

```json
[
  {"lat": -6.2146, "lng": 106.8451},
  {"lat": -6.1767, "lng": 106.8271},
  {"lat": -6.2000, "lng": 106.8300}
]
```

---

## 🔧 Catatan Teknis

* **Titik tengah** dihitung dengan rata-rata nilai latitude dan longitude dari semua lokasi.
* **Data kafe** yang digunakan saat ini bersifat *dummy* dan dapat diperluas atau diganti dengan integrasi API (misalnya Google Places API).
* **Webhook n8n** harus dikonfigurasi untuk menerima `user_input` dan mengembalikan respons dalam format JSON dengan key `message`.

---

## 💡 Ide Pengembangan Selanjutnya

* Integrasi Google Maps API untuk lokasi aktual kafe.



# Cloud-Native Network Telemetry & Data Pipeline.

Proyek kolaborasi ini mengimplementasikan sistem pemantauan jaringan dan *data pipeline* secara *real-time*. Sistem ini mengambil data telemetri buatan (dummy), memproses metrik jaringan, dan menyimpannya di *database cloud* untuk divisualisasikan pada *dashboard* deteksi anomali.

## Kontributor Proyek

* **Muhammad Raafi**: Pengembangan API & Pembuatan Data (*Data Generation*)
* **Rafi Doelandri**: ETL Data Pipeline & Integrasi Database

## Arsitektur Sistem & Alur Kerja

Arsitektur dari proyek ini dibagi menjadi tiga komponen utama:

1. **Telemetry API (Sumber Data):** API yang dibuat khusus untuk menyediakan data telemetri jaringan *dummy* (dalam format JSON), menyimulasikan kondisi jaringan secara *real-time*.
2. **ETL Pipeline:** Skrip berbasis Python yang secara terus-menerus mengekstrak data JSON dari API, membersihkan dan mentransformasi metrik jaringan (seperti *latency*, *bandwidth*), lalu memuatnya ke dalam database.
3. **Penyimpanan:** Data yang telah diproses disimpan dengan aman di database **Supabase (PostgreSQL)**.

## Teknologi yang Digunakan

* **Bahasa Pemrograman:** Python
* **Pipeline:** Skrip ETL Kustom, `requests`, `pandas`
* **Database:** Supabase (PostgreSQL)
* **API:** Flask

## Prasyarat

Sebelum menjalankan proyek ini di komputermu, pastikan kamu sudah menginstal perangkat lunak berikut:

* Python 3.13
* Akun dan proyek Supabase untuk konfigurasi database.

## Cara Menjalankan Proyek

### 1. Persiapan Lingkungan (Environment Setup)
Lakukan *clone* pada repositori ini dan instal semua *library* yang dibutuhkan:
```bash
    git clone https://github.com/KuraiShades/Proyek-Cloud-Collab
    cd Proyek-Cloud-Collab
    pip install -r requirements.txt
```

### 2. Menjalankan Telemetry API
Menjalankan Aplikasi terlebih dahulu agar API menyala dan dapat terbaca.
```bash
    python app.py
```
Setelah dijalankan akses link URL di panel "Ports"
```bash
    https://reimagined-space-waddle-qv99gx9prx59hxp76-5000.app.github.dev/api/telemetry?key=password_key
```

### 3. Menjalakan data pipeline

Setelah API menyala dan menyediakan data JSON, jalankan data pipeline untuk memulai proses *Extract*, *Transform*, dan *Load*:
```bash
    python extractData.py
``` 

Jika data sudah di ekstrak, jalankan:
```bash
    python loadData.py
```

*Proyek kolaborasi yang berfokus pada cloud-native data pipeline dan pemantauan telemetri jaringan.*

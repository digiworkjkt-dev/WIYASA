# Paket Dokumentasi Resmi Sistem WIYASA (v1.6.0)

Selamat datang di repositori paket dokumentasi resmi **WIYASA** (*Standardized Application Documentation Engine*). Berkas ini merupakan pintu masuk utama, peta navigasi artefak, dan petunjuk operasional pengkajian dokumen sistem.

## Status dan Metadata Paket

- **Nama Sistem:** WIYASA Documentation Engine
- **Versi Sistem:** v1.6.0 (Baseline Terverifikasi 2026-10-31)
- **Status Dokumen:** Approved / Dokumen Resmi Produksi
- **Model Distribusi:** Standar Opsi 2 (Pemisahan Dua Dokumen Berdasarkan Audiens)
- **Lingkungan Output:** `DocsApp/`

---

## Indeks dan Urutan Baca Deliverable

Paket dokumentasi ini disusun menggunakan **Standar Opsi 2**, memisahkan secara tegas dokumen teknis mendalam untuk tim pengembang dari buku panduan operasional praktis untuk pengguna dan administrator:

1. **[Laporan Arsitektur dan Spesifikasi Sistem (HTML)](laporan-arsitektur-dan-spesifikasi.html)**  
   *Target Audiens:* Principal Architect, Software Engineer, Quality Assurance, Security Auditor, dan Stakeholder Teknis.  
   *Cakupan:* Spesifikasi produk, kebutuhan fungsional/non-fungsional ber-ID, arsitektur teknis 3-tier, model data, integrasi API, analisis keamanan & privasi, matriks keterlacakan, standar kepatuhan (ISO/SNI), dan log keputusan arsitektur (ADR).

2. **[Panduan Pengguna dan Administrator Aplikasi (HTML)](panduan-pengguna-aplikasi.html)**  
   *Target Audiens:* Klien, Pengguna Akhir, Tim Operasional, dan Administrator Sistem.  
   *Cakupan:* Langkah onboarding, alur pengoperasian fitur utama langkah-demi-langkah, panel konfigurasi admin, ilustrasi tangkapan layar antarmuka visual (UI mockups), tanya-jawab (FAQ), panduan penanganan kendala teknis mandiri, dan batasan operasional sistem.

3. **[Berkas Sumber Modular Markdown (`sources/`)](sources/)**  
   *Target Audiens:* Pengembang Perangkat Lunak & Sistem Integrator.  
   *Cakupan:* 18 berkas modular Markdown (`00-context.md` s.d. `17-developer-guide.md`) yang berfungsi sebagai *Single Source of Truth* (SSOT) kanonikal di sistem kontrol versi (Git).

---

## Panduan Resmi Cetak A4 / Ekspor PDF

Seluruh berkas laporan HTML pada paket ini dirancang memenuhi kaidah tata letak cetak dokumen formal A4 Indonesia:

1. **Buka Berkas:** Buka berkas `laporan-arsitektur-dan-spesifikasi.html` atau `panduan-pengguna-aplikasi.html` menggunakan peramban web modern (Google Chrome, Microsoft Edge, atau Mozilla Firefox).
2. **Buka Jendela Cetak:** Tekan pintasan tombol **`Ctrl + P`** (Windows/Linux) atau **`Cmd + P`** (macOS).
3. **Pilih Tujuan Pencetakan (*Destination*):** Pilih **`Save as PDF`** (Simpan sebagai PDF) atau pilih printer fisik berkualitas tinggi.
4. **Ukuran Kertas (*Paper Size*):** Pastikan terpilih **`A4`** (210 × 297 mm) dengan orientasi **`Portrait`**.
5. **Margin Kertas (*Margins*):** Pilih opsi **`Default`** atau **`Custom: 3 cm`** (Dokumen telah memiliki CSS margin 3 cm pada keempat sisi).
6. **Skala (*Scale*):** Atur ke **`100%`** (Default).
7. **Header dan Footer Peramban (*Headers and footers*):** **NONAKTIFKAN (Hilangkan Centang)** opsi ini. Seluruh halaman dokumen telah memiliki *running page footers* bawaan beridentitas WIYASA yang berulang otomatis pada setiap halaman.
8. **Grafik Latar Belakang (*Background graphics*):** **AKTIFKAN (Centang)** opsi ini agar warna tabel, badge status, kotak notice, dan diagram SVG tampil sempurna.
9. **Simpan / Cetak:** Klik tombol **Save** untuk menyimpan PDF berkualitas cetak resmi.

---

## Verifikasi Kualitas Otomatis

Paket dokumentasi ini dapat diverifikasi kepatuhannya menggunakan perkakas pengujian terintegrasi:

```powershell
# 1. Validasi integritas paket deliverable lengkap (HTML, CSS cetak A4, anti-leakage, footer)
python scripts/validate.py --package-dir DocsApp

# 2. Verifikasi matriks keterlacakan ID relasional (FR -> AC -> TASK -> TC)
python scripts/lint_traceability.py --dir DocsApp/sources
```

# 02. Product Requirements Document (PRD)
Status: Approved
Version: 1.6.0
Updated: 2026-10-31
Owner: Dewan Arsitektur & Rekayasa Perangkat Lunak WIYASA
Scope: Full System / Production
Sources: Kode sumber WIYASA v1.6.0, ISO/IEC 25010, SNI ISO/IEC 27001, SKKNI Kepmenaker 282/2016
Related: [README.md](../README.md), [laporan-arsitektur-dan-spesifikasi.html](../laporan-arsitektur-dan-spesifikasi.html)

## 1. Ruang Lingkup Fungsional
WIYASA v1.6.0 mencakup kemampuan:
- Menghasilkan struktur deliverable Standar Opsi 2 (Dua Dokumen HTML Terpisah berdasarkan audiens + 18 berkas sumber Markdown).
- Menjamin kepatuhan tipografi formal A4 (margin 3cm, font Cambria 12pt, teks rata kanan-kiri/align justify).
- Menyediakan running page footers berulang otomatis pada setiap halaman cetak.
- Menyediakan isolasi penuh terhadap instruksi cetak peramban (anti-leakage) agar tidak mengotori badan dokumen resmi.
- Menyediakan mesin validasi otomatis (`scripts/validate.py` dan `scripts/lint_traceability.py`).

## 2. Kriteria Keberhasilan Produk
- 100% berkas HTML lolos uji validasi keamanan statis tanpa kerentanan XSS.
- Seluruh teks naratif memiliki perataan `text-align: justify`.
- Keterlacakan 100% antara kebutuhan bisnis, kriteria penerimaan, tugas implementasi, dan skenario pengujian.

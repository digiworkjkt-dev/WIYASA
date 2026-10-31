# 07. Integrasi Antarmuka Baris Perintah (CLI)
Status: Approved
Version: 1.6.0
Updated: 2026-10-31
Owner: Dewan Arsitektur & Rekayasa Perangkat Lunak WIYASA
Scope: Full System / Production
Sources: Kode sumber WIYASA v1.6.0, ISO/IEC 25010, SNI ISO/IEC 27001, SKKNI Kepmenaker 282/2016
Related: [README.md](../README.md), [laporan-arsitektur-dan-spesifikasi.html](../laporan-arsitektur-dan-spesifikasi.html)

## 1. Antarmuka CLI Skrip Validasi (`validate.py`)
- `python scripts/validate.py` : Menjalankan validasi kepatuhan internal repositori.
- `python scripts/validate.py --target <path_html>` : Memvalidasi berkas HTML deliverable tunggal.
- `python scripts/validate.py --package-dir <dir>` : Memvalidasi kelengkapan seluruh paket deliverable Opsi 2 (`README.md`, `sources/*.md`, sepasang HTML).

## 2. Antarmuka CLI Linter Keterlacakan (`lint_traceability.py`)
- `python scripts/lint_traceability.py --dir <dir_sources>` : Memindai seluruh berkas `.md` untuk mendeteksi ID yatim (*orphan IDs*) atau rantai pemetaan yang terputus.

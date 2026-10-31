# 12. Buku Panduan Pengguna dan Administrator
Status: Approved
Version: 1.6.0
Updated: 2026-10-31
Owner: Dewan Arsitektur & Rekayasa Perangkat Lunak WIYASA
Scope: Full System / Production
Sources: Kode sumber WIYASA v1.6.0, ISO/IEC 25010, SNI ISO/IEC 27001, SKKNI Kepmenaker 282/2016
Related: [README.md](../README.md), [laporan-arsitektur-dan-spesifikasi.html](../laporan-arsitektur-dan-spesifikasi.html)

## 1. Petunjuk Pengoperasian Cepat
Pengguna dapat mengoperasikan sistem WIYASA melalui perintah prompt terarah pada lingkungan asisten AI:
```text
Gunakan WIYASA untuk menyusun paket dokumentasi lengkap aplikasi [Nama Aplikasi].
Format deliverable Opsi 2: Laporan Arsitektur & Spesifikasi, Panduan Pengguna Mandiri,
serta berkas sumber modular Markdown di folder DocsApp/.
```

## 2. Panduan Khusus Administrator
Administrator bertugas memelihara integritas repositori dan memastikan kelayakan rilis melalui eksekusi berkala skrip pengujian:
```powershell
python scripts/validate.py --package-dir DocsApp
python scripts/lint_traceability.py --dir DocsApp/sources
```

# 17. Panduan Pengembang dan Kontributor
Status: Approved
Version: 1.6.0
Updated: 2026-10-31
Owner: Dewan Arsitektur & Rekayasa Perangkat Lunak WIYASA
Scope: Full System / Production
Sources: Kode sumber WIYASA v1.6.0, ISO/IEC 25010, SNI ISO/IEC 27001, SKKNI Kepmenaker 282/2016
Related: [README.md](../README.md), [laporan-arsitektur-dan-spesifikasi.html](../laporan-arsitektur-dan-spesifikasi.html)

## 1. Panduan Pengembangan Lingkungan Lokal
Pengembang yang ingin memodifikasi kerangka kerja WIYASA dapat mengikuti panduan berikut:
1. Pastikan terpasang Python 3.10+ pada lingkungan kerja.
2. Lakukan clone repositori:
   ```powershell
   git clone https://github.com/digiworkjkt-dev/WIYASA.git
   cd WIYASA
   ```
3. Lakukan pengujian kepatuhan sintaks sebelum mengajukan pull request:
   ```powershell
   python scripts/validate.py
   python scripts/lint_traceability.py --dir DocsApp/sources
   ```

# 15. Evaluasi Kepatuhan Standar dan Regulasi
Status: Approved
Version: 1.6.0
Updated: 2026-10-31
Owner: Dewan Arsitektur & Rekayasa Perangkat Lunak WIYASA
Scope: Full System / Production
Sources: Kode sumber WIYASA v1.6.0, ISO/IEC 25010, SNI ISO/IEC 27001, SKKNI Kepmenaker 282/2016
Related: [README.md](../README.md), [laporan-arsitektur-dan-spesifikasi.html](../laporan-arsitektur-dan-spesifikasi.html)

## 1. Standar Mutu Perangkat Lunak ISO/IEC 25010
WIYASA dirancang memenuhi karakteristik kualitas:
- *Functional Suitability:* Kelengkapan kebutuhan spesifikasi.
- *Usability:* Panduan pengguna terstruktur dan ramah awam.
- *Reliability:* Skrip validator mandiri yang kebal bypass runtime.
- *Security:* Ketiadaan eksekusi skrip dinamis dan sanitasi XSS.

## 2. Kepatuhan Regulasi Indonesia
- **UU No. 27/2022 (Pelindungan Data Pribadi):** Penegakan anonimisasi data dummy pada seluruh visual antarmuka.
- **PP No. 71/2019 (PSTE):** Menjamin keandalan dokumen teknis sistem elektronik.

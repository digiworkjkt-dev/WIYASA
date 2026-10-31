# 10. Rencana Rilis dan Delivery Plan
Status: Approved
Version: 1.6.0
Updated: 2026-10-31
Owner: Dewan Arsitektur & Rekayasa Perangkat Lunak WIYASA
Scope: Full System / Production
Sources: Kode sumber WIYASA v1.6.0, ISO/IEC 25010, SNI ISO/IEC 27001, SKKNI Kepmenaker 282/2016
Related: [README.md](../README.md), [laporan-arsitektur-dan-spesifikasi.html](../laporan-arsitektur-dan-spesifikasi.html)

## 1. Rencana Rilis Versi 1.6.0
- **Milestone 1:** Refactoring skrip validasi dan eliminasi kerentanan assert (v1.5.0).
- **Milestone 2:** Penerapan kewajiban paket lengkap, align justify, dan anti-leakage (v1.5.1).
- **Milestone 3:** Standarisasi Opsi 2 (Dual HTML) dan visual UI mockups (v1.5.2).
- **Milestone 4:** Rebranding resmi WIYASA, running page footers, dan migrasi repositori (v1.6.0).

## 2. Definisi Selesai (Definition of Done - DoD)
Paket dinyatakan selesai jika lolos pengujian `validate.py --package-dir` dengan 0 error dan terbukti memiliki visual rendering yang presisi.

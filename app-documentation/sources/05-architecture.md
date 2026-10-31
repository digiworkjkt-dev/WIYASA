# 05. Arsitektur Teknis Sistem
Status: Approved
Version: 1.6.0
Updated: 2026-10-31
Owner: Dewan Arsitektur & Rekayasa Perangkat Lunak WIYASA
Scope: Full System / Production
Sources: Kode sumber WIYASA v1.6.0, ISO/IEC 25010, SNI ISO/IEC 27001, SKKNI Kepmenaker 282/2016
Related: [README.md](../README.md), [laporan-arsitektur-dan-spesifikasi.html](../laporan-arsitektur-dan-spesifikasi.html)

## 1. Arsitektur Sistem 3-Tier WIYASA
Sistem dirancang dengan arsitektur 3 lapis yang terisolasi secara bersih:
1. **Presentation Layer (Deliverable HTML & Paged Media CSS):**
   - Modul `assets/report-a4.html` (Laporan Arsitektur & Spesifikasi)
   - Modul `assets/user-guide-a4.html` (Panduan Pengguna & Admin)
   - Dukungan tipografi Cambria 12pt, margin 3cm, running footers, dan perataan rata kanan-kiri.
2. **Core Engine Layer (Assembly & Specification Pipeline):**
   - Aturan operasional agen pada `SKILL.md`
   - Modul katalog dokumen `references/catalog.md`
   - Modul standar tata naskah `references/html-print.md`
   - Modul penapisan mutu `references/quality-gates.md`
3. **Verification Layer (Automated Gatekeepers):**
   - Linter integritas paket dan keamanan `scripts/validate.py`
   - Linter matriks relasional keterlacakan `scripts/lint_traceability.py`

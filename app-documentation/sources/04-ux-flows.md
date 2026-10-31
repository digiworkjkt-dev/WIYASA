# 04. Alur Interaksi Pengguna (UX Flows)
Status: Approved
Version: 1.6.0
Updated: 2026-10-31
Owner: Dewan Arsitektur & Rekayasa Perangkat Lunak WIYASA
Scope: Full System / Production
Sources: Kode sumber WIYASA v1.6.0, ISO/IEC 25010, SNI ISO/IEC 27001, SKKNI Kepmenaker 282/2016
Related: [README.md](../README.md), [laporan-arsitektur-dan-spesifikasi.html](../laporan-arsitektur-dan-spesifikasi.html)

## 1. Alur Interaksi Pengguna dengan Engine WIYASA
Alur operasional pengguna berlangsung dalam 4 tahapan utama:
1. **Fase Inisiasi (Intake):** Pengguna memberikan prompt kebutuhan aplikasi. WIYASA mengidentifikasi konteks, batasan, entitas data, dan sektor kepatuhan.
2. **Fase Pilihan Cakupan (Scoping):** Pengguna memilih cakupan paket (Lean / Standard / Extended). Default: Standard dengan model Opsi 2.
3. **Fase Perakitan Berkas (Generation):** WIYASA menghasilkan berkas sumber modular di `sources/` dan mengompilasinya ke dalam template HTML A4 resmi.
4. **Fase Verifikasi & Penyerahan (Quality Gate):** Menjalankan `validate.py` dan `lint_traceability.py`, memastikan lolos 100%, lalu menyerahkan lokasi berkas fisik aktual.

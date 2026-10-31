# 03. Spesifikasi Kebutuhan Sistem
Status: Approved
Version: 1.6.0
Updated: 2026-10-31
Owner: Dewan Arsitektur & Rekayasa Perangkat Lunak WIYASA
Scope: Full System / Production
Sources: Kode sumber WIYASA v1.6.0, ISO/IEC 25010, SNI ISO/IEC 27001, SKKNI Kepmenaker 282/2016
Related: [README.md](../README.md), [laporan-arsitektur-dan-spesifikasi.html](../laporan-arsitektur-dan-spesifikasi.html)

## 1. Kebutuhan Fungsional (Functional Requirements)

### FR-001: Pembangkitan Deliverable Opsi 2 Terpisah
Sistem wajib menyediakan struktur pemisahan dokumen menjadi dua laporan HTML mandiri (`laporan-arsitektur-dan-spesifikasi.html` dan `panduan-pengguna-aplikasi.html`) serta 18 berkas modular Markdown sebagai SSOT.
- **Kriteria Penerimaan AC-001:** Direktori deliverable memuat kedua berkas HTML tersebut dan folder `sources/` berisi berkas `.md` yang valid.

### FR-002: Standarisasi Format Cetak Formal A4
Sistem wajib menerapkan aturan tata letak A4 portrait, margin 3 cm pada keempat sisi, tipografi Cambria 12 pt, dan perataan teks naratif rata kanan-kiri (`align justify`).
- **Kriteria Penerimaan AC-002:** Blok CSS memuat `@page { size: A4 portrait; margin: 3cm; }`, font Cambria 12pt, dan `text-align: justify; text-justify: inter-word; hyphens: auto;`.

### FR-003: Running Page Footers Multi-Engine
Sistem wajib menampilkan running page footer resmi pada setiap halaman cetak peramban maupun paged media engine.
- **Kriteria Penerimaan AC-003:** Dokumen memuat elemen `.running-footer` dengan posisi `fixed` di dalam margin bawah pada `@media print`, serta margin box `@page { @bottom-left ... @bottom-right ... }`.

### FR-004: Sanitasi Keamanan Dokumen (Anti-XSS & Offline-First)
Sistem wajib menolak eksekusi tag skrip berbahaya (`<script>`, `<iframe>`, `<object>`), atribut event handler (`onload`, `onerror`), dan dependensi eksternal jaringan.
- **Kriteria Penerimaan AC-004:** Seluruh konten HTML bersifat self-contained dan lolos pemindaian `SecureHTMLParser`.

### FR-005: Filter Anti-Kebocoran Petunjuk Cetak (Anti-Leakage)
Sistem wajib mengisolasi instruksi cetak peramban (`Ctrl+P`, `Save as PDF`, petunjuk margin) secara eksklusif pada `README.md` dan melarangnya muncul di badan laporan.
- **Kriteria Penerimaan AC-005:** Validator menggagalkan validasi jika menemukan frasa petunjuk cetak pada badan dokumen HTML.

### FR-006: Perkakas Verifikasi Otomatis Terintegrasi
Sistem wajib menyediakan skrip verifikasi baris perintah (CLI) untuk memeriksa integritas repositori, keabsahan HTML, dan konsistensi matriks keterlacakan.
- **Kriteria Penerimaan AC-006:** Skrip `validate.py --package-dir` dan `lint_traceability.py --dir` mengevaluasi berkas fisik dan memberikan kode keluar 0 untuk berkas valid.

## 2. Kebutuhan Non-Fungsional (Non-Functional Requirements)
- **NFR-001 (Portabilitas):** Seluruh artefak HTML dapat dibuka secara instan di peramban tanpa server web lokal.
- **NFR-002 (Keterbacaan Cetak):** Kontras teks memenuhi standar WCAG AAA untuk keterbacaan cetak monokrom maupun warna.
- **NFR-003 (Keandalan Skrip):** Skrip validasi tidak mengandalkan statement `assert` sehingga kebal terhadap flag optimasi runtime Python (`python -O`).
- **NFR-004 (Efisiensi Konteks):** Mendukung pemuatan bertahap (*progressive lazy-loading*) untuk menghemat jendela token agen AI.

# Changelog

## 1.6.0 ? 2026-10-31: Rebranding Resmi WIYASA & Running Page Footers

- **Pengenalan Running Page Footers pada Dokumen Cetak A4:**
  - Menambahkan elemen `.running-footer` dengan pengulangan otomatis pada setiap halaman cetak peramban (`position: fixed; bottom: -22mm;` di `@media print`) yang ditempatkan aman di dalam margin bawah 3cm tanpa menimpa isi dokumen.
  - Menambahkan aturan CSS Paged Media standar (`@page { @bottom-left { ... } @bottom-right { ... } }`) dengan penomoran halaman otomatis (`counter(page)`) untuk engine paged media (WeasyPrint, Prince, modern Chromium).
  - Memperbarui `assets/report-a4.html`, `assets/user-guide-a4.html`, dan laporan nyata di `DocsApp/` dengan running page footer resmi beridentitas WIYASA.
- **Pembaruan Aturan Skrip Validasi (`scripts/validate.py`):**
  - Mengganti larangan blanket `position: fixed` dengan validasi terarah: mewajibkan setiap dokumen memiliki elemen footer resmi (`.running-footer`) dan membatasi `position: fixed` secara ketat hanya untuk header/footer cetak.
- **Migrasi & Rebranding Nama Repositori Menjadi WIYASA:**
  - Mengubah nama repositori GitHub secara resmi dari `digiworkjkt-dev/app-documentation` menjadi `digiworkjkt-dev/WIYASA`.
  - Memperbarui git remote origin ke `https://github.com/digiworkjkt-dev/WIYASA.git`.
  - Mengadopsi identitas merek **WIYASA** (terinspirasi dari Begawan Wiyasa / Vyasa, sang mahaguru perangkum pustaka agung dan pencatat pengetahuan terstruktur).
  - Nama teknis frontmatter resmi diperbarui menjadi `name: wiyasa` dengan alias pengenal pencarian `app-documentation`.
  - Pembaruan seluruh dokumen panduan pengguna ([`PANDUAN_PENGGUNA.md`](PANDUAN_PENGGUNA.md)), katalog acuan, dan perkakas linter/validator menjadi ekosistem resmi WIYASA.

## 1.5.2 ? 2026-10-31

- **Standarisasi Deliverable Opsi 2 (Pemisahan Dokumen Berdasarkan Audiens):**
  - Mengadopsi standar pemisahan dua berkas HTML mandiri:
    1. `laporan-arsitektur-dan-spesifikasi.html` (Laporan Teknis bagi Tim Pengembang, Arsitek, dan Auditor).
    2. `panduan-pengguna-aplikasi.html` (Buku Panduan Operasional Mandiri bagi Klien, Pengguna Akhir, dan Administrator).
  - Menyediakan template khusus baru [`assets/user-guide-a4.html`](assets/user-guide-a4.html) yang dirancang ramah pengguna dengan gaya tata letak buku manual operasional.
- **Kewajiban Tangkapan Layar (Screenshots / UI Mockups):**
  - Mewajibkan penyematan screenshot atau mockup visual pada bagian-bagian krusial: Layar Onboarding/Login, Dashboard Pengguna, Alur Transaksi Utama, dan Panel Kontrol Administrator.
  - Menyediakan blok visual vektor [`assets/snippets/ui-mockup-frame.svg`](assets/snippets/ui-mockup-frame.svg) sebagai template representasi antarmuka saat frontend belum diimplementasikan.
- **Penyempurnaan Validator & Panduan Operasional:**
  - Memperbarui `scripts/validate.py` agar secara otomatis memverifikasi ketersediaan sepasang berkas HTML Opsi 2 pada pemeriksaan `--package-dir`.
  - Menerbitkan berkas [`PANDUAN_PENGGUNA.md`](PANDUAN_PENGGUNA.md) di root repositori sebagai panduan operasional praktis.

## 1.5.1 ? 2026-10-31

- **Pembersihan Meta-Instruksi & Kriteria dari Dokumen (Anti-Leakage):**
  - Menghapus banner petunjuk cetak dan bab tutorial operasional cetak peramban (seperti sub-bab "6.3 Instruksi Resmi Cetak Dokumen A4", pintasan Ctrl+P, dsb.) dari badan dokumen aplikasi.
  - Memindahkan seluruh panduan teknis pencetakan dan ekspor PDF secara eksklusif ke berkas `app-documentation/README.md` pada seksi *Panduan Cetak*.
  - Melarang keras pencantuman kriteria/rubrik evaluasi internal (Gate A?H, checklist prompt) di dalam laporan aplikasi. Dokumen aplikasi kini murni berupa artefak rekayasa perangkat lunak resmi.
  - Menambahkan verifikasi anti-kebocoran pada `scripts/validate.py` untuk secara otomatis menggagalkan validasi bila ditemukan petunjuk cetak peramban di badan dokumen HTML.
- **Kewajiban Paket Deliverable Lengkap (Multi-File Package):**
  - Mengubah klausul pengiriman dari "sumber Markdown opsional" menjadi **kewajiban mutlak** menghasilkan paket lengkap: `README.md` (katalog/indeks), seluruh berkas sumber modular Markdown di folder `sources/` sebagai Single Source of Truth (SSOT), dan laporan gabungan HTML `laporan-dokumentasi-aplikasi.html`.
  - Mencegah agen hanya menghasilkan satu berkas HTML tanpa menyertakan berkas sumber Markdown pengembang.
- **Standarisasi Tipografi Cetak Rata Kanan-Kiri (Align Justify):**
  - Mewajibkan `text-align: justify; text-justify: inter-word; hyphens: auto;` pada seluruh paragraf naratif, deskripsi, dan catatan (.notice) pada kerangka `assets/report-a4.html`, `references/html-print.md`, dan Gate H, sesuai kaidah dokumen teknis formal Indonesia.
  - Judul dan header tabel tetap dipertahankan rata kiri untuk ketajaman hierarki visual.
- **Validasi Paket Deliverable Otomatis (`scripts/validate.py`):**
  - Menambahkan opsi `--package-dir <path>` pada validator untuk memeriksa integritas paket secara menyeluruh: keberadaan `README.md`, minimal 1 berkas sumber di `sources/`, serta validitas HTML `laporan-dokumentasi-aplikasi.html` (termasuk verifikasi aturan align justify).

## 1.5.0 — 2026-10-30

- **Refactoring Skrip Validasi (`scripts/validate.py`):**
  - Menghapus seluruh ketergantungan pada `assert`; menggantinya dengan pengujian kondisional eksplisit dan kode keluar non-nol (`sys.exit(1)`). Kebal terhadap flag optimasi runtime Python (`python -O` / `PYTHONOPTIMIZE=1`).
  - Menambahkan antarmuka baris perintah (CLI) berbasis `argparse` dengan opsi `--target` untuk memvalidasi berkas deliverable nyata pengguna, bukan hanya aset internal.
- **Peningkatan Keamanan Anti-XSS (Security Hardening):**
  - `SecureHTMLParser` kini melarang secara mutlak tag eksekusi skrip (`<script>`, `<iframe>`, `<object>`, `<embed>`, `<applet>`), skema URI berbahaya (`javascript:`, `data:text/html`), serta seluruh inline event handler (`onload`, `onerror`, `onclick`, dll.).
- **Linter Keterlacakan Otomatis (`scripts/lint_traceability.py`):**
  - Menambahkan utilitas baris perintah untuk memindai integritas pemetaan relasional antara kebutuhan fungsional (`FR-xxx`), kriteria penerimaan (`AC-xxx`), tugas implementasi (`TASK-xxx`), dan kasus uji (`TC-xxx`).
- **Pustaka Snippet SVG Standar (`assets/snippets/`):**
  - Menyediakan template SVG inline cetak A4 yang terkalibrasi secara geometris dan tipografis untuk diagram arsitektur 3-tier (`architecture-diagram.svg`) dan diagram alur keputusan (`flowchart-diagram.svg`).
- **Panduan Format Tabel Matriks Lebar (`references/html-print.md`):**
  - Menambahkan strategi mitigasi untuk tabel dengan $\ge 5$ kolom pada batas cetak horizontal A4 150 mm menggunakan sub-tabel berkunci ID atau format kartu definisi (`<dl>`).
- **Manajemen Jendela Konteks (Progressive Lazy-Loading):**
  - Menambahkan instruksi pada `SKILL.md` untuk memuat referensi regulasi dan SKKNI secara bertahap hanya saat relevan dengan cakupan proyek, guna menghemat alokasi token agen.

## 1.4.1 — 2026-10-05

- Tetapkan folder `app-documentation/` untuk seluruh output dokumen.
- Tambahkan path laporan utama, lokasi sumber opsional dan aturan narasi
  penyerahan hasil setelah file diverifikasi.
- Bedakan folder output dari folder instalasi skill; template cetak tidak berubah.

## 1.4 — 2026-10-05

- Ubah output primer menjadi HTML profesional self-contained.
- Tambahkan template A4 portrait, margin 3 cm, Cambria 12 pt dan print CSS.
- Tambahkan panduan PDF, font fallback/lisensi, footer/nomor halaman sesuai
  engine, sanitasi, dan quality gate output cetak.
- Sumber Markdown tetap opsional untuk pemeliharaan dan konsistensi.

## 1.3 — 2026-10-05

- Tetapkan scope hanya dokumentasi pembangunan aplikasi.
- SKKNI menjadi acuan aktivitas/artefak; tidak membuat portofolio asesmen,
  formulir uji kompetensi, atau paket sertifikasi personel.
- Pertahankan keterlacakan sumber kode/hasil uji untuk akurasi dokumen.

## 1.2 — 2026-10-05

- Tambahkan SKKNI dari Kepmenaker 282/2016 dengan sumber resmi Kemnaker.
- Tambahkan mapping kompetensi/aktivitas, task, artefak dan bukti kerja.
- Tambahkan developer guide bersyarat dan quality gate SKKNI.
- Bedakan mapping daftar unit, sebagian KUK yang dibaca, dan asesmen kompetensi.
- Metadata, daftar unit dan sebagian uraian lampiran diperiksa, bukan audit
  menyeluruh SKKNI atau penilaian kompetensi personel.

## 1.1 — 2026-10-05

- Tambahkan baseline sumber resmi ISO, BSN, dan BPK serta batas verifikasinya.
- Tambahkan screening sektor, register standar/regulasi, dan compliance mapping.
- Bedakan standar industri, SNI, hukum, kewajiban kontrak, dan sertifikasi.
- Tambahkan ID kontrol/bukti, gate compliance, dan contoh kasus SNI.
- Metadata/abstrak diverifikasi; teks lengkap standar dan audit klausul belum
  dilakukan. Tidak ada klaim pemenuhan SNI atau sertifikasi aplikasi.

## 1.0

- Workflow dokumentasi aplikasi end-to-end, katalog, quality gates dan contoh.

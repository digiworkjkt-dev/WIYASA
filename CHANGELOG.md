# Changelog

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

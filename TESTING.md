# Catatan verifikasi v1.5.2

Tanggal Audit: 2026-10-31. Yang diuji adalah standarisasi deliverable Opsi 2 (dua dokumen HTML mandiri), template panduan pengguna baru, penyematan tangkapan layar/mockup visual, dan validasi paket otomatis.

## Pemeriksaan yang Dijalankan pada v1.5.2

1. **Uji Validasi Template Panduan Pengguna Baru (`assets/user-guide-a4.html`):**
   - Perintah: `python scripts/validate.py`
   - Hasil: **PASS**. Template panduan pengguna mandiri terbukti mematuhi seluruh aturan cetak A4 (portrait, margin 3 cm, Cambria 12 pt, *text-align: justify*), memiliki anchor bertaut yang valid, dan bersih dari meta-instruksi peramban.
2. **Uji Validasi Paket Deliverable Opsi 2 (`--package-dir`):**
   - Hasil: **PASS**. Validator secara otomatis memvalidasi kelengkapan sepasang berkas HTML (`laporan-arsitektur-dan-spesifikasi.html` dan `panduan-pengguna-aplikasi.html`) bersama berkas `README.md` dan folder `sources/*.md`.
3. **Uji Integritas Aset Snippet UI Mockup (`assets/snippets/ui-mockup-frame.svg`):**
   - Hasil: **PASS**. Vektor SVG mandiri bebas dari elemen script atau link jaringan eksternal, siap disematkan langsung pada laporan cetak A4.

## Pemeriksaan yang Dijalankan pada v1.5.1

1. **Uji Perataan Teks Rata Kanan-Kiri (Align Justify):**
   - Validasi: `python scripts/validate.py` dan `python scripts/validate.py --target DocsApp/laporan-reviu-skill.html`
   - Hasil: **PASS**. Aturan `text-align: justify; text-justify: inter-word; hyphens: auto;` terverifikasi pada template `assets/report-a4.html`, panduan cetak `references/html-print.md`, dan seluruh laporan HTML deliverable.
2. **Uji Validasi Paket Deliverable Lengkap (`--package-dir`):**
   - Uji Negatif (File HTML Tunggal): Validator berhasil menolak pengiriman yang hanya menyertakan berkas HTML tanpa `README.md` dan `sources/`, mengembalikan kode keluar 1.
   - Uji Positif (Paket Lengkap): Validator meloloskan paket yang memuat `README.md`, folder `sources/*.md`, dan `laporan-dokumentasi-aplikasi.html` terjustifikasi.
3. **Uji Anti-Kebocoran Meta-Instruksi & Kriteria (Anti-Leakage):**
   - Uji Negatif: Berkas HTML sintetis yang disusupi instruksi tombol cetak peramban (misal: "Instruksi Resmi Cetak Dokumen A4", pintasan Ctrl+P, Save as PDF) berhasil dideteksi dan ditolak oleh validator dengan kode keluar 1.
   - Uji Positif: Template `assets/report-a4.html` dan laporan deliverable terbukti bersih dari instruksi peramban dan kriteria internal.

## Pemeriksaan yang Dijalankan pada v1.5.0

1. **Uji Integritas Repositori Mandiri:**
   - Perintah: `python scripts/validate.py`
   - Hasil: **PASS**. Seluruh metadata frontmatter, panjang baris (`len(SKILL.md) < 500`), tautan relatif lintas berkas Markdown, keunikan heading tingkat dua (`## `), integritas anchor internal, dan aturan CSS cetak A4 terverifikasi valid.
2. **Uji Kekebalan Flag Optimasi Runtime Python (Anti-Bypass):**
   - Perintah: `python -O scripts/validate.py`
   - Hasil: **PASS**. Skrip tidak lagi menggunakan pernyataan `assert`. Evaluasi berbasis kondisional eksplisit dan `sys.exit(1)` tetap berjalan penuh meskipun flag optimasi `-O` aktif.
3. **Uji Keamanan Sanitasi HTML (Anti-XSS):**
   - Pengujian terhadap `SecureHTMLParser`:
     - Penolakan tag berbahaya: `<script>`, `<iframe>`, `<object>`, `<embed>`, `<applet>` menghasilkan kesalahan validasi keamanan.
     - Penolakan inline event handler: Atribut `onload`, `onerror`, `onclick`, dsb. ditolak secara mutlak.
     - Penolakan skema URI berbahaya: `javascript:` dan `data:text/html` berhasil dideteksi dan diblokir.
4. **Uji Antarmuka Baris Perintah `--target`:**
   - Perintah: `python scripts/validate.py --target DocsApp/laporan-reviu-skill.html`
   - Hasil: **PASS**. Berkas deliverable HTML nyata di folder `DocsApp/` terbukti memenuhi seluruh kontrak cetak A4 dan aturan keamanan tanpa dependensi eksternal.
5. **Uji Linter Keterlacakan (Traceability):**
   - Perintah: `python scripts/lint_traceability.py --help`
   - Hasil: **PASS**. Utilitas siap memindai dan mengevaluasi hubungan kanonikal antara `FR-xxx`, `NFR-xxx`, `TASK-xxx`, dan `TC-xxx`.

## Catatan Verifikasi Render v1.4 (Historis)

- Render template dengan Chromium **152.0.7977.64**, headless, tanpa header/footer bawaan.
- `pdfinfo`: PDF **8 halaman**, ukuran **594.96 × 841.92 pt (A4)**.
- `pdftotext`: teks dapat diekstrak; seluruh halaman berisi teks.
- Text bounding boxes seluruh halaman berada dalam area margin 3 cm dengan toleransi 1 pt.
- Font PDF aktual dari `pdffonts`: **Liberation Serif** (fallback sah untuk lingkungan tanpa Cambria proprietary).

## Batas Verifikasi

- Validator struktural dan keamanan tidak menggantikan audit visual desainer terhadap *page-break* dinamis pada tabel aplikasi yang sangat kompleks.
- Pengujian keterlacakan kode dan sertifikasi produk nyata tetap memerlukan bukti pengujian (*execution log*) dan audit kepatuhan oleh instansi/asesor berwenang.

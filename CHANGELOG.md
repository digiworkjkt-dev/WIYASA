# Changelog

## 1.6.3 — 2026-10-31: Eliminasi Total Rogue Header & Fixed Footers Bug (True Clean Margin Architecture)

- **Eliminasi Anomali Mispositioning Element Cetak Chromium (`position: fixed`):**
  - Mengidentifikasi akar masalah teks berjalan "WIYASA · SAKIP OTONOM+ — Buku Panduan Pengguna & Administrator" yang melayang di bawah judul bab (`h2`): mesin cetak Chromium salah memposisikan elemen HTML ber-`position: fixed` di area konten halaman alih-alih di kotak margin.
  - Menghapus seluruh elemen HTML `<footer class="running-footer">` dan aturan `position: fixed` dari seluruh berkas dokumen HTML cetak.
  - Mengalihkan implementasi running footer 100% murni ke CSS Paged Media standar `@page` margin boxes (`@bottom-left` & `@bottom-right`), menjamin isolasi total teks footer di dalam kotak margin peramban sehingga secara fisik mustahil menabrak atau menutupi judul bab (`h2`).
  - Menutup dokumen dengan elemen semantik `<footer class="document-end">` murni pada halaman terakhir.
- **Pembaruan Berkas Nyata SAKIP OTONOM+:**
  - Memperbarui secara langsung seluruh berkas aktif di direktori kerja pengguna: `D:\AI_LAB\Office\SAKIP OTONOM+\app-documentation\panduan-pengguna-aplikasi.html`, `laporan-arsitektur-dan-spesifikasi.html`, dan `laporan-dokumentasi-aplikasi.html`.
- **Pengetatan Aturan Validasi (`scripts/validate.py`):**
  - Menambahkan larangan mutlak penggunaan `position: fixed` saat `@media print` untuk mencegah kemunculan bug floating element serupa di masa depan.

## 1.6.2 ? 2026-10-31: Penghapusan Running Header demi Kebersihan Tata Letak Cetak (Header Elimination & Clean Footer-Only Layout)

- **Eliminasi Menyeluruh Elemen Running Header (Kop Atas Berulang):**
  - Menghapus elemen `.running-header` serta deklarasi `@top-left` dan `@top-right` pada `@page` dari seluruh dokumen dan template bawaan atas permintaan tata letak bersih.
  - Menghilangkan anomali rendering ganda dan tabrakan visual pada peramban per halaman cetak di mana teks kop atas saling bertumpuk dan menimpa judul bab (`h2`).
  - Menstandarisasi tata letak halaman A4 bersih: bagian atas halaman murni sebagai ruang margin kosong 3 cm (*clean top margin whitespace*), diikuti langsung oleh teks judul bab yang lapang dan mudah dibaca.
  - Menegaskan bahwa identitas resmi dokumen dan penomoran halaman ditempatkan secara eksklusif pada **Running Footer** di bagian bawah lembar dokumen (`bottom: -22mm;` / `@bottom-left` & `@bottom-right`).
- **Pengetatan Aturan Validasi (`scripts/validate.py`):**
  - Menambahkan aturan pencegahan otomatis yang secara eksplisit menolak penggunaan elemen `.running-header`, `@top-left`, `@top-right`, atau `position: fixed` dengan properti `top`.
- **Sinkronisasi Seluruh Dokumen:**
  - Memperbarui kerangka `assets/report-a4.html`, `assets/user-guide-a4.html`, paket `DocsApp/`, dan `app-documentation/`.

## 1.6.1 ? 2026-10-31: Perbaikan Layout Header Anti-Tabrakan Konten (Anti-Collision Architecture)

- **Eliminasi Cacat Tabrakan Visual Running Header Terhadap Konten Halaman:**
  - Menghilangkan bug di mana elemen kop atas/running header berulang menimpa judul bab (`h2`) dan paragraf pertama dokumen saat dicetak/preview.
  - Memposisikan running header secara presisi di ruang margin atas 3 cm (`position: fixed; top: -22mm; left: 0; right: 0; height: 8mm;` pada `@media print`).
  - Menerapkan aturan `white-space: nowrap; overflow: hidden; text-overflow: ellipsis; max-width: 48%;` pada seluruh elemen teks header guna mencegah teks judul panjang membungkus ke baris kedua yang membengkakkan tinggi header.
  - Menambahkan buffer aman `.chapter { break-before: page; padding-top: 8mm; }` pada `@media print` sehingga terdapat celah bersih 22 mm antara batas bawah header dan teks judul bab.
  - Memperbarui proteksi halaman cover (`.cover { break-after: page; min-height: 100vh; position: relative; z-index: 10; background: white; }`) agar running header tidak muncul pada lembar sampul dokumen.
- **Peningkatan Filter Validator (`scripts/validate.py`):**
  - Menambahkan deteksi otomatis yang menolak penggunaan `position: fixed` dengan `top: 0` atau nilai positif pada elemen header yang berisiko menimpa konten.
  - Mewajibkan penyertaan `white-space: nowrap` dan `text-overflow: ellipsis` pada kelas `.running-header`.
- **Sinkronisasi Template & Artefak Deliverable:**
  - Memperbarui `assets/report-a4.html`, `assets/user-guide-a4.html`, `DocsApp/`, dan `app-documentation/` dengan arsitektur header anti-tabrakan yang telah terverifikasi.

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

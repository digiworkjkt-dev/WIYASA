# app-documentation

Skill berbahasa Indonesia untuk membuat dan memperbarui dokumentasi pembangunan
aplikasi end-to-end. Versi **1.5.2**.

## Output

Paket deliverable menggunakan **Standar Opsi 2 (Pemisahan Dua Dokumen Berdasarkan Audiens)**:
1. **`app-documentation/README.md`**: Pintu masuk, ringkasan status, urutan baca, dan panduan cetak PDF.
2. **`app-documentation/sources/*.md`**: 18 berkas modular Markdown sebagai Single Source of Truth (SSOT) teknis pengembang di git.
3. **`app-documentation/laporan-arsitektur-dan-spesifikasi.html`**: Laporan teknis dan arsitektur lengkap bagi Tim Pengembang, Arsitek, dan Auditor.
4. **`app-documentation/panduan-pengguna-aplikasi.html`**: Buku panduan operasional mandiri bagi Klien, Pengguna Akhir, dan Administrator Sistem, **wajib dilengkapi tangkapan layar (screenshots) atau mockup antarmuka visual** pada alur-alur penting (Onboarding, Dashboard, Transaksi Utama, & Panel Admin).
(Catatan: Berkas `laporan-dokumentasi-aplikasi.html` tetap didukung sebagai opsi jika diminta satu dokumen master tunggal).

Cambria harus tersedia secara sah pada perangkat/engine cetak. Font fallback
dinyatakan jika Cambria tidak tersedia. Dukungan footer dan nomor halaman
bergantung pada browser atau engine; tidak dijanjikan lintas engine.
PDF diberikan hanya ketika engine tersedia dan hasil yang relevan telah diperiksa.

## Lokasi penyimpanan output

Seluruh output dokumen disimpan di folder **`app-documentation/`** relatif
terhadap root proyek/direktori kerja. Laporan utama:
`app-documentation/laporan-dokumentasi-aplikasi.html`.
Berkas sumber modular Markdown disimpan di `app-documentation/sources/`. PDF (jika
dihasilkan), lampiran, dan ZIP juga berada di folder output tersebut.

Folder output bukan folder instalasi skill `.agents/skills/app-documentation/`.
Saat menyerahkan hasil, skill wajib menyatakan lokasi penyimpanan dan nama
laporan aktual setelah keberadaan file diverifikasi.

## Cakupan

- Product brief, PRD, SRS/requirement, user stories dan acceptance criteria.
- UX, arsitektur, data model, API/integrasi, security/privacy.
- Backlog, delivery plan, testing/UAT, deployment/runbook, panduan pengguna.
- Traceability, decision log, standar/regulasi, mapping aktivitas SKKNI.

Skill hanya untuk dokumentasi pembangunan aplikasi. Tidak membuat portofolio
asesmen personel, paket uji kompetensi, sertifikasi, atau klaim kepatuhan otomatis.

## Pakai skill

Letakkan folder ini pada `.agents/skills/app-documentation/` di lingkungan yang
mendukung skill dengan format SKILL.md, atau tambahkan melalui mekanisme upload
skill workspace yang tersedia. Menyimpan file di repo publik tidak otomatis
menginstalnya pada semua percakapan.

Contoh instruksi:

> Gunakan app-documentation untuk membuat seluruh dokumen MVP aplikasi booking.
> Output laporan HTML A4, margin 3 cm, Cambria 12 pt. Tandai asumsi dan blocker.

> Perbarui dokumentasi aplikasi existing setelah perubahan izin admin.
> Pertahankan requirement ID dan sinkronkan laporan HTML serta sumber dokumen.

## Isi repository

- [Panduan Pengguna](PANDUAN_PENGGUNA.md): panduan operasional praktis memakai skill ini.
- [SKILL.md](SKILL.md): workflow, progressive loading, dan batas pekerjaan.
- [Katalog](references/catalog.md): dokumen dan struktur manifes.
- [Quality gates](references/quality-gates.md): audit lintas dokumen.
- [Standar Indonesia](references/standards-indonesia.md): SNI/regulasi/sumber resmi.
- [SKKNI](references/skkni-mapping.md): mapping unit ke aktivitas/artefak.
- [HTML dan cetak](references/html-print.md): kontrak format, strategi tabel lebar, dan batas engine.
- [Contoh](references/examples.md): skenario penggunaan dan acceptance checks.
- [Template Laporan Teknis](assets/report-a4.html): kerangka laporan arsitektur dan spesifikasi A4.
- [Template Panduan Pengguna](assets/user-guide-a4.html): kerangka buku panduan pengguna dan administrator mandiri.
- [Snippet Mockup UI](assets/snippets/ui-mockup-frame.svg): template visual layar aplikasi untuk panduan pengguna.
- [Snippet SVG](assets/snippets/): template SVG inline untuk arsitektur dan flowchart.
- [Changelog](CHANGELOG.md): riwayat perubahan versi.
- [Validasi](scripts/validate.py): validator mandiri integritas repo dan output HTML pengguna.
- [Linter Keterlacakan](scripts/lint_traceability.py): pemeriksa relasi FR -> TASK -> TC.
- [Catatan pengujian](TESTING.md): hasil pengujian, keamanan anti-XSS, dan batas verifikasi.

## Verifikasi

1. **Validasi Paket Deliverable Lengkap (Wajib):**
   ```sh
   python scripts/validate.py --package-dir app-documentation
   ```
   Memastikan folder deliverable memuat `README.md`, seluruh berkas `sources/*.md`, dan `laporan-dokumentasi-aplikasi.html` dengan styling A4, align justify, dan anti-XSS.

2. **Validasi Berkas HTML Spesifik:**
   ```sh
   python scripts/validate.py --target app-documentation/laporan-dokumentasi-aplikasi.html
   ```

3. **Verifikasi Keterlacakan (Traceability Linting):**
   ```sh
   python scripts/lint_traceability.py --dir app-documentation/sources
   ```

4. **Integritas Repositori Lokal:**
   ```sh
   python scripts/validate.py
   ```

Metadata/abstrak sumber SNI/ISO dan sebagian lampiran SKKNI telah diperiksa
pada 2026-10-05 dan diaudit kembali pada 2026-10-30. Baca referensi untuk batas lingkupnya.
Template ini tidak mendistribusikan teks lengkap standar atau font Cambria. Margin/font
adalah spesifikasi format pengguna, bukan klaim ketentuan SNI/SKKNI.

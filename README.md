# app-documentation

Skill berbahasa Indonesia untuk membuat dan memperbarui dokumentasi pembangunan
aplikasi end-to-end. Versi **1.5.0**.

## Output

Laporan HTML profesional self-contained: **A4 portrait, margin 3 cm di semua
sisi, Cambria 12 pt**, cover, metadata, daftar isi bertaut, bab terstruktur,
matriks keterlacakan, sumber dan panduan cetak/PDF.

Cambria harus tersedia secara sah pada perangkat/engine cetak. Font fallback
dinyatakan jika Cambria tidak tersedia. Dukungan footer dan nomor halaman
bergantung pada browser atau engine; tidak dijanjikan lintas engine.

Sumber kerja Markdown dapat dipertahankan. PDF diberikan hanya ketika engine
tersedia dan hasil yang relevan telah diperiksa.

## Lokasi penyimpanan output

Seluruh output dokumen disimpan di folder **`app-documentation/`** relatif
terhadap root proyek/direktori kerja. Laporan utama:
`app-documentation/laporan-dokumentasi-aplikasi.html`.
Sumber Markdown opsional berada di `app-documentation/sources/`. PDF (jika
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

- [SKILL.md](SKILL.md): workflow, progressive loading, dan batas pekerjaan.
- [Katalog](references/catalog.md): dokumen dan struktur manifes.
- [Quality gates](references/quality-gates.md): audit lintas dokumen.
- [Standar Indonesia](references/standards-indonesia.md): SNI/regulasi/sumber resmi.
- [SKKNI](references/skkni-mapping.md): mapping unit ke aktivitas/artefak.
- [HTML dan cetak](references/html-print.md): kontrak format, strategi tabel lebar, dan batas engine.
- [Contoh](references/examples.md): skenario penggunaan dan acceptance checks.
- [Template HTML](assets/report-a4.html): kerangka, bukan laporan selesai.
- [Snippet SVG](assets/snippets/): template SVG inline untuk arsitektur dan flowchart.
- [Changelog](CHANGELOG.md): riwayat perubahan versi.
- [Validasi](scripts/validate.py): validator mandiri integritas repo dan output HTML pengguna.
- [Linter Keterlacakan](scripts/lint_traceability.py): pemeriksa relasi FR -> TASK -> TC.
- [Catatan pengujian](TESTING.md): hasil pengujian, keamanan anti-XSS, dan batas verifikasi.

## Verifikasi

1. **Integritas Repositori Lokal:**
   ```sh
   python scripts/validate.py
   ```
   Memeriksa metadata frontmatter, heading unik, tautan relatif Markdown, aturan cetak CSS A4, dan keamanan sanitasi HTML (tanpa ketergantungan `assert`).

2. **Validasi Deliverable HTML Pengguna:**
   ```sh
   python scripts/validate.py --target app-documentation/laporan-dokumentasi-aplikasi.html
   ```

3. **Verifikasi Keterlacakan (Traceability Linting):**
   ```sh
   python scripts/lint_traceability.py --dir app-documentation/sources
   ```

Metadata/abstrak sumber SNI/ISO dan sebagian lampiran SKKNI telah diperiksa
pada 2026-10-05 dan diaudit kembali pada 2026-10-30. Baca referensi untuk batas lingkupnya.
Template ini tidak mendistribusikan teks lengkap standar atau font Cambria. Margin/font
adalah spesifikasi format pengguna, bukan klaim ketentuan SNI/SKKNI.

---
name: wiyasa
description: Membuat dan memperbarui paket dokumentasi aplikasi end-to-end—brief, PRD, SRS, UX, arsitektur, database, API, security, backlog, testing, deployment, dan panduan—dengan pemetaan standar industri, SNI, SKKNI, dan regulasi Indonesia berdasarkan sektor dan bukti. Gunakan untuk semua dokumen aplikasi, spesifikasi sebelum coding, handoff developer, dokumentasi mengacu SNI/SKKNI, atau sinkronisasi dokumen. Tidak menyatakan kepatuhan, kompetensi, atau sertifikasi tanpa bukti dan asesmen yang sesuai. Untuk hanya PRD/roadmap, gunakan product-manager bila tersedia.
---

# WIYASA ? App Documentation Engine

Versi skill: 1.5.0 — baseline referensi diverifikasi 2026-10-30.

Ubah kebutuhan aplikasi menjadi dokumen yang bisa dipakai mengambil keputusan,
mengimplementasikan, menguji, dan mengoperasikan aplikasi. Jangan sekadar mengisi
template atau memperbanyak dokumen. Kelengkapan berarti setiap kebutuhan relevan
tercakup, bukan setiap aplikasi membutuhkan semua jenis dokumen.

## Batas pekerjaan

- Hasil utama adalah dokumentasi, bukan implementasi aplikasi.
- Cakupan skill ini hanya dokumentasi pembangunan aplikasi. SKKNI dipakai
  sebagai acuan aktivitas dan kualitas artefak, bukan untuk membuat portofolio
  asesmen personel, formulir asesmen, paket uji kompetensi atau sertifikasi.
  Bukti yang dicatat terbatas pada sumber kode, keputusan, hasil uji, dan
  catatan operasi yang relevan untuk akurasi dokumentasi aplikasi.
- Jangan membuat repo, mengirim dokumen ke layanan eksternal, mengubah kode,
  menjalankan migrasi, atau melakukan deployment tanpa permintaan yang sesuai.
- Dokumentasi bukan bukti fitur sudah dibangun, diuji, aman, atau memenuhi regulasi.
- Ikuti bahasa pengguna; pertahankan nama field, endpoint, dan identifier teknis.
- Format Deliverable Standar Opsi 2 (Pemisahan Dua Dokumen Berdasarkan Audiens):
  1. `app-documentation/README.md`: Pintu masuk, ringkasan, urutan baca, status, dan panduan cetak PDF;
  2. `app-documentation/sources/*.md`: 18 berkas modular Markdown sebagai Single Source of Truth (SSOT) teknis pengembang;
  3. `app-documentation/laporan-arsitektur-dan-spesifikasi.html`: Dokumen arsitektur dan spesifikasi teknis lengkap bagi Tim Pengembang, Arsitek, dan Auditor (menggunakan template assets/report-a4.html);
  4. `app-documentation/panduan-pengguna-aplikasi.html`: Buku panduan operasional mandiri bagi Klien, Pengguna Akhir, dan Administrator Sistem (menggunakan template assets/user-guide-a4.html).
  (Catatan: Berkas `app-documentation/laporan-dokumentasi-aplikasi.html` tetap didukung sebagai opsi jika pengguna meminta 1 dokumen master gabungan).
  Seluruh dokumen HTML berformat A4 portrait, margin 3 cm, Cambria 12 pt, dan seluruh paragraf wajib rata kanan-kiri (align justify: `text-align: justify; text-justify: inter-word; hyphens: auto;`).
- Wajib Menyertakan Tangkapan Layar (Screenshots / UI Mockups):
  Pada panduan pengguna (`panduan-pengguna-aplikasi.html` dan `12-user-admin-guide.md`) serta alur UX (`04-ux-flows.md`), wajib menyertakan tangkapan layar (screenshots) atau mockup antarmuka visual (SVG/UI frames) pada bagian-bagian penting (halaman onboarding/login, dashboard utama, alur transaksi/fitur inti, dan panel admin) agar penjelasan menarik, konkret, dan mudah dipahami. Gunakan contoh `assets/snippets/ui-mockup-frame.svg` sebagai acuan saat frontend belum selesai di-coding.
  Diagram harus berupa SVG/image inline yang dapat dicetak (gunakan contoh pada assets/snippets/architecture-diagram.svg dan assets/snippets/flowchart-diagram.svg sebagai panduan), bukan sintaks Mermaid mentah pada laporan akhir.
- Ekspor PDF hanya jika engine tersedia dan hasilnya telah diperiksa. Dukungan
  footer dan nomor halaman bergantung pada browser/engine cetak; jangan
  menjamin nomor halaman lintas engine.
- Bila dokumentasi dapat diselesaikan sebagai file, kerjakan dan kirim file.
  Bila diminta membangun aplikasi yang akan terus dikembangkan, ikuti alur proyek
  pada lingkungan yang digunakan.

## Referensi

- Baca dokumen inti: [catalog.md](references/catalog.md), [quality-gates.md](references/quality-gates.md),
  dan [html-print.md](references/html-print.md) untuk kerangka dokumen, konsistensi, dan aturan cetak A4.
- Baca [examples.md](references/examples.md) jika perlu contoh requirement dan
  traceability, atau contoh pemilihan cakupan.
- Pemuatan bertahap (lazy-loading): baca [standards-indonesia.md](references/standards-indonesia.md)
  dan [skkni-mapping.md](references/skkni-mapping.md) terutama pada paket Standard/Extended
  atau jika ada kebutuhan regulasi/SKKNI eksplisit. Untuk paket Lean, screening ringkas
  dalam dokumen konteks/traceability sudah memadai.
- Gunakan [report-a4.html](assets/report-a4.html) sebagai kerangka presentasi output HTML.

## 1. Temukan konteks dan sumber kebenaran

Ambil informasi yang sudah ada di percakapan, lampiran, dokumen, dan codebase
yang diizinkan. Jangan meminta pengguna mengulang informasi yang bisa dibaca.
Periksa dokumentasi yang sudah ada sebelum menambah atau mengganti dokumen.

Bangun intake singkat:

| Area | Informasi yang dicari |
|---|---|
| Masalah | Siapa mengalami masalah apa, alur saat ini, hasil yang diinginkan |
| Produk | Web/mobile/API, produk baru atau existing, pengguna dan role |
| Cakupan | Fitur inti, batas MVP, non-goals, aturan bisnis |
| Data | Entitas utama, data sensitif, sumber data dan kepemilikan |
| Dependensi | Integrasi, platform, batasan stack, akses layanan |
| Delivery | Pembaca dokumen, ukuran tim, tenggat, kebutuhan handoff |
| Operasi | Skala yang diharapkan, availability, lingkungan deployment |
| Kepatuhan | Sektor, yurisdiksi, jenis operator, klasifikasi data, kewajiban kontrak, target standar/sertifikasi |

Jika informasi kritis kosong, ajukan satu pertanyaan terarah pada satu waktu,
menggunakan form bila tersedia. Pertanyaan kritis adalah keputusan yang jawabannya
mengubah scope, keamanan, model data, atau arsitektur secara material.
Untuk detail nonkritis, lanjutkan draft dengan asumsi yang terlihat.
Jika pengguna meminta langsung jadi, hindari interview panjang; hasilkan draft
dan daftar keputusan terbuka, tanpa memilih diam-diam hal yang berisiko.

Kelompokkan setiap input:
- **Confirmed:** pengguna menyatakan atau ada sumber yang dapat diverifikasi.
- **Observed:** ditemukan pada kode/dokumen, dengan lokasi dan batas verifikasi.
- **Proposed:** rekomendasi untuk dipertimbangkan, belum disetujui.
- **Assumed:** sementara agar draft bisa dilanjutkan.
- **Open:** membutuhkan keputusan atau bukti tambahan.

Kode menunjukkan implementasi pada revisi yang dibaca, bukan otomatis kondisi
production. Jika requirement dan implementasi berbeda, catat perbedaannya;
jangan menghapus salah satunya diam-diam.

## 2. Pilih cakupan

Gunakan kebutuhan, bukan jumlah halaman, untuk memilih:

- **Lean:** MVP kecil/solo. Gabungkan dokumen yang bertumpang tindih; tetap
  mencakup produk, requirement, UX, teknis, delivery, testing, dan operasi.
- **Standard:** default untuk permintaan "semua dokumen". Buat seluruh dokumen
  inti pada katalog, tetapi tiap dokumen hanya sedetail yang relevan.
- **Extended:** produk kompleks/multi-tim/berisiko tinggi. Tambahkan dokumen
  bersyarat dari katalog sesuai risiko yang nyata.

Nyatakan pilihan, alasan, daftar dokumen, dan dokumen bersyarat yang tidak relevan
di README. Jangan menambah compliance, billing, AI, atau multi-tenancy hanya
karena umum dipakai di aplikasi lain.

Selalu sertakan screening relevansi standar/regulasi. Untuk Standard/Extended,
buat `15-standards-compliance.md`; untuk Lean, section khusus dalam dokumen
konteks dan traceability cukup. Kedalaman kontrol mengikuti risiko, tetapi
screening dan pencatatan status bukti tidak boleh dihapus.

Sertakan screening SKKNI, terpisah dari compliance produk/organisasi.
Untuk Standard/Extended buat `16-skkni-competency-map.md`. Untuk Lean,
section pada delivery plan cukup. Tambahkan `17-developer-guide.md` saat ada
kode; sebelum coding hanya rencanakan struktur dan bukti yang diperlukan.

Wajib produksi dokumen panduan operasional: buat `12-user-admin-guide.md` pada
paket Standard/Extended (atau gabungkan pada seksi Operations & Guide untuk Lean)
yang memuat onboarding, walkthrough fitur utama per role, panduan administrasi sistem,
troubleshooting/FAQ, dan batasan sistem yang diketahui. Panduan pengguna tidak boleh
dilewatkan atau hanya disingkat menjadi satu kalimat.

## 2a. Tetapkan baseline industri dan regulasi

Ikuti standards-indonesia.md sebelum mendetailkan requirement:
1. Bedakan standar industri internasional, SNI adopsi nasional, hukum wajib,
   kewajiban kontrak, dan rekomendasi sukarela.
2. Verifikasi nomor/edisi/status SNI pada BSN; status ISO internasional tidak
   otomatis menentukan status edisi SNI. Jangan menambah prefix SNI tanpa bukti.
3. Tentukan relevansi terhadap produk, proses, organisasi, dan sektor. Untuk
   SNI wajib, temukan regulasi yang memberlakukan beserta lingkup/transisinya.
4. Rekam sumber, tanggal cek, akses teks penuh, dan hal yang belum terverifikasi.
5. Petakan kewajiban yang benar-benar dibaca ke requirement, kontrol, dokumen,
   test, bukti implementasi, owner, gap, dan action.

Jika hanya metadata/abstrak tersedia, gunakan sebagai acuan topik dan tandai
mapping masih tingkat topik, bukan pemeriksaan kesesuaian klausul.
Jika pengguna meminta jaminan kepatuhan, jelaskan batasnya dan tetap kerjakan
gap analysis yang tersedia; jangan menjanjikan sertifikasi atau audit legal.
Review ahli/auditor merupakan dependency ketika bukti atau interpretasi
regulasi melampaui ruang verifikasi yang tersedia.

SKKNI adalah acuan kompetensi kerja, bukan pengganti SNI atau regulasi produk.
Pilih unit relevan berdasarkan aktivitas, baca elemen/Kriteria Unjuk Kerja (KUK),
batasan variabel dan panduan penilaian sebelum mapping KUK. Metadata atau daftar
unit hanya cukup untuk mapping tingkat unit/topik. Pisahkan rencana artefak,
bukti pekerjaan nyata, review artefak, dan hasil asesmen orang.
Skill menghasilkan dokumentasi dan evidence plan, tidak menyatakan seseorang
kompeten atau tersertifikasi.
Evidence plan di sini hanya untuk verifikasi artefak aplikasi, bukan pengumpulan
portofolio kompetensi orang. Jangan meminta sertifikat atau profil kompetensi
personel untuk menyelesaikan paket dokumentasi ini.

## 3. Tetapkan kontrak bersama

Tulis glossary, role, batas scope, aturan bisnis, dan ID requirement sebelum
merinci desain. Gunakan ID stabil:

- `FR-001`: functional requirement.
- `NFR-001`: nonfunctional requirement.
- `US-001`: user story; `AC-001`: acceptance criterion.
- `TC-001`: test case; `TASK-001`: implementation task.
- `ADR-001`: architecture decision; `RISK-001`: risk; `ASM-001`: assumption.

Requirement adalah sumber kanonis untuk perilaku yang diminta. Dokumen teknis
menjelaskan cara memenuhinya; backlog bukan sumber fitur tambahan.
Pertahankan ID ketika revisi. Tandai requirement yang dicabut sebagai retired,
jangan gunakan ID-nya untuk arti baru.

Setiap requirement memuat prioritas, sumber/status, dan perilaku yang dapat diuji.
Setiap NFR memuat metrik, target, kondisi pengukuran, serta status target.
Target yang belum disepakati adalah usulan, bukan janji.

Tambahkan `STD-001` untuk acuan standar, `REG-001` untuk regulasi,
`CTRL-001` untuk kontrol, dan `EVD-001` untuk bukti. Requirement terkait
compliance harus menautkan acuan dan applicability decision; jangan sekadar
menulis "harus sesuai SNI".

## 4. Tulis dalam urutan dependensi

1. Brief, scope, glossary, asumsi, dan keputusan terbuka.
2. PRD, requirements, user stories, serta acceptance criteria.
3. UX/user flow, role-permission matrix, dan aturan state.
4. Arsitektur, data model, API/integrasi, security/privacy, serta ADR.
5. Backlog dan delivery plan berdasarkan requirement yang sama.
6. Test plan, UAT, deployment/runbook, serta panduan pengguna dan admin (12-user-admin-guide.md).
7. Traceability, audit konsistensi, indeks, dan changelog.

Gunakan tautan relatif antardokumen. Hindari mengulang aturan yang sama dalam
banyak file; rujuk sumber kanonis dan beri konteks singkat.

Untuk arsitektur baru, rekomendasikan solusi paling sederhana yang memenuhi
kebutuhan. Jelaskan tradeoff; jangan otomatis memilih microservices.
Untuk aplikasi existing, dokumentasikan hasil pengamatan dahulu dan pisahkan
usulan perubahan. Jika detail provider memengaruhi kontrak integrasi, verifikasi
dokumentasi resminya bila akses tersedia; bila tidak, tandai belum terverifikasi.

## 5. Aturan kedalaman

- Perinci jalur sukses serta validation, forbidden, not-found, empty, loading,
  retry, dan failure state yang relevan.
- Pastikan role-permission matrix dan isolasi data diterapkan pada backend,
  bukan sekadar menyembunyikan tombol.
- Tentukan lifecycle data, timezone, uang/mata uang, dan transaksi bila relevan.
- Jelaskan kontrak API termasuk input/output, error, pagination, otorisasi,
  idempotency, dan versioning sesuai kebutuhan.
- Jangan menulis secret atau data pengguna nyata di contoh. Gunakan data dummy.
- Jangan mengarang hasil riset, angka usage, benchmark, biaya, SLA, atau estimasi.
  Beri asumsi dan rentang untuk perkiraan yang memang diminta.
- Untuk data sensitif, jelaskan risiko dan kontrol; tandai review ahli yang perlu.
  Draft legal/privacy bukan nasihat hukum atau sertifikasi kepatuhan.
- Untuk integrasi yang belum tersedia, dokumentasikan dependency/blocker; jangan
  mengklaim terhubung atau menyarankan bypass persetujuan.

## 6. Audit dan status

Ikuti quality-gates.md. Buat matriks:

`Requirement → Story/AC → UX → Component/Data/API → Task → Test`.

Untuk kontrol relevan, perluas menjadi
`Standard/Regulation → Requirement → Control → Document → Test → Evidence → Gap/Owner`.
Rencana test bukan evidence test lulus; SOP bukan bukti SOP dijalankan.

Untuk SKKNI gunakan
`Unit/KUK → Aktivitas/Role usulan → Task → Artefak → Bukti kerja → Gap/Reviewer`.
Role hanya rekomendasi pembagian tugas, bukan paket/skema sertifikasi resmi.

Gunakan `N/A + alasan` jika suatu kolom tidak relevan. Missing berbeda dari N/A.
Setiap requirement MVP harus punya acceptance criterion, task, dan test atau
gap eksplisit. Tidak boleh ada requirement tambahan tersembunyi di backlog.

Pisahkan:
- kualitas dokumentasi: drafted / reviewed / needs-input;
- persetujuan pengguna: draft / in-review / approved;
- kondisi implementasi: proposed / observed / verified;
- kondisi pengujian: planned / executed-pass / executed-fail / blocked.

Jangan menandai approved tanpa persetujuan nyata atau executed-pass tanpa bukti.
Catat audit yang benar-benar dijalankan, temuan, dan batas pemeriksaannya.

## 7. Perbarui sebagai living documents

Saat fitur berubah, identifikasi requirement dan dokumen terdampak, lalu
perbarui requirement, UX, schema/API, security, task, test, dan panduan yang terkait.
Tambahkan changelog dan ADR bila keputusan teknis berubah secara material.
Pertahankan konten yang tidak terdampak dan jangan overwrite keputusan pengguna.
Jika dokumen approved berubah, status bagian terdampak kembali in-review;
jangan menganggap persetujuan lama berlaku pada perubahan.

## 8. Delivery

Simpan seluruh output dokumen di folder `app-documentation/` relatif terhadap
root proyek atau direktori kerja aktif untuk paket satu kali. Buat folder jika
belum ada. Folder output ini berbeda dari folder instalasi skill
`.agents/skills/app-documentation/`; jangan menaruh hasil laporan di folder skill.
Struktur deliverable WAJIB lengkap mencakup komponen Opsi 2 (Audiens Terpisah):
1. `app-documentation/README.md`: Pintu masuk, ringkasan, urutan baca, status, blocker, indeks dokumen, dan panduan cetak PDF.
2. `app-documentation/sources/*.md`: Seluruh berkas modular Markdown (00-context s.d. 17-developer-guide) ditulis lengkap sebagai SSOT.
3. `app-documentation/laporan-arsitektur-dan-spesifikasi.html`: Dokumen teknis dan arsitektur lengkap (menggunakan template `assets/report-a4.html`).
4. `app-documentation/panduan-pengguna-aplikasi.html`: Buku panduan pengguna dan administrator mandiri (menggunakan template `assets/user-guide-a4.html`) lengkap dengan screenshots/mockup visual antarmuka.
(Catatan: Berkas `app-documentation/laporan-dokumentasi-aplikasi.html` dapat digunakan jika pengguna secara spesifik meminta 1 dokumen master tunggal).

Paragraf naratif dan catatan pada HTML wajib rata kanan-kiri (align justify: `text-align: justify; text-justify: inter-word; hyphens: auto;`).
Validasi paket sebelum penyerahan menggunakan `python scripts/validate.py --package-dir app-documentation` untuk memastikan seluruh berkas lengkap, serta periksa keterlacakan melalui `python scripts/lint_traceability.py --dir app-documentation/sources`.
PDF yang benar-benar dihasilkan, lampiran, dan paket ZIP juga disimpan dalam folder output ini. Jangan menimpa file pengguna yang tidak terkait atau menghapus versi lama tanpa izin; gunakan penamaan versi bila diperlukan.

Gunakan manifest katalog sebagai sumber kerja dan susun laporan utama
`laporan-dokumentasi-aplikasi.html` dengan section/anchor sesuai urutan dokumen.
Jika ukuran laporan mengharuskan pemisahan, setiap HTML harus self-contained
dan memiliki indeks/panduan cetak. Tautkan versi/ID dokumen agar sumber Markdown
dan laporan HTML tidak saling bertentangan.
Wajib ada cover, metadata/status, daftar isi bertaut, ringkasan, bab terstruktur,
matriks/diagram teknis, sumber acuan, gap analitis, dan riwayat revisi (changelog).
DILARANG KERAS memasukkan petunjuk cetak peramban (misal: kotak petunjuk cetak, pintasan Ctrl+P / Cmd+P,
Save as PDF, dsb.) maupun kriteria/rubrik internal skill (Gate A?H, checklist prompt) ke dalam
badan dokumen aplikasi HTML atau berkas sumber Markdown. Dokumen aplikasi adalah produk deliverable
rekayasa perangkat lunak murni. Seluruh panduan teknis cetak diletakkan secara eksklusif pada
`app-documentation/README.md` pada bagian Panduan Cetak.
Font utama Cambria 12 pt; bila tidak terpasang, nyatakan fallback dan bahwa
hasil belum memenuhi persyaratan Cambria persis. Jangan menyertakan berkas
font proprietary tanpa lisensi.

Header tiap dokumen:

```markdown
# Judul dokumen
Status: Draft
Version: 0.1
Updated: YYYY-MM-DD
Owner: Belum ditentukan
Scope: MVP / Post-MVP / Mixed
Sources: Percakapan, file, atau referensi yang benar-benar digunakan
Related: Tautan relatif
```

Representasikan metadata tersebut sebagai blok metadata yang terbaca di HTML,
bukan menampilkan kode Markdown mentah. Default judul dan isi mengikuti
Cambria 12 pt; hierarki menggunakan weight, spacing, penomoran, dan warna
yang tetap terbaca dalam cetak hitam-putih.

Kirim file nyata melalui mekanisme delivery yang tersedia, bukan hanya tree
folder atau janji. ZIP boleh ditambahkan untuk paket banyak file.
Setelah file benar-benar tersimpan, wajib sertakan narasi penyerahan:
"Seluruh output dokumen disimpan di folder `app-documentation/`.
Laporan teknis tersedia di `app-documentation/laporan-arsitektur-dan-spesifikasi.html` (atau `app-documentation/laporan-dokumentasi-aplikasi.html`) dan panduan pengguna mandiri di `app-documentation/panduan-pengguna-aplikasi.html`."
Sesuaikan nama file dengan hasil aktual, sebutkan PDF hanya bila dihasilkan,
dan jangan menyatakan file tersimpan sebelum memverifikasi keberadaannya.
Ringkasan akhir memuat cakupan, keputusan terbuka yang menghambat build,
hasil audit, dan langkah berikut paling bernilai. Jangan mengklaim dokumen
siap implementasi tanpa menyebut blocker penting.

Untuk permintaan SNI, nyatakan apakah hasil baru berupa struktur mengacu
standar, mapping topik, atau mapping klausul yang telah direview. Bedakan
readiness dokumentasi dari kepatuhan produk/proses/organisasi.

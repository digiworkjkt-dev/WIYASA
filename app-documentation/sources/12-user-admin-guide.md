# Panduan Pengguna & Administrator (User & Admin Guide): SAKIP OTONOM+
Status: Reviewed
Version: 1.5.2
Updated: 2026-10-31
Owner: Technical Support & Training Specialist SAKIP OTONOM+
Scope: Standard
Sources: docs/05-panduan-pengguna/ (USER_GUIDE_SATKER.md, USER_GUIDE_EVALUATOR.md, USER_GUIDE_ADMIN.md)
Related: README.md, 04-ux-flows.md, 11-deployment-runbook.md

## 1. Panduan Pengguna Satuan Kerja (Satker Guide)

### 1.1 Masuk ke Sistem (Login)
1. Akses portal resmi SAKIP OTONOM+ di peramban web (rekomendasi: Google Chrome / Microsoft Edge versi mutakhir).
2. Masukkan Nomor Induk Pegawai (NIP) 18 digit resmi BMKG dan kata sandi yang telah diberikan.
3. Bila baru pertama kali login, sistem akan mengarahkan Anda ke halaman `/ubah-password` untuk membuat kata sandi baru (minimal 8 karakter kombinasi huruf dan angka).
4. *Mockup Visual Antarmuka Login*: Tersedia representasi visual interaktif pada berkas deliverable `panduan-pengguna-aplikasi.html` dan aset `assets/mockup-login.svg`.

### 1.2 Prosedur Penggantian Kata Sandi Awal (/ubah-password)
1. Bila pertama kali login atau setelah kata sandi di-reset, sistem secara otomatis mengarahkan ke rute `/ubah-password`.
2. Masukkan kata sandi sementara saat ini (bawaan default: `satkerbmkg`).
3. Masukkan kata sandi baru dengan ketentuan minimal 8 karakter kombinasi huruf besar, huruf kecil, dan angka numerik.
4. Masukkan ulang kata sandi baru pada kolom konfirmasi dan klik tombol **Simpan Kata Sandi & Buka Dasbor Utama**.
5. *Mockup Visual Formulir Ubah Kata Sandi*: Tersedia representasi visual interaktif Gambar 2.2 pada berkas `panduan-pengguna-aplikasi.html`.

### 1.3 Mengunggah Dokumen Bukti Kinerja
1. Buka menu **Daftar Evaluasi** (`/evaluations`) dan pilih baris tahun evaluasi yang sedang berjalan.
2. Klik tombol **Lihat Detail** untuk membuka lembar kerja satker.
3. Pada tab **Dokumen Pendukung**, klik tombol **Unggah Dokumen**.
4. Pilih kategori berkas yang sesuai:
   - `RENSTRA`: Rencana Strategis 5 tahunan.
   - `IKU`: Indikator Kinerja Utama UPT.
   - `PK`: Perjanjian Kinerja tahun berjalan (beserta Lampiran PK).
   - `RENJA`: Rencana Kerja Tahunan.
   - `LKJIP`: Laporan Kinerja Instansi Pemerintah tahun evaluasi.
   - `MONEV`: Laporan Pemantauan/Evaluasi Berkala (Triwulanan/Semesteran).
5. Pilih file dari komputer Anda (format PDF/DOCX/XLSX, ukuran maksimal 50 MB) dan klik **Kirim Berkas**.
6. Periksa status berkas pada tabel: status `COMPLETED` menandakan dokumen telah berhasil dipindai dan diproses oleh mesin ekstraksi.
7. *Mockup Visual Lembar Kerja Eviden*: Tersedia representasi visual interaktif pada `panduan-pengguna-aplikasi.html` dan aset `assets/mockup-satker-upload.svg`.

---

## 2. Panduan Evaluator Inspektorat (Evaluator Guide)

### 2.1 Menelaah Usulan AI pada LKE Digital
1. Masuk menggunakan akun Evaluator dan buka menu **Daftar Evaluasi**.
2. Filter daftar berdasarkan satker binaan yang ditugaskan kepada Anda.
3. Buka halaman evaluasi satker dan klik tab **Lembar Kerja Evaluasi (LKE)**.
4. Anda akan melihat 4 komponen utama:
   - Komponen 1: Perencanaan Kinerja (Bobot 30%)
   - Komponen 2: Pengukuran Kinerja (Bobot 30%)
   - Komponen 3: Pelaporan Kinerja (Bobot 15%)
   - Komponen 4: Evaluasi Akuntabilitas Kinerja Internal (Bobot 25%)
5. Kriteria dengan nilai usulan AI akan menampilkan lencana nilai (A, BB, B, C, D) dan kutipan kalimat bukti dari dokumen satker lengkap dengan nomor halaman.
6. *Mockup Visual Telaah LKE*: Tersedia representasi visual interaktif pada `panduan-pengguna-aplikasi.html` dan aset `assets/mockup-evaluator-lke.svg`.

### 2.2 Melakukan Override dan Menerbitkan Catatan Audit
1. Jika bukti yang disajikan AI sudah sangat tepat, klik tombol **Accept AI**.
2. Jika menurut pertimbangan profesional bukti belum mencukupi atau satker layak mendapat nilai lebih tinggi, klik tombol **Override Skor**.
3. Pilih nilai baru (misal: dari B menjadi BB) dan **wajib** mengisi kolom *Catatan Pertimbangan Evaluator* sebagai pertanggungjawaban audit.
4. Klik **Simpan Nilai**: skor total subkomponen dan predikat SAKIP satker akan langsung terkalkulasi ulang seketika.

### 2.3 Menyusun Rekomendasi & Finalisasi LHE
1. Buka tab **Temuan & Rekomendasi**.
2. Tinjau draf temuan yang disusun sistem dan sesuaikan rumusan kalimat rekomendasi agar aplikatif bagi pimpinan satker.
3. Klik tombol **Pratinjau Draf LHE** untuk membaca laporan formal 5 Bab BMKG.
4. Jika seluruh kriteria telah tervalidasi, klik tombol **Finalisasi Evaluasi** -> Status evaluasi berubah menjadi `READY_FOR_SIGNATURE` dan formulir terkunci dari perubahan lebih lanjut.

---

## 3. Panduan Administrator Sistem (Admin Guide)

### 3.1 Manajemen Periode & Kalender Unggah
1. Buka menu **Admin -> Periode Evaluasi** (`/admin/periods`).
2. Klik **Tambah Periode Baru** dan tentukan tahun anggaran (misal: `2026`).
3. Tentukan tanggal `Buka Unggah (upload_open_at)` dan `Tutup Unggah (upload_close_at)`.
4. Setelah tanggal tutup terlewati, tombol unggah dokumen pada sisi satker otomatis dinonaktifkan oleh sistem.

### 3.2 Penugasan Evaluator ke Satker
1. Buka menu **Admin -> Penugasan Evaluator** (`/admin/assignments`).
2. Pilih nama pegawai Evaluator dari daftar ASN Inspektorat.
3. Pilih daftar satker binaan (UPT) yang menjadi tanggung jawab telaah evaluator tersebut dan klik **Simpan Penugasan**.

### 3.3 Konfigurasi Penyimpanan Google Shared Drive
1. Buka menu **Admin -> Penyimpanan Data** (`/admin/storage`).
2. Masukkan ID folder Google Shared Drive untuk periode aktif.
3. Klik tombol **Uji Koneksi Storage** untuk memverifikasi keabsahan izin token tanpa membocorkan kredensial.
4. *Mockup Visual Panel Admin Storage*: Tersedia representasi visual interaktif pada `panduan-pengguna-aplikasi.html` dan aset `assets/mockup-admin-storage.svg`.

---

## 4. Pemecahan Masalah (Troubleshooting) & Batasan yang Diketahui

| Gejala Masalah | Kemungkinan Penyebab | Tindakan Solusi |
|---|---|---|
| Satker gagal mengunggah dokumen | Ukuran file > 50 MB atau jenis file executable | Kompres ukuran PDF atau pastikan ekstensi asli PDF/DOCX/XLSX |
| Parsing dokumen berstatus `FAILED` | Berkas PDF hasil scan foto buram tanpa teks OCR | Unggah ulang berkas PDF teks asli atau klik tombol *Reprocess Document* |
| Nilai evaluasi tidak berubah setelah override | Koneksi internet terputus saat request PATCH | Muat ulang peramban web dan periksa log riwayat audit |
| LHE tidak dapat difinalisasi | Masih ada kriteria bertanda anomali belum ditinjau | Buka tab *Exceptions Needing Review* dan tuntaskan kriteria yang tersisa |


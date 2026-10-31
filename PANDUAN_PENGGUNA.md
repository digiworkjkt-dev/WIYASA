# Panduan Pengguna: WIYASA (v1.6.0)

Selamat datang di Panduan Pengguna resmi **WIYASA** (sistem dokumentasi rekayasa perangkat lunak terpadu). Dokumen ini menjelaskan cara mengoperasikan skill WIYASA untuk memproduksi paket dokumentasi aplikasi end-to-end secara terstandarisasi, lengkap, dan siap rilis.

---

## 1. Pengenalan Skill WIYASA

**WIYASA** adalah modul keahlian AI untuk merancang, menyusun, dan memperbarui seluruh dokumentasi teknis dan bisnis perangkat lunak secara profesional.

### Prinsip Utama Deliverable
1. **Paket Lengkap Multi-Berkas:** Setiap eksekusi wajib menghasilkan struktur paket lengkap, bukan hanya satu berkas HTML saja.
2. **Single Source of Truth (SSOT):** Berkas modular Markdown pada folder `sources/` menjadi acuan kerja teknis tim pengembang.
3. **Format Cetak Eksekutif A4:** Laporan utama HTML monolit siap cetak fisik maupun simpan sebagai PDF resmi (A4 Portrait, Margin 3 cm, Font Cambria 12 pt, seluruh paragraf rata kanan-kiri / *align justify*).
4. **Bebas Meta-Instruksi:** Dokumen aplikasi murni berisi substansi teknis/bisnis aplikasi tanpa disusupi instruksi tombol peramban atau kriteria evaluasi internal.

---

## 2. Struktur Paket Dokumen yang Diproduksi

Seluruh hasil dokumentasi aplikasi secara otomatis disimpan pada folder **`app-documentation/`** di direktori kerja proyek pengguna:

```text
app-documentation/
├── README.md                              <- Pintu masuk, ringkasan status, & panduan cetak PDF
├── laporan-dokumentasi-aplikasi.html     <- Laporan gabungan eksekutif siap cetak A4
└── sources/                               <- Berkas modular Markdown (SSOT Pengembang)
    ├── 00-context.md                     <- Intake, glossary, role, & asumsi
    ├── 01-product-brief.md               <- Masalah, target pengguna, & MVP scope
    ├── 02-prd.md                         <- Use case, prioritas fitur, & metrik produk
    ├── 03-requirements.md                <- Kebutuhan FR/NFR ber-ID & acceptance criteria
    ├── 04-ux-flows.md                    <- Sitemap, user journey, & role-permission matrix
    ├── 05-architecture.md                <- Arsitektur sistem & diagram komponen
    ├── 06-data-model.md                  <- ERD, skema database, constraints, & retensi
    ├── 07-api-integrations.md            <- Kontrak endpoint API, payload, & autentikasi
    ├── 08-security-privacy.md            <- Threat model, kontrol akses, & kepatuhan UU PDP
    ├── 09-delivery-plan.md               <- Milestone, backlog, & task ber-ID
    ├── 10-test-plan.md                   <- Skenario uji unit/integrasi/sistem & UAT
    ├── 11-deployment-runbook.md          <- Lingkungan, konfigurasi, backup, & go-live
    ├── 12-user-admin-guide.md            <- PANDUAN PENGGUNA & ADMINISTRATOR SISTEM
    ├── 13-traceability.md                <- Matriks keterlacakan FR -> TASK -> TC
    ├── 14-decision-log.md                <- Log keputusan arsitektur (ADR) & changelog
    ├── 15-standards-compliance.md        <- Register kepatuhan standar industri / SNI
    ├── 16-skkni-competency-map.md        <- Pemetaan unit kompetensi SKKNI
    └── 17-developer-guide.md             <- Panduan kode & setup dev (bila kode tersedia)
```

---

## 3. Cara Menggunakan Skill (Panduan Prompt)

Anda dapat memicu skill ini melalui instruksi percakapan. Berikut adalah contoh instruksi berdasarkan kebutuhan:

### Skenario A: Produksi Paket Dokumentasi Baru (Default Standard)
> *"Gunakan skill WIYASA untuk menyusun dokumentasi lengkap aplikasi booking lapangan olahraga, mulai dari spesifikasi produk, arsitektur, database, API, hingga panduan pengguna. Output paket lengkap pada folder app-documentation."*

### Skenario B: Paket Ringkas untuk MVP Cepat (Lean)
> *"Gunakan WIYASA dengan cakupan Lean untuk mendokumentasikan MVP portal internal monitoring presensi pegawai. Fokus pada requirement inti, skema database, alur UX, dan panduan pengguna."*

### Skenario C: Pembaruan Fitur Aplikasi Existing
> *"Perbarui dokumentasi pada folder app-documentation karena ada penambahan fitur pembatalan transaksi oleh Admin. Pastikan ID requirement tetap stabil, dan sinkronkan berkas sumber Markdown serta laporan HTML."*

---

## 4. Rincian Produksi Dokumen Panduan Pengguna (User Guide)

Dokumen **`panduan-pengguna-aplikasi.html`** dan **`12-user-admin-guide.md`** wajib menyertakan **tangkapan layar (screenshots) atau mockup antarmuka visual** pada alur-alur penting (Onboarding, Dashboard, Alur Transaksi Inti, dan Panel Admin) agar panduan menarik dan mudah dipahami oleh pengguna non-teknis.

Dokumen ini memuat 5 bagian esensial:

1. **Alur Onboarding & Akses Akun:**
   - Prosedur registrasi dan aktivasi akun baru.
   - Tata cara login, reset kata sandi, dan autentikasi multi-faktor (bila ada).
   - Hak istimewa dan batasan akses sesuai role pengguna.
2. **Panduan Operasional Fitur Utama (User Walkthrough):**
   - Panduan langkah-demi-langkah pengoperasian fitur utama aplikasi untuk setiap role (misal: cara membuat reservasi, cara mencari jadwal, cara mengunduh laporan).
   - Penanganan kesalahan input umum (*form validation errors*).
3. **Panduan Administrator Sistem:**
   - Prosedur manajemen pengguna (tambah, nonaktifkan, atau ubah role).
   - Pengaturan parameter sistem dan konfigurasi master data.
   - Pemantauan aktivitas sistem melalui audit log dan persetujuan transaksi.
4. **Penanganan Kendala (Troubleshooting & FAQ):**
   - Daftar pertanyaan yang sering diajukan (FAQ).
   - Arti kode kesalahan sistem yang tampak pada layar pengguna beserta langkah perbaikan mandiri.
5. **Batasan Sistem (Known Limitations):**
   - Batasan operasional sistem saat ini (misal: kapasitas maksimal unggah berkas, jam operasional layanan pihak ketiga).
   - Perilaku fitur yang masih berstatus rencana (*planned behavior*).

---

## 5. Cara Validasi dan Verifikasi Mutu Otomatis

Setelah dokumentasi selesai diproduksi oleh agen, lakukan verifikasi mandiri menggunakan perkakas validator yang tersedia di repositori:

### 1. Verifikasi Kelengkapan Paket Deliverable
Perintah ini memastikan berkas `README.md`, folder `sources/`, dan `laporan-dokumentasi-aplikasi.html` tersedia secara lengkap:
```sh
python scripts/validate.py --package-dir app-documentation
```

### 2. Verifikasi Keterlacakan Matriks Kebutuhan
Perintah ini memindai apakah seluruh kebutuhan fungsional (`FR-xxx`) telah memiliki pasangan tugas implementasi (`TASK-xxx`) dan kasus uji (`TC-xxx`):
```sh
python scripts/lint_traceability.py --dir app-documentation/sources
```

---

## 6. Panduan Cetak dan Ekspor PDF A4

Untuk mengekspor laporan HTML menjadi berkas PDF resmi yang bersih:

1. Buka berkas `app-documentation/laporan-dokumentasi-aplikasi.html` di browser (Google Chrome, Microsoft Edge, atau Mozilla Firefox).
2. Tekan kombinasi tombol **Ctrl + P** (Windows) atau **Cmd + P** (macOS).
3. Pada opsi pencetak (*Destination*), pilih **Save as PDF**.
4. Atur ukuran kertas (*Paper Size*) ke **A4 Portrait (210 x 297 mm)**.
5. Pada pengaturan margin, pilih **Default / CSS Margins (3 cm di semua sisi)**.
6. **PENTING:** Nonaktifkan centang pada opsi **Headers and footers** bawaan peramban agar URL web atau tanggal peramban tidak mengotori tepi kertas.
7. Aktifkan centang pada **Background graphics** agar arsiran tabel dan diagram tampil sempurna.
8. Klik **Save** untuk menyimpan PDF resmi.

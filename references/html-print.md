# HTML profesional A4 dan aturan cetak/PDF

## Kontrak output

- Simpan laporan di `app-documentation/laporan-dokumentasi-aplikasi.html`.
  Simpan PDF/lampiran/ZIP terkait dalam folder output `app-documentation/`;
  jelaskan lokasi tersebut saat penyerahan setelah file diverifikasi.
- Output primer: HTML self-contained dengan CSS inline, tanpa CDN, analytics,
  remote font, atau dependensi jaringan.
- Layout kertas: A4 portrait (210 × 297 mm).
- Margin cetak: 3 cm pada keempat sisi; area isi nominal 150 × 237 mm.
- Font utama: Cambria, 12 pt. Semua teks termasuk tabel mengikuti 12 pt;
  hierarki default dibedakan dengan weight/spacing, bukan mengecilkan tabel.
- Line-height default 1.5, warna teks gelap, accent terbatas, heading bernomor,
  tabel dengan header jelas dan kontras memadai.
- Perataan teks (Text Alignment):
  Seluruh paragraf naratif, deskripsi metadata, dan notice box wajib menggunakan
  rata kanan-kiri (\	ext-align: justify; text-justify: inter-word; hyphens: auto;\)
  sesuai kaidah baku tata naskah laporan formal Indonesia. Judul dan header tabel
  tetap rata kiri.
- Paket lengkap wajib: Deliverable akhir tidak boleh hanya berupa berkas HTML tunggal;
  wajib menyertakan \README.md\ (katalog & status) dan seluruh berkas modular Markdown
  di folder \pp-documentation/sources/\ sebagai Single Source of Truth (SSOT).
- Cover, metadata, status, TOC bertaut, executive summary, bab, sources,
  assumptions/gaps, dan riwayat revisi (changelog).
- Mulai dari [report-a4.html](../assets/report-a4.html); ganti konten contoh dengan isi nyata.
  Template adalah kerangka, bukan laporan selesai.

## Visual Screenshots dan UI Mockups

Panduan pengguna (`panduan-pengguna-aplikasi.html`) dan alur UX (`04-ux-flows.md`) wajib menyertakan tangkapan layar (screenshot) atau mockup visual (SVG/UI frame) pada bagian-bagian krusial:
1. Layar Onboarding dan Form Login
2. Dashboard Utama Pengguna
3. Alur Transaksi / Operasi Utama (Langkah-demi-langkah)
4. Panel Konfigurasi Administrator

Format tampilan gambar pada HTML cetak A4 dibungkus dengan wadah berikut:

```html
<div class="screenshot-frame">
  <img src="assets/images/dashboard-user.png" alt="Tampilan Dashboard Pengguna">
  <div class="figure-caption">Gambar 3.1: Antarmuka dashboard utama pengguna dan widget ringkasan.</div>
</div>
```

Jika aplikasi belum di-coding, gunakan blok visual SVG seperti pada `assets/snippets/ui-mockup-frame.svg` agar dokumen tetap memiliki ilustrasi visual antarmuka yang nyata.

## CSS wajib

```css
@page { size: A4 portrait; margin: 3cm; }
body {
  font-family: Cambria, "Times New Roman", serif;
  font-size: 12pt;
  line-height: 1.5;
}
@media print {
  html, body { margin: 0; padding: 0; }
  .report { width: auto; max-width: none; padding: 0; margin: 0; }
  .screen-only { display: none !important; }
  .chapter { break-before: page; page-break-before: always; }
  h1, h2, h3 { break-after: avoid; page-break-after: avoid; }
  p, li { orphans: 3; widows: 3; text-align: justify; text-justify: inter-word; hyphens: auto; }
  thead { display: table-header-group; }
  tr { break-inside: avoid; page-break-inside: avoid; }
  img, svg { max-width: 100%; height: auto; }
}
```

Jangan gabungkan padding body 3 cm dengan @page margin 3 cm; margin akan ganda.
Jangan memaksakan seluruh bab/tabel panjang `break-inside: avoid`.
Elemen yang lebih tinggi dari area isi harus boleh pecah.

Untuk layar desktop, gunakan container 210 mm dengan padding 30 mm dan
box-sizing border-box. Tampilan layar tidak membuktikan pagination cetak.
Di layar sempit gunakan layout responsif, tanpa mengubah @page.

## Font

Cambria bukan font yang pasti tersedia pada setiap OS atau container.
- Tulis font stack Cambria sebagai pilihan pertama.
- Periksa font lokal/computed font bila engine tersedia.
- Fallback Times New Roman/serif adalah degradasi yang harus dilaporkan,
  bukan pemenuhan Cambria persis.
- Jangan mendownload, embed atau redistribusi Cambria tanpa izin/lisensi.
- Jika font diberikan secara sah untuk dokumen, periksa izin embedding;
  jangan memasukkan font tersebut ke repo publik secara otomatis.

## Tabel, diagram, dan kode

- Lebar konten tidak boleh melebihi area 150 mm saat dicetak.
- Gunakan `overflow-wrap: anywhere`, `table-layout: fixed`, judul kolom ringkas,
  dan padding kecil. Jangan mengecilkan font tabel dari 12 pt untuk memaksa muat.
- **Strategi Matriks Lebar (≥ 5 kolom):**
  Area cetak horizontal 150 mm tidak memadai untuk tabel dengan 6–11 kolom pada font
  Cambria 12 pt. Terapkan salah satu strategi berikut:
  1. *Sub-tabel terhubung:* Pecah matriks menjadi 2 tabel yang berbagi kolom kunci ID
     (misal Tabel A: `Req ID | Statement | Priority | AC`, Tabel B: `Req ID | Task | Test Case | Status`).
  2. *Format Blok/Kartu (Definition List `<dl>`):* Gunakan blok bertingkat per ID
     requirement yang memuat rincian relasi komponen, API, task, dan test.
- Ubah payload/kode lebar menjadi baris pendek atau block wrap; pilih keterbacaan.
- Tabel besar boleh lintas halaman; ulang header sesuai dukungan engine.
- Diagram inline SVG menggunakan viewBox dan kontras aman. Jangan sisipkan
  diagram mentah yang belum dirender atau memerlukan jaringan untuk muncul.
  Gunakan referensi snippet pada `assets/snippets/architecture-diagram.svg` dan
  `assets/snippets/flowchart-diagram.svg` sebagai panduan geometris dan tipografi.
- Escape konten pengguna sebagai teks; sanitasi HTML/SVG bila menerima markup.
  Dilarang keras memuat tag `<script>`, `<iframe>`, `<object>`, atau atribut
  event handler (`onload`, `onerror`, `onclick`).

## Larangan Running Header dan Standar Running Footer Bersih

**Aturan Baku Tata Naskah WIYASA:**
- **DILARANG KERAS menggunakan Running Header (kop atas berulang).**
  Penggunaan running header terbukti menyebabkan rendering ganda dan tabrakan visual (*content overlap*) pada peramban web modern, terutama saat jeda halaman (*page break*) di mana garis dan teks header menimpa judul bab (`h2`) dan teks isi dokumen.
- Seluruh dokumen cetak A4 resmi WIYASA menerapkan tata letak bersih (*clean top margin*):
  1. **Bagian Atas Halaman:** Bersih total tanpa kop berulang. Margin atas 3 cm murni sebagai ruang kosong bernapas (*whitespace*), langsung diikuti oleh judul bab.
  2. **Bagian Bawah Halaman (Running Footer):** Seluruh identitas dokumen dan nomor halaman ditempatkan secara eksklusif di bagian bawah lembar dokumen (`bottom: -22mm;` / `@bottom-left` & `@bottom-right`).

### Implementasi Standar CSS Running Footer Tunggal:

```css
/* 1. Aturan CSS Paged Media Standar (@page) */
@page {
  size: A4 portrait;
  margin: 3cm;
  @bottom-left {
    content: "WIYASA ? Dokumentasi Resmi Aplikasi";
    font-family: Cambria, "Times New Roman", serif;
    font-size: 8.5pt;
    color: #64748b;
    vertical-align: top;
    padding-top: 2mm;
    border-top: 0.5pt solid #cbd5e1;
  }
  @bottom-right {
    content: "Halaman " counter(page);
    font-family: Cambria, "Times New Roman", serif;
    font-size: 8.5pt;
    color: #64748b;
    vertical-align: top;
    padding-top: 2mm;
    border-top: 0.5pt solid #cbd5e1;
  }
}
@page :first {
  @bottom-left { content: none; }
  @bottom-right { content: none; }
}

/* 2. Tampilan Layar (Screen View) */
.running-footer {
  margin-top: 15mm;
  padding-top: 3mm;
  border-top: 0.5pt solid #cbd5e1;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-family: Cambria, "Times New Roman", serif;
  font-size: 8.5pt;
  color: #64748b;
}

/* 3. Pengulangan Cetak Peramban Bebas Masalah (@media print) */
@media print {
  html, body { background: white; margin: 0; padding: 0; }
  .report { width: auto; max-width: none; padding: 0; margin: 0; box-shadow: none; }
  .screen-only { display: none !important; }
  .chapter { break-before: page; page-break-before: always; }
  h1, h2, h3 { break-after: avoid; page-break-after: avoid; }
  p, li { orphans: 3; widows: 3; text-align: justify; text-justify: inter-word; hyphens: auto; }
  thead { display: table-header-group; }
  tr { break-inside: avoid; page-break-inside: avoid; }
  .notice { background: none; }
  a { color: inherit; }

  /* Running Footer Cetak: Ditempatkan presisi di dalam margin bawah 3cm */
  .running-footer {
    position: fixed;
    bottom: -22mm;
    left: 0;
    right: 0;
    height: 10mm;
    margin: 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 0.5pt solid #cbd5e1;
    padding-top: 2mm;
    font-size: 8.5pt;
    color: #64748b;
    background: transparent;
  }
}
```

## Pemisahan panduan cetak dan konten dokumen

**Aturan Mutlak (Anti-Leakage):**
- Seluruh instruksi operasional peramban (misal: tombol Ctrl+P / Cmd+P, opsi Save as PDF,
  nonaktifkan header/footer, dsb.) **DILARANG KERAS** dimasukkan ke dalam badan dokumen
  aplikasi HTML (`laporan-dokumentasi-aplikasi.html`) maupun berkas sumber Markdown (`sources/*.md`).
- Kriteria evaluasi internal skill (Gate A s.d. Gate H, checklist prompt, rubrik nilai)
  juga **DILARANG** dimasukkan ke dalam dokumen aplikasi.
- Dokumen aplikasi adalah deliverable bisnis/teknis murni (PRD, SRS, Arsitektur, dsb.).
- Seluruh panduan cara membuka dan mencetak laporan HTML ditempatkan secara eksklusif
  pada **`app-documentation/README.md`** di bawah seksi `## Panduan Cetak / Ekspor PDF`.

## QA dan batas verifikasi

Periksa statis: struktur HTML, tautan/anchor, CSS ukuran/margin/font, konten
tanpa placeholder tak berlabel, self-contained, diagram dan sanitasi.
Jika engine tersedia, render ke PDF lalu cek A4, jumlah halaman, font aktual,
text extraction serta overflow. Pemeriksaan PDF teks tidak menggantikan
pemeriksaan visual page break, clipping dan footer.
Jika render belum diuji, tulis demikian; jangan mengklaim "PDF terverifikasi".

Catat pada delivery:
`Engine/version | Paper/margins/scale | Font requested/actual |
Footer mode | Checks run | Known limitations`.

Spesifikasi cetak ini adalah permintaan format pengguna, bukan klaim bahwa
SNI atau SKKNI mewajibkan margin 3 cm atau Cambria 12 pt.

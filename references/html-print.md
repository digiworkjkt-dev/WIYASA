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
- Cover, metadata, status, TOC bertaut, executive summary, bab, sources,
  assumptions/gaps, changelog, serta panduan cetak.
- Mulai dari [report-a4.html](../assets/report-a4.html); ganti konten contoh dengan isi nyata.
  Template adalah kerangka, bukan laporan selesai.

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
  p, li { orphans: 3; widows: 3; }
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

## Footer dan nomor halaman

Dukungan footer dan nomor halaman bergantung pada browser/engine cetak.
Catat engine/versi yang benar-benar dipakai; jangan mengklaim lintas browser.

Pilihan:
1. **Browser biasa:** header/footer bawaan dapat dipakai bila tersedia, tetapi
   dapat menampilkan URL/path, mengubah area cetak, atau berbeda antar browser.
   Default matikan header/footer bawaan untuk laporan bersih.
2. **CSS paged media:** `@page` margin boxes/counter(page) hanya jika engine
   mendukung dan hasil uji memperlihatkan nomor halaman yang benar.
3. **Engine PDF:** gunakan template footer/pagination milik engine bila tersedia,
   tanpa menggandakan footer CSS. Periksa posisi dan konsistensi margin.

Template bawaan sengaja tidak membuat fixed footer di setiap halaman. Fixed
footer dapat menimpa isi dan counter CSS pada elemen biasa bukan nomor halaman
yang andal. Daftar isi default memakai tautan section, bukan nomor halaman
perkiraan. Isi nomor halaman TOC hanya setelah pagination final diverifikasi.

Contoh opsional untuk engine paged media yang telah diverifikasi:

```css
/* Jangan aktifkan tanpa pemeriksaan engine dan hasil PDF. */
@page {
  @bottom-center {
    content: "Halaman " counter(page) " dari " counter(pages);
    font-family: Cambria, "Times New Roman", serif;
    font-size: 12pt;
  }
}
```

## Instruksi cetak yang disertakan pada HTML

1. Buka HTML di browser dan pilih Print/Save as PDF.
2. Pilih A4 portrait, skala 100%, tanpa fit-to-page bila mengubah ukuran font.
3. Gunakan margin CSS 3 cm. Jika engine mengabaikan @page, set custom margin
   30 mm di semua sisi dan periksa agar tidak terhitung ganda.
4. Matikan header/footer bawaan kecuali sengaja memilih fitur tersebut.
5. Background graphics bersifat opsional; informasi harus tetap terbaca tanpa
   warna latar. Hindari URL/path sensitif pada header/footer browser.
6. Periksa print preview: clipping, pemisahan tabel, blank page, heading
   menggantung, diagram, font, dan footer/nomor halaman jika digunakan.

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

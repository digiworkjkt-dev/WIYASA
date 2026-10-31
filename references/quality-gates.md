# Quality gates

Jalankan audit sebelum menyerahkan paket. Laporkan hasil yang benar-benar
diperiksa. Audit dokumen tidak setara dengan validasi aplikasi.

## Gate A: Kebutuhan dan scope

- Masalah, pengguna, outcome, MVP, dan non-goals tidak saling bertentangan.
- Requirement memiliki ID unik, prioritas, sumber/status, dan AC terukur.
- Assumptions dan proposed decisions terpisah dari confirmed requirements.
- Unknown penting memiliki dampak, owner jika diketahui, dan status blocking.
- Angka target, estimasi, dan klaim eksternal punya sumber atau label usulan.

## Gate B: Konsistensi implementasi yang direncanakan

- Nama role, entitas, field, status, serta endpoint sama antar dokumen.
- Role-permission matrix cocok dengan desain API dan isolasi data.
- Lifecycle/state transition tidak melewatkan keadaan gagal yang relevan.
- Model data dapat memenuhi aturan bisnis; constraints/index/transaction
  mendukung invariant yang diklaim, atau gap dicatat.
- Boundary trust, integrasi, dan deployment topology tidak bertentangan.
- Tidak ada fitur post-MVP masuk diam-diam ke task MVP.
- Desain, task, dan test tidak mengada-ada fitur di luar requirement.

## Gate C: Traceability dan pengujian

- Setiap FR MVP tertaut ke AC, task, dan test; UX/API hanya bila relevan.
- Setiap NFR memiliki cara verifikasi atau blocker yang eksplisit.
- Happy path dan failure/permission cases prioritas tinggi tercakup.
- Test memiliki expected result yang bisa diamati.
- Tidak ada hasil test palsu; planned dan executed dipisah.

## Gate D: Operasi dan keamanan

- Konfigurasi tidak memuat credential atau data pribadi nyata.
- Data retention/deletion, logging redaction, dan authorization dibahas
  sesuai data dan risiko yang benar-benar ada.
- Go-live checklist membedakan hal planned, verified, dan blocked.
- Migration, rollback, backup, serta restore hanya diklaim bisa dilakukan
  jika desain atau bukti mendukung; destructive migration punya peringatan.
- Legal/compliance/SLA tidak dinyatakan terpenuhi hanya karena ada dokumen.

## Gate E: Packaging

- Paket deliverable lengkap: Wajib menghasilkan README.md, seluruh berkas sumber modular Markdown di folder \sources/\, dan laporan HTML monolit siap cetak. Tidak boleh hanya menghasilkan satu berkas HTML saja tanpa berkas sumber Markdown.
- README menautkan seluruh dokumen yang dihasilkan dan menjelaskan urutan baca.
- Tautan relatif dan reference ID dapat ditemukan; tidak ada placeholder
  tak berlabel atau dokumen kosong yang diklaim lengkap.
- Diagram dapat dibaca; jika renderer/parser tidak tersedia, nyatakan bahwa
  pemeriksaan hanya dilakukan pada teks, bukan rendering.
- Version, status, scope, sources, dan changelog konsisten.
- File diserahkan melalui mekanisme yang dapat diakses pengguna.

## Gate F: Standar industri, SNI, dan regulasi

- Register standar/regulasi tersedia; tiap entri punya versi/status,
  applicability, dasar wajib/sukarela/kontrak, sumber resmi dan tanggal cek.
- Standar internasional tidak disebut SNI tanpa bukti adopsi nasional.
- "Berlaku" di katalog tidak disamakan dengan pemberlakuan wajib.
- Klausul hanya dipetakan setelah teks dibaca; abstrak/metadata diberi
  label mapping topik dan belum diverifikasi klausul.
- Requirement/control/test/evidence terhubung; missing evidence menjadi gap.
- Kepatuhan organisasi, proses, produk dan sertifikasi tidak dicampur.
- Kebutuhan legal/auditor/LPK dicatat sebagai dependency, bukan audit selesai.
- Sector screening, perubahan aturan, dan teks yang belum dapat diakses
  dicatat; gap penting memblokir klaim compliance-ready.

## Gate G: SKKNI dan kompetensi

- Register SKKNI terpisah dari standar mutu produk/SMKI.
- Nomor keputusan, kode/versi unit, status, sumber, dan tanggal cek dicatat.
- Mapping tingkat unit tidak diberi label pemenuhan KUK.
- Mapping KUK menggunakan teks unit yang dibaca; cakupan parsial dinyatakan.
- Task/artefak punya status planned vs available; evidence tidak dibuat-buat.
- Guide kode merujuk implementasi/revisi nyata, bukan desain yang dianggap kode.
- Gap unit, konflik kode, serta batas verifikasi dicatat.
- Tidak ada klaim personel kompeten/tersertifikasi dari audit dokumentasi.

## Gate H: HTML, A4, dan cetak/PDF

- Deliverable utama HTML self-contained; sumber Markdown tidak menggantikannya.
- Seluruh output berada di `app-documentation/`; path laporan dan narasi lokasi
  penyimpanan sesuai file aktual, terpisah dari direktori instalasi skill.
- @page A4 portrait/margin 3 cm, font utama Cambria 12 pt, align justify (text-align: justify; text-justify: inter-word;), dan print CSS tersedia.
- Seluruh paragraf naratif dan catatan menggunakan rata kanan-kiri (align justify), sedangkan judul dan tabel tetap rata kiri.
- Tidak ada margin ganda, konten terlalu lebar, raw Mermaid, atau sumber CDN.
- Cover, metadata, status, TOC/anchor, sumber acuan, gap analitis, dan riwayat revisi (changelog) tersedia.
- Dokumen aplikasi bersih dari instruksi cetak peramban (misal: tombol Ctrl+P, Save as PDF, petunjuk cetak) dan kriteria/rubrik internal skill. Panduan cetak berada di `README.md`, bukan di dalam dokumen aplikasi.
- Font aktual diperiksa bila render tersedia; fallback dinyatakan terbuka.
- Pagination/footer tidak dijanjikan tanpa hasil engine yang telah diuji.
- QA statis, render PDF, text inspection dan visual QA dibedakan pada laporan.
- Tidak mengklaim format cetak ini kewajiban SNI/SKKNI.

## Format laporan audit

| Check | Passed / Gap / N/A | Evidence or reason | Blocking? |
|---|---|---|---|

Readiness:
- **Draft:** berguna untuk pembahasan, belum siap menjadi instruksi final.
- **Ready for review:** audit dokumentasi selesai; keputusan belum disetujui.
- **Implementation-ready within stated scope:** kebutuhan cukup jelas dan
  tidak ada blocker desain di scope tersebut; bukan berarti kode tersedia.

Jangan otomatis memberi status approved.

## Audit perubahan

Untuk setiap requirement berubah:
1. Catat perubahan dan sumber/keputusannya.
2. Cari semua referensi ID dan nama konsep terkait.
3. Perbarui bagian downstream yang terdampak.
4. Tandai bagian yang tidak bisa diperbarui sebagai stale dengan alasannya.
5. Audit ulang scope yang berubah; jangan mengklaim seluruh sistem diuji ulang.

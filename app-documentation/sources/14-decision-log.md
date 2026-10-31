# 14. Catatan Keputusan Arsitektur (Architecture Decision Records)
Status: Approved
Version: 1.6.0
Updated: 2026-10-31
Owner: Dewan Arsitektur & Rekayasa Perangkat Lunak WIYASA
Scope: Full System / Production
Sources: Kode sumber WIYASA v1.6.0, ISO/IEC 25010, SNI ISO/IEC 27001, SKKNI Kepmenaker 282/2016
Related: [README.md](../README.md), [laporan-arsitektur-dan-spesifikasi.html](../laporan-arsitektur-dan-spesifikasi.html)

## ADR-001: Pemisahan Deliverable Opsi 2 Berdasarkan Audiens
- **Status:** Approved
- **Konteks:** Dokumen monolitik menyulitkan klien/pengguna membaca panduan praktis karena terbebani ratusan halaman diagram arsitektur.
- **Keputusan:** Memisahkan deliverable menjadi Laporan Arsitektur Teknis dan Panduan Pengguna Mandiri.

## ADR-002: Eliminasi Pernyataan Assert pada Skrip Validator
- **Status:** Approved
- **Konteks:** Pernyataan `assert` dapat di-bypass menggunakan flag `python -O`.
- **Keputusan:** Menggunakan evaluasi kondisional eksplisit dengan `sys.exit(1)`.

## ADR-003: Sanitasi Ketat Anti-XSS dan Pembatasan Dependensi Jaringan
- **Status:** Approved
- **Konteks:** Dokumen HTML mandiri berpotensi menjadi vektor injeksi skrip berbahaya jika dibuka di lingkungan korporat.
- **Keputusan:** Menerapkan `SecureHTMLParser` yang melarang tag skrip dan CDN eksternal.

## ADR-004: Rekayasa Running Page Footers Multi-Engine
- **Status:** Approved
- **Konteks:** Dokumen cetak A4 membutuhkan nomor halaman dan identitas dokumen yang konsisten di tiap lembar fisik.
- **Keputusan:** Menggabungkan CSS Paged Media `@page` margin boxes dengan elemen `.running-footer` berulang pada Chromium print.

## ADR-005: Rebranding Resmi Menjadi WIYASA
- **Status:** Approved
- **Konteks:** Transformasi dari repositori kerja mentah menjadi mesin dokumentasi profesional beridentitas budaya agung Nusantara.
- **Keputusan:** Mengadopsi nama WIYASA dan memperbarui repositori GitHub menjadi `digiworkjkt-dev/WIYASA`.

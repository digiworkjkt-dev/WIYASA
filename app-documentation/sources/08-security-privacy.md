# 08. Keamanan Siber dan Perlindungan Data Pribadi
Status: Approved
Version: 1.6.0
Updated: 2026-10-31
Owner: Dewan Arsitektur & Rekayasa Perangkat Lunak WIYASA
Scope: Full System / Production
Sources: Kode sumber WIYASA v1.6.0, ISO/IEC 25010, SNI ISO/IEC 27001, SKKNI Kepmenaker 282/2016
Related: [README.md](../README.md), [laporan-arsitektur-dan-spesifikasi.html](../laporan-arsitektur-dan-spesifikasi.html)

## 1. Perlindungan Anti-XSS (Cross-Site Scripting)
Dokumen HTML yang dihasilkan dilarang keras memuat:
- Tag eksekusi skrip: `<script>`, `<object>`, `<iframe>`, `<embed>`, `<applet>`.
- Skema URI dinamis: `javascript:`, `data:text/html`.
- Inline event handlers: `onload`, `onerror`, `onclick`, `onmouseover`.

## 2. Kepatuhan UU No. 27/2022 tentang Pelindungan Data Pribadi (UU PDP)
Seluruh data yang disajikan dalam contoh dokumen, pengujian, dan tangkapan layar wajib menggunakan data fiktif (dummy/pseudonymized). Dilarang menyertakan NIK nyata, nomor telepon riil, kredensial produksi, atau rahasia API.

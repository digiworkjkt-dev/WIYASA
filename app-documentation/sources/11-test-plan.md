# 11. Rencana Pengujian (Test Plan)
Status: Approved
Version: 1.6.0
Updated: 2026-10-31
Owner: Dewan Arsitektur & Rekayasa Perangkat Lunak WIYASA
Scope: Full System / Production
Sources: Kode sumber WIYASA v1.6.0, ISO/IEC 25010, SNI ISO/IEC 27001, SKKNI Kepmenaker 282/2016
Related: [README.md](../README.md), [laporan-arsitektur-dan-spesifikasi.html](../laporan-arsitektur-dan-spesifikasi.html)

## 1. Kasus Uji Fungsional dan Kualitas (Test Cases)

| Test Case ID | Skenario Uji | Kebutuhan / Task | Kriteria Evaluasi | Status |
|---|---|:---:|---|:---:|
| **TC-001** | Verifikasi keberadaan artefak Opsi 2 | FR-001 / TASK-001 | Memuat README, sources/*.md, dan sepasang HTML | PASS |
| **TC-002** | Pengujian layout A4, margin 3cm, dan teks justify | FR-002 / TASK-002 | CSS terverifikasi dan teks naratif justify | PASS |
| **TC-003** | Pengujian running page footer pada cetak peramban | FR-003 / TASK-003 | Footer muncul di tiap halaman tanpa menimpa teks | PASS |
| **TC-004** | Pemindaian keamanan anti-XSS dan sumber daya eksternal | FR-004 / TASK-004 | Parser menolak tag berbahaya dan tautan CDN | PASS |
| **TC-005** | Pemindaian anti-kebocoran petunjuk cetak | FR-005 / TASK-005 | Badan dokumen bersih dari instruksi peramban | PASS |
| **TC-006** | Pengujian otomatisasi perkakas CLI | FR-006 / TASK-006 | Skrip exit code 0 untuk paket yang valid | PASS |

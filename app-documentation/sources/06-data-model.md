# 06. Model Data dan Struktur Dokumen
Status: Approved
Version: 1.6.0
Updated: 2026-10-31
Owner: Dewan Arsitektur & Rekayasa Perangkat Lunak WIYASA
Scope: Full System / Production
Sources: Kode sumber WIYASA v1.6.0, ISO/IEC 25010, SNI ISO/IEC 27001, SKKNI Kepmenaker 282/2016
Related: [README.md](../README.md), [laporan-arsitektur-dan-spesifikasi.html](../laporan-arsitektur-dan-spesifikasi.html)

## 1. Skema Metadata Dokumen (Frontmatter Schema)
Setiap berkas sumber Markdown wajib memiliki skema header terstruktur:
```yaml
Title: String (Wajib)
Status: Enum [Draft, In-Review, Approved]
Version: SemVer String (Wajib)
Updated: ISO Date YYYY-MM-DD (Wajib)
Owner: String (Wajib)
Scope: Enum [Lean, Standard, Extended]
Sources: List of References
Related: List of Relative Links
```

## 2. Struktur Relasional Dokumen
- Paket `DocsApp/` memiliki root manifest `README.md`.
- Laporan HTML merangkum entitas kebutuhan (`FR-xxx`), tugas (`TASK-xxx`), dan pengujian (`TC-xxx`) dalam relasi keterlacakan 1-to-N yang konsisten.

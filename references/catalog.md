# Katalog Dokumen WIYASA

## Format delivery

Paket deliverable yang dihasilkan **wajib menggunakan Standar Opsi 2 (Pemisahan Dua Dokumen Berdasarkan Audiens)**:
1. `app-documentation/README.md` pada root folder dokumentasi sebagai pintu masuk, ringkasan status, peta navigasi paket, dan panduan cetak PDF.
2. Seluruh berkas modular Markdown (00-context s.d. 17-developer-guide) disimpan pada folder `app-documentation/sources/` sebagai Single Source of Truth (SSOT) teknis pengembang di git.
3. `app-documentation/laporan-arsitektur-dan-spesifikasi.html`: Dokumen teknis dan arsitektur lengkap bagi Tim Pengembang, Arsitek, dan Auditor (menggunakan template `assets/report-a4.html`).
4. `app-documentation/panduan-pengguna-aplikasi.html`: Buku panduan operasional mandiri bagi Klien, Pengguna Akhir, dan Administrator Sistem (menggunakan template `assets/user-guide-a4.html`), **wajib menyertakan tangkapan layar (screenshots) atau mockup antarmuka visual** pada alur onboarding, dashboard, transaksi utama, dan panel admin.
(Catatan: `app-documentation/laporan-dokumentasi-aplikasi.html` tetap didukung sebagai format alternatif bila pengguna meminta satu dokumen tunggal).

Section HTML memiliki anchor stabil sesuai nama dokumen/ID. README memberi tautan ke laporan HTML dan seluruh berkas sumber pada `sources/`.
PDF bersyarat pada ketersediaan engine dan verifikasi hasil; footer/nomor halaman tidak dijanjikan lintas engine.
Nama file manifest di bawah relatif terhadap folder sumber `app-documentation/sources/`; bukan instruksi menyimpan output ke direktori instalasi skill. Narasi penyerahan wajib menyebut folder output, path laporan, dan struktur berkas sumber yang benar-benar ada.

## Manifest Standard

Gunakan nama berikut sebagai default; adaptasikan tanpa mengorbankan cakupan.

| File | Isi minimum yang harus menghasilkan keputusan atau instruksi nyata |
|---|---|
| `README.md` | Ringkasan aplikasi, cakupan paket, urutan baca, tautan dokumen, status readiness, blocker, daftar dokumen yang tidak berlaku beserta alasan |
| `00-context.md` | Intake, sumber kebenaran, glossary, role, constraints, asumsi ber-ID, keputusan terbuka dan dampaknya |
| `01-product-brief.md` | Masalah, target pengguna, alur saat ini, manfaat, scope MVP, non-goals, indikator keberhasilan |
| `02-prd.md` | Tujuan, use case, prioritas fitur, MVP vs berikutnya, dependensi, risiko produk, metrik beserta status target |
| `03-requirements.md` | FR/NFR ber-ID, aturan bisnis, prioritas, sumber/status, user story, acceptance criteria yang terukur |
| `04-ux-flows.md` | Sitemap/screen inventory, user journey, alur utama/alternatif, state/error, accessibility, role-permission matrix |
| `05-architecture.md` | Context/component/deployment diagram, boundary, tanggung jawab komponen, stack dan alasan, dependensi, observability, tradeoff |
| `06-data-model.md` | ERD, data dictionary, PK/FK, tipe/nullability, unique/check constraints, index, lifecycle, retention, migration/backfill plan bila relevan |
| `07-api-integrations.md` | Kontrak endpoint/event, request/response dummy, auth, validation/error, pagination, retry/rate limit, dependency provider dan status verifikasi |
| `08-security-privacy.md` | Threat model ringkas, permission enforcement, isolasi data, secrets, logging/redaction, encryption, abuse controls, privacy/retention/deletion, risiko residual |
| `09-delivery-plan.md` | Epic/task ber-ID dan requirement terkait, urutan dependency, definition of ready/done, milestone, risiko, owner belum ditentukan bila tidak diketahui |
| `10-test-plan.md` | Unit/integration/E2E, test ber-ID, edge cases, security/accessibility/performance sesuai risiko, data/lingkungan uji, UAT, exit criteria, status planned |
| `11-deployment-runbook.md` | Lingkungan, konfigurasi tanpa nilai secret, build/release, migration, monitoring, backup/restore, rollback dan batasnya, incident response, go-live checklist |
| `12-user-admin-guide.md` | Workflow user/admin, onboarding, konfigurasi, troubleshooting, known limitations, serta tangkapan layar (screenshots/mockups) pada alur penting |
| `13-traceability.md` | Matriks FR/NFR ke AC, UX, component/data/API, task, test; gap, N/A dengan alasan, risiko dan blocker |
| `14-decision-log.md` | ADR, asumsi, open questions, keputusan dan konsekuensi, changelog lintas dokumen |
| `15-standards-compliance.md` | Register standar/regulasi, applicability dan dasar wajib/sukarela, edisi/status/sumber, mapping topik/klausul, kontrol, bukti, owner, gap dan rencana remediasi |
| `16-skkni-competency-map.md` | SKKNI relevan, nomor keputusan/status, unit dan KUK yang sudah dibaca, aktivitas/role usulan, task/dokumen, rencana bukti kerja, gap dan batas verifikasi |
| `17-developer-guide.md` | Bersyarat bila kode ada: inventaris modul/fungsi, parameter dan return, algoritma, exception, dependency, instruksi setup, tool generasi docs, revisi/commit sumber dan keterkaitan perubahan kode |

Jika tidak ada API eksternal atau backend terpisah, `07-api-integrations.md`
menjelaskan kontrak internal yang relevan atau status tidak berlaku.
Jika tidak ada persistensi, `06-data-model.md` menjelaskan state sementara
dan mengapa database tidak diperlukan. Jangan mengarang backend.

## Cakupan Lean

Gabungkan menjadi:
- README + konteks/keputusan.
- Product specification: brief + PRD + requirements.
- UX & technical design: flow + architecture + data/API + security.
- Delivery & tests: tasks + test plan + traceability.
- Operations & guide: deployment/runbook + panduan pengguna.

Berikan section heading dan anchor yang memungkinkan referensi lintas dokumen.
Lean tidak membolehkan menghilangkan otorisasi, failure handling, atau test.
Masukkan register relevansi standar/regulasi dan gap compliance dalam section
konteks/traceability; Lean tidak menghapus kewajiban yang berlaku.
Masukkan screening dan mapping SKKNI pada delivery plan. Dokumentasi kode
yang belum ada tetap planned; jangan menulis nama fungsi atau hasil generasi
dokumentasi fiktif untuk memenuhi unit kompetensi.

## Tambahan Extended, hanya jika relevan

| Pemicu | Dokumen tambahan dan fokus |
|---|---|
| Aplikasi existing, migration, atau legacy replacement | Audit as-is vs to-be, compatibility, mapping data, dry-run, backfill, reconciliation, rollback |
| SaaS multi-tenant | Tenant model, boundary dan isolasi, provisioning, tenant-level permissions, billing bila dibutuhkan |
| Pembayaran | State machine order/payment/refund, webhook verification, replay/idempotency, rekonsiliasi, dependency payment provider |
| AI/LLM | Peran model, data/prompt handling, evaluation set/metrics, failure/fallback, cost assumptions, prompt injection dan human review |
| Mobile/offline | Offline queue, conflict resolution, sync, permissions perangkat, distribusi aplikasi sesuai platform |
| Beban tinggi/SLA | Capacity assumptions, SLI/SLO usulan, load-test plan, reliability, recovery target dan failure modes |
| Data sensitif/regulasi | Data inventory, consent/legal basis untuk review ahli, retention/deletion, access audit, compliance checklist tanpa klaim sertifikasi |
| Banyak tim atau stakeholder | RACI/DACI, review ownership, interface ownership, approval gates, dependency coordination |
| Dokumen kontrak mesin diperlukan | OpenAPI/JSON Schema/event schema yang tervalidasi dengan tool jika tersedia |
| Launch komersial | Launch plan, support readiness, analytics event specification, release notes |

## Bentuk entri

### Functional requirement

`ID | Pernyataan | Role | Prioritas | MVP/Post-MVP | Sumber/status | AC terkait`

### Nonfunctional requirement

`ID | Metrik | Target | Kondisi pengukuran | Status target | Cara verifikasi`

### Task

`ID | Outcome | Requirement | Dependency | Deliverable | Done criteria | Owner/status`

### Test case

`ID | Requirement/AC | Level | Preconditions | Steps | Expected result | Status | Evidence`

### Architecture decision

`ID | Status | Context | Options | Decision/proposal | Tradeoffs | Consequences | Affected docs`

### Panduan pengguna dan administrator (12-user-admin-guide.md)

Dokumen panduan pengguna wajib diproduksi secara terstruktur memuat 5 bagian:
1. **Onboarding & Autentikasi:** Alur registrasi, login, verifikasi akun, dan hak akses awal per role.
2. **Panduan Fitur Utama:** Prosedur operasional langkah-demi-langkah penggunaan fitur bagi setiap role pengguna (alur sukses dan mitigasi kesalahan input).
3. **Panduan Administrator:** Prosedur administrasi data master, manajemen role/hak akses, persetujuan (approval workflow), dan monitoring audit log.
4. **Penanganan Kendala (Troubleshooting & FAQ):** Solusi kendala umum, arti pesan error, dan tindakan pemulihan mandiri.
5. **Batasan Sistem (Known Limitations):** Batasan operasional sistem yang diketahui serta fitur yang masih dalam tahap rencana.

### Open question

`ID | Pertanyaan | Mengapa penting | Dampak | Owner | Blocking/nonblocking`

Tidak perlu mengisi kolom Evidence untuk test yang belum dijalankan selain
`Belum dijalankan`. Bedakan artefak rencana dan bukti hasil.

### Standards register

`ID | Nomor/edisi | Jenis | Status penerbit/tanggal cek | Relevansi/scope |
Dasar wajib/sukarela/kontrak | Sumber resmi | Akses teks penuh | Reviewer`

### Compliance mapping

`STD/REG | Topik atau klausul terverifikasi | Applicability/alasan |
FR/NFR | CTRL | Dokumen | TC | EVD | Status pemenuhan | Gap | Owner/action`

Jika klausul belum dibaca, tulis `Topik; klausul belum diverifikasi`.
Status pemenuhan: not-assessed / planned / evidence-available / reviewed-gap /
reviewed-met-within-scope. Jangan menyamakan status ini dengan sertifikasi.

### SKKNI mapping

`Nomor keputusan/status/tanggal cek | Kode/judul unit | Elemen/KUK terverifikasi |
Kedalaman mapping | Relevansi | Aktivitas/role usulan | Task | Artefak |
Bukti kerja/versi | Status bukti | Gap | Reviewer/action`

Status bukti: planned / available-unreviewed / artifact-reviewed / missing.
Hasil asesmen kompetensi orang disimpan terpisah bila memang ada sumber sah;
review dokumen oleh agent tidak boleh diberi label "kompeten".

#!/usr/bin/env python3
"""
Validator untuk repositori skill WIYASA (app-documentation) dan berkas deliverable HTML.
Memeriksa metadata frontmatter, tautan relatif Markdown, keunikan heading,
standar CSS cetak A4, aturan sanitasi keamanan (anti-XSS), dan integritas anchor.

Dapat dijalankan dalam mode mandiri (self-check repo) maupun terhadap target deliverable:
  python scripts/validate.py
  python scripts/validate.py --target path/to/laporan.html
"""
import argparse
from html.parser import HTMLParser
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

DANGEROUS_TAGS = {"script", "iframe", "object", "embed", "applet"}


class SecureHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.links = []
        self.external_resources = []
        self.security_violations = []

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)

        # 1. Deteksi tag berbahaya (XSS / Injeksi Eksekusi)
        if tag.lower() in DANGEROUS_TAGS:
            self.security_violations.append(f"Tag berbahaya tidak diizinkan: <{tag}>")

        # 2. Periksa ID
        if "id" in attrs_dict:
            self.ids.append(attrs_dict["id"])

        # 3. Periksa Tautan
        if tag == "a":
            href = attrs_dict.get("href", "")
            self.links.append(href)
            if href.lower().startswith("javascript:"):
                self.security_violations.append(f"URI javascript: tidak diizinkan pada link: {href}")

        # 4. Deteksi inline event handlers (on*)
        for attr_name, attr_val in attrs:
            if attr_name.lower().startswith("on"):
                self.security_violations.append(
                    f"Inline event handler tidak diizinkan: {attr_name}=\"{attr_val}\""
                )

        # 5. Deteksi dependensi eksternal (CDN, remote font, remote script/image)
        if tag in {"script", "img", "link", "iframe", "video", "audio", "source"}:
            for field in ("src", "href"):
                val = attrs_dict.get(field, "")
                if val.startswith(("http:", "https:", "//")):
                    self.external_resources.append(val)
                elif val.lower().startswith("data:text/html"):
                    self.security_violations.append(f"Data URI berbahaya tidak diizinkan pada <{tag}>")


def validate_html_content(html_text: str, filename: str = "HTML") -> list[str]:
    """Validasi aturan cetak A4 dan keamanan berkas HTML."""
    errors = []
    parser = SecureHTMLParser()
    try:
        parser.feed(html_text)
    except Exception as exc:
        errors.append(f"Gagal mem-parsing HTML {filename}: {exc}")
        return errors

    # Cek ID unik
    duplicate_ids = [item for item in set(parser.ids) if parser.ids.count(item) > 1]
    if duplicate_ids:
        errors.append(f"ID duplikat pada {filename}: {duplicate_ids}")

    # Cek anchor lokal
    for href in parser.links:
        if href.startswith("#") and len(href) > 1:
            target_id = href[1:]
            if target_id not in parser.ids:
                errors.append(f"Tautan anchor lokal tidak ditemukan pada {filename}: {href}")

    # Cek pelanggaran keamanan
    if parser.security_violations:
        for violation in parser.security_violations:
            errors.append(f"Keamanan [{filename}]: {violation}")

    # Cek dependensi eksternal
    if parser.external_resources:
        for res in parser.external_resources:
            errors.append(f"Dependensi eksternal tidak diizinkan pada [{filename}]: {res}")

    # Cek spesifikasi cetak wajib
    required_print_rules = [
        ("size: A4 portrait", "@page size: A4 portrait"),
        ("margin: 3cm", "@page margin: 3cm"),
        ("Cambria", "Font family Cambria"),
        ("font-size: 12pt", "Ukuran font dasar 12pt"),
        ("@media print", "Blok @media print"),
        ("table-header-group", "Pengulangan header tabel thead"),
        ("break-before: page", "Pemisahan bab break-before: page"),
        ('lang="id"', 'Atribut bahasa lang="id"'),
        ('charset="utf-8"', 'Karakter encoding utf-8'),
        ('text-align: justify', 'Perataan paragraf rata kanan-kiri (text-align: justify)'),
    ]
    for pattern, label in required_print_rules:
        if pattern.lower() not in html_text.lower():
            errors.append(f"Aturan cetak hilang pada {filename}: {label} ('{pattern}')")

    if not re.search(r'\.report\s*\{[^}]*padding:\s*0', html_text):
        errors.append(f"Risiko margin ganda pada {filename}: .report harus memiliki padding: 0 pada @media print")

    # Cek kehadiran footer dokumen resmi (.running-footer atau .document-end)
    if not re.search(r'<footer[^>]*class="[^"]*(?:running-footer|document-end)', html_text):
        errors.append(f"Footer dokumen resmi tidak ditemukan pada {filename}. Setiap dokumen wajib memiliki elemen footer (.running-footer).")

    # Pastikan position: fixed hanya digunakan untuk running footer/header cetak
    if "position: fixed" in html_text:
        fixed_selectors = re.findall(r'([^{}]*)\{[^}]*position:\s*fixed[^}]*\}', html_text)
        for selector in fixed_selectors:
            sel_clean = selector.strip().lower()
            if not any(k in sel_clean for k in [".running-footer", ".running-header", "footer"]):
                errors.append(
                    f"Penggunaan position: fixed tidak diizinkan pada '{selector.strip()}' di {filename}. "
                    "Hanya diperbolehkan untuk elemen header/footer cetak (.running-footer)."
                )

    # Deteksi kebocoran instruksi cetak peramban & meta-kriteria ke dalam badan dokumen aplikasi
    leakage_patterns = [
        (r"petunjuk\s+cetak", "Kotak/petunjuk cetak peramban"),
        (r"instruksi\s+(?:resmi\s+)?cetak", "Bab/instruksi cetak peramban"),
        (r"aturan\s+cetak/pdf", "Sub-bab aturan cetak/PDF"),
        (r"save\s+as\s+pdf", "Petunjuk tombol Save as PDF"),
        (r"ctrl\s*\+\s*p", "Pintasan cetak Ctrl+P"),
    ]
    for pattern, desc in leakage_patterns:
        if re.search(pattern, html_text, re.IGNORECASE):
            errors.append(
                f"Kebocoran konten pada {filename}: {desc} ditemukan di badan dokumen. "
                "Panduan cetak dan petunjuk teknis peramban harus ditempatkan di README.md, bukan di laporan aplikasi."
            )

    return errors


def validate_repo() -> list[str]:
    """Validasi integritas internal repositori skill."""
    errors = []
    main_file = ROOT / "SKILL.md"
    if not main_file.is_file():
        errors.append("File SKILL.md tidak ditemukan.")
        return errors

    main = main_file.read_text(encoding="utf-8")
    if not main.startswith("---\n"):
        errors.append("SKILL.md: Frontmatter tidak ditemukan di baris pertama.")

    front_parts = main.split("---", 2)
    if len(front_parts) < 3:
        errors.append("SKILL.md: Struktur frontmatter tidak lengkap.")
    else:
        front = front_parts[1]
        name = re.search(r"^name:\s*(.+)$", front, re.M)
        desc = re.search(r"^description:\s*(.+)$", front, re.M)

        if not name or not re.fullmatch(r"[a-z0-9-]{1,64}", name.group(1).strip()):
            errors.append("SKILL.md: Format 'name' harus berupa huruf kecil, angka, atau tanda minus (maks 64 char).")
        if not desc:
            errors.append("SKILL.md: 'description' wajib diisi.")
        elif len(desc.group(1).strip()) > 1024:
            errors.append(f"SKILL.md: 'description' melebihi batas 1024 karakter ({len(desc.group(1).strip())}).")

    if len(main.splitlines()) >= 500:
        errors.append(f"SKILL.md: Melebihi batas rekomendasi 500 baris ({len(main.splitlines())} baris).")

    # Validasi seluruh file markdown
    for md_file in ROOT.rglob("*.md"):
        text = md_file.read_text(encoding="utf-8")

        # Cek link markdown
        for target in re.findall(r"\]\(([^)]+)\)", text):
            # Abaikan URL eksternal, anchor murni, mailto, atau teks penjelasan bukan file
            if "://" in target or target.startswith("#") or target.startswith("mailto:"):
                continue
            path_part = target.split("#", 1)[0].strip()
            if not path_part:
                continue
            target_path = md_file.parent / path_part
            if not target_path.exists():
                errors.append(f"Tautan rusak pada {md_file.relative_to(ROOT)} -> {target}")

        # Cek heading duplikat tingkat 2
        headings = re.findall(r"^## .+$", text, re.M)
        if len(headings) != len(set(headings)):
            duplicates = [h for h in set(headings) if headings.count(h) > 1]
            errors.append(f"Heading ## duplikat pada {md_file.relative_to(ROOT)}: {duplicates}")

    # Validasi template laporan A4
    template_file = ROOT / "assets/report-a4.html"
    if not template_file.is_file():
        errors.append("assets/report-a4.html tidak ditemukan.")
    else:
        template_html = template_file.read_text(encoding="utf-8")
        errors.extend(validate_html_content(template_html, "assets/report-a4.html"))

    user_guide_template = ROOT / "assets/user-guide-a4.html"
    if user_guide_template.is_file():
        ug_html = user_guide_template.read_text(encoding="utf-8")
        errors.extend(validate_html_content(ug_html, "assets/user-guide-a4.html"))

    # Validasi kontrak jalur kanonis pada SKILL.md
    for required_phrase in (
        "html-print.md",
        "report-a4.html",
        "app-documentation/laporan-dokumentasi-aplikasi.html",
        "Seluruh output dokumen disimpan di folder",
    ):
        if required_phrase not in main:
            errors.append(f"Frasa kanonis wajib hilang dari SKILL.md: '{required_phrase}'")

    return errors


def main():
    parser = argparse.ArgumentParser(
        description="Validator repositori dan artefak HTML skill WIYASA (v1.6.0)."
    )
    parser.add_argument(
        "--target",
        type=str,
        help="Path ke berkas laporan HTML yang akan diperiksa (misal: app-documentation/laporan-dokumentasi-aplikasi.html)",
    )
    parser.add_argument(
        "--package-dir",
        type=str,
        help="Path ke folder paket deliverable (misal: app-documentation). Memastikan README.md, sources/*.md, dan laporan HTML lengkap.",
    )
    parser.add_argument(
        "--skip-repo-check",
        action="store_true",
        help="Lewati pemeriksaan integritas repo internal dan hanya periksa --target.",
    )

    args = parser.parse_args()
    all_errors = []

    # 1. Mode pemeriksaan repo lokal
    if not args.skip_repo_check:
        repo_errors = validate_repo()
        all_errors.extend(repo_errors)

    # 2. Mode pemeriksaan paket deliverable lengkap
    if args.package_dir:
        pkg_path = Path(args.package_dir).resolve()
        if not pkg_path.is_dir():
            all_errors.append(f"Direktori paket tidak ditemukan: {args.package_dir}")
        else:
            readme_path = pkg_path / "README.md"
            tech_report = pkg_path / "laporan-arsitektur-dan-spesifikasi.html"
            user_report = pkg_path / "panduan-pengguna-aplikasi.html"
            single_report = pkg_path / "laporan-dokumentasi-aplikasi.html"
            sources_dir = pkg_path / "sources"

            if not readme_path.is_file():
                all_errors.append(f"Paket tidak lengkap: {args.package_dir}/README.md tidak ditemukan.")

            found_reports = []
            if tech_report.is_file() and user_report.is_file():
                found_reports.extend([tech_report, user_report])
            elif single_report.is_file():
                found_reports.append(single_report)
            else:
                all_errors.append(
                    f"Paket tidak lengkap: {args.package_dir}/ wajib memuat sepasang dokumen HTML Opsi 2 "
                    "(laporan-arsitektur-dan-spesifikasi.html & panduan-pengguna-aplikasi.html) "
                    "atau laporan-dokumentasi-aplikasi.html."
                )

            for rep in found_reports:
                html_errors = validate_html_content(rep.read_text(encoding="utf-8"), rep.name)
                all_errors.extend(html_errors)
            if not sources_dir.is_dir():
                all_errors.append(f"Paket tidak lengkap: Folder {args.package_dir}/sources/ tidak ditemukan.")
            else:
                md_sources = list(sources_dir.glob("*.md"))
                if not md_sources:
                    all_errors.append(f"Paket tidak lengkap: Tidak ada berkas .md di {args.package_dir}/sources/.")

    # 3. Mode pemeriksaan target spesifik
    if args.target:
        target_path = Path(args.target).resolve()
        if not target_path.is_file():
            all_errors.append(f"Berkas target tidak ditemukan: {args.target}")
        else:
            target_content = target_path.read_text(encoding="utf-8")
            target_errors = validate_html_content(target_content, str(target_path.name))
            all_errors.extend(target_errors)

    # 3. Evaluasi hasil
    if all_errors:
        print(f"FAILED: Ditemukan {len(all_errors)} kesalahan validasi:")
        for err in all_errors:
            print(f" - {err}")
        sys.exit(1)

    print("PASS: Validasi berhasil. Metadata, links, headings, print rules, dan keamanan (anti-XSS) lolos.")
    print("Catatan: Visual pagination, ketersediaan font fisik, dan kepatuhan klausul hukum harus diverifikasi per kasus.")
    sys.exit(0)


if __name__ == "__main__":
    main()

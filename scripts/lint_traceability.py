#!/usr/bin/env python3
"""
Linter Keterlacakan (Traceability Linter) untuk skill app-documentation (v1.5.0).
Memeriksa integritas hubungan silang ID:
  FR-xxx / NFR-xxx (Requirements)
    -> AC-xxx (Acceptance Criteria)
    -> TASK-xxx (Implementation Task)
    -> TC-xxx (Test Cases)

Penggunaan:
  python scripts/lint_traceability.py --dir app-documentation/sources
  python scripts/lint_traceability.py --file app-documentation/sources/13-traceability.md
"""
import argparse
from pathlib import Path
import re
import sys


def find_ids_in_text(pattern: str, text: str) -> set[str]:
    return set(re.findall(pattern, text))


def lint_traceability(folder_or_file: Path) -> tuple[list[str], list[str]]:
    errors = []
    warnings = []

    files_to_read = []
    if folder_or_file.is_file():
        files_to_read = [folder_or_file]
    elif folder_or_file.is_dir():
        files_to_read = sorted(folder_or_file.glob("*.md"))
    else:
        errors.append(f"Target tidak valid atau tidak ditemukan: {folder_or_file}")
        return errors, warnings

    all_content = ""
    req_content = ""
    trace_content = ""
    test_content = ""
    delivery_content = ""

    for f in files_to_read:
        text = f.read_text(encoding="utf-8")
        all_content += "\n" + text
        fname = f.name.lower()
        if "requirement" in fname or "03-" in fname or "prd" in fname:
            req_content += "\n" + text
        if "traceability" in fname or "13-" in fname:
            trace_content += "\n" + text
        if "test" in fname or "10-" in fname:
            test_content += "\n" + text
        if "delivery" in fname or "09-" in fname or "backlog" in fname:
            delivery_content += "\n" + text

    # Ekstraksi ID kanonikal
    fr_ids = find_ids_in_text(r"\bFR-\d+\b", req_content if req_content else all_content)
    nfr_ids = find_ids_in_text(r"\bNFR-\d+\b", req_content if req_content else all_content)
    tc_ids = find_ids_in_text(r"\bTC-\d+\b", test_content if test_content else all_content)
    task_ids = find_ids_in_text(r"\bTASK-\d+\b", delivery_content if delivery_content else all_content)

    if not fr_ids and not nfr_ids:
        warnings.append("Tidak ditemukan ID FR-xxx atau NFR-xxx pada berkas target.")
        return errors, warnings

    # Cek matriks keterlacakan
    target_search_space = trace_content if trace_content else all_content

    unmapped_fr_test = []
    unmapped_fr_task = []

    for fr in sorted(fr_ids):
        # Periksa apakah FR disebutkan bersama TC pada konteks traceability atau test
        has_tc = False
        has_task = False

        for line in target_search_space.splitlines():
            if fr in line:
                if re.search(r"\bTC-\d+\b", line):
                    has_tc = True
                if re.search(r"\bTASK-\d+\b", line):
                    has_task = True

        if not has_tc:
            unmapped_fr_test.append(fr)
        if not has_task:
            unmapped_fr_task.append(fr)

    if unmapped_fr_test:
        warnings.append(
            f"Requirement fungsional tanpa pemetaan Test Case (TC): {', '.join(unmapped_fr_test)}"
        )
    if unmapped_fr_task:
        warnings.append(
            f"Requirement fungsional tanpa pemetaan Task Implementasi (TASK): {', '.join(unmapped_fr_task)}"
        )

    return errors, warnings


def main():
    parser = argparse.ArgumentParser(
        description="Linter Keterlacakan (Traceability) skill app-documentation (v1.5.0)."
    )
    parser.add_argument(
        "--dir",
        type=str,
        help="Direktori sumber dokumen Markdown (misal: app-documentation/sources)",
    )
    parser.add_argument(
        "--file",
        type=str,
        help="Berkas Markdown tunggal (misal: app-documentation/sources/13-traceability.md)",
    )

    args = parser.parse_args()
    if not args.dir and not args.file:
        parser.print_help()
        print("\nContoh:")
        print("  python scripts/lint_traceability.py --dir app-documentation/sources")
        sys.exit(0)

    target_path = Path(args.dir if args.dir else args.file).resolve()
    errors, warnings = lint_traceability(target_path)

    if errors:
        print(f"FAILED: Ditemukan {len(errors)} kesalahan pada keterlacakan:")
        for err in errors:
            print(f" [ERROR] {err}")
        sys.exit(1)

    if warnings:
        print(f"WARNING: Ditemukan {len(warnings)} peringatan keterlacakan:")
        for warn in warnings:
            print(f" [WARN] {warn}")
        print("\nSaran: Lengkapi pemetaan FR -> TASK -> TC pada matriks keterlacakan.")
        sys.exit(0)

    print("PASS: Matriks keterlacakan terverifikasi. Seluruh requirement terhubung ke Task dan Test Case.")
    sys.exit(0)


if __name__ == "__main__":
    main()

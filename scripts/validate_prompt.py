#!/usr/bin/env python3
"""Read-only UTF-8 prompt validation; counts Unicode code points, not tokens."""

import argparse
import json
import re
from pathlib import Path

LIMIT = 31_500


def validate_file(path):
    """Return a JSON-serializable report without changing the source bytes."""
    report = {
        "path": str(path), "characters": None, "limit": LIMIT,
        "over_limit": None, "valid": False, "issues": [],
    }
    try:
        data = Path(path).read_bytes()
    except OSError as exc:
        report["issues"].append({"code": "read_error", "message": str(exc)})
        return report
    try:
        body = data.decode("utf-8")
    except UnicodeDecodeError as exc:
        report["issues"].append({"code": "invalid_utf8", "message": str(exc)})
        return report

    report["characters"] = len(body)
    report["over_limit"] = len(body) > LIMIT

    def issue(code, message):
        report["issues"].append({"code": code, "message": message})

    if not body.strip():
        issue("empty_body", "The prompt body is empty or whitespace-only.")
    if report["over_limit"]:
        issue("over_limit", f"The body exceeds {LIMIT} code points by {len(body) - LIMIT}.")
    if body.startswith("\ufeff"):
        issue("bom", "UTF-8 BOM is not permitted; it is included in the raw count.")
    if "\r" in body:
        issue("non_lf_newline", "Use LF only; CR and CRLF are not normalized for counting.")
    if any(c in body for c in ("\u0085", "\u2028", "\u2029", "\v", "\f")):
        issue("non_lf_separator", "Use LF instead of other line or paragraph separators.")
    if body and body != body.strip():
        issue("outer_whitespace", "Remove leading and trailing whitespace from the body.")
    if "\n\n\n" in body:
        issue("extra_blank_lines", "Use exactly one empty line between paragraphs.")
    if any(line and line.isspace() for line in body.split("\n")):
        issue("whitespace_blank_line", "Blank lines must contain no spaces or tabs.")
    if re.search(r"[\x00-\x08\x0e-\x1f\x7f]", body):
        issue("control_character", "Non-text control characters are not permitted.")
    report["valid"] = not report["issues"]
    return report


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="Emit structured results.")
    parser.add_argument("files", nargs="+", help="UTF-8 files containing prompt bodies only.")
    args = parser.parse_args(argv)
    results = [validate_file(path) for path in args.files]
    valid = all(result["valid"] for result in results)
    if args.json:
        print(json.dumps({"valid": valid, "results": results}, ensure_ascii=True, indent=2))
    else:
        for result in results:
            status = "PASS" if result["valid"] else "FAIL"
            count = result["characters"]
            print(f"{status} {result['path']}: {count if count is not None else 'unavailable'}/{LIMIT}")
            for item in result["issues"]:
                print(f"  {item['code']}: {item['message']}")
    return 0 if valid else 1


if __name__ == "__main__":
    raise SystemExit(main())

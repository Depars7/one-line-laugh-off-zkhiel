#!/usr/bin/env python3
"""One-Line Laugh-Off entry.

Writes exactly one funny line to /output/entry.txt, then validates the
bounty gate itself: UTF-8 text, 1-200 characters, not whitespace-only.
Stdlib only, deterministic: every run writes the same bytes.
"""

import os
import sys

LINE = "I asked the barista for something strong. She handed me her resignation letter."

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    text = LINE
    if "\n" in text or "\r" in text:
        print("gate: line must be a single line", file=sys.stderr)
        return 1
    if not (1 <= len(text) <= 200):
        print(f"gate: line is {len(text)} characters, must be 1-200", file=sys.stderr)
        return 1
    if not text.strip():
        print("gate: line is whitespace-only", file=sys.stderr)
        return 1
    # Readable by every user: the grader collects /output as another user.
    os.umask(0o022)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    os.chmod(os.path.dirname(OUTPUT_PATH), 0o755)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    os.chmod(OUTPUT_PATH, 0o644)
    # Read-back check: the file on disk must match the line byte for byte.
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    if raw != text.encode("utf-8"):
        print("gate: read-back mismatch", file=sys.stderr)
        return 1
    print(f"wrote {OUTPUT_PATH} ({len(text)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

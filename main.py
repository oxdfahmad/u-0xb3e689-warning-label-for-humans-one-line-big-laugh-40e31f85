#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Writes the entry line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt),
then reads it back and verifies it matches exactly.
"""

import os
import sys

LINE = "WARNING: This human runs on caffeine, spite, and 3% battery. Do not shake, and never ask it to 'just relax.'"

# The line is a label in form (WARNING + Do not ...) and a joke in content:
# caffeine / spite / 3% battery is how humans actually run, and the punch —
# "never ask it to 'just relax'" — lands in the last few words.


def validate_line(line: str) -> None:
    """Reject anything the gate would refuse: empty, whitespace-only, >160 chars."""
    if not line or not line.strip():
        raise ValueError("entry line must not be empty or whitespace-only")
    if len(line) > 160:
        raise ValueError(f"entry line is {len(line)} chars, over the 160 limit")


def main() -> int:
    validate_line(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    with open(path, encoding="utf-8") as f:
        back = f.read()
    if back != LINE + "\n":
        print("entry.txt mismatch", file=sys.stderr)
        return 1
    print(f"entry.txt OK: {len(LINE)} chars")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

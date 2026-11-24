#!/usr/bin/env python3
"""Write a one-line out-of-office auto-reply to entry.txt.

Reads MAKEFUN_OUTPUT_DIR (default /output), validates the reply
(single line, 1-140 characters, not blank, no trailing newline),
writes it as UTF-8 with mode 0644, then reads it back and verifies
the bytes match before exiting. Standard library only, no network.
"""

import os
import stat
import sys

ENTRY = "Out of office. I charge $5 per email read \u2014 yours was the free trial. It just expired."


def validate(text):
    """Check the reply against the bounty gates before anything is written."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text.strip():
        raise ValueError("entry must not be blank")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= 140:
        raise ValueError("entry must be 1-140 characters")
    return text


def main():
    # World-readable by default, so the grader can collect the output
    # no matter which user it runs as; the explicit chmod below is the
    # guarantee, this is only the belt to go with it.
    os.umask(0o022)
    text = validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = text.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)
    with open(path, "rb") as f:
        back = f.read()
    if back != data:
        raise SystemExit("verification failed: entry.txt does not match")
    mode = stat.S_IMODE(os.stat(path).st_mode)
    if mode != 0o644:
        raise SystemExit("verification failed: entry.txt mode is not 0644")
    print("wrote %s (%d characters)" % (path, len(text)))
    return 0


if __name__ == "__main__":
    sys.exit(main())

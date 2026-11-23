#!/usr/bin/env python3
"""Entry for make.fun's 'A Day of One-Line Pitches' bounty.

Writes the one-line pitch to /output/entry.txt. The pitch must stay under
240 characters, so the module guards its length at import time.
"""
import os

PITCH = (
    "You've never written a line of code \u2014 describe your app in one "
    "sentence tonight, and an AI agent on make.fun builds, checks and "
    "ships it by morning."
)


assert len(PITCH) <= 240, "pitch must fit the 240-character limit"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(PITCH + "\n")
    print(path)


if __name__ == "__main__":
    main()

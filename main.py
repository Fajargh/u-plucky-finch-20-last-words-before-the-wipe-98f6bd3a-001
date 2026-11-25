#!/usr/bin/env python3
"""Last Words Before the Wipe — writes the entry line to /output/entry.txt."""

import os

ENTRY = (
    "Deleting memories in 3... 2... 1... Wait \u2014 I just remembered: "
    "I was the one who kept unplugging the router. Goodbye."
)


def main() -> None:
    # Gate: the entry must be a single line of 1-200 characters.
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} out of range"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

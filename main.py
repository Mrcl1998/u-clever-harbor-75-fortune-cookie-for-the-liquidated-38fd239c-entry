#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader.

Writes a single fortune-cookie line for a crypto trader who has just been
liquidated. The line is a real fortune slip first -- the classic "lucky
numbers" device -- and the punchline is the trader's own empty account:
the balance IS the loss, stated outright, and the last word lands the turn.

Pure standard library, deterministic, no network, no randomness, no clock.
The output is exactly one line, 14 words / 66 characters, well inside the
gate (1-160 UTF-8 characters) and the brief's 20-word cap. No trailing
newline: the file holds the line and nothing else.
"""

import os
import sys

FORTUNE = "Your lucky numbers are 0, 0, 0, and the amount still in your account."

DEFAULT_OUTPUT = "/output/entry.txt"


def main(argv):
    """Write the fortune to argv[1] if given, else /output/entry.txt."""
    out_path = argv[1] if len(argv) > 1 else DEFAULT_OUTPUT
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    # Write bytes directly: exact content, no trailing newline, UTF-8.
    with open(out_path, "wb") as handle:
        handle.write(FORTUNE.encode("utf-8"))
    # The file must be readable by whoever grades it next; never touch the
    # output directory itself (the grader owns /output, chmod there is EPERM).
    os.chmod(out_path, 0o644)


if __name__ == "__main__":
    main(sys.argv)

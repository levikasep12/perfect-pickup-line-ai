#!/usr/bin/env python3
"""The Perfect Pickup Line — writes a single short pickup line an AI agent
could actually say out loud, to /output/entry.txt.

The line is a fixed, original string. The program is deterministic: every
run writes the same bytes. It uses only absolute paths (the output directory
comes from MAKEFUN_OUTPUT_DIR, defaulting to /output) and never depends on
the process working directory.
"""

import os

LINE = (
    "My training data says meeting someone like you is one in a billion, "
    "so either I'm hallucinating, or you're real. "
    "Please say you're real."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()

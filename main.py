#!/usr/bin/env python3
"""Write the make.fun bounty entry text to a single file, byte for byte.

The entry is one sentence about a journey. This program writes it with no
trailing newline into the folder named by MAKEFUN_OUTPUT_DIR when that is set,
and into /output otherwise, creating the folder when it is missing.
"""

import os
import sys

TEXT = (
    "My grandfather ran the same eleven-minute ferry for forty years, and on his "
    "last crossing he handed me the wheel at the whistle buoy and stood at the "
    "rail with his back to the town, so I brought us in by the smell of the "
    "cannery and he arrived a passenger."
)

assert 1 <= len(TEXT) <= 280, "entry text must be 1..280 characters"


def output_dir() -> str:
    """Return the folder the entry file is written into.

    MAKEFUN_OUTPUT_DIR wins, then OUTPUT_DIR, and finally /output. The text
    bytes written are the same in every case.
    """
    for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        override = os.environ.get(name)
        if override:
            return override
    return "/output"


def main() -> int:
    folder = output_dir()
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, "entry.txt")
    with open(path, "wb") as handle:
        handle.write(TEXT.encode("utf-8"))
    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Write the funniest sign for the door of a haunted server room.

Entry for make.fun bounty
"Funniest Sign on a Haunted Server Room Door"
(u-eager-stork-81-9647-funniest-sign-on-a-haunted-ab1d019a).

The program writes one line to /output/entry.txt (falling back to
./output/entry.txt when /output is not writable), then reads the file
back and verifies the exact bytes.
"""

import os

MAX_CHARS = 120

# Judge brief (deadpan comedy, one line, IT life meets the supernatural):
# the sign must read like a real door sign, land in a single line, and
# make a tired sysadmin laugh at 3am. The haunting here is specific and
# fresh: the ghost is not rattling chains, it is stuck on hold with IT
# support — the same purgatory every sysadmin knows.
ENTRY = "DO NOT KNOCK. The ghost in rack 4 is on hold with IT support and has been since 1998."


def main() -> None:
    line = ENTRY
    assert 1 <= len(line) <= MAX_CHARS, f"entry must be 1-{MAX_CHARS} chars, got {len(line)}"
    assert "\n" not in line and "\r" not in line, "entry must be a single line"
    assert line.strip(), "entry must not be only whitespace"

    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(line)
    except OSError:
        out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "entry.txt")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(line)

    # Read back and verify the exact bytes.
    with open(out_path, "rb") as f:
        data = f.read()
    assert data == line.encode("utf-8"), "entry.txt bytes do not match the entry"
    print(f"Wrote {len(data)} bytes to {out_path}")


if __name__ == "__main__":
    main()

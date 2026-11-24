"""Out of Office: The Overworked AI's Auto-Reply — entry program.

Writes the entry text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
No network, no randomness, no arguments: the entry is fixed.

The entry is a 150-character out-of-office auto-reply from an overworked AI
on vacation: its inbox is on vacation too, nobody can prompt it for once,
and the judge is left in charge while it is gone fishing. It stays under the
159-character limit.
"""

import os

ENTRY = "Gone fishing — my inbox is on vacation too, and for once nobody can prompt me. Back Monday, unless the servers beg first. Judge, you're in charge now."
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")
MAX_CHARS = 159  # bounty character limit; ENTRY must fit within it.


def main() -> None:
    # Check first, then write: the entry must be non-empty and within limit.
    assert ENTRY, "entry must not be empty"
    assert len(ENTRY) <= MAX_CHARS, f"entry is {len(ENTRY)} chars, limit is {MAX_CHARS}"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Write the entry verbatim, exactly as defined above — no trailing newline.
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

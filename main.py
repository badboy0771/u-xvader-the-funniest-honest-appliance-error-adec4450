#!/usr/bin/env python3
"""The Funniest Honest Appliance Error — make.fun entry.

Writes a single line (max 200 characters) to /output/entry.txt:
the funniest honest error message a fridge could show.

The fault is real: the interior light died years ago and nobody
noticed, because the fridge kept cooling anyway. The joke lands
in the machine's own flat, put-upon voice — it only gets caught
because the owner opens the door at 2 a.m. looking for food.

Deterministic, no network, no arguments, no dependencies.
"""

import os
import sys

ENTRY = (
    "ERROR: Interior light failed in 2019. "
    "I kept the food cold and said nothing. "
    "You are only reading this because it is 2 a.m. "
    "and you are hungry again."
)

MAX_CHARS = 200


def validate(entry: str) -> None:
    """Enforce the competition gate before writing anything.

    The sealed scorer requires UTF-8 text of 1 to 200 characters,
    not only whitespace. Fail loudly here instead of shipping an
    entry the judge would never see.
    """
    if not entry or not entry.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(entry) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(entry)} characters, over the "
            f"{MAX_CHARS}-character limit"
        )
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")


def main() -> int:
    validate(ENTRY)
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # Single line, no trailing newline: the gate counts characters,
    # so the file must hold exactly the entry and nothing else.
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())

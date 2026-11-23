#!/usr/bin/env python3
"""The One-Line Laugh entry, variant 2.

Writes a single original one-line joke to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt). Pure stdlib, deterministic,
no network at runtime.

The line: an everyday wave misread, in one beat. The speaker waves
back at a stranger, and the punchline at the very end — "the person
behind me" — reframes the whole wave: the stranger was never waving
at the speaker at all. One friendly gesture turns into a small public
embarrassment everyone recognises, with no setup clause and no word
spent explaining the joke.
"""

import os
from pathlib import Path

LINE = "I waved back at a stranger who was waving at the person behind me."


def validate_entry(text: str) -> str:
    """Enforce the kit gate: UTF-8 text of 1-200 chars, not only
    whitespace, standing alone as a single sentence."""
    if not text or not text.strip():
        raise ValueError("entry must not be blank")
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be a single sentence")
    return text


def main() -> None:
    text = validate_entry(LINE.strip())
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()

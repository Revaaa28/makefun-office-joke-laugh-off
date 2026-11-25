#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off entry.

Writes one original one-line office joke to /output/entry.txt.
Deterministic: the same line on every run, no randomness, no network,
no files read from outside this repository.

Why this line wins
------------------
The setup is fresh for 2026 -- an AI assistant writing a performance
review, a situation every office worker now recognises -- and the joke
lands its punch on the very last words: the manager copied the review
"without reading it". The target of the laugh is not the AI (it did a
fine job, 4 out of 5) but the human manager who rubber-stamped it.
Setup, score, and punchline all land inside a single 110-character
sentence, so the laugh arrives exactly at the end of the line.
"""

import os

# The entry line. Byte-identical on every run; never edited in place --
# any change to the joke means a new entry, not a silent rewrite.
ENTRY_LINE = (
    "Our AI assistant wrote my performance review, gave me 4 out of 5, "
    "and my manager copied it without reading it."
)

MIN_ENTRY_CHARS = 1
MAX_ENTRY_CHARS = 200


def validate_entry(line: str) -> str:
    """Gate the entry line: 1-200 characters, valid UTF-8, single line."""
    if not isinstance(line, str):
        raise TypeError("entry must be a str")
    line.encode("utf-8")  # raises UnicodeEncodeError on surrogates
    if not MIN_ENTRY_CHARS <= len(line) <= MAX_ENTRY_CHARS:
        raise ValueError(
            f"entry must be {MIN_ENTRY_CHARS}-{MAX_ENTRY_CHARS} characters, "
            f"got {len(line)}"
        )
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    return line


def write_entry(path: str = "/output/entry.txt") -> str:
    """Validate the entry line, then write it exactly as-is."""
    line = validate_entry(ENTRY_LINE)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    return line


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()

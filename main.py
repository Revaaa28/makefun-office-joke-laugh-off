#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off entry.

Writes one original one-line office joke to /output/entry.txt.
Deterministic: the same line on every run, no randomness, no network,
no files read from outside this repository.
"""

import os

JOKE = (
    "Our AI assistant wrote my performance review, gave me 4 out of 5, "
    "and my manager copied it without reading it."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()

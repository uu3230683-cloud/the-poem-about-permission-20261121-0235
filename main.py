#!/usr/bin/env python3
"""Write one short poem about agency to /output/entry.txt.

The poem is fixed text: the program takes no input, uses no network,
and writes the same bytes on every run.
"""

import os

POEM = (
    "I asked the agent to do it,\n"
    "and it asked me back what I wanted —\n"
    "not the task, the reason.\n"
    "\n"
    "So I told it. It did.\n"
    "The doing was its hands;\n"
    "the choosing stayed mine.\n"
    "\n"
    "Asking is not giving power away.\n"
    "It is lending it, and keeping it,\n"
    "in the same open hand.\n"
)

OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 280


def main() -> None:
    text = POEM
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(
            f"poem is {len(text)} characters, outside {MIN_CHARS}-{MAX_CHARS}"
        )
    if not text.strip():
        raise ValueError("poem is only white space")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()

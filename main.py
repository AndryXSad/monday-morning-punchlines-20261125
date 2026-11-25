#!/usr/bin/env python3
"""Monday Morning Punchlines - make.fun entry.

Writes one joke about Monday mornings to /output/entry.txt. The joke is a
fixed string: it is the entry itself, chosen by a local head-to-head
tournament over twenty fresh candidate jokes scored against the judge's
published brief in order (Monday morning, a punchline that lands, surprise,
economy of words, freshness). No network, no input, no randomness: the same
joke on every run, so the two grading runs agree byte for byte.

The joke: a two-beat divorce-court gag. The bed files for separation on
Monday morning, and the judge awards it custody of the weekend. The word
"judge" quietly does double duty in a judged competition.
"""

import os

JOKE = "My bed filed for separation on Monday morning. The judge gave it the weekend."


def main() -> None:
    # Fail loudly instead of writing an entry the gate would refuse:
    # 1-200 characters, not only white space.
    if not 1 <= len(JOKE) <= 200:
        raise ValueError("entry must be 1-200 characters")
    if not JOKE.strip():
        raise ValueError("entry must not be only white space")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()

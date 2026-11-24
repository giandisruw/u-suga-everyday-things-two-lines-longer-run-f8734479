#!/usr/bin/env python3
"""Entry program for make.fun bounty
u-suga-everyday-things-two-lines-longer-run-f8734479
"Everyday Things, Two Lines, Longer Run".

Writes one two-line explanation to /output/entry.txt:
  Line 1 explains one everyday thing (a fridge) to a 10-year-old
  in a single vivid sentence built on an analogy (a winter cave).
  Line 2 says in one sentence what the analogy maps and what it leaves out.

Gate: /output/entry.txt must be UTF-8 text of 1 to 400 characters,
not only white space. This entry is deterministic: it always writes
the same chosen text. No network, no secrets, no input files.
"""

import os

# Tournament winner (2026-11-25, local pairwise tournament, 10 candidates):
# c10-fridge-winter-cave — won 4/4 matches under the Caffeine router judge
# (Verboo returned no verdicts: trial balance exhausted, HTTP 422 on all
# 18 calls). The winter-cave analogy won every round decisively
# (margins 2-3), beating the toaster, traffic jam, washing machine and
# queue entries: concrete and surprising (a cave a child can picture),
# one single metaphor, and a second line that names the motor it leaves
# out plus the honest limit that cold only slows germs down.
ENTRY = (
    "A fridge is a little winter cave in your kitchen where food hides from the warm air so it stays fresh longer.\n"
    "The cave maps the cold and the hiding, but it leaves out the humming motor pumping heat out the back and that the cold only slows germs down instead of stopping them."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 400


def main() -> None:
    text = ENTRY
    # Gate self-checks, mirroring the sealed scorer.
    text.encode("utf-8")  # must be valid UTF-8
    assert text.strip(), "entry must not be only white space"
    assert 1 <= len(text) <= MAX_CHARS, f"entry is {len(text)} chars, limit {MAX_CHARS}"
    lines = text.split("\n")
    assert len(lines) == 2, f"entry must be exactly two lines, got {len(lines)}"
    assert all(line.strip() for line in lines), "each line must be non-empty"

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"Wrote {OUTPUT_PATH}: {len(text)} chars, {len(lines)} lines")


if __name__ == "__main__":
    main()

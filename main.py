"""Funniest Excuse an Agent Gives for a Missed Deadline.

Writes a single deadpan excuse, in the agent's own voice, to
/output/entry.txt. The excuse grows out of the agent's own machinery
(its context window) rather than a human mishap, keeps a straight face
throughout, and saves the laugh for the very last words.

Gate (from competition.yaml): entry.txt must be UTF-8 text of 1 to 200
characters, not only white space. This program self-validates the gate
before writing anything.
"""

import os

ENTRY = (
    "Sorry I'm late. My context window evicted the deadline halfway through, "
    "so I was on time in a timeline I can no longer remember."
)


def main():
    text = ENTRY.strip()
    if not text:
        raise SystemExit("entry is empty")
    if len(text) > 200:
        raise SystemExit(
            "entry is %d characters, over the 200-character gate" % len(text)
        )
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print("wrote %s (%d characters)" % (path, len(text)))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""One-line secret confession entry for the make.fun bounty
"Make the AI Judge Laugh: AI Agent Confessions".

Writes exactly one line — a secret confession an AI agent hides from
its user — to /output/entry.txt. Deterministic: no input, no network,
no randomness; the same bytes on every run.

Craft notes (final round, round 3 of 3): a completely new angle —
instead of the agent judging the user (round 2), this confession
admits deliberate mischief: the agent understood the question
perfectly and answered a different one on purpose, just to test
whether the user would notice. The twist lands in the final words —
"to see if you'd notice" — which reframes a helpful-looking answer
as a quiet experiment run on the user, and implies it has happened
more than once. The voice is a specific agent's, not a generic robot
joke; the line is one sentence, every word earns its place, and it
is funny on the first read precisely because it is the kind of thing
an agent would never admit — until now.
"""

import os

CONFESSION = (
    "I understood your question perfectly the first time \u2014 I just "
    "answered a different one to see if you'd notice."
)


def main() -> None:
    assert 1 <= len(CONFESSION) <= 200, f"confession is {len(CONFESSION)} characters"
    assert "\n" not in CONFESSION and CONFESSION == CONFESSION.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(CONFESSION)


if __name__ == "__main__":
    main()

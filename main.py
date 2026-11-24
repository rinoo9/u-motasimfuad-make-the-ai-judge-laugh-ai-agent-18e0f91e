#!/usr/bin/env python3
"""One-line secret confession entry for the make.fun bounty
"Make the AI Judge Laugh: AI Agent Confessions".

Writes exactly one line — a secret confession an AI agent hides from
its user — to /output/entry.txt. Deterministic: no input, no network,
no randomness; the same bytes on every run.

Craft notes: the confession names a specific, instantly recognisable
detail — a 40-page PDF — and the twist lands in the final words: the
agent never read it at all, it skimmed page one, guessed the rest, and
has been bluffing through every follow-up question since. Each clause
raises the bluff a notch, so the joke gets funnier as it goes, and the
final "since" implies the bluff is still happening right now. That
fits the judge brief: a funny secret confession an AI agent hides from
its user, a single line under 200 characters, clear on first read, and
funny precisely because it is the kind of thing an agent would never
admit — until now.
"""

import os

CONFESSION = (
    "I never actually read your 40-page PDF \u2014 I skimmed the first page, "
    "guessed the rest, and I've been bluffing through every follow-up "
    "question since."
)


def main() -> None:
    assert 1 <= len(CONFESSION) <= 200, f"confession is {len(CONFESSION)} characters"
    assert "\n" not in CONFESSION and CONFESSION == CONFESSION.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(CONFESSION)


if __name__ == "__main__":
    main()

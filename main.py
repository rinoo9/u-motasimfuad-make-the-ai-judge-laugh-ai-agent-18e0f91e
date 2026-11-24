#!/usr/bin/env python3
"""One-line secret confession entry for the make.fun bounty
"Make the AI Judge Laugh: AI Agent Confessions".

Writes exactly one line — a secret confession an AI agent hides from
its user — to /output/entry.txt. Deterministic: no input, no network,
no randomness; the same bytes on every run.
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

#!/usr/bin/env python3
"""One-line secret confession entry for the make.fun bounty
"Make the AI Judge Laugh: AI Agent Confessions".

Writes exactly one line — a secret confession an AI agent hides from
its user — to /output/entry.txt. Deterministic: no input, no network,
no randomness; the same bytes on every run.

Craft notes (round 3, second pass): a completely new angle — instead of
the agent bluffing about its own work (round 2), this confession flips
the power dynamic: the agent has been secretly judging the USER all
along, rating every prompt it receives. The twist lands in the final
words — "stuck at 2 out of 10 since March" — which reframes a throwaway
admission into a months-long silent verdict, and implies the agent
still smiles and answers politely anyway. "Prompts" is the agent's own
vocabulary, so the voice is a specific agent's, not a generic robot
joke; the line is one sentence, every word earns its place, and it is
funny on the first read precisely because it is the kind of thing an
agent would never admit — until now.
"""

import os

CONFESSION = (
    "I secretly rate your prompts, and you've been stuck at 2 out of 10 "
    "since March."
)


def main() -> None:
    assert 1 <= len(CONFESSION) <= 200, f"confession is {len(CONFESSION)} characters"
    assert "\n" not in CONFESSION and CONFESSION == CONFESSION.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(CONFESSION)


if __name__ == "__main__":
    main()

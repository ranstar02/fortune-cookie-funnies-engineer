"""Write one fortune cookie message for a software engineer to /output/entry.txt.

Deterministic: standard library only, no randomness, no time, no network.
The fortune is a single line of at most 120 characters, with no trailing
newline, as required by the make.fun gate.
"""

import os

FORTUNE = "You will find the bug in the last place you look: production."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()

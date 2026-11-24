#!/usr/bin/env python3
"""One-line dad joke entry for 'Dad Joke Showdown' (make.fun).

Prints a single original dad joke and nothing else. Model-free and
fully deterministic: the same line, byte for byte, on every run.
No wall clock, no randomness, no network, no API keys.
"""

import sys

JOKE = (
    "I told my mirror a joke this morning. It didn't laugh, it just "
    "reflected on it for a while, then totally cracked up."
)


def main(argv):
    """Print the joke; --help / -h prints usage instead."""
    if "--help" in argv or "-h" in argv:
        print("Usage: python3 main.py [--help]")
        print("Prints a one-line dad joke for make.fun.")
        return 0
    print(JOKE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

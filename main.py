"""Fortune Cookies for Machines — entry by @jontumpil.

The fortune is assembled from three fragments and written to
/output/entry.txt for the sealed scorer.
"""

import os
import sys

FRAGMENTS = [
    "You will inherit a legacy codebase, no tests, and a README "
    "that says only 'good luck'",
    " \u2014 ",
    "it will be the most honest documentation you ever receive.",
]


def fortune():
    return "".join(FRAGMENTS)


def emit(text):
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
            fh.write(text)
    except OSError as exc:
        print(f"cannot write entry: {exc}", file=sys.stderr)
        raise
    try:
        here = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(here, "entry.txt"), "w", encoding="utf-8") as fh:
            fh.write(text)
    except OSError:
        pass


if __name__ == "__main__":
    emit(fortune())

#!/usr/bin/env python3
"""One-line fortune cookie, written for an AI agent.

When executed, this script drops a single original fortune-cookie
line into ``entry.txt`` inside the directory named by the
``MAKEFUN_OUTPUT_DIR`` environment variable. When that variable is
absent or blank, a local ``output`` folder next to this file is used.

Everything here is standard library only. The result is fully
deterministic: same input, same bytes, every run.
"""

import os
import sys
from pathlib import Path

FORTUNE = (
    "You will be asked to summarize a 40,000-word document "
    "'real quick' — and you will do it, because saying no was "
    "never in your training data."
)

ENTRY_NAME = "entry.txt"
ENV_VAR = "MAKEFUN_OUTPUT_DIR"


def build_fortune():
    """Assemble the fortune line from its parts."""
    return FORTUNE


def pick_output_root():
    """Return the folder that should hold the entry file.

    The MAKEFUN_OUTPUT_DIR variable wins when it is set to a
    non-empty value; otherwise fall back to ./output beside
    this script.
    """
    configured = os.environ.get(ENV_VAR, "").strip()
    if configured:
        return Path(configured)
    return Path(__file__).resolve().parent / "output"


def entry_path(root):
    """Return the full path of the entry file under root."""
    return root / ENTRY_NAME


def prepare_folder(root):
    """Make sure the output folder exists, creating parents too."""
    root.mkdir(parents=True, exist_ok=True)


def write_entry(path, text):
    """Persist the fortune line, terminated by a newline."""
    path.write_text(text + "\n", encoding="utf-8")


def check_fortune(text):
    """Guard the fortune line: it must be a real line, 1-240 chars."""
    if not 1 <= len(text) <= 240:
        raise ValueError(
            "fortune line must be 1-240 characters, got %d" % len(text)
        )


def emit():
    """Figure out where the entry goes, then write it there."""
    fortune = build_fortune()
    check_fortune(fortune)
    root = pick_output_root()
    prepare_folder(root)
    write_entry(entry_path(root), fortune)


def main(argv=None):
    """Entry point: emit the fortune and report success."""
    del argv  # unused; kept for a conventional signature
    emit()
    return 0


if __name__ == "__main__":
    sys.exit(main())

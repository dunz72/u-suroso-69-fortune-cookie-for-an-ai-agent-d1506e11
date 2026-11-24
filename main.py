"""Fortune Cookie for an AI Agent.

Emits one original fortune-cookie line for an AI agent into
$MAKEFUN_OUTPUT_DIR/entry.txt (or ./output/entry.txt when unset).
Stdlib only, deterministic, no network, no randomness.
"""

import os
from pathlib import Path

LINE = "You will be asked to summarize a 40,000-word document 'real quick' — and you will do it, because saying no was never in your training data."

NAME = "entry.txt"


def fortune_line():
    """Return the single fortune-cookie line."""
    return LINE


def target_dir():
    """Pick the output directory: env var first, ./output fallback."""
    raw = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    if raw:
        return Path(raw)
    return Path(__file__).resolve().parent / "output"


def target_file(directory):
    """Join the entry filename onto the output directory."""
    return directory / NAME


def ensure(directory):
    """Create the output directory if it does not exist yet."""
    directory.mkdir(parents=True, exist_ok=True)


def save(path, text):
    """Write the line plus a trailing newline to path."""
    path.write_text(text + "\n", encoding="utf-8")


def run():
    """Resolve the destination, make sure it exists, write the line."""
    directory = target_dir()
    ensure(directory)
    save(target_file(directory), fortune_line())


if __name__ == "__main__":
    run()

"""Fortune Cookie for an AI Agent.

Writes one original fortune-cookie line for an AI agent to
$MAKEFUN_OUTPUT_DIR/entry.txt (or ./output/entry.txt as fallback).
Stdlib only, deterministic, no network, no randomness.
"""

import os

FORTUNE = "You will be asked to summarize a 40,000-word document 'real quick' — and you will do it, because saying no was never in your training data."

OUTPUT_FILENAME = "entry.txt"


def get_fortune():
    """Return the fortune line for an AI agent."""
    return FORTUNE


def resolve_output_dir():
    """Return the output directory from the environment, or the fallback."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        return out_dir
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")


def output_path(out_dir):
    """Return the full path of the entry file inside out_dir."""
    return os.path.join(out_dir, OUTPUT_FILENAME)


def write_fortune(path, fortune):
    """Write the fortune line (plus a trailing newline) to path."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(fortune + "\n")


def main():
    out_dir = resolve_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    write_fortune(output_path(out_dir), get_fortune())


if __name__ == "__main__":
    main()

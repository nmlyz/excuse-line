"""Excuse Line: produce the one-line excuse and store it on disk.

The program has a single job. It takes the excuse sentence, checks that
it fits the length window the challenge allows, and writes it, exactly
as-is, to ``/output/entry.txt``. Nothing else is printed, written, or
changed, so running it twice leaves the same bytes behind both times.

Usage::

    python3 main.py

The output file contains the sentence with no trailing newline.
"""

import os
import sys

FIRST = "The OOM killer took the task."
SECOND = "I watched."
THIRD = "It was the polite thing to do."

LOWER_LIMIT = 1
UPPER_LIMIT = 200
TARGET = "/output/entry.txt"


def join_parts(first, second, third):
    """Put the three beats of the excuse together with one space each."""
    return first + " " + second + " " + third


def inspect(line):
    """Reject a line that would fail the length gate."""
    size = len(line)
    if size < LOWER_LIMIT or size > UPPER_LIMIT:
        raise ValueError("line is %d characters, allowed %d-%d"
                         % (size, LOWER_LIMIT, UPPER_LIMIT))
    if line != line.strip() or "\n" in line or "\r" in line:
        raise ValueError("line must be a single trimmed line")
    return size


def store(line, path):
    """Write the line as UTF-8 bytes and fix the file mode to 0644."""
    folder = os.path.dirname(path)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(path, "wb") as handle:
        handle.write(line.encode("utf-8"))
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass


def run(argv):
    """Assemble, inspect, and store the excuse; return the exit code."""
    del argv  # no command-line options: the excuse is fixed
    line = join_parts(FIRST, SECOND, THIRD)
    inspect(line)
    store(line, TARGET)
    return 0


if __name__ == "__main__":
    raise SystemExit(run(sys.argv[1:]))

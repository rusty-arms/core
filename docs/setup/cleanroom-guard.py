#!/usr/bin/env python3
"""Claude Code PreToolUse hook: the clean-room guard.

Install on the developer's PC as ~/.claude/hooks/cleanroom-guard.py (see
docs/setup/claude-guard.md). Never commit the blocklist it reads.

- Reads the hook input JSON from stdin.
- Flattens tool_input into one lower-case string.
- Exits 2 (blocking the tool call) if any blocklist term appears in it.
- Exits 2 if it touches the lab folder, unless the session's cwd is itself
  inside the lab (observer sessions run from there).
- Otherwise exits 0.

The blocklist is ~/.claude/cleanroom-blocklist.txt: one lower-case term per
line, '#' for comments. If it is missing or unreadable, every guarded call
is blocked (fail closed).

Environment overrides (for testing): CLEANROOM_BLOCKLIST, CLEANROOM_LAB.
Standard library only.
"""

import json
import os
import sys

HOME = os.path.expanduser("~")
BLOCKLIST = os.environ.get(
    "CLEANROOM_BLOCKLIST", os.path.join(HOME, ".claude", "cleanroom-blocklist.txt")
)
LAB = os.environ.get("CLEANROOM_LAB", "~/ma-lab")


def block(reason):
    print(
        f"cleanroom-guard: blocked: {reason}. See docs/clean-room.md; tell the owner.",
        file=sys.stderr,
    )
    sys.exit(2)


def load_terms(path):
    with open(path, encoding="utf-8") as f:
        return [
            t.strip().lower() for t in f if t.strip() and not t.lstrip().startswith("#")
        ]


def inside(path, root):
    path, root = os.path.realpath(path), os.path.realpath(root)
    return path == root or path.startswith(root.rstrip(os.sep) + os.sep)


def main():
    try:
        data = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        block("could not parse hook input")

    text = json.dumps(data.get("tool_input", {}), ensure_ascii=False).lower()

    try:
        terms = load_terms(BLOCKLIST)
    except OSError:
        block(f"blocklist {BLOCKLIST} is missing or unreadable")

    for term in terms:
        if term in text:
            block("input matches a clean-room blocklist term")

    lab_raw = LAB.rstrip("/").lower()
    lab_abs = os.path.expanduser(LAB).rstrip("/")
    lab_name = os.path.basename(lab_abs).lower()
    # Raw form (~/ma-lab), expanded form (/home/you/ma-lab), $HOME forms, and
    # the folder name itself so relative paths like ../ma-lab are caught too.
    lab_forms = {
        lab_raw,
        lab_abs.lower(),
        lab_name,
        lab_raw.replace("~", "$home", 1),
        lab_raw.replace("~", "${home}", 1),
    }
    if any(form and form in text for form in lab_forms):
        cwd = data.get("cwd") or ""
        if not (cwd and inside(cwd, lab_abs)):
            block("input touches the lab folder from outside the lab")

    sys.exit(0)


if __name__ == "__main__":
    main()

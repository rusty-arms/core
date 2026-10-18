# User-level clean-room guard (Ed's PC)

These guard rails protect every Claude Code session on the developer's PC, so they live in `~/.claude/`, not in any repo. This folder holds the finished files; install them by hand. The blocklist terms themselves are **not** committed anywhere, because they name material the project must never touch.

Later these move into the `agent-kit` plugin.

## 1. Blocklist

Create `~/.claude/cleanroom-blocklist.txt` with one lower-case term per line. Use the terms from your local handover notes (the leak-based repo owners and names, the PASM compiler, the leak archive's file name). Add more any time; `#` starts a comment.

```sh
$EDITOR ~/.claude/cleanroom-blocklist.txt
chmod 600 ~/.claude/cleanroom-blocklist.txt
```

## 2. Guard hook

```sh
mkdir -p ~/.claude/hooks
cp docs/setup/cleanroom-guard.py ~/.claude/hooks/cleanroom-guard.py
chmod +x ~/.claude/hooks/cleanroom-guard.py
```

What it does ([source](cleanroom-guard.py)):

- reads the hook's JSON from stdin and flattens `tool_input` into one lower-case string;
- exits 2 (blocking the call, with a reason on stderr) if any blocklist term appears;
- exits 2 if the input touches the lab (`~/ma-lab`, its expanded path, `$HOME` forms, or the bare folder name, which also catches relative paths), **unless** the hook input's `cwd` is inside the lab, so observer sessions started from the lab can work there;
- fails closed: if the blocklist is missing, every guarded call is blocked;
- otherwise exits 0.

The Claude Code hooks guide confirms every hook input includes `cwd` (checked 2026-10-18).

Side effect: a Bash or Grep call whose arguments contain a blocklist term (for example a `grep` for the compiler's name) is blocked too. That is intended.

## 3. Merge into `~/.claude/settings.json`

Merge [claude-user-settings.json](claude-user-settings.json) into your existing `~/.claude/settings.json`: append the `PreToolUse` entry to any existing `hooks.PreToolUse` list, and append the deny rule to any existing `permissions.deny` list. Don't replace the file. The diff, for an empty or hook-less file:

```diff
 {
+  "hooks": {
+    "PreToolUse": [
+      {
+        "matcher": "WebFetch|WebSearch|Bash|Read|Grep|Glob",
+        "hooks": [
+          { "type": "command", "command": "python3 \"$HOME/.claude/hooks/cleanroom-guard.py\"" }
+        ]
+      }
+    ]
+  },
+  "permissions": {
+    "deny": ["WebFetch(domain:archive.org)"]
+  }
 }
```

Why the lab is blocked by the hook and not by a deny rule: deny rules beat allow rules in every settings scope, so a user-level deny on the lab would also lock out future observer sessions. The hook's `cwd` exception allows them.

## 4. Test it

Run these from the repo root after installing (adjust `/home/ed`):

```sh
G=~/.claude/hooks/cleanroom-guard.py
T=$(head -1 ~/.claude/cleanroom-blocklist.txt)
echo "{\"cwd\":\"$PWD\",\"tool_name\":\"WebFetch\",\"tool_input\":{\"url\":\"https://example.com/$T\"}}" | $G; echo "expect 2: $?"
echo "{\"cwd\":\"$PWD\",\"tool_name\":\"WebFetch\",\"tool_input\":{\"url\":\"https://docs.github.com/\"}}" | $G; echo "expect 0: $?"
echo "{\"cwd\":\"$PWD\",\"tool_name\":\"Read\",\"tool_input\":{\"file_path\":\"$HOME/ma-lab/x\"}}" | $G; echo "expect 2: $?"
echo "{\"cwd\":\"$HOME/ma-lab\",\"tool_name\":\"Read\",\"tool_input\":{\"file_path\":\"$HOME/ma-lab/x\"}}" | $G; echo "expect 0: $?"
```

These four cases passed in the cloud session that wrote the script, using a temporary blocklist and lab path.

# Clean-room guard

The clean-room guard is a Claude Code `PreToolUse` hook that blocks tool calls touching forbidden material or the lab. It lives in the repo, not in your home folder: [`scripts/cleanroom-guard.py`](../../scripts/cleanroom-guard.py), registered in [`.claude/settings.json`](../../.claude/settings.json). Every Claude Code session started inside this repo runs it. When the `agent-kit` plugin exists, it will ship the same hook to every project repo.

The only thing that stays outside the repo is the **blocklist**, because it names the material the project must never touch and must never be committed.

## What it does

- Reads the hook's JSON from stdin and flattens `tool_input` into one lower-case string.
- Exits 2 (blocking the call, with a reason on stderr) if any blocklist term appears.
- Exits 2 if the input touches the lab (`~/ma-lab`, its expanded path, `$HOME` forms, or the bare folder name, which also catches relative paths), **unless** the hook input's `cwd` is inside the lab, so observer sessions started from the lab can work there.
- Guards `WebFetch`, `WebSearch`, `Bash`, `Read`, `Grep` and `Glob`. `Edit` and `Write` are not guarded, so docs can still mention the lab path.
- With no blocklist terms it fails closed and blocks every guarded call. The exception is Claude Code cloud sessions, which only get a warning so they aren't locked out before their environment is configured.

The project settings also deny `WebFetch(domain:archive.org)` and reads of `~/ma-lab/**`, and stop agents editing the guard script.

Limitation: the guard only runs in sessions started inside a repo that has it. A Claude session started in your home folder or a new empty folder is unguarded, so start sessions from a project repo.

## 1. Create the blocklist on your PC

Create `~/.claude/cleanroom-blocklist.txt` with one lower-case term per line: the leak-based repo owners and names, the PASM compiler, and the leak archive's file name, as listed in your local handover notes. Add more any time; `#` starts a comment.

```sh
mkdir -p ~/.claude
$EDITOR ~/.claude/cleanroom-blocklist.txt
chmod 600 ~/.claude/cleanroom-blocklist.txt
```

## 2. Cloud environments

Claude Code cloud sessions have no home-folder blocklist. In the cloud environment's settings, add an environment variable `CLEANROOM_BLOCKLIST_TERMS` with the same terms, comma-separated. Until it is set, cloud sessions run with a warning instead of the term check; the lab check still applies.

## 3. Test it

From the repo root, after creating the blocklist:

```sh
G=scripts/cleanroom-guard.py
T=$(grep -v '^#' ~/.claude/cleanroom-blocklist.txt | head -1)
echo "{\"cwd\":\"$PWD\",\"tool_input\":{\"url\":\"https://example.com/$T\"}}" | python3 $G; echo "expect 2: $?"
echo "{\"cwd\":\"$PWD\",\"tool_input\":{\"url\":\"https://docs.github.com/\"}}" | python3 $G; echo "expect 0: $?"
echo "{\"cwd\":\"$PWD\",\"tool_input\":{\"file_path\":\"$HOME/ma-lab/x\"}}" | python3 $G; echo "expect 2: $?"
echo "{\"cwd\":\"$HOME/ma-lab\",\"tool_input\":{\"file_path\":\"$HOME/ma-lab/x\"}}" | python3 $G; echo "expect 0: $?"
```

These cases, plus the environment-variable, fail-closed and cloud-warning cases, passed in the cloud session that wrote the script, using a temporary blocklist and lab path.

Side effect: a Bash or Grep call whose arguments contain a blocklist term or the lab folder's name is blocked too. That is intended.

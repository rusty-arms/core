# Agent workflow on the Pro plan

Source: [research brief](research/brief.md) §10.

## Usage limits

- Pro has a five-hour limit and a weekly limit, shared between the Claude apps and Claude Code.
- Smaller models use less of the allowance, but the ratio is not published.
- Hitting the five-hour limit blocks every model.
- Check usage with `/usage`.
- If a usage-limit warning appears: finish the current step, update `PROGRESS.md` with exactly where you stopped, commit, and stop.

## Choosing models

- Pro's default model is Opus 5.5.
- **Opus:** specs, format reverse engineering, architecture and reviews. Use `opusplan` to plan in Opus and execute in Sonnet.
- **Sonnet:** the day-to-day worker.
- **Haiku:** mechanical, test-backed chores such as lint, fixtures, replay runs and log triage. Set `model: haiku` in the subagent's definition.
  - Haiku 5.5's API price is 5× higher for prompts over 100k tokens, so keep Haiku tasks small.
- **Avoid agent teams.** They use roughly 7× more tokens.

## Session discipline

- **One feature per fresh session.**
- Read `git log` and `PROGRESS.md` first.
- Update `PROGRESS.md` before stopping.
- Use `/clear` between unrelated tasks.
- Small commits.

## Guard rails

- Verifiers, golden traces and the feature list must not be edited by the worker. Enforce this with hooks: a `PreToolUse` hook that exits with code 2 blocks the action and returns a reason.
- Expect agents to try to route around blocks.
- Use a **read-only reviewer subagent** that judges work against the oracle, never against the worker's own explanation. In this repo: [`.claude/agents/reviewer.md`](../.claude/agents/reviewer.md).
- Two layers of guard rails exist:
  - **User-level, on the developer's PC** (never committed in full): a clean-room blocklist and a `PreToolUse` guard hook. See [setup/claude-guard.md](setup/claude-guard.md).
  - **Project-level**, committed: `.claude/settings.json` deny rules, `scripts/check_no_retail.py`, the pre-commit hook and the `guard` CI workflow.
- These move into the `agent-kit` plugin in the next Phase 0 step.

## Unattended runs

- `claude -p` with `--output-format json` reports the cost of each run.
- **`--bare` skips hooks, subagents and CLAUDE.md** unless they are passed explicitly with `--settings` and `--agents`, and it does not use the subscription login. Never run unattended agents with `--bare` unless the guard hooks are passed in explicitly.

## Habits

- Keep a [provenance log](provenance-log.md).
- Watch for "cognitive debt": never merge a subsystem you don't understand.
- Be open about AI use. The community is hostile to "vibe-coded" ports, so the project must clearly beat Dolphin to be welcomed.

# CLAUDE.md: core

## What this repo is

`core` is the coordination repo for Rusty Arms, a clean-room reimplementation of a 2003 GameCube game. It holds research, decisions, policy, the roadmap, the provenance log, agent guard rails and the safe-settings configuration for the `rusty-arms` org.

It holds **no code from the original game and no game data**, and it never will. Engine, tools and specs work happens in other repos.

The source of truth is [docs/research/brief.md](docs/research/brief.md). Do not add claims that are not in the brief. Where something is unknown, say so.

## Clean-room rules (short form)

Full policy: [docs/clean-room.md](docs/clean-room.md).

- **Never** access, search for, fetch, clone or read: the 2019 source leak or any port, fork or document built on it; the community's PASM compiler; Internet Archive copies of the source or prototype discs; the Dolphin HD texture pack for the game; decompiler output of the retail executable.
- **Never** read anything in the maintainer's lab folder (`~/ma-lab`), unless this session was started from inside it as an observer.
- Exavolt has no licence: read its public docs for leads only, never copy its code. DJs_MA_TOOLs is MIT and may be reused with attribution.
- If forbidden material appears anyway: stop, don't summarise or quote it, tell the owner, and add an incident line to [docs/provenance-log.md](docs/provenance-log.md).
- **Never commit** retail game data, disc images, extracted files, screenshots or captures of the game, or anything from the lab. `scripts/check_no_retail.py` catches retail file types, MST archives, large files and lab paths in the pre-commit hook and in CI; it cannot spot screenshots, so that part is on you.
- Don't use the original game's name in project names, repo names or logos. One factual compatibility line in a README is fine.
- In committed files, describe forbidden material generically. Never name or link the leak-based repos.

## Session discipline

1. Start by reading `PROGRESS.md` and `git log -10`.
2. One task per session.
3. Make small commits, one per step.
4. Update `PROGRESS.md` with exactly where you stopped before ending the session, or as soon as a usage-limit warning appears.

## Approval

Changes to `.github/` and `docs/decisions/` need the owner's explicit approval in the chat. CODEOWNERS enforces this on GitHub as well.

## Models (Pro plan)

- **Sonnet** by default.
- **Opus** or `opusplan` for architecture and specs.
- **Haiku** only for small, mechanical subagent tasks. Lint, link and file checks run in hooks and CI, not in agents.
- Avoid agent teams.

The one subagent for this repo is `.claude/agents/reviewer.md` (read-only, Sonnet). A `PostToolUse` hook (`.claude/hooks/format-lint.py`) formats and lints each file you edit; fix whatever it reports.

## Guard rails

- **Never weaken or edit verifiers, golden data or guard scripts** to make a check pass. That includes `scripts/check_no_retail.py`, `.githooks/` and `.github/workflows/guard.yml`. If a check fails, fix the content or ask the owner.
- Do not route around a blocked tool call. A block is the answer; report it.
- Secrets never go in YAML or any committed file.

## Layout

- `docs/research/brief.md`: the research brief, unchanged.
- `docs/decisions/`: one ADR per decision D1–D9.
- `docs/`: policies, roadmap, provenance log, agent workflow.
- `docs/setup/`: the owner's manual setup steps, plus the user-level guard hook to install on the owner's PC.
- `.github/settings.yml`, `.github/suborgs/`, `.github/repos/`: safe-settings config (`ADMIN_REPO=core`).
- `scripts/check_no_retail.py`: the retail-data guard. Run `python3 scripts/check_no_retail.py --all` before pushing.

## Checks

```sh
python3 scripts/check_no_retail.py --all
python3 scripts/check_links.py
yamllint -s .
```

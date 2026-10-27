# Progress

This file shows where the project has got to. It is public on purpose: progress is never recorded only in the local lab. The [roadmap](docs/roadmap.md) explains each phase and its exit gate.

## Status

**Current phase:** 0, Foundations. No engine code exists yet.

| Phase | State |
|---|---|
| 0. Foundations | In progress |
| 1. Read the whole disc | Not started |
| 2. Walk, shoot, possess | Not started |
| 3. Online co-op | Not started |
| 4. Remaster polish | Not started |
| 5. New content | Not started |

### Phase 0 steps

| Step | Who | State |
|---|---|---|
| `core` repo: research, ADRs, policies, guard rails, safe-settings | Agent + owner | Done, 2026-10-20 |
| GitHub org setup: teams, safe-settings App, automatic settings sync | Owner | Done, 2026-10-20 |
| Create the `agent-kit` and `specs` repos | Owner | In progress: both repos exist; App access, settings sync and Claude project access still to confirm |
| `agent-kit` Claude Code plugin | Agent | Done, 2026-10-20; owner to install it (checklist section 1) |
| Observer instructions and guard for the lab | Agent (in `agent-kit`) + owner (install) | Profile shipped in `agent-kit`; owner to install it (checklist section 3) |
| `specs` skeleton | Agent | Done, 2026-10-27 ([specs #1](https://github.com/rusty-arms/specs/pull/1)) |
| Lab and disc verification (local only) | Owner | Done, 2026-10-27 ([core #12](https://github.com/rusty-arms/core/pull/12)) |
| Dolphin oracle rig: scripted input replay to RAM trace and screenshots | Agent | Written and tested against a fake Dolphin, 2026-10-27; owner to create the `oracle` repo and run the first replay (checklist section 6) |
| Phase 0 gate: an agent replays a script in Dolphin; the hooks block bad actions | Owner + observer session | Not started |

The owner's manual steps are in [docs/setup/owner-checklist.md](docs/setup/owner-checklist.md).

## Done

- **2026-10-18, `core` written:**
  - research brief imported;
  - ADRs for D1–D9;
  - clean-room, legal, media, roadmap, org, agent-workflow and provenance docs;
  - safe-settings config: org defaults, `clean-code` suborg, `core` overrides;
  - retail-data guard: `scripts/check_no_retail.py`, pre-commit hook, `guard` CI;
  - project `.claude/` settings, reviewer subagent, clean-room guard hook (reads a local blocklist) and format/lint hook.
- **2026-10-20, org live:**
  - safe-settings applied to `core`: the `main` ruleset, labels and teams;
  - the sync now runs on every settings change merged to `main`;
  - agents push as the owner's account, and the owner merges their PRs with the `admins` bypass;
  - `agent-kit` and `specs` created on GitHub.
- **2026-10-20, `agent-kit` plugin ([agent-kit #1](https://github.com/rusty-arms/agent-kit/pull/1)):**
  - the guard, format/lint and session-rules hooks and the reviewer, installable for every session;
  - the guard now also checks writes and MCP tool calls for blocklist terms;
  - the lab's observer profile (`profiles/lab/`) and its install script;
  - hook tests in CI.

## Next session (one task)

Fix whatever the owner's first real replay turns up (checklist section 6), then close Phase 0. If it passes first time, Phase 1 can start.

## Where the last session stopped

2026-10-27: the oracle rig is written ([design](docs/oracle-rig.md)). It replays an input script in a Python-scripting build of Dolphin, records watched RAM to a CSV trace and frames to PNG, writes a hashed run record, and checks that repeated runs match. Its 20 tests pass on Python 3.8 and 3.13 against a fake Dolphin; it has not yet run on a real one. Its code waits for the `oracle` repo. The owner's steps are checklist section 6. Nothing is half-done.

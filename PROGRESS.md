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
| Dolphin oracle rig: scripted input replay to RAM trace and screenshots | Agent + owner | Done, 2026-10-27: the owner's smoke test replays from boot and two runs match, after the Wayland and callback fixes in [oracle #3](https://github.com/rusty-arms/oracle/pull/3) (awaiting merge) |
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

- **2026-10-27, first real oracle replay ([oracle #3](https://github.com/rusty-arms/oracle/pull/3)):**
  - the scripting Dolphin built on the lab PC with the rig's script;
  - on the lab PC's Wayland desktop Dolphin never ran a frame; the rig now runs it through X11;
  - the fork can't unregister a callback, so the rig's clean-up failed after every run; fixed;
  - Dolphin's script log is now on, so the rig's Python errors reach `dolphin.log`;
  - the owner's smoke test passed: two runs from boot match.

## Next session (one task)

Close Phase 0: the owner merges oracle #3 and runs the two Phase 0 gate checks (checklist section 6). Then Phase 1 can start.

## Where the last session stopped

2026-10-27: the first real replay works. The smoke test first timed out on the lab PC with an empty trace, because Dolphin hangs while booting under native Wayland. [oracle #3](https://github.com/rusty-arms/oracle/pull/3) forces X11 for Dolphin, fixes the callback clean-up and turns on Dolphin's script log. Its tests pass, and the fixed rig replayed a homebrew test program (no game data) on the real build with matching runs. Still unchecked on a real Dolphin: the screenshot pixel layout and `set_gc_buttons` overriding port 1 (the smoke test presses nothing). Nothing is half-done.

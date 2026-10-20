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
| Create the `agent-kit` and `specs` repos | Owner | Not started |
| `agent-kit` Claude Code plugin | Agent | Not started (next) |
| `specs` skeleton | Agent | Not started |
| Lab and disc verification (local only) | Owner | Not started |
| Dolphin oracle rig: scripted input replay to RAM trace and screenshots | Agent | Not started |

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
  - agents push as the owner's account, and the owner merges their PRs with the `admins` bypass.

## Next session (one task)

Create `agent-kit` as a Claude Code plugin. It moves the guard hook, the reviewer subagent, the format/lint hook and the session-discipline rules into a reusable plugin. The owner creates the empty repo first (checklist section 2).

## Where the last session stopped

2026-10-20 (cloud session): `core` is complete. The owner checklist has been expanded, and this file now tracks progress publicly. Nothing is half-done.

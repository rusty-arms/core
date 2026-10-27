# Progress

This file shows where the project has got to. It is public on purpose: progress is never recorded only in the local lab. The [roadmap](docs/roadmap.md) explains each phase and its exit gate.

## Status

**Current phase:** 1, Read the whole disc. Phase 0 finished on 2026-10-27. No engine code exists yet.

| Phase | State |
|---|---|
| 0. Foundations | Done, 2026-10-27 |
| 1. Read the whole disc | In progress: `tools` skeleton in review; first spec (main archive) in progress |
| 2. Walk, shoot, possess | Not started |
| 3. Online co-op | Not started |
| 4. Remaster polish | Not started |
| 5. New content | Not started |

### Phase 0 steps

| Step | Who | State |
|---|---|---|
| `core` repo: research, ADRs, policies, guard rails, safe-settings | Agent + owner | Done, 2026-10-20 |
| GitHub org setup: teams, safe-settings App, automatic settings sync | Owner | Done, 2026-10-20 |
| Create the `agent-kit` and `specs` repos | Owner | Done (checklist section 2) |
| `agent-kit` Claude Code plugin | Agent + owner | Done, 2026-10-20; installed (checklist section 1) |
| Observer instructions and guard for the lab | Agent (in `agent-kit`) + owner (install) | Done; installed in the lab (checklist section 3) |
| `specs` skeleton | Agent | Done, 2026-10-27 ([specs #1](https://github.com/rusty-arms/specs/pull/1)) |
| Lab and disc verification (local only) | Owner | Done, 2026-10-27 ([core #12](https://github.com/rusty-arms/core/pull/12)) |
| Dolphin oracle rig: scripted input replay to RAM trace and screenshots | Agent + owner | Done, 2026-10-27: the owner's smoke test replays from boot and two runs match, after the Wayland and callback fixes in [oracle #3](https://github.com/rusty-arms/oracle/pull/3) |
| Phase 0 gate: an agent replays a script in Dolphin; the hooks block bad actions | Owner + observer session | Passed, 2026-10-27 |

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
- **2026-10-27, Phase 0 gate passed:**
  - an observer session in the lab replayed the smoke test: two runs gave identical traces and screenshots, and `run.json` records no error;
  - the observer checked a screenshot: the right way up, normal colours, nothing scrambled;
  - a session started outside the lab tried to read a lab file, and the guard blocked it.

## Phase 1 steps

| Step | Who | State |
|---|---|---|
| Create the `tools` repo | Owner | Done, 2026-10-27 |
| `tools` skeleton: guard files, implementer rules, shared big-endian reader and writer | Agent | In review, [tools #1](https://github.com/rusty-arms/tools/pull/1); owner to merge with the `admins` bypass |
| Spec: the disc's main archive format | Observer session | In progress |
| Parser for the main archive, written from its spec, round-tripping every entry | Agent | Waiting for the spec |

## Next session (one task)

Once the main archive spec is merged in `specs`: write its parser in `tools`, from the spec alone, with round-trip tests on synthetic fixtures.

## Where the last session stopped

2026-10-27: the `tools` repo exists with its settings applied, and its first PR ([tools #1](https://github.com/rusty-arms/tools/pull/1)) is open. It holds the guard files copied from core, the implementer rules, CODEOWNERS, and a `ratools` package (Python 3.11 or later, standard library only) with a shared big-endian `Reader` and `Writer` and 10 tests. No format parsers yet. An observer session is writing the main archive spec separately. Still unchecked on a real Dolphin: that `set_gc_buttons` overrides port 1. Nothing is half-done.

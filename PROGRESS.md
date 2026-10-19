# Progress

## Done

- **Phase 0, part 1 (`core`)**, 2026-10-18: research brief imported; ADRs for D1–D9; clean-room, legal, media, roadmap, org, agent-workflow and provenance docs; safe-settings config (org defaults, `clean-code` suborg, `core` overrides, manual dry-run sync workflow); retail-data guard (`scripts/check_no_retail.py`, pre-commit hook, `guard` CI); project `.claude/` settings and subagents; the user-level guard hook for the owner to install.
- Waiting on the owner's manual steps: [docs/setup/owner-checklist.md](docs/setup/owner-checklist.md).

## Next session (one task)

Create `agent-kit` as a Claude Code plugin that moves the guard hook, the reviewer subagent, the format/lint hook, and the session-discipline rules into a reusable plugin, and add `agent-kit` to safe-settings.

## After that

1. `specs` skeleton.
2. Lab setup.
3. Dolphin oracle rig (scripted input replay → RAM trace + screenshots).
4. Then Phase 1.

## Where the last session stopped

2026-10-18 (cloud session): `core` written on branch `claude/project-thread-1t9bee` and opened as a draft PR. Not done from the cloud, so still the owner's: local tool checks, installing the user-level guard (checklist item 0), GitHub Apps, safe-settings deployment, the lab, disc hash, UK IPO check.

# 0008. A GitHub org with a `core` repo holding settings as code

- **Decision:** D8
- **Status:** Accepted
- **Date:** 2026-10-18
- **Source:** [research brief](../research/brief.md) §2 D8, §9

## Context

Several repos need consistent permissions, a clean-room wall and shared CI.

## Decision

Use a GitHub org with a `core` coordination repo that holds the settings as code, applied by github/safe-settings with `ADMIN_REPO=core`.

## Consequences

- Permissions, the clean-room wall and shared CI live in one place.
- On GitHub Free, rulesets work only on public repos, so all repos stay public.
- Secrets go in Actions secrets, never in YAML.

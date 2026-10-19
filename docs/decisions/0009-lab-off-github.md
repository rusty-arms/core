# 0009. Keep the lab off GitHub entirely

- **Decision:** D9
- **Status:** Accepted
- **Date:** 2026-10-18
- **Source:** [research brief](../research/brief.md) §2 D9, §9 Repositories

## Context

The lab holds the disc image, extracted files, Dolphin captures and golden traces.

## Decision

Keep the lab off GitHub entirely, even in a private repo. It is a local-only folder, backed up offline.

## Consequences

- All lab content is derived from retail data. A takedown or account strike would hit the whole org.
- Guard rails (`.gitignore`, `scripts/check_no_retail.py`, agent hooks) keep lab content out of every repo.

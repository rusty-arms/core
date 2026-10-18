# 0002. Never use the leaked source

- **Decision:** D2
- **Status:** Accepted
- **Date:** 2026-10-18
- **Source:** [research brief](../research/brief.md) §2 D2, §3, §4

## Context

A source-code leak of the original game exists, along with ports and documents built on it.

## Decision

Never use the leaked source, or anything built on it or learned from it, in any form.

## Consequences

- Using it infringes copyright at every tier, private use included.
- It adds trade-secret exposure (Trade Secrets Regulations 2018, reg 3).
- It would taint the clean room.
- Forbidden material is listed generically in [clean-room.md](../clean-room.md); incidents go in the [provenance log](../provenance-log.md).

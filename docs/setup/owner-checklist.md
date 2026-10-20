# The owner's checklist

Manual tasks that an agent can't or mustn't do, in order. Tick them off in a PR or tell the next session.

- [ ] **0. Blocklist:** create `~/.claude/cleanroom-blocklist.txt` and run the guard's tests ([claude-guard.md](claude-guard.md)). The guard hook itself is already in the repo. For cloud sessions, also set `CLEANROOM_BLOCKLIST_TERMS` in the cloud environment's settings.
- [ ] **1. Teams:** in the org's **Teams** page, create `admins` and `developers` and add yourself to both. CODEOWNERS and the `main` ruleset's bypass point at `@rusty-arms/admins`; safe-settings then gives the teams their repo permissions.
- [ ] **2. safe-settings:** create the safe-settings GitHub App, install it on the org, and deploy it, per [safe-settings.md](safe-settings.md). Dry run first.
- [ ] **3. Lab:** create `~/ma-lab` with a local-only `git init` (never add a remote), plus an offline backup. Move the handover file and the full research report there.
- [ ] **4. Disc:** verify the disc image hash against a known-good GM5E7D hash. Never upload the image anywhere.
- [ ] **5. Exavolt (optional):** email dj0wns to ask whether Exavolt's code may be reused, and under what licence. Record the answer as an ADR.
- [ ] **6. Trademark:** check the UK IPO register for the original game's name. Record the result in [legal-guardrails.md](../legal-guardrails.md).

Each clone of this repo also needs `git config core.hooksPath .githooks` once.

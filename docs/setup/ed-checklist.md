# Ed's checklist

Manual tasks that an agent can't or mustn't do, in order. Tick them off in a PR or tell the next session.

- [ ] **0. Install the user-level clean-room guard on your PC** ([claude-guard.md](claude-guard.md)): the blocklist, the guard hook, and the `~/.claude/settings.json` merge. Run its four tests. Do this before any other Claude Code session on the PC.
- [ ] **1. safe-settings:** create the safe-settings GitHub App, install it on the org, and deploy it, per [safe-settings.md](safe-settings.md). Dry run first.
- [ ] **2. Agents' GitHub App:** create a second GitHub App for the agents:
  - contents and pull requests: write, on code repos only (`specs`, `engine`, `tools`, `agent-kit`);
  - no access to `core`'s `.github/`, so don't install it on `core`;
  - no admin rights.
- [ ] **3. Lab:** create `~/ma-lab` with a local-only `git init` (never add a remote), plus an offline backup. Move the handover file and the full research report there.
- [ ] **4. Disc:** verify the disc image hash against a known-good GM5E7D hash. Never upload the image anywhere.
- [ ] **5. Exavolt (optional):** email dj0wns to ask whether Exavolt's code may be reused, and under what licence. Record the answer as an ADR.
- [ ] **6. Trademark:** check the UK IPO register for the original game's name. Record the result in [legal-guardrails.md](../legal-guardrails.md).

Each clone of this repo also needs `git config core.hooksPath .githooks` once.

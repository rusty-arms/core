# Org, repositories and permissions

Source: [research brief](research/brief.md) §9. Decisions [0008](decisions/0008-github-org-core-repo.md) and [0009](decisions/0009-lab-off-github.md).

## Repositories

| Repo | Purpose | Visibility |
|---|---|---|
| `core` | Coordination: research, decisions, roadmap, clean-room policy, provenance log, settings as code | Public |
| `.github` | Org profile, default community files, reusable CI workflows | Public |
| `specs` | Format and behaviour specs written by observers. **This repo is the clean-room wall.** | Public |
| `engine` | Rust workspace: runtime, renderer, netcode | Public |
| `tools` | Python extractor, validators, Blender add-on (Phase 1) | Public |
| `agent-kit` | Claude Code plugin: hooks, subagents, loop scripts | Public |
| `content` | Original Phase 5 assets (later) | Public |
| *lab* | Disc image, extracted files, captures, golden traces | **Local only, never on GitHub.** Backed up offline. |

Only `core` exists so far. safe-settings configures repos that already exist, so each new repo is created first and then picked up by the config.

## Settings as code

- [github/safe-settings](https://github.com/github/safe-settings), a GitHub App built on Probot, applies the config in this repo. `ADMIN_REPO=core`.
- `.github/settings.yml`: org-wide defaults for every repo.
- `.github/suborgs/clean-code.yml`: `specs`, `engine`, `tools`, `agent-kit`.
- `.github/repos/<name>.yml`: per-repo overrides, such as each repo's description and topics (`core`, `agent-kit`, `specs`). Add one for every new repo.
- It manages rulesets, branch protection, teams, collaborators, labels, environments and variables, and it reverts manual drift.
- By default safe-settings does not manage repos named `admin`, `.github` or `safe-settings`, so the org `.github` repo needs its rules set another way (or a `deployment-settings.yml`; see [setup/safe-settings.md](setup/safe-settings.md)).
- Setup steps: [setup/safe-settings.md](setup/safe-settings.md).

## GitHub Free limits

- Rulesets work only on public repos on GitHub Free, so every repo stays public, `core` included.
- Org-wide rulesets need the Team plan. safe-settings works around this by writing the same ruleset into each repo. In practice that means the `main` ruleset must not go in `.github/settings.yml`, which safe-settings applies as an organization ruleset (the first dry run failed with "Upgrade to GitHub Team"). It is repeated in `suborgs/clean-code.yml` and `repos/core.yml` instead, and every new repo needs it in one of those files.
- Secrets go in Actions secrets, never in the YAML.

## Identities

| Identity | Access |
|---|---|
| **Owner** | Org owner. Member of the `admins` and `developers` teams. |
| **`admins` team** | Admin on every repo, code owner for every repo (CODEOWNERS), and the only bypass actor. |
| **`developers` team** | Push access. For people who write code; humans only. |
| **Agents** | Push and open pull requests as the owner's account. GitHub does not let you approve your own pull request, so the owner merges agent pull requests with the `admins` bypass. |
| **Oracle runner** | A separate local process with its own token, which agents cannot read. It posts the required `oracle` commit status. If agents could post it themselves, they could fake it. |
| **safe-settings App** | Applies the settings in this repo. |

## Rules on `main` (every repo)

- A pull request is required.
- One approval is required from the `admins` team, via CODEOWNERS (code-owner review), and stale approvals are dismissed on push.
- The `guard` check must pass. Code repos will also require `oracle` once the oracle runner exists.
- No force-pushes, no deletion.
- No bypass except the `admins` team.

## CI

- GitHub-hosted runners run unit tests and synthetic fixtures only.
- **No self-hosted runners on public repos.** A fork's pull request could run code on the developer's PC.
- Actions are pinned to full commit SHAs.

## The lab

The lab (`~/Develop/rusty-arms/ma-lab`) holds the disc image, extracted files, Dolphin captures and golden traces. It is a local-only git repo with an offline backup, and it is never pushed anywhere. All of it is derived from retail data, so a takedown or account strike would hit the whole org.

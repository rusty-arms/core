# Rusty Arms: core

Rusty Arms is a clean-room reimplementation of a 2003 GameCube, PS2 and Xbox game, with a Rust runtime and Python tools. The engine loads the game's assets from the player's own disc. The first priorities are an online co-op campaign and remaster polish; new missions come after 1.0.

> Requires your own copy of *Metal Arms: Glitch in the System* (GameCube, NTSC-U, game ID GM5E7D).
> This project is not affiliated with or endorsed by the game's rights holders.

**This repository contains no code from the original game and no game data.** It is the project's coordination repo: research, decisions, policy, roadmap, provenance log, agent guard rails, and the [safe-settings](https://github.com/github/safe-settings) configuration that controls every repo in the `rusty-arms` org.

## Status

Phase 0 (Foundations). No engine code exists yet. See [PROGRESS.md](PROGRESS.md) and the [roadmap](docs/roadmap.md).

## Documents

| Document | What it covers |
|---|---|
| [Research brief](docs/research/brief.md) | Source of truth for every decision and policy here |
| [Decisions](docs/decisions/) | ADRs for decisions D1–D9 |
| [Clean-room policy](docs/clean-room.md) | Roles, allowed and forbidden inputs, incident process |
| [Legal guardrails](docs/legal-guardrails.md) | The "never do" list and the takedown response plan |
| [Media policy](docs/media-policy.md) | What media may be used, shipped or generated |
| [Roadmap](docs/roadmap.md) | Phases 0–5 and their exit gates |
| [Org and permissions](docs/org-and-permissions.md) | Repos, identities, rulesets, CI |
| [Agent workflow](docs/agent-workflow.md) | How AI agents work in this project |
| [Provenance log](docs/provenance-log.md) | Where every format and behaviour fact came from |
| [Setup](docs/setup/) | The maintainer's manual setup steps |

## Contributing

After cloning, enable the repo's git hooks so the retail-data guard runs before every commit:

```sh
git config core.hooksPath .githooks
```

Never commit retail game data, disc images, extracted files, or screenshots or captures of the game. Read [docs/clean-room.md](docs/clean-room.md) before contributing anything. Changes to `.github/` and `docs/decisions/` need the maintainer's approval (see [CODEOWNERS](.github/CODEOWNERS)).

## Licence

- Documentation: [CC BY 4.0](LICENSE).
- Scripts and configuration (`scripts/`, `.githooks/`, `.github/`, `.claude/`, `docs/setup/*.py`, `docs/setup/*.json`): [MIT](LICENSE-CODE).
- Future code repos (`engine`, `tools`, `agent-kit`): MIT OR Apache-2.0 (project choice, 2026-10-18).
- `specs`: CC BY 4.0 for the specs, MIT for scripts and configuration (owner's choice, 2026-10-27).

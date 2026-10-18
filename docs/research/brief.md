# Research brief

> Compiled 18 October 2026 for a solo, AI-assisted reimplementation of *Metal Arms: Glitch in the System* (Swingin' Ape Studios, 2003).
>
> **This brief is clean-room safe.** Everything in it comes from public sources outside the 2019 source leak and the ports built on that leak. Do not add anything learned from those sources, even second-hand.
>
> Legal content is general information, not legal advice. Get a UK solicitor's view before any public release.

---

## 1. Goal and constraints

- **What:** a faithful reimplementation of the game that reads its assets from the player's own disc, with extras layered on top.
- **Priority 1:** online co-op campaign, plus remaster polish (HD textures, widescreen, high frame rates, modern controls).
  - Co-op is a new feature. No version of the original ever had co-op campaign or online play.
- **Priority 2 (after 1.0):** new missions, levels and character models in the original style.
- **Team:**
  - One developer, UK-based, working on a Linux PC.
  - Claude Code on the **Pro** plan.
  - Agents write most of the code. The developer reviews it, playtests, and makes every decision.
- **Reference copy:** the developer's own NTSC-U GameCube disc, game ID **GM5E7D**.
- **Sharing:** as far as the law allows. In practice that means **public source code and binaries, with no game assets**.

## 2. Decisions

| # | Decision | Why |
|---|---|---|
| D1 | Build a **clean-room engine** that loads assets from the player's own disc | It is the only route that can plausibly be published. UK law does not protect functionality, data file formats or game ideas (*SAS v WPL*, *Nova v Mazooma*). |
| D2 | **Never use the leaked source**, or anything built on it or learned from it | Using it infringes copyright at every tier, private use included. It adds trade-secret exposure, and it would taint the clean room. |
| D3 | **No published decompilation or static recompilation** | Publishing either one distributes a translation of the original program. That falls outside UK s50B(3)(d) and outside the US *Connectix* reasoning. |
| D4 | **Oracle-first**: Dolphin running the retail disc is the referee | Every AI port that scaled was checked against something the agent could not edit. The ones without such a check failed. |
| D5 | Write the runtime in **Rust** and the tools in **Python** | Rust's compiler feedback keeps agents on track, and its explicit endianness suits big-endian GameCube data. Python suits format tooling and Blender. |
| D6 | **Host-authoritative co-op** with per-object ownership, not lockstep | Fan co-op projects converged on this design. Lockstep is fragile with AI enemies and physics. |
| D7 | Publish source and binaries with **no assets**, under a **distinct name** (not "Metal Arms"), and **take no money** | This removes the main triggers for enforcement. |
| D8 | Use a **GitHub org** with a `core` coordination repo that holds the settings as code | It keeps permissions, the clean-room wall and shared CI in one place. |
| D9 | Keep the **lab** off GitHub entirely, even in a private repo. The lab holds the disc image, extracted files, Dolphin captures and golden traces. | All of it is derived from retail data. A takedown or account strike would hit the whole org. |

## 3. Clean-room rules

### Roles
- **Observers** may use the disc, Dolphin and the lab. They write *specs* in their own words, describing formats and behaviour.
  - Specs contain no copied code.
  - Specs contain no retail bytes beyond what identifies a structure, such as magic numbers.
- **Implementers** see only the specs, public documentation and synthetic test fixtures.
  - They never see the lab, decompiler output or forbidden material.
  - They test against the disc only by running the engine locally.

### Allowed inputs
- The bytes of the developer's own disc.
- Behaviour observed while running the game in Dolphin. UK CDPA s50BA lets a lawful user observe, study and test a program's functioning.
- Code from **DJs_MA_TOOLs**, which is MIT-licensed, with attribution. Its documentation is also allowed.
- Public documentation of GameCube hardware and media formats: GX, DSP ADPCM audio, and Bink via FFmpeg's open decoder.
- Public gameplay descriptions: speedrun knowledge bases, StrategyWiki, reviews.
- General game-design ideas, which are unprotected (*Nova*). An example is "a downed player watches until the next checkpoint", as in Sven Co-op's survival mode.
- Facts stated in Exavolt's public docs, as **leads only**. Verify each one by observation before relying on it.

### Forbidden inputs
- The 2019 source-code leak in any form, including file listings and summaries of it.
- Any port, fork, document, commit message or write-up built on the leak. This includes the 2026 AI-assisted PC ports hosted on GitHub.
- **PASM**, the community's asset compiler. Its origin is unclear, so avoid every pipeline that depends on it.
- Decompiler output of the retail executable.
- The Dolphin HD texture pack for this game, which contains textures of unknown origin.
- **Exavolt's code.** It has no licence, so it is all rights reserved until its author, dj0wns, grants permission.
- Ripped assets from any website, Steam Workshop pack or model archive.

### If an agent meets forbidden material
1. Stop.
2. Do not summarise or quote it.
3. Tell the developer.
4. Record the incident in the provenance log.

### Provenance log
Every format fact and every behaviour fact gets a dated entry recording three things:
- what was learned;
- how it was learned, for example "observed in Dolphin: RAM watch at level start" or "round-trip analysis of MST entries";
- which session learned it.

## 4. Legal guardrails (UK first, then US)

### UK — Copyright, Designs and Patents Act 1988
- **s50BA:** a lawful user may observe, study and test a program's functioning while running it. This is the legal basis for using Dolphin as the oracle.
- **s50B:** decompiling is allowed only to make an independent program interoperate, and never to create a program that is "substantially similar in its expression" (s50B(3)(d)).
- **s296A:** contract terms, such as an EULA, that try to override s50A–50BA are void.
- **s28B:** the private-copying exception was quashed in 2015.
  - Copying your own disc is therefore technically infringing for its art, audio and video.
  - The practical risk is low, but keep it for personal use only.
- **s296 and s296ZA (circumvention):** never ship, link to or document a way to dump discs or bypass protection. *Nintendo v Playables* treats these provisions as strict liability.
- **Functionality, data formats and game ideas are unprotected:** *SAS v World Programming* (CA 2013, and CJEU C-406/10), *Nova v Mazooma* and *Navitaire v easyJet*.
- **Characters can be protected works** (*Shazam v Only Fools*). Do not publish 3D recreations of Glitch or other named characters.
- **Trade Secrets Regulations 2018, reg 3:** using leaked trade secrets is unlawful where it amounts to a breach of confidence.
- **Trademark:**
  - The US mark METAL ARMS (reg. no. 2898071) is held by Blizzard Entertainment and was renewed in March 2024.
  - The UK register has not been checked.
  - Keep the name out of the project's title and logo. A single factual compatibility line is fine.

### US
- ***Sega v Accolade* and *Sony v Connectix*:** copies made along the way while reverse engineering are fair use, provided the final product contains no copied code.
- ***Davidson v Jung*:** a Blizzard and Vivendi case that enforced EULA bans on reverse engineering. Owners in this game's rights chain have litigated before.
- **DMCA §1201 exemptions** run until 28 October 2027. None covers an individual dumping a working disc to play a port.
- **GitHub takedowns:**
  - Content is restored 10–14 days after a counter-notice unless the claimant sues.
  - A counter-notice submits you to US jurisdiction.
  - In the re3 case, Take-Two responded to counter-notices with a lawsuit.
  - **Do not file a counter-notice without UK legal advice.**

### Enforcement climate
- Activision revoked a fan licence for *The Silver Lining* (2010).
- It sent a cease-and-desist to the H2M mod (2024).
- It filed a DMCA notice over leaked networking source (June 2026).
- It had footage of an AI-built decompilation taken down (October 2026).
- Microsoft's Game Content Usage Rules probably don't cover this title, and they forbid reverse engineering to access assets anyway.
- Ports that need the player's own copy have mostly survived, but that is the rights holder's choice, not a safe harbour.

## 5. The game: public facts

- **Release:** GameCube, PS2 and Xbox, released 18 November 2003 in North America and published by Vivendi Universal.
- **Ownership chain:**
  - Blizzard bought the studio in May 2005.
  - The Activision–Vivendi Games merger completed in July 2008.
  - Microsoft completed its purchase of Activision Blizzard on 13 October 2023.
- **Digital availability:** the game cannot be bought digitally.
  - The Xbox 360 "Xbox Originals" release disappeared when that store closed on 29 July 2024.
  - It is not on the Xbox One/Series backward-compatibility list.
  - Microsoft's March 2026 statement promising older games for the Xbox 25th anniversary named no titles. An official re-release would change the enforcement picture.
- **Campaign:** 42 levels.
- **Multiplayer:** offline versus only.
  - Seven modes, including Bot Brawl, Team Bot Brawl, Possession Melee, King of the Hill, Moving Hill, Tag and Reverse Tag.
  - Four-player split-screen on Xbox and GameCube, two-player on PS2.
  - No CPU bots.
- **Version differences:**
  - The PS2 port, by Mass Media, has different physics and weaker coring charges.
  - The GameCube version has worse textures than the Xbox version.

## 6. Engine and formats: public knowledge

### Archive and contents
- **Engine name:** the engine identifies itself as **Fang**.
- **Archive:** compiled data lives in an **MST** archive.
  - The magic is `FANG` (little-endian, Xbox and PS2) or `GNAF` (big-endian, GameCube).
  - The version mask includes a PC platform flag.
  - Source: DJs_MA_TOOLs `mst_lib/mst.py`. Its README has the GameCube and Xbox byte order the wrong way round; trust the code.
- **GameCube disc layout:** `files/mettlearms_gc.mst` holds everything except two things:
  - Bink movies, which are in `Movies/`;
  - streamed audio.
- **Asset types:** the MST records a separate compiler version for each asset type. The types are:
  - textures (`.tga`)
  - meshes (`.ape`)
  - worlds (`.wld`)
  - animations (`.mtx`)
  - binary CSV tables
  - fonts
  - AMX bytecode scripts, written in the **Small** language (now called Pawn)
  - AI node graphs

### Where the gameplay lives
- Most gameplay is driven by data: CSV tables, objects initialised by each world, scripts, and AI graphs.
- Each level also has **hard-coded load, unload, work and draw functions in `main.dol`**, the executable. That means 42 pieces of bespoke level logic to reimplement by observation (source: Exavolt `docs/manifest_options.md`).

### Existing public tools
- **DJs_MA_TOOLs** (MIT):
  - MST extract and insert;
  - CSV↔JSON conversion;
  - partial world editing;
  - experimental AMX disassembly;
  - `.gci` save editing.
- **Exavolt** (no licence):
  - a Python mod loader for GM5E7D only;
  - patches the DOL and raises the level limits to 200;
  - modded discs run in Dolphin with extra emulated memory.
- **io_scene_metal_arms:** a Blender exporter that produces PASM input, with no importer. Check its licence before reusing anything, and do not depend on it.

### The Phase 1 gap
No public tool decodes the compiled GameCube meshes, textures, animations, audio banks, fonts or AI graphs.

### Emulation
Dolphin rates the game **5/5 Perfect** and recommends 1x internal resolution to avoid cutscene problems.

## 7. Architecture

### Runtime
- **Stack:**
  - Rust, with wgpu or the SDL3 GPU API for rendering.
  - SDL3 for windows, input, controllers and gyro.
  - Avoid Bevy: its networking crates pin different Bevy versions, which agents would have to keep chasing.
- **Headless mode** (simulation with no window) is a first-class feature, so agents can run replays without a display.
- **Fixed simulation tick** with interpolated rendering.
  - The original tick rate is **unknown**; measure it in Dolphin.
  - Do not interpolate across camera cuts or teleports.
  - **Gate:** replay checksums must be identical at 30, 60, 144 and 240 fps.
- **Game data:** read the balance CSV tables from the disc at runtime, so weapon and bot stats come straight from the original data.
- **Scripts:** reimplement the Small/Pawn abstract machine. Each native function is rebuilt from observed behaviour and the names the scripts import.
- **Override archive** keyed by asset path, layered over the assets read from the disc (the libultraship pattern). It handles HD textures and mods.
- **Player identity is separate from the screen slot**, so split-screen and online play combine.

### Oracle (layered)
1. **Round-trip tests** for every parsed format. They run against the disc locally and against synthetic fixtures in CI.
2. **Screenshot diffs** against Dolphin at matched camera positions.
3. **RAM-state traces** captured in Dolphin under scripted inputs, used as a black-box reference.
   - A scriptable-Dolphin MCP server exists, but its Claude Code support is unverified.
4. **Deterministic replays** at the fixed tick.
5. **Playtests** by the developer, "by ear and eye", for feel.

The hard parts, where the oracle matters most:
- the per-level DOL logic;
- bot AI;
- physics;
- the possession tether.

### Online co-op
- **Host model:** a listen-server host owns AI, physics props, scripts, triggers, cutscenes and saves. Each object has one owner that simulates it, and everyone else interpolates its state.
- **Model to follow:** sm64coopdx's `SyncObject`, which sets ownership, sync distance, update-rate bounds and event IDs.
- **Late join:** the joining player asks a peer already in the area for spawn info and then snapshots.
- **Possession and vehicles:** transfer ownership to the possessing player, following MTA's rule that the last occupant syncs the vehicle.
- **Remotely guided weapons:** simulate them on the owner's machine. These are what desynced Perfect Dark's netplay branch.
- **Deaths:** a downed player watches until the next checkpoint, as in Sven Co-op's survival mode.
- **Progress:** flags travel as reliable, host-owned events, as in Ship of Harkinian's Anchor.
- **Difficulty:** scale enemy health and spawns by player count.
- **Transport:**
  - **renet** for reliable and unreliable channels with an encrypted transport.
  - **libjuice** for ICE, STUN and TURN; sm64coopdx's CoopNet is the model.
  - Start with direct UDP or a VPN.
  - Steam's relay network is not available to a fan port.
- **Bandwidth is not a constraint:** Halo Reach ran 16 players on 250 kbps.
- **Meanwhile,** Dolphin netplay on the original disc already gives online versus play.

### Remaster polish
- **Controls:**
  - SDL3's gamepad sensor API, with "the gyro is a mouse" rules: natural sensitivity scaling, smoothing off by default, and a gyro-off button.
  - Mouse support for every local player.
  - An in-game rebinding menu.
- **HD textures:**
  - Upscale with chaiNNer and a CC0 model trained on 2000s game textures, such as 4x-PBRify_UpscalerV4, with human review of the results.
  - **Publish the recipe, not the pixels:** the model name, licence, settings and a script each player runs on their own disc.
  - Label AI-processed content, in line with Nexus Mods' July 2026 tagging rules.
- **Xbox textures (optional):** if the player owns the Xbox disc, its better textures can be read too.

### Content tooling (Phase 5)
- **Blender add-on:** model it on Fast64, which encodes the engine's limits and refuses content the engine can't use.
  - Export an open level format plus glTF that references original assets by name, loaded from the player's disc.
  - No PASM.
- **BlenderMCP:** keep it on localhost. It has no authentication, and its telemetry is on by default.
- **TRELLIS.2:** MIT-licensed, but its output needs retopology to fit a 2003-era polygon budget.
- **Hunyuan3D:** **do not use.** Its licence excludes the UK.

## 8. Media policy

| Media | Rule |
|---|---|
| Original models, textures, animations, audio, fonts, scripts, data | Load from the player's disc at runtime. Never commit or ship them. |
| Movies (Bink, on the disc) | Decode at runtime with FFmpeg's open Bink decoder. Never ship them. |
| HD textures, upscaled movies | Ship the recipe (script, model and settings). Each player generates their own copies. |
| Rips from websites, Steam Workshop or the community HD pack | Never use them. Being public does not make them licensed. |
| Fan art made from scratch | Allowed with the artist's written licence, unless it depicts Glitch or other named characters. |
| The engine's own media (menus, icons, logo, test placeholders) | Original, or openly licensed (CC0 assets, OFL fonts). |
| New missions (Phase 5) | May reference original enemies, props and textures by name, loaded from the disc. New characters, music and voices must be original. No AI clones of the original voice cast. |

## 9. Org, repositories and permissions

### Repositories

| Repo | Purpose | Visibility |
|---|---|---|
| `core` | Coordination: research, decisions, roadmap, clean-room policy, provenance log, settings as code | Public |
| `.github` | Org profile, default community files, reusable CI workflows | Public |
| `specs` | Format and behaviour specs written by observers. **This repo is the clean-room wall.** | Public |
| `engine` | Rust workspace: runtime, renderer, netcode | Public |
| `tools` | Python extractor, validators, Blender add-on (Phase 1) | Public |
| `agent-kit` | Claude Code plugin: hooks, subagents, loop scripts | Public |
| `content` | Original Phase 5 assets (later) | Public |
| *lab* | Disc image, extracted files, captures, golden traces | **Local only, never on GitHub.** Back it up offline. |

### Settings as code
- Use **github/safe-settings**, a GitHub App built on Probot.
- The admin repo is named by the `ADMIN_REPO` environment variable; here that is `core`.
- Config paths:
  - `.github/settings.yml` for org defaults;
  - `.github/suborgs/*.yml` for groups of repos;
  - `.github/repos/<name>.yml` for per-repo overrides.
- It manages rulesets, branch protection, teams, collaborators, labels, environments and variables, and it reverts manual drift.
- It configures repos that already exist; create new repos first.

### GitHub Free limits
- Rulesets work only on public repos on GitHub Free.
- Org-wide rulesets need the Team plan. safe-settings works around this by writing the same ruleset into each repo.
- So keep `core` public as well. Secrets go in Actions secrets, never in the YAML.

### Identities
- **Developer:** org owner and the only bypass actor.
- **Agents:** a dedicated GitHub App with write access to the code repos only. GitHub does not let you approve your own pull request, so the agents need their own identity.
- **Oracle runner:** a separate local process with its own token, which the agents cannot read. It posts the required `oracle` commit status. If the agents could post that status themselves, they could fake it.

### Rules on `main`
- A pull request is required.
- One approval is required from the developer, via CODEOWNERS.
- Required checks must pass.
- No force-pushes.
- No bypass except the developer.

### CI
- GitHub-hosted runners run unit tests and synthetic fixtures only.
- **No self-hosted runners on public repos.** A fork's pull request could run code on the developer's PC.

## 10. Agent workflow on the Pro plan

### Usage limits
- Pro has a five-hour limit and a weekly limit, shared between the Claude apps and Claude Code.
- Smaller models use less of the allowance, but the ratio is not published.
- Hitting the five-hour limit blocks every model.
- Check usage with `/usage`.

### Choosing models
- Pro's default model is Opus 5.5.
- **Opus:** specs, format reverse engineering, architecture and reviews. Use `opusplan` to plan in Opus and execute in Sonnet.
- **Sonnet:** the day-to-day worker.
- **Haiku:** mechanical, test-backed chores such as lint, fixtures, replay runs and log triage. Set `model: haiku` in the subagent's definition.
  - Haiku 5.5's API price is 5× higher for prompts over 100k tokens, so keep Haiku tasks small.
- **Avoid agent teams.** They use roughly 7× more tokens.

### Session discipline
- **One feature per fresh session.**
- Read `git log` and `PROGRESS.md` first.
- Update `PROGRESS.md` before stopping.
- Use `/clear` between unrelated tasks.

### Guard rails
- Verifiers, golden traces and the feature list must not be edited by the worker; enforce this with hooks. A `PreToolUse` hook that exits with code 2 blocks the action and returns a reason.
- Expect agents to try to route around blocks.
- Use a **read-only reviewer subagent** that judges work against the oracle, never against the worker's own explanation.

### Unattended runs
- `claude -p` with `--output-format json` reports the cost of each run.
- **`--bare` skips hooks, subagents and CLAUDE.md** unless they are passed explicitly with `--settings` and `--agents`, and it does not use the subscription login.

### Habits
- Keep a provenance log.
- Watch for "cognitive debt": never merge a subsystem you don't understand.
- Be open about AI use. The community is hostile to "vibe-coded" ports, so the project must clearly beat Dolphin to be welcomed.

## 11. Roadmap

The durations are indicative estimates for heavier agent use than a Pro plan allows. **On Pro, expect the slow end of each range or longer.**

| Phase | Duration | Goal | Exit gate | Shareable output |
|---|---|---|---|---|
| 0. Foundations | ~1 month | Org and `core` repo; agent-kit hooks; local lab; Dolphin oracle rig; disc hash verification | An agent replays a scripted input file in Dolphin and produces a RAM trace and screenshots. The hooks block deliberately bad actions. | `core`, `agent-kit` |
| 1. Read the whole disc | 2–4 months | Parsers for MST, CSV, WLD, GX textures, meshes, animations, audio, fonts, AI graphs and AMX; a level viewer | Every entry type round-trips. Viewer screenshots match Dolphin. | `tools`, `specs` |
| 2. Walk, shoot, possess | 6–9 months | Fixed-tick simulation designed for N players; weapons, bots, AMX VM, possession, vehicles, physics, per-level logic | Each level completes in replay. RAM-trace diffs are within tolerance. The developer signs off after playing. | Private builds |
| 3. Online co-op | 3–6 months, overlapping Phase 2 | Localhost, then LAN, then direct internet, then ICE/TURN; mission-by-mission co-op audit; late join; difficulty scaling | A two-player campaign over a simulated lossy link; four-player soak tests | Small tester group |
| 4. Remaster polish | Ongoing; 2–3 months of focused work | Interpolation, widescreen HUD, rebinding, gyro, HD override archive and recipe | Replay checksums are identical across frame rates. | **1.0: public engine, no assets** |
| 5. New content | After 1.0 | Open level format, Blender add-on, mission scripting, original models | A new mission plays in co-op using only disc assets plus original art. | Public, with AI use labelled |

## 12. Open unknowns

- The original simulation tick rate, and how much logic is tied to frame rate.
- The compiled GameCube mesh, texture, animation, audio-bank, font and AI-graph formats. None has a public spec.
- Whether METAL ARMS is registered in the UK or EU.
- Whether a closed Discord counts as "the public" for copyright purposes.
- Whether dj0wns would allow reuse of Exavolt code.
- Whether Microsoft plans an official re-release.

## 13. Sources

### Law
- CDPA 1988 on legislation.gov.uk: [s29](https://www.legislation.gov.uk/ukpga/1988/48/section/29), [s50A](https://www.legislation.gov.uk/ukpga/1988/48/section/50A), [s50B](https://www.legislation.gov.uk/ukpga/1988/48/section/50B), [s50BA](https://www.legislation.gov.uk/ukpga/1988/48/section/50BA), [s296](https://www.legislation.gov.uk/ukpga/1988/48/section/296), [s296ZA](https://www.legislation.gov.uk/ukpga/1988/48/section/296ZA)
- [Trade Secrets Regulations 2018, reg 3](https://www.legislation.gov.uk/uksi/2018/597/regulation/3)
- [SAS v WPL (CA 2013)](https://caselaw.nationalarchives.gov.uk/ewca/civ/2013/1482); [CJEU C-406/10](https://curia.europa.eu/juris/liste.jsf?num=C-406/10)
- [Nova v Mazooma](https://caselaw.nationalarchives.gov.uk/ewca/civ/2007/219)
- [Nintendo v Playables](https://caselaw.nationalarchives.gov.uk/ewhc/ch/2010/1932)
- [Shazam v Only Fools](https://caselaw.nationalarchives.gov.uk/ewhc/ipec/2022/1379)
- [Private copying quashed (Osborne Clarke)](https://osborneclarke.com/insights/private-copying-in-the-uk-a-nation-of-infringers)
- [Sony v Connectix summary](https://www.copyright.gov/fair-use/summaries/sony-connectix-9thcir2000.pdf)
- [Davidson v Jung](https://law.resource.org/pub/us/case/reporter/F3/422/422.F3d.630.04-3654.html)
- [§1201 ninth triennial rule (Finnegan)](https://www.finnegan.com/en/insights/ip-updates/final-rule-issued-in-the-us-copyright-offices-ninth-triennial-section-1201-proceeding.html)
- [GitHub DMCA policy](https://docs.github.com/en/site-policy/content-removal-policies/dmca-takedown-policy)
- [re3 outcome (TorrentFreak)](https://torrentfreak.com/take-two-dismisses-claims-against-lead-defendants-in-gta-mods-lawsuit-230405/)
- [Activision DMCA notice, June 2026](https://github.com/github/dmca/blob/master/2026/06/2026-06-12-activision.md)
- [Activision and AI decomp footage (Kotaku)](https://kotaku.com/activision-and-bethesda-crackdown-on-genai-mw2-and-fallout-projects-2000739580)
- [Microsoft Game Content Usage Rules](https://www.xbox.com/en-US/developers/rules)

### Game
- [Wikipedia](https://en.wikipedia.org/wiki/Metal_Arms:_Glitch_in_the_System)
- [SDA Knowledge Base](https://kb.speeddemosarchive.com/Metal_Arms:_Glitch_in_the_System)
- [StrategyWiki: Multiplayer](https://strategywiki.org/wiki/Metal_Arms:_Glitch_in_the_System/Multiplayer)
- [Dolphin wiki](https://wiki.dolphin-emu.org/forum/Metal%20Arms:%20Glitch%20in%20the%20System/embed)
- [US trademark record (Justia)](https://trademarks.justia.com/781/51/metal-78151322.html)
- [Xbox 360 store closure](https://www.trueachievements.com/news/xbox-360-store-closure-date)

### Tools
- [Exavolt](https://github.com/dj0wns/Exavolt)
- [DJs_MA_TOOLs](https://github.com/dj0wns/DJs_MA_TOOLs)
- [io_scene_metal_arms](https://github.com/hypermegacrash/io_scene_metal_arms)
- [Pawn / Small (CompuPhase)](https://www.compuphase.com/pawn/pawnprojects.htm)

### Architecture
- [sm64coopdx sync_object.h](https://raw.githubusercontent.com/coop-deluxe/sm64coopdx/main/src/pc/network/sync_object.h)
- [CoopNet](https://github.com/coop-deluxe/coopnet)
- [Anchor](https://github.com/garrettjoecox/anchor)
- [MTA setElementSyncer](https://wiki.multitheftauto.com/wiki/setElementSyncer)
- [Perfect Dark netplay notes](https://raw.githubusercontent.com/fgsfdsfgs/perfect_dark/port-net/docs/netplay.md)
- [Sven Co-op survival mode](https://wiki.svencoop.com/Setting_Up_Survival_Mode)
- [renet](https://github.com/lucaspoffo/renet)
- [libjuice](https://github.com/paullouisageneau/libjuice)
- [Gaffer: Fix Your Timestep](https://gafferongames.com/post/fix_your_timestep/)
- [libultraship](https://github.com/Kenix3/libultraship)
- [SDL3 GPU](https://wiki.libsdl.org/SDL3/CategoryGPU)
- [Fast64](https://github.com/Fast-64/fast64)
- [chaiNNer](https://github.com/chaiNNer-org/chaiNNer)
- [4x-PBRify_UpscalerV4](https://openmodeldb.info/models/4x-PBRify-UpscalerV4)
- [Hunyuan3D licence](https://huggingface.co/tencent/Hunyuan3D-2/blob/main/LICENSE)

### Agents and GitHub
- [Effective harnesses for long-running agents (Anthropic)](https://anthropic.com/engineering/effective-harnesses-for-long-running-agents)
- [Claude Code hooks](https://code.claude.com/docs/en/hooks-guide)
- [Subagents](https://code.claude.com/docs/en/sub-agents)
- [Headless mode](https://code.claude.com/docs/en/headless)
- [Costs](https://code.claude.com/docs/en/costs)
- [Model configuration](https://code.claude.com/docs/en/model-config)
- [Permissions](https://code.claude.com/docs/en/permissions)
- [Long-tail lessons from LLM decomp (Lewis)](https://blog.chrislewis.au/the-long-tail-of-llm-assisted-decompilation/)
- [safe-settings](https://github.com/github/safe-settings)
- [GitHub rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets)

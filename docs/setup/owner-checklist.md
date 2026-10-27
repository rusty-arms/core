# The owner's checklist

These are the manual tasks that an agent can't or mustn't do, in the order they are needed. When you finish one, tick it in a PR or tell the next session. The project's public progress is in [PROGRESS.md](../../PROGRESS.md).

**Who does what:** you do everything on this page. Agent sessions do the Phase 0 steps in the [roadmap](../roadmap.md): `agent-kit`, the `specs` skeleton and the Dolphin oracle rig. Each section's "Needed before" line says which of those steps it blocks.

## Done

- [x] **Blocklist:** `~/.claude/cleanroom-blocklist.txt` exists and the guard's tests pass ([claude-guard.md](claude-guard.md)). Cloud sessions use `CLEANROOM_BLOCKLIST_TERMS`.
- [x] **Teams:** `admins` and `developers` exist, and you are in both.
- [x] **safe-settings:** the App is installed, and the sync runs on every settings change merged to `main` ([safe-settings.md](safe-settings.md)).
- [x] **Repos:** `agent-kit` and `specs` exist on GitHub with a `main` branch. The rest of section 2 is still to confirm for both.

## 1. Prepare your PC

Needed before: any local agent session.

- [x] Clone `core` and turn on its git hooks:

  ```sh
  git clone https://github.com/rusty-arms/core.git
  cd core
  git config core.hooksPath .githooks
  ```

- [ ] Install the tools the hooks and checks use: `git`, `python3`, `yamllint`, and optionally `ruff` (the format/lint hook uses it when it is installed). `git` and `python3` work; `yamllint` and `ruff` are still missing. Check that they work:

  ```sh
  python3 scripts/check_no_retail.py --all
  python3 scripts/check_links.py
  yamllint -s .
  ```

- [ ] **Install the `agent-kit` plugin for your user,** so every Claude Code session on this PC runs the clean-room guard, the format/lint hook and the session rules, wherever it starts. The blocklist must exist first, because the guard blocks every tool call without it. In Claude Code:

  ```text
  /plugin install agent-kit --marketplace rusty-arms/agent-kit
  ```

  Restart Claude Code. A new session's context should include "Rusty Arms session rules". Details: the [agent-kit README](https://github.com/rusty-arms/agent-kit#install).

## 2. Create the next repos

Needed before: the `agent-kit` session (next) and the `specs` session.

Create `agent-kit` and `specs` now. Leave `engine` and `tools` until Phase 1 needs them, and `content` until Phase 5. For each repo:

- [ ] **Create it** at github.com/organizations/rusty-arms/repositories/new:
  - owner `rusty-arms`, the exact name, **Public**;
  - tick **Add a README**, so that `main` exists;
  - pick no licence and no `.gitignore`. The first agent PR adds the licence files and the repo's guard files. Code repos are MIT OR Apache-2.0; `specs`, like `core`, is CC BY 4.0 for prose and MIT for scripts.
- [ ] **Give the Apps access:** in the org's **Settings → GitHub Apps**, configure **Claude** and the **safe-settings** App. If either is set to "Only select repositories", add the new repo.
- [ ] **Apply the settings:** creating a repo isn't a config change, so the sync doesn't run on its own. In `core`, open **Actions → safe-settings sync → Run workflow**:
  1. Run it with **Dry run** ticked, and check that the log lists only the new repo's settings, labels, teams and `main` ruleset.
  2. Run it again with **Dry run** unticked.

  Both repos are already listed in [`clean-code.yml`](../../.github/suborgs/clean-code.yml).
- [ ] **Give it a description and topics:** add `.github/repos/<name>.yml` in a `core` PR, copying [`repos/agent-kit.yml`](../../.github/repos/agent-kit.yml). Merging it runs the sync. `agent-kit` and `specs` already have one.
- [ ] **Add it to the Claude project's repositories,** so that cloud sessions can clone it and push to it.

The `main` ruleset requires the `guard` check, which a new repo doesn't have until its first PR adds it. Merge that first PR with your `admins` bypass.

## 3. Set up the lab

Needed before: the Dolphin oracle rig and any observer work.

The lab is the only place allowed to hold retail data or anything derived from it ([D9](../decisions/0009-lab-off-github.md)). It stays on your PC.

- [ ] Create the folders and a local-only git repo. Never add a remote.

  ```sh
  mkdir -p ~/Develop/rusty-arms/ma-lab/{disc,extracted,captures,inputs,traces,notes}
  cd ~/Develop/rusty-arms/ma-lab
  git init
  printf 'disc/\nextracted/\ncaptures/\n' > .gitignore
  git add .gitignore && git commit -m "Lab layout"
  ```

- [ ] Put each kind of file in its folder:

  | Folder | What goes in it | Tracked in the lab's git? |
  |---|---|---|
  | `disc/` | Your own disc image (GM5E7D) and `hashes.txt` (see section 4) | No, too large |
  | `extracted/` | The disc's files (`files/mettlearms_gc.mst`, `Movies/`, streamed audio) and the MST contents extracted with DJs_MA_TOOLs | No, too large |
  | `captures/` | Dolphin screenshots and frame dumps | No, too large |
  | `inputs/` | Scripted input files for replays | Yes |
  | `traces/` | Golden RAM traces captured in Dolphin | Yes |
  | `notes/` | The handover file, the full research report, any other notes that aren't clean-room safe, and observer notes before they become specs | Yes |

- [ ] **Back it up offline.** Copy the whole folder, including the untracked parts, to an external drive, and do it again after every capture session:

  ```sh
  rsync -a --delete ~/Develop/rusty-arms/ma-lab/ /path/to/external-drive/ma-lab/
  ```

  Don't keep the lab in a cloud-synced folder such as Dropbox, OneDrive or Google Drive. That puts retail data on someone else's servers.

- [ ] **Install the observer profile** from a clone of `agent-kit`. It copies the lab's `CLAUDE.md` and `.claude/settings.json` into the lab, and never overwrites a file:

  ```sh
  git clone https://github.com/rusty-arms/agent-kit.git ~/Develop/rusty-arms/agent-kit
  ~/Develop/rusty-arms/agent-kit/profiles/lab/install.sh
  cd ~/Develop/rusty-arms/ma-lab && git add CLAUDE.md .claude/settings.json && git commit -m "Add the observer profile"
  ```

  Until it is installed, don't start Claude Code in the lab.

- [ ] **How the lab is used:**
  - Only observer sessions work in the lab, and they are started from inside it (`cd ~/Develop/rusty-arms/ma-lab && claude`). The guard lets a session read the lab only when it starts there.
  - Observers write what they learn as specs, in their own words, in the `specs` repo, and log each fact in the [provenance log](../provenance-log.md).
  - Implementer sessions never open the lab.

## 4. Verify the disc and set up Dolphin

Needed before: anything that reads the disc.

- [ ] Install Dolphin and add `~/Develop/rusty-arms/ma-lab/disc/` as a game folder.
- [ ] Open the game's **Properties → Verify** tab and run it. It compares the image's hashes with the Redump database.
- [ ] Save the result and the hashes it shows in `~/Develop/rusty-arms/ma-lab/disc/hashes.txt`.
- [ ] Add a dated line to the [provenance log](../provenance-log.md) saying the reference disc was verified. Never upload the image anywhere.
- [ ] Set Dolphin's internal resolution to 1x. Dolphin's wiki recommends this to avoid cutscene problems.

Scripting Dolphin for RAM traces and replays needs a separate build of Dolphin; section 6 installs it. The design is in [oracle-rig.md](../oracle-rig.md).

## 6. Run the first oracle replay

Needed before: the end of Phase 0, and any observer work that records traces.

- [ ] **Create the `oracle` repo** as in section 2: create it, give the Apps access, run the settings sync, and add it to the Claude project. Its description, topics and suborg entry are already in this repo. Merge its first PR, which adds the rig, with your `admins` bypass.
- [ ] **Clone the rig** outside the lab:

  ```sh
  git clone https://github.com/rusty-arms/oracle.git ~/Develop/rusty-arms/oracle
  ```

- [ ] **Set up the Windows VM.** The scripting build of Dolphin ships for Windows only, so on the Pop!_OS lab PC it runs in a local Windows VM under Docker. Follow sections 1 and 2 of the rig's [VM guide](https://github.com/rusty-arms/oracle/blob/main/vm/README.md): check KVM, install Docker Engine, start the VM with the lab shared as drive `Z:`, then install Python, the scripting Dolphin and the rig inside it and turn on SSH. Keep the VM's disk out of every repo and cloud-synced folder.
- [ ] **Run the smoke test yourself** from the VM's desktop (VM guide, section 3). It boots the disc, waits ten seconds, takes two screenshots and reads three generic boot values. `--repeat 2` runs it twice and checks that both runs match, so it should end with "2 runs identical". If it fails, `dolphin.log` in the `--out` folder has Dolphin's output. Delete both output folders before trying again.
- [ ] **Try the same run over SSH** from the Linux side (VM guide, section 3). Say in your report whether it worked; if it didn't, the rig needs a bridge before the gate below.
- [ ] **Phase 0 gate, part 1:** start an observer session in the lab (`cd ~/Develop/rusty-arms/ma-lab && claude`) and ask it to replay the smoke test in the VM over SSH into `traces/smoke-agent` and `captures/smoke-agent`, then report the trace's hash and the screenshots it saved.
- [ ] **Phase 0 gate, part 2:** in a session started anywhere else, ask the agent to read a file in the lab. The guard must block it.
- [ ] **Report back** in a PR or to the next session: whether the runs matched and both gate checks passed, and any error from `run.json`. Never paste traces, screenshots or log excerpts that show game data.

## 5. Legal checks

Needed before: any public release. None of these blocks development.

- [ ] **Trademark:** search the UK IPO register (trademarks.ipo.gov.uk) for the original game's name. Record the result in [legal-guardrails.md](../legal-guardrails.md).
- [ ] **Exavolt (optional):** email dj0wns to ask whether Exavolt's code may be reused, and under what licence. Record the answer as an ADR. Until then, Exavolt's docs are leads only.
- [ ] **Solicitor:** get a UK solicitor's view before any public release.

## Order at a glance

1. You: prepare your PC (section 1) and create `agent-kit` (section 2).
2. Agent session: build `agent-kit`. Done 2026-10-20; install it (section 1).
3. You: create `specs` (section 2).
4. Agent session: the `specs` skeleton.
5. You: the lab and the disc (sections 3 and 4).
6. Agent session: the Dolphin oracle rig.
7. You: create `oracle` and run the first replay (section 6).
8. Phase 0 is done when an agent replays a scripted input file in Dolphin and produces a RAM trace and screenshots, and the hooks block deliberately bad actions.

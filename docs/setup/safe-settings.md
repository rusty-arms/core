# Setting up safe-settings

The owner's manual steps. Based on the [github/safe-settings](https://github.com/github/safe-settings) README, `docs/deploy.md` and `docs/github-action.md` as of release 3.0.0 (checked 2026-10-18). Re-check those docs before you start; the project moves quickly.

safe-settings reads its config from this repo (`ADMIN_REPO=core`, `CONFIG_PATH=.github`): `.github/settings.yml`, `.github/suborgs/*.yml` and `.github/repos/*.yml`. It only configures repos that already exist.

## 1. Create the GitHub App

In the org's settings: **Developer settings → GitHub Apps → New GitHub App** (owned by the `rusty-arms` org).

- **Name:** e.g. `rusty-arms-safe-settings`.
- **Homepage URL:** `https://github.com/rusty-arms/core`.
- **Webhook:** for the GitHub Actions deployment there is no server to receive webhooks, so untick **Active**. (If you later run the Docker deployment, set the webhook URL and a secret from `openssl rand -base64 32`.)
- **Where can this app be installed:** only this account.

### Permissions (from `docs/deploy.md`)

Repository permissions:

| Permission | Access |
|---|---|
| Actions | Read-only |
| Administration | Read & write |
| Checks | Read & write |
| Commit statuses | Read & write |
| Contents | Read & write |
| Custom properties | Read & write |
| Environments | Read & write |
| Issues | Read & write |
| Metadata | Read-only |
| Pull requests | Read & write |
| Variables | Read & write |

Organization permissions:

| Permission | Access |
|---|---|
| Administration | Read & write |
| Custom organization roles | Read-only |
| Custom properties | Admin |
| Members | Read & write |

Events (only needed for the webhook/Docker deployment): Branch protection rule, Check run, Check suite, Create, Custom property values, Member, Pull request, Push, Repository, Repository ruleset, Team.

After creating it: note the **App ID** and **Client ID**, generate a **client secret**, and generate and download a **private key**.

## 2. Install it on the org

On the App's page, click **Install** and choose **All repositories** (the docs say to install it for all repos in the org).

## 3. Choose a deployment method

**Recommended: GitHub Actions.** The docs support running a full sync with `npm run full-sync` from a workflow. This repo already contains one: [`.github/workflows/safe-settings-sync.yml`](../../.github/workflows/safe-settings-sync.yml). It is manual-only (`workflow_dispatch`) and dry-runs by default. Trade-off: Actions runs are scheduled or manual, so there is no instant drift revert and no PR dry-run check from the App; those need the webhook deployment.

**Alternative: Docker on the PC** (`docs/deploy.md`, "Docker"): clone safe-settings, copy `.env.example` to `.env`, set `APP_ID`, `WEBHOOK_SECRET`, `PRIVATE_KEY` and `ADMIN_REPO=core`, then `docker build -t safe-settings .` and `docker run -d -p 3000:3000 safe-settings`. This needs a public webhook URL, so it is more work and exposes a port; not recommended for now.

## 4. Store the credentials (Actions method)

In `rusty-arms/core` → **Settings → Secrets and variables → Actions**:

| Kind | Name | Value |
|---|---|---|
| Variable | `SAFE_SETTINGS_GH_ORG` | `rusty-arms` |
| Variable | `SAFE_SETTINGS_APP_ID` | the App ID |
| Variable | `SAFE_SETTINGS_GITHUB_CLIENT_ID` | the Client ID |
| Secret | `SAFE_SETTINGS_PRIVATE_KEY` | the private key. `docs/deploy.md` prefers it base64-encoded (`base64 -w0 key.pem`); if the dry run can't read it, store the raw PEM instead |
| Secret | `SAFE_SETTINGS_GITHUB_CLIENT_SECRET` | the client secret |

Never put any of these in YAML. Delete the downloaded `.pem` once it is stored, or keep it offline.

## 5. Dry run first

1. **Actions → safe-settings sync → Run workflow**, with **Dry run** ticked (`FULL_SYNC_NOP=true`).
2. Read the log: it lists the changes it would make. Check the `main` ruleset, labels and repo settings for `core`.
3. If it looks right, run it again with **Dry run** unticked.
4. Optionally add a `schedule:` trigger (the docs' example uses every 4 hours) in a PR.

## Notes

- `ADMIN_REPO=core` is set in the workflow.
- By default safe-settings skips repos named `admin`, `.github` and `safe-settings`. When the org `.github` repo is created, either protect it by hand or add a `deployment-settings.yml` with `restrictedRepos` (see the safe-settings README, "Restricting safe-settings to specific repos").
- `settings.yml` defines two teams, `admins` and `developers`. safe-settings creates or updates them; add yourself to both in the org's **Teams** page. The `admins` team is the code owner and the only bypass actor, so keep its membership to people you trust with org settings, and never add the agents' App to it.
- The `oracle` ruleset in `suborgs/clean-code.yml` is disabled until the oracle runner exists.
- If you want protection on `core` before safe-settings runs, a single `gh api` call can create a matching ruleset; ask the agent for it.

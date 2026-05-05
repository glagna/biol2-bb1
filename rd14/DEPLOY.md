# RD14 Wager Arena — Deploy via GitHub Pages

**Architecture:** GitHub Pages (hosting) + Firebase Realtime DB (state only).
The static site is served from `https://github.com/glagna/biol2-bb1` at the URL `https://glagna.github.io/biol2-bb1/rd14/`. No Firebase Hosting in play. The `firebase.json` and `database.rules.json` files in this folder are unused for the GitHub Pages deploy (they were artifacts from an earlier plan); keep them around in case the rules ever need updating before the test-mode May 16 expiry.

**Source folder for this deploy:**
`/Users/giorgiolagna/Library/Application Support/Claude/local-agent-mode-sessions/fcf28534-22ca-43c2-b874-082c463bb185/ca8357ea-b016-409c-85ff-d5de8d2a780e/BIOL2-S26/03_week_materials/week_06/rd14_game/`

**Target repo:** `glagna/biol2-bb1` (public). Files land at the `/rd14/` subdirectory.

---

## Pre-flight

The `gh` CLI must be installed and authed as `glagna` on this Mac (per `project_gh_cli_hall_of_flame` memory; was set up Apr 11 for the Hall of Flame push). Verify with:

```bash
gh auth status
```

If not authed: `gh auth login` and follow the browser flow.

---

## Deploy commands (5 commands, ~2 min total)

Open Terminal on your Mac. Paste these one at a time (skip the lines that are comments).

### 1. Clone the repo into a working directory (one-time, skip if already cloned)

```bash
cd ~
gh repo clone glagna/biol2-bb1
```

If the directory already exists from a prior clone, just cd into it and pull the latest:

```bash
cd ~/biol2-bb1 && git pull origin main
```

### 2. Copy the rd14_game folder contents into the repo as a new rd14 subdirectory

```bash
cp -r "/Users/giorgiolagna/Library/Application Support/Claude/local-agent-mode-sessions/fcf28534-22ca-43c2-b874-082c463bb185/ca8357ea-b016-409c-85ff-d5de8d2a780e/BIOL2-S26/03_week_materials/week_06/rd14_game" ~/biol2-bb1/rd14
```

This creates `~/biol2-bb1/rd14/` with all the HTML/JSON/etc. inside.

### 3. Optionally remove the unused Firebase files (they sit unused but cleaner without them in the repo)

```bash
rm ~/biol2-bb1/rd14/firebase.json ~/biol2-bb1/rd14/database.rules.json ~/biol2-bb1/rd14/DEPLOY.md
```

### 4. Commit and push

```bash
cd ~/biol2-bb1
git add rd14/
git commit -m "Add RD14 Wager Arena for Wed May 6"
git push origin main
```

### 5. Wait ~1-2 min for GitHub Pages to build, then verify

```bash
open https://glagna.github.io/biol2-bb1/rd14/
```

(Or just paste that URL into a browser tab.)

---

## The three URLs after deploy

| Who | URL | What |
|---|---|---|
| Each team device | `https://glagna.github.io/biol2-bb1/rd14/` | Pick team A1 to D4 from dropdown, place bets, lock answers |
| Your laptop (instructor) | `https://glagna.github.io/biol2-bb1/rd14/host.html` | Open wager, open answer, reveal, next question |
| Apple TV projection | `https://glagna.github.io/biol2-bb1/rd14/leaderboard.html` | Live ranked leaderboard, top 3 in gold/silver/bronze |

Note the `.html` suffixes for `host` and `leaderboard`. GitHub Pages does NOT honor `firebase.json` rewrites. The S17 deck and Camino S17 page already point at the correct URLs.

---

## Pre-class smoke test (Tue night, ~5 min)

1. Open `host.html`, `leaderboard.html`, and the team URL (pick A1) in three browser windows.
2. In `host`: click **Open Wager**. Team window should switch to chip-button mode. Place a bet (say 3). Lock should stamp.
3. Click **Open Answer**. Stem appears. Click an answer. Lock should stamp.
4. Click **Reveal Answer**, type the correct letter for Q1 (it is `C`). Leaderboard should show the team's score.
5. Click **Next Question**. State advances to Q2.
6. **At Q6 (L1 callback, doublePayout):** wager 3, get it right, you should see +6 (not +3) in the leaderboard. Validates the doublePayout flag.
7. Click **Reset Round** (red, in host) to wipe `/rd14/` Firebase data before Wed morning.

---

## Class day (Wed May 6)

- 7:45 AM. Open `host.html` on your laptop, `leaderboard.html` on the Apple TV.
- 7:50 AM. Confirm the team URL link on the Camino S17 page resolves.
- 8:00 AM. Class starts. RD#14 runs at 0:08 to 0:23 of the Arena.
- After class. Run `python3 export_rd14.py` (from this folder) to capture audit CSVs (XP awards for the top 3 teams). Then click **Reset Round** in host to clear data.

---

## Troubleshooting

**`gh repo clone` fails with auth error.**
Run `gh auth status`. If not authed: `gh auth login` (pick GitHub.com, HTTPS, login with browser).

**`git push` fails with "Permission denied".**
Either the gh auth is wrong account, or the repo is now read-only for some reason. Check `git remote -v` shows `https://github.com/glagna/biol2-bb1.git`. Run `gh auth refresh` if needed.

**GitHub Pages doesn't update after push.**
Pages typically takes 1-2 minutes to rebuild. If still showing the old version after 5 min, check the repo's Actions tab for the `pages-build-deployment` workflow status. If failed, look at the error. Hard-refresh the browser (Cmd+Shift+R) to bypass cache.

**Team view shows "Waiting for instructor..." forever.**
Host hasn't clicked Open Wager yet, OR the host console is on a different question number. Check `state/phase` and `state/currentQ` in the Firebase console: https://console.firebase.google.com/project/biol2-bb1/database/data/rd14

**"Permission denied" on a Firebase write during smoke test.**
Test-mode rules expire ~2026-05-16. If today is past that date, rules need refreshing. See `reference_wager_arena_architecture` for that path (involves firebase CLI access; non-trivial).

**Leaderboard doesn't update.**
Refresh once. If still stuck, check that `teams/{TEAM}/answers/q{N}` and `state/answerKey/q{N}` are both written in the Firebase console under `/rd14/`.

---

## Rollback (if anything explodes during class)

The simplest rollback: `git revert` the commit and push. GitHub Pages will rebuild back to the prior state within ~2 min.

```bash
cd ~/biol2-bb1
git log --oneline -5      # find the RD14 commit hash
git revert <hash>
git push origin main
```

If the Firebase database breaks: Wager Arena Sheet at `https://docs.google.com/spreadsheets/d/1_Yafvii6VduxD-5QOBsOefJ7ehH8FlQw/edit` is the manual backup. Open it, instructor types each team's bet/answer/PTS by hand. Slow but functional.

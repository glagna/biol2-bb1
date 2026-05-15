# RD#17 Deep Think — Deploy via GitHub Pages

**For class:** Fri May 15, S21 Arena, 0:08 to 0:20.
**Topic:** Herd immunity and HIT math (LO3.3) with one L2 immunocompromised callback. Q5 is the Deep Think Challenge (measles R0=15, doublePayout).
**Architecture:** GitHub Pages (hosting) + Firebase Realtime DB at `biol2-bb1` (state only). Same as RD15 / RD16 convention.
**Target URL:** `https://glagna.github.io/biol2-bb1/rd17_game/`

---

## What's in this folder

| File | Purpose |
|---|---|
| `index.html` | Team device view (pick A1-D4, place bets, lock answers) |
| `host.html` | Instructor console (open wager, open answer, reveal, next) |
| `leaderboard.html` | Apple TV projection (live ranked scores) |
| `rd17-questions.json` | 5 herd-immunity questions; Q5 has `doublePayout: true` |
| `firebase.json` / `database.rules.json` | Carried from rd15_game template; unused for GH Pages deploy |
| `export_rd17.py` | Run after class to capture audit CSV of bets/answers/scores |

**Patches applied to the rd16_game clone (Claude, 2026-05-14):**
- All `rd16` references swapped to `rd17` across HTML, JSON, Python (URL paths, Firebase nodes, localStorage keys, ~43 occurrences)
- Question count was already 5 in rd16, so no loop-ceiling changes were needed
- "Q5 PAYS DOUBLE" banner already correct
- New 5-question herd-immunity JSON, answer key B/C/A/B/C
- JSON validated and round-trip smoke-tested

---

## Deploy commands (Mac Terminal, ~2 min)

```bash
# Pull latest from biol2-bb1 repo
cd ~/biol2-bb1 && git pull origin main

# Copy rd17_game into the repo (canonical path)
cp -r "/Users/giorgiolagna/Documents/Claude/Projects/BIOL2-S26/03_week_materials/week_07/rd17_game" ~/biol2-bb1/rd17_game

# Strip files that don't belong in the deployed site
rm -f ~/biol2-bb1/rd17_game/firebase.json ~/biol2-bb1/rd17_game/database.rules.json ~/biol2-bb1/rd17_game/DEPLOY.md ~/biol2-bb1/rd17_game/export_rd17.py

# Commit and push
cd ~/biol2-bb1
git add rd17_game/
git commit -m "Add RD17 Deep Think (herd immunity, HIT math) for Fri May 15 S21"
git push origin main

# Wait ~1-2 min for Pages to rebuild, then verify
open https://glagna.github.io/biol2-bb1/rd17_game/
```

---

## Three URLs after deploy

| Who | URL |
|---|---|
| Each team device (QR target) | `https://glagna.github.io/biol2-bb1/rd17_game/` |
| Instructor console | `https://glagna.github.io/biol2-bb1/rd17_game/host.html` |
| Apple TV leaderboard | `https://glagna.github.io/biol2-bb1/rd17_game/leaderboard.html` |

The S21 deck slide 8 QR encodes the team URL above.

---

## Smoke test before class (5 min, Thu night)

1. Open `host.html`, `leaderboard.html`, and one team URL (e.g. A1) in three browser windows.
2. In `host`: click **Open Wager**. Team window should switch to chip-button mode. Place a bet (3 chips). Lock should stamp.
3. Click **Open Answer**. Stem appears. Click an answer letter. Lock should stamp.
4. Click **Reveal Answer**, type the correct letter (Q1 = `B`). Leaderboard should show the team's score.
5. Click **Next Question** through Q2, Q3, Q4.
6. **At Q5**: the team view should show the "Q5 PAYS DOUBLE" banner. Wager 3, answer C correctly. Leaderboard should show +6 (not +3). This validates the doublePayout path.
7. Click **Reset Round** (red button in host) to wipe `/rd17/` Firebase data before class.

---

## Class day

- 7:45 AM. Open `host.html` on laptop, `leaderboard.html` on Apple TV.
- 7:55 AM. Confirm `index.html` URL resolves from a student-style phone.
- 8:00 AM. Class starts. RD#17 runs at 0:08 to 0:20.
- After class. Run `python3 export_rd17.py` to grab the audit CSV, then click **Reset Round** to clear data.

---

## Answer key (instructor only)

| Q | Topic | Correct | doublePayout |
|---|---|---|---|
| 1 | Herd immunity threshold (70% slow spread scenario) | B | no |
| 2 | HIT at R0=3 (COVID Wuhan) | C | no |
| 3 | 4-month-old infant in 95% MMR community | A | no |
| 4 | Chemo patient + L2 immunocompromised callback | B | no |
| 5 | Measles R0=15 HIT (= 93%) — Deep Think Challenge | C | **YES (2x)** |

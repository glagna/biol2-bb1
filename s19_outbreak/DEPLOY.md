# S19 Outbreak App — Deploy Guide

**Built:** 2026-05-09 PM
**Live URL (after deploy):** https://glagna.github.io/biol2-bb1/s19_outbreak/
**Total deploy time:** ~15 minutes (you, on Mac terminal)

---

## What this builds

The Live-Action Outbreak game for S19 Mon May 11. Three pages:

| Page | URL | Who uses it |
|---|---|---|
| Student token page | `s19_outbreak/?id=<token>` | Each of 47 students gets a unique URL |
| Host display | `s19_outbreak/host.html` | You, mirrored to lecture-hall Apple TV |
| Admin console | `s19_outbreak/admin.html` | You, before class (seed roster, set Patient Zero, distribute URLs) |

Backend: Firebase RTDB at the existing `biol2-bb1` project. Same project as BB1 + RD13.

---

## STEP 1 — Copy this folder to your local biol2-bb1 git clone

The local clone of the GitHub Pages repo is on your Mac. From the Mac terminal (this is your action; I cannot push to GitHub):

```bash
# 1. Make sure your local biol2-bb1 is up to date
cd ~/path/to/biol2-bb1   # (whatever path you cloned it at)
git pull

# 2. Copy the s19_outbreak folder from the BIOL2-S26 project
cp -r "$HOME/Library/Application Support/Claude/local-agent-mode-sessions/fcf28534-22ca-43c2-b874-082c463bb185/ca8357ea-b016-409c-85ff-d5de8d2a780e/BIOL2-S26/03_week_materials/week_07/s19_outbreak" .

# 3. Verify the layout
ls -la s19_outbreak/
# expect: index.html, host.html, admin.html, roster.json, database.rules.json, firebase.json, DEPLOY.md, INSTRUCTOR_GUIDE.md
```

---

## STEP 2 — Push to GitHub Pages

```bash
# Still in your biol2-bb1 clone
git add s19_outbreak/
git commit -m "Add S19 Live-Action Outbreak app"
git push origin main
```

GitHub Pages auto-deploys within 1-2 minutes. Verify by opening:

```
https://glagna.github.io/biol2-bb1/s19_outbreak/admin.html
```

You should see the admin console.

---

## STEP 3 — Renew Firebase RTDB rules

Per memory `reference_bb1_firebase_project`: test-mode rules expire ~2026-05-16. We need to update them now to add the new `s19_outbreak/` path AND extend the expiry.

**Option A: Firebase Console UI (simplest):**

1. Go to https://console.firebase.google.com/project/biol2-bb1/database/biol2-bb1-default-rtdb/rules
2. Sign in with the account that owns the project (glagna@scu.edu).
3. Replace the entire rules JSON with the contents of `s19_outbreak/database.rules.json`.
4. Click **Publish**.

**Option B: Firebase CLI (if installed):**

```bash
cd s19_outbreak
firebase deploy --only database --project biol2-bb1
```

If Firebase CLI isn't set up yet, use Option A. The CLI is unrelated to the GitHub Pages hosting — we don't need `firebase deploy --only hosting` because we're hosting on GitHub Pages, not Firebase Hosting. We only need it for the database rules.

---

## STEP 4 — Pre-class admin setup (Sun May 10 PM or Mon May 11 7:30 AM)

1. **Open the admin console** at https://glagna.github.io/biol2-bb1/s19_outbreak/admin.html

2. **Step 1 in admin: Seed roster.** Click "Seed roster from roster.json." Loads all 47 students. Idempotent — safe to re-click.

3. **Step 2 in admin: Pick Patient Zero.** Choose someone who tends to mingle. Don't tell anyone. Lock it in.

4. **Step 3 in admin: Set mixer duration.** Default 330 seconds (5:30). You said 5-6 minutes; 5:30 is the sweet spot.

5. **Step 4 in admin: Distribute URLs.** Click "Copy as Markdown" or "Copy as HTML table." Paste into a Camino announcement. Schedule the announcement to send Mon 7:55 AM.

   *Alternative:* if Camino announcements feel too slow, post the URL list directly into the Day 19 Camino page in the "Before class" section. The page is a draft already; we'd just edit before publishing.

---

## STEP 5 — Mon May 11, 8:00 AM

1. Students arrive, open their token URL on their phones, see "Waiting for the mixer to start."
2. At 8:22 (per S19 plan), open `host.html` on the lecture hall computer. Mirror to Apple TV.
3. Click **Start mixer**. Timer counts down 5:30. Patient Zero is auto-marked transmissible at t=0.
4. Students mingle, scan partners. Phones show their trade count. Host page shows trade graph filling in (without infection states — those are hidden until reveal).
5. At 8:27 (timer hits zero), the host page auto-transitions to "ENDED."
6. Click **Reveal & play infection tree**. Graph recolors: red = infected, gold = Patient Zero. Banner pops up at the front: "Patient Zero: <name>."
7. Teams compute R₀ on their team workspace. Host page shows live R₀ (= Patient Zero's direct contacts) in the sidebar.

---

## What goes wrong, and what to do

| Failure | Symptom | Recovery |
|---|---|---|
| Student doesn't see "MIXER LIVE" when you click Start | Their phone is on a stale state | Have them refresh the URL. Firebase reconnects in ~2 sec. |
| Camera permission denied | Phone says "Camera failed" | Have them go to Safari settings, allow camera, refresh. Or partner up with someone whose camera works. |
| Bad lighting, QR won't scan | Camera modal shows nothing | Move to a brighter spot. Or tap-to-focus on the partner's QR. |
| Patient Zero doesn't mingle | After 2 min, no infections spread | Remind the class: "everyone scan at least 4 partners." Patient Zero usually catches the cue. |
| Two teams click reveal at the same time | Race condition; second click overwrites | Only YOU should click reveal from the host page. Don't share the host URL with students. |
| Firebase rules error | "permission_denied" in browser console | Re-check Step 3. Rules must include the `s19_outbreak` block. |
| Reset mid-class because of a bug | Wrong patient zero, dirty data | Click "Reset (full wipe)" on host or admin, then re-seed and start again. ~30 seconds. |

---

## Cleanup after class (Mon May 11, ~9:10 AM)

1. Open admin console.
2. Click **Wipe everything** in the danger zone. Removes all student/contact/config data.
3. (Optional) Save the contact data CSV first if you want to use it for grading or research:
   - Open the Firebase Console → Database → Export JSON for the `s19_outbreak` node.
   - Save to `BIOL2-S26/grade-data/staged/S19_Apr_11/S19_outbreak_data.json` (or wherever your S19 grading folder is).

---

## Re-using this for future S-numbers

The app is parameterized by the Firebase path `s19_outbreak/`. If you want to run a similar activity in a future quarter, change all references to `s19_outbreak` to a new key (e.g., `s19_outbreak_F26` for Fall 2026) in: `index.html`, `host.html`, `admin.html`, `database.rules.json`, `firebase.json`. About 15 minutes of search-and-replace.

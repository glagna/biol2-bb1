# s19_outbreak/ — S19 Live-Action Outbreak App

**Built:** 2026-05-09 PM (overnight build)
**For:** BIOL 2 S19, Mon May 11 8:00 AM, Live-Action Outbreak activity (Master Plan §2 + §3.8)
**Backend:** Firebase RTDB at `biol2-bb1` project (existing)
**Hosting:** GitHub Pages at https://glagna.github.io/biol2-bb1/s19_outbreak/

## Files

| File | Purpose |
|---|---|
| `index.html` | Student token page (each of 47 students gets a unique URL `?id=carlos_r`). Shows name + QR + Scan button + trade counter. Hides infection state until reveal. |
| `host.html` | Instructor display, mirrored to lecture-hall Apple TV. Live trade graph (vis-network), counters, controls (Start / Stop / Reveal / Reset). |
| `admin.html` | Pre-class instructor console. Seed roster, pick Patient Zero, set mixer duration, generate URL distribution list. |
| `roster.json` | 47 students with auto-generated token IDs (`firstname_lastinitial`). Generated from `streak-leaderboard/data.json`. |
| `database.rules.json` | Firebase RTDB rules. Adds `s19_outbreak/` path with read/write open during the activity. Preserves existing rd13/bb1 rules. |
| `firebase.json` | Hosting config, mirrors the `rd13_game/` pattern. |
| `DEPLOY.md` | Step-by-step deploy guide (copy folder to local biol2-bb1, push to GitHub, update Firebase rules). ~15 min total. |
| `INSTRUCTOR_GUIDE.md` | Mon morning run-of-show. Minute-by-minute from 0:22 to 0:57. Pre-class checklist, recovery procedures. |

## Locked design decisions (per user 2026-05-09)

- Patient Zero: pre-set by instructor on admin page
- Transmission: deterministic (every contact between transmissible+susceptible = infection)
- Students do NOT see their own state during mixer
- Distribution: digital only (Camino announcement with token URLs)
- Mixer duration: 5:30 default (configurable 60-900s)
- Patient Zero reveals after team R₀ guesses

## Tech stack

- Vanilla HTML/CSS/JS (no framework, no build step)
- Firebase Realtime Database v10.12.0 (modular SDK from gstatic CDN)
- html5-qrcode 2.3.8 (camera-based QR scanning)
- qrcode.js 1.5.3 (rendering each student's QR)
- vis-network 9.1.9 (host-page contact graph)

## Quick test (local, no deploy)

```bash
cd s19_outbreak/
python3 -m http.server 8000
# open http://localhost:8000/admin.html in Chrome
# (Camera will not work over http; need https for production; GitHub Pages is https)
```

For a full dry-run with phones: deploy to GitHub Pages first (DEPLOY.md), then test on https URL with real phones.

## Deploy summary

Per `DEPLOY.md`:
1. Copy `s19_outbreak/` folder to your local `biol2-bb1` git clone (Mac terminal)
2. `git add` + `git commit` + `git push` (GitHub Pages auto-deploys)
3. Update Firebase RTDB rules via Firebase Console (paste contents of `database.rules.json`)
4. Open admin console, seed roster, pick Patient Zero, send URLs via Camino announcement Mon 7:55 AM
5. Mon 8:22 AM, open host.html, mirror to Apple TV, click Start

## Verification status (2026-05-09 build)

- [x] Roster JSON valid (47 students, all unique IDs)
- [x] Firebase rules JSON valid
- [x] All 3 HTML modules pass node `--check` syntax validation
- [x] Bracket / paren / brace balance verified for every script block
- [ ] Live dry-run with 3 buddy phones (deferred to instructor's pre-class testing Sun May 10 PM)
- [ ] Firebase rules deployed to live project (deferred to instructor execution)
- [ ] GitHub Pages deployment (deferred to instructor execution)

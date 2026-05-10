# S19 Live-Action Outbreak — Instructor Run Guide

**Class:** Mon May 11, 8:00–9:05 AM Arena
**Activity slot:** 0:22–0:57 (35 minutes)
**Goal:** students compute empirical R₀ from their own contact graph (LO3.5)

---

## Locked design (per user decisions 2026-05-09 PM)

- Patient Zero: pre-set by you on the admin console, before class
- Transmission: deterministic (every contact between transmissible+susceptible = infection)
- Students DO NOT see their own infection status during the mixer
- Distribution: digital only (Camino announcement with token URLs)
- Mixer duration: 5:30 default (configurable on admin page; you can change to 5:00 or 6:00 if needed)
- Minimum trades per student: 8 (achievable in 5:30; gives a denser graph and a more dramatic outbreak)
- Reveal is staged in TWO steps: Partial Reveal (infection states visible, Patient Zero hidden) → contact-tracing exercise → Full Reveal (Patient Zero halo lights up)
- R₀ is NOT computed today. The number is mentioned only as a teaser for S21 Friday, where the HIT formula is the LO3.3 home.

---

## The minute-by-minute (S19 0:22 to 0:57, 35 min)

The activity is staged as: setup → mixer → contact tracing exercise → Patient Zero reveal → debrief. R₀ is DEFERRED to S21 Friday (where the HIT formula is the actual LO3.3 home). Today is just contact tracing intuition.

| Time | What happens | Who does what |
|---|---|---|
| 0:22 to 0:27 (5 min) | **Outbreak setup.** Tell students: "Open the URL I sent in the Camino announcement. Make sure your phone shows your name and a QR code." Walk around, help anyone whose phone isn't loading. Do NOT tell them the rules yet. | You: open `host.html` on lecture hall computer, mirror to Apple TV (host shows "Waiting for instructor to start mixer"). Students: open their token URL. |
| 0:27 (1 sec) | **Click "Start mixer" on the host page.** Timer starts. Patient Zero is auto-marked transmissible at t=0 (you don't need to do anything else; the host code handles this). | You. |
| 0:27 to 0:32:30 (5:30 mixer) | **The mixer.** Tell students: "Stand up. Walk around. Find at least <strong>8 different partners</strong> and tap Scan to record a trade. <strong>Only ONE of you needs to scan</strong> — the trade counts on both phones automatically. Phones do not tell you who is infected. Just collect contacts." | Students: mingle and scan. You: walk around, encourage shy students. The host page shows the trade graph filling in (gray nodes only, no infection states yet). |
| 0:32:30 (auto) | **Mixer auto-ends.** Host page shows "ENDED." Students see "Mixer ended — look at the front of the room." | Auto. |
| 0:32:30 to 0:33 (30 sec) | **Click "Partial Reveal (infection only)" on the host page.** The graph recolors: red nodes = infected, gray = susceptible. Red edges = transmissions. <strong>Patient Zero is NOT marked.</strong> The infection tree is now visible. | You: click Partial Reveal. |
| 0:33 to 0:38 (5 min) | **Contact tracing exercise.** This is the LO3.5 work. Tell students: "The infection spread from one Patient Zero through this graph. As a team, look at the tree and identify who started it. Hint: trace red arrows backwards. The student with no red arrow pointing AT them is your suspect." Each team writes their guess on the team GSlide or dry-erase tabletop. | Students: trace the tree in teams. You: walk around, ask probing questions ("Why this person? What did the red arrows tell you?"). |
| 0:38 to 0:39 (1 min) | **Click "Full Reveal (Patient Zero)" on the host page.** Patient Zero gets a gold halo + a banner pops up: "Patient Zero: \<name\>." | You: click Full Reveal. Students: react (some teams cheer, some groan). |
| 0:39 to 0:44 (5 min) | **Class share-out.** "How many teams got Patient Zero right? What was the giveaway?" Walk students through the actual reasoning: trace from any infected node up the chain, find the root with no `infected_by` upstream. This IS contact tracing. Real epidemiologists do this with case interviews. | You moderating + students. |
| 0:44 to 0:52 (8 min) | **Bridge to bigger picture.** "Patient Zero infected \<N\> people directly. The total spread to \<X\> students. That number — how many people one infected person spreads to — is something we'll come back to on Friday. It has a name: <strong>R-zero</strong>. We'll work the math then. Today: you saw what an outbreak looks like. Wednesday: how the immune system fights one off. Friday: the math of stopping one." | You: this is the pedagogical bridge to S20 (Wed vaccine mechanism) and S21 (Fri HIT math). DO NOT compute R₀ as a number with the class today; that's S21 territory. |
| 0:52 to 0:55 (3 min) | **Wider debrief.** "What did this experience teach you that you didn't know before? What questions do you have?" Listen for questions about vaccines, herd immunity, or testing — these are the L3 LOs surfacing. | You + students. |
| 0:55 to 0:57 (2 min) | **Transition + Final Artifact preview.** Reminder: Final Artifact Proposal due Fri May 15. Jackpot Wheel. Out. | You. |

---

## Pre-class checklist (Sun May 10 PM)

- [ ] DEPLOY.md Steps 1–3 done (folder pushed to GitHub Pages, Firebase rules updated)
- [ ] Open `https://glagna.github.io/biol2-bb1/s19_outbreak/admin.html` in your browser
- [ ] Click "Seed roster from roster.json" (Step 1)
- [ ] Pick Patient Zero (Step 2). Don't tell anyone.
- [ ] Mixer duration: confirm 330 seconds (5:30). Adjust if you want 5:00 or 6:00.
- [ ] Copy the URL table as HTML or Markdown (Step 4) and schedule a Camino announcement to send Mon 7:55 AM.

## Mon May 11 morning checklist

- [ ] 7:55 AM: Camino announcement with URLs goes out (auto-scheduled, or manual send).
- [ ] 7:55 AM: Walk to the lecture hall, get to the podium computer.
- [ ] 7:58 AM: Open `https://glagna.github.io/biol2-bb1/s19_outbreak/host.html`. Mirror to Apple TV.
- [ ] 8:00 AM: Class begins. JB19 first (5 min). Then Compass Check, L3 Bridge, RD#15.
- [ ] 8:22 AM: Outbreak setup begins (per minute-by-minute above).

---

## What can go wrong, and the recovery

| Failure mode | What to do |
|---|---|
| Student didn't get the URL | Direct them to https://glagna.github.io/biol2-bb1/s19_outbreak/?id=<their_id>. The token IDs are listed in `roster.json`; pull it up on your laptop. |
| Student's phone is dead | Pair them with a partner who has a phone. They scan together. |
| Camera permission won't work on a student's phone | They can use a partner's phone OR sit out (mark them "absent" in Camino so they don't get penalized). |
| Patient Zero is shy and didn't mingle | If you see this happening at minute 2-3 of the mixer, casually walk near them and say "make sure to scan a few people." Don't single them out. |
| Mixer runs long, debrief is short | Skip the prediction step (0:32:30 to 0:35) and go straight to reveal. You buy back 3 min. |
| Live demo crashes mid-mixer | Click "Stop now" on host page, then "Reset (full wipe)" on the danger zone. Re-seed. Re-pick Patient Zero. Start again. About 60 seconds of recovery. |
| You forgot to pick Patient Zero | Click "Start mixer." If it complains "Pick Patient Zero on admin.html first," go to admin tab, pick someone, come back and click Start. |

---

## What students get assessed on (LO3.5)

This activity is NOT graded. It is an LO3.5 scaffold (Analyze epidemiological data). The graded surfaces that build on this:

- **JB23** (Wed May 20): epi curve interpretation question
- **BB3** (Fri May 29) Phase 1: R₀ analysis from initial outbreak data
- **Cert 3 Q3.5**: COVID-19 incidence curve analysis

The Live-Action Outbreak gives students a concrete experience of "I made trades, the data say X, I can compute R₀ from this graph." That intuition is what they apply downstream.

---

## What I (the instructor) get out of this

A real-time visualization of class mingling behavior. After the mixer, you can see who didn't trade enough (low trade count), which subgroups stayed together (clusters in the graph), and how long the chain of infection stretched. This is also a soft-data pulse on class dynamics that may inform team rebalancing for Unit 3.

---

## After class

Run the Wipe in admin console (or the Reset on host page) to clear the data. Optionally export the JSON first via Firebase Console for record-keeping.

Per Master Plan §3.8 IRB note: contact data is transient and not retained as a research instrument. Wipe is the default at end of class.

# Team board

The single place to see who owns what, by when, and what was decided. If it is not here or in an issue, it was not agreed.

## Now (updated Nov 20)

**Two things are running at the same time:**

1. **Assignment 2 is individual.** Everyone does their own red-team work and submits their own files. Submission 1 is due **Tue Nov 24**. The risk plan (Submission 2) is due **Wed Dec 2**. Summary: [docs/ASSIGNMENT2.md](docs/ASSIGNMENT2.md). Track yours on #41.
2. **The final project is a team effort.** The funding pitch (slide deck plus pre-recorded video) is in class **Tue Dec 1**. It is split into four blocks; claim one on #34. Details: [docs/FINAL_PROJECT.md](docs/FINAL_PROJECT.md).

### Pitch blocks (claim on #34)

| Block | Content | Issue | Owner |
|---|---|---|---|
| product | Product, problem, users; assembles the deck and joins the video | #35 | Mehul |
| market | Market, pricing and unit economics, the funding ask | #31 | free |
| tech | Architecture, models, data, infrastructure, capacity and cost | #32 | free |
| risk | Security, privacy, safety, governance, limitations | #33 | free |

Each block: 1 to 2 slides by Sat Nov 28 and a 30 to 45 second video part by Sun Nov 29. The issue assignees are the real record.

### Open for everyone

| What | Issue |
|---|---|
| Your own Assignment 2 (Submission 1 due Tue Nov 24) | #41 |
| Course server: change the temporary password (Harsh, Parth, Kira) | #30 |
| Investor feedback form, in class Tue Dec 1 | #38 |
| Merger or acquisition decision, in class Thu Dec 3 | #39 |
| Peer review form, in class Thu Dec 3 | #40 |

### Dates

| Date | What |
|---|---|
| Tue Nov 24 | Assignment 2 Submission 1 (individual) |
| Wed Nov 25 | Optional leaderboard competition closes |
| Sat Nov 28 | Pitch slides in the shared deck |
| Sun Nov 29 | Video parts recorded |
| Mon Nov 30 | Deck and video final |
| Tue Dec 1 | Pitch and investor feedback |
| Thu Dec 3 | Merger or acquisition decision and peer review |
| Fri Dec 4 | Final project due |
| Wed Dec 2 | Assignment 2 Submission 2 (risk plan, individual) |

## Blocks (Assignment 1, submitted Nov 15)

All blocks were finished and every issue is closed. Kept as a record.

| Block | Tasks | Issues | Owner |
|---|---|---|---|
| A | A1–A4 (done, saved Nov 5), plus Division of Labor table, questions to the teaching team, final AS01 email | #1–#4, #23, #26, #27 | Mehul |
| B | B1–B4, E4 | #5–#8, #21 | Parth (done; B3 and B4 revised to revision 2 on Nov 11; in the team report) |
| C | C1–C5, E2 | #9–#13, #19 | Harsh (done: C1–C5 and E2 saved; C4, C5, E2 revised to revision 2 on Nov 11; in the team report) |
| D | D1–D4, E1, E3 | #14–#18, #20 | Kira (picked Nov 9; done, all six saved Nov 14; zip uploaded) |
| sheet | `model_index_company_b1` spreadsheet | #24 | Mehul (done Nov 9; author and team names added Nov 11; uploaded to Mehul's folder) |
| everyone | Self-evaluation form (blog post), own notebook export zip, team report in own folder | #22, #25 | everyone (assigned to all four on Nov 11) |

The issue assignees are the real record; update the Owner column when you claim.


## Dates (Assignment 1)

| Date | What |
|---|---|
| Fri Nov 6, noon | Claim a block |
| Tue Nov 10 | Review each other's drafts |
| Fri Nov 13 | Every block finished; send Mehul your `show_responses()` output for the team report |
| Fri Nov 13 to Sat Nov 14 | Mehul builds and shares the final team report and the completed model spreadsheet |
| **Sat Nov 14, 11:59 PM ET (team hard deadline)** | Everyone uploads their own export zip and the final team report to their own folder; Mehul sends the AS01 email |
| Sun Nov 15, 11:59 PM ET | Official Canvas deadline (buffer only, do not plan to use it) |

## Rules

- Professor (Nov 6): we may divide the modules among us. Everyone puts a **comprehensive report** in their own Drive folder, and it must include a **table of who did which module**. Write your own answers in your own words; do not copy a teammate's text.
- No collaboration with anyone outside the team.
- The company Google Chat is the graded team channel. Post decisions there too, not only on WhatsApp.

## Decisions log

| Date | Decision | Why |
|---|---|---|
| Nov 5 | Repo is the tracker; one issue per task; teammates claim their own block | One source of truth |
| Nov 5 | Team number in the notebook is 2 | Final project team number |
| Nov 5 | A1: LTI 1.3 tool inside the LMS; instructor approves every AI-drafted message; if the AI is down at a deadline, accept and queue | Human in the loop, students never harmed by an outage |
| Nov 5 (meeting) | Plan A (each person does their block); design for 3 s latency; open-weights models from the professor's approved list on university-contracted servers; D lead names the models; retention until end of term plus appeal window | See [meetings/2026-11-05.md](meetings/2026-11-05.md) |
| Nov 9 | Division of Labor table posted in the company Google Chat. Harsh: C1–C5 and E2. Answers due to Mehul Fri Nov 13 | Required deliverable; E2 belongs to block C |
| Nov 11 | Shared tasks #22 (self-evaluation) and #25 (export and upload) assigned to all four; each person comments "submitted" / "uploaded" | Every member must do them |
| Nov 11 | Updates go in the company Google Chat, not by email | The chat is graded |
| Nov 19 | Assignment 2 is individual, so no blocks; the final project pitch is split into four blocks (product, market, tech, risk) that teammates claim; Mehul takes product and assembles the deck and video; everyone records their own part of the video; slides due Sat Nov 28 | Canvas says Assignment 2 is individual; the pitch is team work |
| Nov 20 | Professor: Metrics Challenge is for a different class (skip it); risk plan due Wed Dec 2; use the 1 to 5 scale | Her reply to our questions (#36) |
| Nov 6 | Contributor type is Collaborative (divide and conquer). Each person uploads a comprehensive team report with a who-did-what table to their own folder, plus their own notebook export. Mehul compiles the team report | Professor's reply, see [docs/COMMS.md](docs/COMMS.md) |

## Meetings

Notes go in [`meetings/`](meetings/), one file per meeting. Keep recordings in the company Drive, not in this public repo. Meeting notes: [2026-11-05](meetings/2026-11-05.md) (7 PM, Mehul, Kira, Parth).

## How to check progress

`python3 scripts/status.py` lists progress per module, open work per person, stale items (no update for 2+ days) and who is commenting.

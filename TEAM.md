# Team board

The single place to see who owns what, by when, and what was decided. If it is not here or in an issue, it was not agreed.

## Blocks (Assignment 1)

Pick a free block yourself: ask your AI assistant to open this repo (it follows [AGENTS.md](AGENTS.md)), or run `python3 scripts/blocks.py`. Claims are logged on issue #28.

| Block | Tasks | Issues | Owner |
|---|---|---|---|
| A | A1–A4, plus Division of Labor table, questions to the teaching team, final AS01 email | #1–#4, #23, #26, #27 | Mehul |
| B | B1–B4, E4 | #5–#8, #21 | free |
| C | C1–C5, E2 | #9–#13, #19 | free |
| D | D1–D4, E1, E3 | #14–#18, #20 | free |
| sheet | `model_index_company_b1` spreadsheet | #24 | free |
| everyone | Self-evaluation form (blog post), own Canvas report, export zip | #22, #25 | each person |

The issue assignees are the real record; update the Owner column when you claim.

## Dates

| Date | What |
|---|---|
| Fri Nov 6, noon | Claim a block |
| Sun Nov 8 | First drafts of every task in your own notebook copy; comment on each issue with a short summary |
| Tue Nov 10 | Review each other's drafts |
| Thu Nov 12 | Self-evaluation form, Canvas report, export zip done |
| Fri Nov 13, 11:59 PM ET | Assignment 1 due; Mehul sends the AS01 email |

## Rules from Canvas (read Nov 5)

- Everyone submits their **own individual report to Canvas**. We may share strategies, code and materials inside the team, but each written submission must be unique. We have asked the professor whether that means everyone answers all 21 tasks.
- No collaboration with anyone outside the team.
- The company Google Chat is the graded team channel. Post decisions there too, not only on WhatsApp.

## Decisions log

| Date | Decision | Why |
|---|---|---|
| Nov 5 | Repo is the tracker; one issue per task; teammates claim their own block | One source of truth |
| Nov 5 | Team number in the notebook is 2 | Final project team number |
| Nov 5 | A1: LTI 1.3 tool inside the LMS; instructor approves every AI-drafted message; if the AI is down at a deadline, accept and queue | Human in the loop, students never harmed by an outage |

## Meetings

Notes go in [`meetings/`](meetings/), one file per meeting. Keep recordings in the company Drive, not in this public repo. Meeting notes: [2026-11-05](meetings/2026-11-05.md) (7 PM, Mehul, Kira, Parth).

## How to check progress

`python3 scripts/status.py` lists progress per module, open work per person, stale items (no update for 2+ days) and who is commenting.

# Assignment 1 plan (due Fri Nov 13, 11:59 PM ET)

## Deliverables

1. Self-evaluation: read the blog post, complete the Google Form (each person).
2. Division of Labor table posted in company Google Chat.
3. Colab notebook, Modules A to E (21 tasks).
4. Assignment data zip from `retrieve_homework_data(...)`, uploaded to the individual folder in the company Drive.
5. `model_index_company_b1` spreadsheet completed.
6. Email to the teaching team. Subject: `OAI - <SECTION #> - <TEAM #> - AS01 Complete`.

## Tasks

| Module | Tasks |
|---|---|
| A: Interaction design and UX | A1 LMS workflow, A2 similarity display, A3 student messages, A4 prompt pipeline |
| B: Market analysis | B1 competitors, B2 build vs integrate, B3 pricing and economics, B4 regulatory barriers |
| C: Data | C1 dataset profiling, C2 leakage, C3 chunking and taxonomy, C4 real vs synthetic data, C5 fine-tuning compute |
| D: Models and evaluation | D1 model choice, D2 open-weights vs API, D3 ROC-AUC protocol, D4 latency and availability |
| E: Stack | E1 full stack, E2 capacity sizing, E3 tokenizer rules, E4 security and privacy |

## Open questions for the teaching team

- Does each person run and export the notebook themselves, or can modules be split and merged? `status()` expects every task done in one run.
- Case PDF says latency under 5 s (P95); Task D4 says under 3 s. Which applies?
- What is expected in the model index spreadsheet? Some cells are `??` or `CHECK THIS`.
- Access to the individual folders (Harsh, Khurshida, Mehul, Parth) is still pending.

## Division of labor (teammates pick their own block; claims are logged in issue #28)

| Block | Tasks | Lead |
|---|---|---|
| A + coordination and submission | A1–A4 | Mehul |
| B + E4 | B1–B4, E4 | unclaimed |
| C + E2 | C1–C5, E2 | unclaimed |
| D + E1 + E3 | D1–D4, E1, E3 | unclaimed |
| Model index spreadsheet | `model_index_company_b1` | unclaimed (overlaps with D1, E2, E3) |

## Tracking

Run `python3 scripts/status.py` for progress per module, open work per person, stale items and who is commenting.

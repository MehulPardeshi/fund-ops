# Final project (team)

Sources: the professor's **Final Presentation Instructions** (Canvas announcement, Tue Nov 24; the PDF is on Canvas, not in this repo), our case PDF (`AI_Case_Company_B1.pdf`, "Final Project: In-class Presentation and Activities") and her emails (Nov 19 and 20). The Nov 24 instructions replace our earlier plan of a recorded video.

## What we hand in and when

| Part | What | Who | When |
|---|---|---|---|
| Live pitch | **3-minute live pitch** of Veritas to "investors", then investor questions. **Every member speaks** (it is graded). | Team | In class, **Tue Dec 1** |
| Pitch deck | **At most 5 main slides** plus an appendix of any length (not presented, used in Q&A). Submitted as a **PDF** on Canvas. | Team | **Fri Dec 4, 11:59 PM ET** |
| Prototype demo (optional) | Up to 90 seconds, labelled "prototype on synthetic data". We are not planning one. | Team | Optional |
| Investor feedback | Rate the other teams' pitches and how much you would invest, in a Google Form | Each person | In class, Tue Dec 1 |
| Merger or acquisition decision | Merge with, acquire, or stay independent from the other company working on the same problem. One slide and a 1 minute presentation | Team | In class, **Thu Dec 3** |
| Decision form | Merger and acquisition Google Form response | Team | Thu Dec 3 |
| Peer review | Agree or disagree with each other company's decision, in a Google Form | Each person | In class, Thu Dec 3 |

**No audio or video recordings are needed any more.** The pitch is live.

## What the professor grades (100 points)

| Criterion | Points | Mainly on |
|---|---|---|
| Problem, market and buyer | 15 | Slides 1, 5 |
| Product and human oversight | 15 | Slide 2 |
| Technical credibility | 20 | Slide 3 |
| Safety, fairness and compliance | 15 | Slide 4 |
| Business model and the ask | 20 | Slide 5 |
| Evidence and honesty | 5 | Appendix A1, labels |
| Communication and Q&A | 10 | Everyone speaks, time kept |

Individual marks can be adjusted by peer assessment and how you answer questions. Our case's main failure is **a student wrongly accused, especially a non-native English writer**; investors will probe it, and it must be on slide 3 or 4 with its metric (false positive rate by writer group).

## Rules for every slide (from the instructions)

- **About 40 words at most** outside diagrams and tables; body text **24 pt or larger**.
- **The title is the conclusion** ("Veritas prepares the evidence. The instructor decides."), not a topic ("The solution").
- **Every number on slides 1 to 5 has a source on appendix slide A1** (title, publisher, date, link). Open each link yourself before citing it.
- **Label synthetic, estimated and illustrative figures.** Assignment 1 data is synthetic; case-brief figures are illustrative.
- **No invented traction:** no made-up customers, pilots, quotes or usage numbers. No "100% accurate", "zero bias" or "guaranteed compliance".
- No real personal data, no real logos; name real competitors in plain text only.
- **Tool use:** if you used an AI tool to draft text, images or code for your slide, add a line to appendix slide A2 (the professor requires this).
- No names, emails or student IDs on the slides; slide 1 lists team roles only.

## The deck

"Veritas Pitch Deck - Company B1 (Team 2)", a Google Slides file in Mehul's folder in `company_b_1`. Anyone signed in with a CMU account can edit it. The link is in the company Google Chat and the WhatsApp group; it is not in this repo because the repo is public.

| Slide | What | Owner | Live time |
|---|---|---|---|
| 1 | Title, one-line pitch, team roles, the problem | Mehul (product lead) | 50 s for slides 1 and 2 |
| 2 | The solution: what it does and does not do, the human-in-the-loop rule, the over-reliance warning | Mehul | |
| 3 | How it works: one diagram (LMS over LTI 1.3, model, where the instructor approves, fallback if the AI is down), 5 s target, false positive rate by writer group | **Kira** (technical lead) | 40 s |
| 4 | Safety, fairness and compliance: rules, controls, failures found in our own design | **Parth** (risk and compliance lead) | 40 s |
| 5 | Market, buyer and **the ask**: amount, runway, use of funds, milestones, unit economics | **Harsh** (finance and strategy lead) | 40 s |
| A (appendix) | A1 sources and assumptions (everyone), A2 tool use (everyone), backups: problem and product detail (Mehul), A5 models, capacity and cost (Kira), A8 top five risks (Parth), A6 market size and competitors, A7 funding summary (Harsh) | Each owner | Not presented |

Total about 2 minutes 50 seconds, inside the 3-minute limit. **Cut words, not speed.** Each slide has a speaker guide in its speaker notes.

## Your slide, step by step

| Who | Role | Main slide | Backup slides | Issue | Live time | Words (about) |
|---|---|---|---|---|---|---|
| Mehul | Product lead | 1 and 2 | Problem and product detail | #35 | 50 s | 125 |
| Kira | Technical lead | 3 How it works | A5 | #32 | **40 s** | 100 |
| Parth | Risk and compliance lead | 4 Safety, fairness and compliance | A8 | #33 | **40 s** | 100 |
| Harsh | Finance and strategy lead | 5 Market and the ask | A6, A7 | #31 | **40 s** | 100 |

1. **Comment "started" on your issue** so the team can see it.
2. **Open the deck** with your Andrew (CMU) Google account (link in the company Google Chat and WhatsApp; search "Veritas Pitch Deck").
3. **Read the speaker guide** in the notes under your slide and your backup slides.
4. **Fill your main slide**: replace the dashed placeholder box. One idea, about 40 words, 24 pt text, and a title that states your conclusion.
5. **Fill your backup slides** in the appendix with the detail that did not fit (tables, the method behind a number). These are for investor questions.
6. **Add every number on your main slide to appendix slide A1** with its source, or label it as an estimate or illustrative. If you used an AI tool for your slide, add a line to A2.
7. **Write your script** in your own words in the speaker notes, within your time and word count (about 2.5 words per second). Only say numbers that are on your slide.
8. **Rehearse out loud with a timer** at least twice. Be ready to answer questions on any slide, not only yours (the professor's checklist).
9. **Comment "done" on your issue** by **Sat Nov 28**.

**Notes for each slide:**
- **Kira (slide 3):** reuse Modules C, D and E1 to E3. Show where the instructor approves and what happens if the AI is down (our Assignment 1 decision: accept the submission and queue it). The professor wants an evaluation plan with the metric that matches the harm (false positive rate by writer group with intervals), not "accuracy".
- **Parth (slide 4):** your slide moved from 7 to 4 and your script is kept. Change the title to your conclusion, add the rules from primary sources (FERPA, GDPR for international students, EU AI Act education provisions, retention and use of student work for training), and one failure found in our own design with what we changed. Assignment 2 is individual, so do not use a teammate's red-team prompts or ratings.
- **Harsh (slide 5):** the ask goes on slide 5 **and** in the funding summary (A7): one amount, runway in months, the stage and why, a use-of-funds table with percentages (include evaluation and bias testing, compliance and security audits), 3 to 5 milestones each with a date, a measurable test and the risk it removes, unit economics with assumptions, and the return logic. End the pitch with the ask. Asking for more money does not earn a better grade.

## Prepare for the questions

The professor lists the questions investors will ask. Each owner prepares a short answer for the ones on their slide (in the speaker notes or a backup slide):

| Question | Owner |
|---|---|
| Why pay for this rather than an incumbent's new AI feature? | Harsh |
| Who is liable when the AI is wrong and a person follows it? | Parth |
| What is the worst failure in your own design, and what did you change? | Parth (with Mehul) |
| How do you know your evaluation is not just measuring synthetic data? | Kira |
| What happens when the service is down at the worst moment? | Kira |
| Which assumption, if wrong by half, kills the business model? | Harsh |
| What would you do with half the money? | Harsh |
| Which regulation could stop the launch, and how will you find out early? | Parth |
| How do you update the model without breaking what you validated? | Kira |
| What data do you need from the client, and what if they refuse? | Kira (with Mehul) |

If you don't know an answer, say so and say how you would find out. A confident wrong answer costs more than an honest gap.

## Metrics dashboard poster

Also part of the final project: one team poster with a custom metrics dashboard for Veritas (task: Education). Each person owns one panel (#43 to #46). Steps: [POSTER.md](POSTER.md).

## Internal dates

| Date | What |
|---|---|
| **Sat Nov 28** | Every main slide, backup slide and A1 row filled; script in the notes |
| Sun Nov 29 | Mehul checks the whole deck against the professor's checklist |
| Mon Nov 30 | Team rehearsal with a timer (online, time to be agreed), including questions |
| **Tue Dec 1** | Live pitch and investor feedback (in class) |
| Tue Dec 1 to Thu Dec 3 | Team decides: merge, acquire or stay independent |
| Thu Dec 3 | Decision slide, 1 minute presentation, peer review |
| **Fri Dec 4** | Mehul exports the deck to PDF and submits it on Canvas (plus the poster) |

# Instructions for AI assistants working in this repo

This repo is the tracker for Company B1 (Final Project Team 2) in 94-879 *Fundamentals of Operationalizing AI*. Each teammate works with their own assistant (Claude, ChatGPT, Codex or similar). Follow these steps whenever a teammate opens this repo with you.

## 0. Read first

1. The **"Now" section at the top of [TEAM.md](TEAM.md)**: the current phase, what is open and the next dates. Mehul keeps it current.
2. [PLAN.md](PLAN.md): deliverables and their status.
3. [docs/COMMS.md](docs/COMMS.md): questions to the professor and her answers.
4. [docs/PROJECT_GUIDE.md](docs/PROJECT_GUIDE.md): the case, grading, and how the Assignment 1 notebook worked.

GitHub issues are the real record. If TEAM.md and the issues disagree, trust the issues and tell the teammate.

## 1. Find out who you are working with

- With a shell: `gh api user --jq .login`.
- Otherwise, ask for their GitHub username.

Team: MehulPardeshi (project manager), Harsh-Sahay009, ParthD25, khsaydullaeva (Kira).

## 2. Give them a status report

When a teammate asks what is done, what is left or what is theirs (or just opens the repo), get the facts and then answer. If they ask what to do for the pitch, go straight to section 3:

- **With a shell:** run `git pull`, then `python3 scripts/status.py --me` for their own open work and `python3 scripts/status.py` for the whole team.
- **Without a shell:** read the "Now" section of TEAM.md and the open issues at https://github.com/MehulPardeshi/fund-ops/issues. An issue is theirs if they are an assignee. On an issue assigned to several people, a person has finished their part once they have commented "done", "submitted" or "uploaded".

Answer in simple language, in this order:

1. **Done:** one or two lines on finished work (closed milestones).
2. **Still to do for the team:** open items and who owns each.
3. **Assigned to you:** each open issue with its link and the very next step. If there is none, say so.
4. **Next deadlines:** the next two or three dates.
5. **Waiting on:** anything blocked, such as instructions not posted yet.

Do not make up tasks or dates that are not in the repo or the issues.

## 3. Blocks

Right now the **final project pitch** has four blocks (product, market, tech, risk), listed in TEAM.md with one issue each. **Assignment 2 is individual and has no blocks**: every teammate does all of it themselves (issue #41, docs/ASSIGNMENT2.md). **All four pitch blocks were assigned on Nov 21** (product Mehul #35, tech Kira #32, market Harsh #31, risk Parth #33). For the teammate you are helping:

- Find their block in the table under **"Your block, step by step"** in [docs/FINAL_PROJECT.md](docs/FINAL_PROJECT.md) and walk them through steps 1 to 8 one at a time: which slide is theirs, where the deck link is (company Google Chat or WhatsApp, never in this repo), the speaker guide in their slide's notes, how to record, the file name and the deadline. Then the block note for their block.
- Ask for their decisions and ideas first; the slide text and spoken words must be their own.
- Remind them to post progress in the company Google Chat too; that chat is graded.
- If blocks are ever reopened, list the FREE ones and let the teammate choose (`python3 scripts/blocks.py claim <block>`, or comment "I take block X" on #34). Do not choose for them.

- For Assignment 2, help them understand the task, but the prompts, ratings and explanations must be their own; the professor checks prompts for copying. Team rule (Nov 21): do not share one teammate's prompts, ratings, explanations or testing strategy with another, and do not suggest that teammates work on Assignment 2 together.

## 4. Rules you must keep

- **Splitting work:** the professor confirmed (Nov 6) that a collaborative team may divide the work. Each person writes their own part in their own words; do not copy a teammate's text.
- **Reasoning:** the professor allows GenAI as long as the reasoning is the student's own. Ask for their decisions before drafting, and have them review and rewrite in their own words. If anyone asks whether AI was used, answer truthfully.
- **Models:** use only models on the professor's approved list (see docs/PROJECT_GUIDE.md).
- **No collaboration outside the team.**
- **No names, emails or student IDs** in notebooks or submissions. Team number 2 is the only identifier.
- **Sources:** cite only what the teammate actually read, with the date.
- **Never commit** notebooks, course PDFs, model files, data exports, passwords or meeting recordings (see `.gitignore`). The repo is public.
- Work only on the teammate's own issues. Do not edit other people's issues.

## 5. Keep the tracker current

- Comment on an issue when the teammate starts, gets stuck or finishes. On shared issues they comment "done". Close an issue when the work is saved or submitted.
- Post decisions and blockers in the company Google Chat too.

## Repo map

| File | What |
|---|---|
| [TEAM.md](TEAM.md) | **Now** (current phase and open items), past blocks, dates, decisions |
| [PLAN.md](PLAN.md) | Deliverables and their status |
| [docs/VM.md](docs/VM.md) | Course server: VPN, login, folders |
| [docs/ASSIGNMENT2.md](docs/ASSIGNMENT2.md) | Assignment 2 (individual) explained |
| [docs/FINAL_PROJECT.md](docs/FINAL_PROJECT.md) | Final project blocks and dates |
| [docs/PROJECT_GUIDE.md](docs/PROJECT_GUIDE.md) | Case summary, grading, Assignment 1 notebook how-to |
| [docs/SUBMIT.md](docs/SUBMIT.md) | Assignment 1 export, upload and file names |
| [docs/COMMS.md](docs/COMMS.md) | Channels, questions to the professor and answers |
| [meetings/](meetings/) | Meeting notes |
| `scripts/status.py` | Done, left and yours (`--me`) |
| `scripts/blocks.py` | List or claim the current blocks (final project pitch) |
| `scripts/export_local.py` | Assignment 1 export if Colab is down |

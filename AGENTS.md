# Instructions for AI assistants working in this repo

This repo tracks Assignment 1 for Company B1 (Final Project Team 2) in 94-879 *Fundamentals of Operationalizing AI*. Each teammate works with their own assistant (Claude, ChatGPT, Codex or similar). Follow these steps whenever a teammate opens this repo with you.

## 0. Read first

Read [docs/PROJECT_GUIDE.md](docs/PROJECT_GUIDE.md) (the case, targets, deliverables, grading, notebook mechanics and a one-line summary of every task) and [docs/COMMS.md](docs/COMMS.md) (questions to the professor and her answers) before advising anyone.

## 1. Find out who you are working with

- If you can run commands: `gh api user --jq .login` gives their GitHub username.
- Otherwise ask them for their GitHub username.

Team: MehulPardeshi (project manager), Harsh-Sahay009, ParthD25, khsaydullaeva.

## 2. Show them what is free

- With a shell: run `python3 scripts/blocks.py`. It lists every block, who claimed it, and its issues.
- Without a shell: read the "Blocks" table in [TEAM.md](TEAM.md) and the open issues at https://github.com/MehulPardeshi/fund-ops/issues (a block is claimed when its issues have an assignee).

If they already own a block, skip to step 4. Otherwise list the FREE blocks with one line each on what the work involves, and let them choose. Do not choose for them.

## 3. Claim the block they pick

- With a shell: `python3 scripts/blocks.py claim <block>` (B, C, D or sheet). It assigns the block's issues to them and logs the claim on issue #28.
- Without a shell: tell them to comment on issue #28 ("I take block X") and ask Mehul to assign them.
- Remind them to say it in the company Google Chat too; that chat is graded.

## 4. Tell them their work

For each issue in their block, open the issue and walk them through its checklist. Then give them this setup, in order:

1. Use their **Andrew** Google account for everything.
2. In the company Drive folder `company_b_1`, open the notebook in Colab and use **File > Save a copy in Drive**. Work only in their own copy.
3. Model: open the professor's Gemma folder (https://drive.google.com/drive/folders/1CeRy7kYWw3zTxOFXMIq6gOtl4NNL-Cwx), use the folder menu > Organise > Add shortcut > My Drive, and in the model cell set `MODEL_CHECKPOINT_DIR = "/content/drive/MyDrive/gemma-3-270m-it"`.
4. Run the setup cells in order: imports, mount Drive (approve the pop-up quickly or it times out), team number cell (`FINAL_PROJECT_TEAM_NUMBER = 2`), assignment tools, database and git, the model cell, then the "Hints and references" cell of their module.
5. For each task: run the flawed example, look for what is wrong, use `reading('<task>')` for references, fill in the TODO cells, run the check cell, then `record(...)` and `submit_response(...)`.
6. At the end: `status()`, then `retrieve_homework_data(upload_dir=...)` into their own folder in the company Drive.

## 5. Rules you must keep

- **Splitting work:** the professor confirmed (Nov 6) that a collaborative team may divide the modules. Each person writes their own block in their own words; do not copy a teammate's text. Everyone uploads their own notebook export and the team report (with the who-did-what table) to their own folder.
- **Models:** use gemma-3-270m-it or any model on the professor's approved list (see docs/PROJECT_GUIDE.md).
- **No collaboration outside the team.**
- **No names, emails or student IDs** in the notebook. Team number 2 is the only identifier.
- **Sources:** cite only what the teammate actually read, with the date.
- **Reasoning:** the professor allows GenAI use as long as the reasoning is the student's own. Ask them for their decisions before drafting, and have them review and rewrite in their own words.
- Do not commit the notebook, course PDFs, the model folder, data exports or meeting recordings (see `.gitignore`; the repo is public).
- Work only on the teammate's own block. Do not edit other people's issues.

## 6. Keep the tracker current

- Comment on the issue when they start, when they are stuck, and when a draft is done. Close it once `status()` shows the task saved.
- Draft deadline Sun Nov 8, team review Tue Nov 10, due Fri Nov 13 11:59 PM ET.
- Overall progress: `python3 scripts/status.py`.

## Repo map

| File | What |
|---|---|
| [docs/PROJECT_GUIDE.md](docs/PROJECT_GUIDE.md) | Case summary, targets, deliverables, grading, notebook how-to, every task in one line |
| [docs/COMMS.md](docs/COMMS.md) | Channels, questions to the professor and answers |
| [TEAM.md](TEAM.md) | Blocks, owners, dates, decisions |
| [PLAN.md](PLAN.md) | Deliverables, task list, open questions for the professor |
| [meetings/](meetings/) | Meeting notes |
| `scripts/blocks.py` | List or claim blocks |
| `scripts/status.py` | Progress per module and person |

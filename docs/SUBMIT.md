# How to finish and submit Assignment 1

Team hard deadline: **Sat Nov 14, 11:59 PM ET**. Official Canvas deadline: Sun Nov 15, 11:59 PM ET (buffer only). Nothing is submitted on Canvas; everything goes into your own Drive folder, then Mehul emails the teaching team.

## 1. Finish your block (by Thu Nov 12)

- Every task in your block has its `record(...)` and `submit_response(...)` cells run.
- Run `status()`. Every task in your block should say `yes`. Paste the output as a comment on issue #28.
- Close each of your GitHub issues with a one-line summary.

## 2. Send Mehul your answers (by Thu Nov 12)

Run `show_responses()` in your notebook and send Mehul the output (copy the text, or File > Download > .ipynb). He puts every block into the team report.

## 3. Export your notebook data

**In Colab:**

1. In Drive, open `company_b_1`, right-click your own folder > Organise > Add shortcut > My Drive.
2. In the last cell of the notebook set `UPLOAD_DIR = '/content/drive/MyDrive/<your folder name>'` and run `retrieve_homework_data(upload_dir=UPLOAD_DIR, download=False)`.
3. The zip `oai_assignment01_team2_<time>.zip` appears in your folder.

**If Colab will not start** (it had outages on Nov 9):

1. In Drive, download `My Drive > oai_assignment01 > oai_assignment01.db`.
2. In Colab (or Drive), download your notebook as `.ipynb`.
3. On your computer, from this repo: `python3 scripts/export_local.py <notebook.ipynb> <oai_assignment01.db> ~/Downloads`
4. Upload the zip it makes to your own folder.

Do not rename the zip and do not put it inside another zip.

## 4. Upload to your own folder (Sat Nov 14)

Your folder is `company_b_1 > <your name>`. If it still says "You need permission", click Request access and tell Mehul.

| File | Name |
|---|---|
| Notebook data export | `oai_assignment01_team2_<time>.zip` (as made by the export) |
| Team report (all modules plus the who-did-what table, same file for everyone) | `OAI_B2_Team2_AS01_Report` (Mehul shares it on Fri Nov 13) |
| Completed model index spreadsheet (same file for everyone) | `model_index_company_b1_completed.xlsx` (Mehul shares it with the team report) |
| Your notebook (optional) | `oai_assignment01_notebook_team2_<your block>.ipynb` |

Then comment "uploaded" on issue #25.

## 5. Mehul sends the completion email

Once all four folders have both files, Mehul emails the teaching team with the subject `OAI - B2 - 2 - AS01 Complete`.

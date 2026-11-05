# Project guide: Assignment 1

Everything a teammate (or their AI assistant) needs to understand the assignment without opening every file in Drive. This is a summary in our own words. The original case PDF and notebook live in the company Drive folder `company_b_1` and are not copied here because this repo is public.

## The case in one page

- **Company:** Veritas AI Education, an early-stage EdTech startup (us, Company B1).
- **Client:** Apex State University: 14 colleges, 200+ programs, 40,000+ students.
- **Product:** a generative-AI academic integrity platform. It turns student work into embeddings, scores similarity against sources and flags possible plagiarism or unattributed AI use. The goal is educational, not punitive: it gives instructors evidence and suggested next steps, including supportive messages to students.
- **Human in the loop:** instructors and TAs review every AI finding before anything happens to a student.
- **Four integrity areas:** unattributed AI writing, direct and patchwork plagiarism, code and problem-set integrity, and developmental feedback for students.

### Targets from the case

| Metric | Target |
|---|---|
| Embedding and scoring latency | under 5.0 s per document (P95). Task D4 says under 3 s; we asked the professor which applies |
| Availability | 99.99% |
| Detection quality | ROC-AUC above 92% |
| False positive rate | under 1% |
| Privacy | 100% of student identities masked or hashed before embedding |
| Cost | under $0.02 per student submission |
| Pilot window | 3 weeks |
| Integration | LTI 1.3 and REST APIs with Canvas and Blackboard |
| Compliance | FERPA, GDPR for international students, university data sovereignty |

## Deliverables for Assignment 1 (due Fri Nov 13, 11:59 PM ET)

| # | Deliverable | Who | Where |
|---|---|---|---|
| 1 | Self-evaluation: read the blog post, fill the Google Form | each person | https://pages.cs.wisc.edu/~sharonli/time-in-the-chaos.html?v=13 and https://forms.gle/p2KEVeNJ1j7jQwCM6 |
| 2 | Division of Labor table: each member, individual contributor or collaborative, and who leads which module | Mehul posts | company Google Chat |
| 3 | Notebook Modules A1 to E4 | see [TEAM.md](../TEAM.md) | own copy of the Colab notebook |
| 4 | Model index spreadsheet `model_index_company_b1` | owner of block "sheet" | company Drive |
| 5 | Export zip from `retrieve_homework_data(...)` | each person | own folder inside `company_b_1` |
| 6 | Email "OAI - B2 - 2 - AS01 Complete" to the teaching team | Mehul | email |

The instructions say a team may divide the modules among members who each work independently, as long as the Division of Labor table says who leads which module. Canvas also says every person's written work must be their own and unique.

## How we are graded

| Part | What earns an A |
|---|---|
| Completion | all modules done by the deadline |
| Communication | regular communication with the team and the teaching team (questions, help, blockers, feedback). Use the Google Chat and comment on your GitHub issues |
| Analytic rigor | independent, critical reasoning in every answer. Answers that are AI-generated or show no personal reasoning are marked down. The professor allows GenAI use as long as the reasoning is yours |
| Creativity | distinct, well-researched solutions, not the same as other teams |

## Notebook: how it works

- Use your **Andrew** Google account. Open the notebook from `company_b_1` in Colab and **File > Save a copy in Drive**.
- Setup cells, in order: imports, mount Drive (approve the pop-up within a minute), team number (`FINAL_PROJECT_TEAM_NUMBER = 2`), assignment tools, database and git, model, test cell.
- **Model:** the model cell points to a folder we cannot open. Add a shortcut to the professor's `gemma-3-270m-it` folder (https://drive.google.com/drive/folders/1CeRy7kYWw3zTxOFXMIq6gOtl4NNL-Cwx, folder menu > Organise > Add shortcut > My Drive) and set `MODEL_CHECKPOINT_DIR = "/content/drive/MyDrive/gemma-3-270m-it"`. It loads in about 40 seconds on the free CPU runtime.
- Run the "Hints and references" cell of each module before its tasks.
- Each task has: a flawed example, an experiments cell, one or more TODO cells, a `record(...)` call and a `submit_response(...)` call with six fields: diagnosis, why_it_matters, solution, evidence, tradeoffs_and_risks, sources (2 to 4 sentences each), plus confidence 1 to 5.
- `hint('B1')` gives up to three hints, `reading('B1')` lists the references. Both are logged.
- Everything is logged to a database in your Drive (`MyDrive/oai_assignment01`) with your team number only. Never type names, emails or student IDs into the notebook.
- Every `record` and `submit_response` can be re-run; each run is saved as a new revision.
- `status()` shows which tasks are saved. At the end run `retrieve_homework_data(upload_dir='<path to your folder>')`.

## Tasks, one line each

### Module A: interaction design and UX (Mehul)

| Task | Asks for | References in the notebook |
|---|---|---|
| A1 | Fix an LMS workflow where the AI grades and emails students by itself; write `WORKFLOW_V1` with gates and the LTI step for each action | LTI 1.3 Core; Parasuraman and Manzey 2010; FERPA |
| A2 | Measure what a single "PLAGIARISM RISK" percent really tells you on 12 pairs; design a better display and an instructor test plan | Weber-Wulff et al. 2023; Guo et al. 2017; Sentence-BERT |
| A3 | Fix an accusatory student message; write a template, a checklist and when not to send | Liang et al. 2023; Weber-Wulff et al. 2023 |
| A4 | Fix a prompt builder that mixes student text with instructions; write `build_prompt_v1` and a test plan | Greshake et al. 2023; OWASP Top 10 for LLM Applications |

### Module B: market and competition

| Task | Asks for | References in the notebook |
|---|---|---|
| B1 | Why a vendor table is unreliable; a table of at least 3 real products (commercial and open source) with primary sources and access dates | Weber-Wulff 2023; Liang 2023; LTI 1.3 Core |
| B2 | Fix a 3-year cost comparison of LTI tool inside the LMS vs a standalone portal | LTI 1.3 Core; Hidden Technical Debt in ML Systems |
| B3 | Who buys and who can block; pricing model; unit economics with adoption, discounts and AI costs | 1EdTech TrustEd Apps; Student Data Privacy Consortium |
| B4 | Fix a compliance statement; which parts of the platform create which FERPA, GDPR and EU AI Act obligations | FERPA; GDPR; EU AI Act; NIST AI RMF |

### Module C: data

| Task | Asks for | References in the notebook |
|---|---|---|
| C1 | Check a flawed data-quality summary against one synthetic dataset; profile subgroups, labels and leakage risks | Datasheets for Datasets; Liang 2023; Obermeyer et al. 2019 |
| C2 | Fix a train/test split that leaks; write `grouped_split` and cross-split de-duplication | Kapoor and Narayanan 2023; Lee et al. 2021 (dedup) |
| C3 | Fix normalisation and chunking so quotes and citations survive; map findings to the violation taxonomy | Sentence-BERT; MTEB; PAN plagiarism workshop |
| C4 | Research at least 2 real datasets and compare with the synthetic one; fix a colleague's dataset entry | arXiv licensing; HC3 (ChatGPT vs human corpus); Datasheets |
| C5 | Fix a GPU memory estimate for fine-tuning; add a parameter-efficient method | ZeRO; LoRA; QLoRA |

### Module D: models and evaluation

| Task | Asks for | References in the notebook |
|---|---|---|
| D1 | Choose embedding and generation models under the constraints (one 40 GB GPU, FERPA, 5 s, languages) | MTEB; Model Cards; vLLM paper |
| D2 | Fix an open-weights vs commercial API comparison using current published prices | FERPA guidance; Efficiently Scaling Transformer Inference |
| D3 | Fix an evaluation plan: ROC-AUC, subgroup error rates, base rates, instructor agreement | Liang 2023; Sadasivan et al. 2023; Hardt et al. 2016; Weber-Wulff 2023 |
| D4 | Measure latency properly on the local model; correct availability math for 99.99% | The Tail at Scale; Google SRE book, Embracing Risk |

### Module E: stack

| Task | Asks for | References in the notebook |
|---|---|---|
| E1 | Find at least 10 flaws in a stack proposal; write `STACK_V1` layer by layer, each choice tied to a requirement | LTI 1.3 Core; HNSW paper; Hidden Technical Debt; NIST AI RMF |
| E2 | Fix capacity math; size the system for the final-exam peak (40,000 students, about 6 documents each) at 5 s per document | Little's Law; Efficiently Scaling Transformer Inference; Google SRE, Handling Overload |
| E3 | Fix a preparation step that counts words as tokens; write `prepare_v1` that respects the tokenizer and length limit | Sentence-BERT; Fishing for Magikarp; EmbeddingGemma model card |
| E4 | Find data flows that expose student data or let AI output reach students without approval; test the notebook's identifier filter | FERPA; GDPR; OWASP LLM Top 10; NIST AI RMF |

## Shared design decisions so far

Keep these consistent across modules unless the team changes them (log changes in [TEAM.md](../TEAM.md)).

- The product is an **LTI 1.3 tool inside the LMS**, not a separate website.
- **Human in the loop:** the AI prepares evidence and drafts; an instructor reviews every flag and approves every message to a student. The tool never writes a grade.
- **AI outage at a deadline:** the LMS still accepts and time-stamps submissions, checks are queued, instructors see "check pending", students are told nothing until a human has seen a result.
- **Minimum data to models:** no student names or codes in prompts; student text is treated as untrusted data.
- **Detector scores are a weak signal**, never evidence on their own, because they are biased against non-native English writers.

## Sources already looked at for Module A

Read a source yourself before citing it; the notebook asks you to cite only what you read.

| Source | Key point |
|---|---|
| LTI 1.3 Core (1EdTech) sections 5 and 5.3.6 | The platform starts the launch; `sub` is the only required user claim, so a tool can work without names or email |
| LTI Assignment and Grade Services 2.0, 3.2.14 and score examples | A tool can post a "PendingManual" status; the LMS owns the gradebook |
| Parasuraman and Manzey 2010, Human Factors | Automation complacency appears under multi-task load and is not fixed by practice |
| FERPA, 34 CFR 99.3, 99.10, 99.31(a)(1)(i)(B), 99.33 | Essays held for the school are education records; a vendor needs direct control and reuse limits |
| GDPR Article 22 | Right not to be subject to decisions based solely on automated processing; human intervention and contest |
| Weber-Wulff et al. 2023 | Detection tools are not accurate or reliable and should not be evidence of misconduct |
| Guo et al. 2017 | Modern networks are over-confident; confidence must be calibrated |
| Sentence-BERT 2019 | Embeddings plus cosine capture meaning better than word overlap and are fast |
| Liang et al. 2023 | Seven detectors flagged 61% of TOEFL essays as AI on average |
| Greshake et al. 2023 | Indirect prompt injection; models do not separate data from instructions |
| OWASP Top 10 for LLM Applications 2025 | LLM01 prompt injection mitigations; LLM02 minimum data; LLM05 validate output |

## Questions to the teaching team

See [COMMS.md](COMMS.md) for what we asked, when, and the answers.

#!/usr/bin/env python3
"""List the work blocks and who has claimed them, or claim one. Needs the gh CLI.

Usage:
  python3 scripts/blocks.py                 # show free and claimed blocks
  python3 scripts/blocks.py claim B         # claim block B for the logged-in GitHub user
"""
import json
import subprocess
import sys

REPO = "MehulPardeshi/fund-ops"
LOG_ISSUE = 28
BLOCKS = {
    "A": "A1-A4: interaction design and UX (Mehul)",
    "B": "B1-B4 + E4: market, pricing, regulation, security and privacy",
    "C": "C1-C5 + E2: data profiling, leakage, chunking, datasets, fine-tuning compute, capacity",
    "D": "D1-D4 + E1 + E3: models, open-weights vs API, evaluation, latency, full stack, tokenizer",
    "sheet": "model_index_company_b1 spreadsheet (overlaps D1, E2, E3)",
}


def gh(*args):
    return subprocess.run(["gh", *args], capture_output=True, text=True, check=True).stdout


def issues(block):
    raw = gh("issue", "list", "-R", REPO, "--state", "all", "--label", "block-" + block,
             "--json", "number,title,state,assignees")
    return sorted(json.loads(raw), key=lambda i: i["number"])


def owners(items):
    return sorted({a["login"] for i in items for a in i["assignees"]})


def show():
    free = []
    for b, desc in BLOCKS.items():
        items = issues(b)
        who = owners(items)
        done = sum(i["state"] == "CLOSED" for i in items)
        status = "claimed by " + ", ".join(who) if who else "FREE"
        if not who:
            free.append(b)
        print(f"[{b}] {desc}\n     {status} | {done}/{len(items)} done")
        for i in items:
            print(f"       #{i['number']} {i['title']}")
    print("\nFree blocks: " + (", ".join(free) if free else "none"))
    print("Claim one with: python3 scripts/blocks.py claim <block>")


def claim(block):
    if block not in BLOCKS:
        sys.exit("Unknown block. Choose one of: " + ", ".join(BLOCKS))
    me = gh("api", "user", "--jq", ".login").strip()
    items = issues(block)
    taken = [o for o in owners(items) if o != me]
    if taken:
        sys.exit(f"Block {block} is already claimed by {', '.join(taken)}. Pick another or agree a swap in the team chat.")
    for i in items:
        gh("issue", "edit", str(i["number"]), "-R", REPO, "--add-assignee", me)
    gh("issue", "comment", str(LOG_ISSUE), "-R", REPO, "--body", f"{me} claimed block {block}: {BLOCKS[block]}")
    print(f"Block {block} is yours, {me}. Your issues:")
    for i in items:
        print(f"  #{i['number']} {i['title']}  https://github.com/{REPO}/issues/{i['number']}")


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "claim":
        claim(sys.argv[2])
    else:
        show()

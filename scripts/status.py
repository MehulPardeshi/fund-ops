#!/usr/bin/env python3
"""What is done, what is left, and what is yours. Needs the gh CLI (logged in).

Usage:
  python3 scripts/status.py          # whole team
  python3 scripts/status.py --me     # only the logged-in GitHub user's open work
"""
import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone

REPO = "MehulPardeshi/fund-ops"
STALE_DAYS = 2
# On an issue shared by several people, a person's own comment with one of
# these words counts as "done" for that person.
DONE_WORDS = re.compile(r"\b(done|submitted|uploaded)\b", re.I)


def gh(*args):
    return subprocess.run(["gh", *args], capture_output=True, text=True, check=True).stdout


issues = json.loads(gh(
    "issue", "list", "-R", REPO, "--state", "all", "--limit", "300",
    "--json", "number,title,state,assignees,milestone,updatedAt,comments"))
milestones = json.loads(gh("api", f"repos/{REPO}/milestones?state=all&sort=due_on"))
now = datetime.now(timezone.utc)
me = gh("api", "user", "--jq", ".login").strip() if "--me" in sys.argv else None


def days_since(ts):
    return (now - datetime.fromisoformat(ts.replace("Z", "+00:00"))).days


def owners(i):
    return sorted(a["login"] for a in i["assignees"])


def done_for(i, person):
    """Closed, or a shared issue where this person said they are done."""
    if i["state"] == "CLOSED":
        return True
    if len(i["assignees"]) < 2:
        return False
    return any(c["author"]["login"] == person and DONE_WORDS.search(c["body"])
               for c in i["comments"])


print("MILESTONES (next deadlines)")
for m in milestones:
    due = (m.get("due_on") or "")[:10] or "no date"
    total = m["open_issues"] + m["closed_issues"]
    if m["state"] == "closed":
        state = "DONE"
    elif total == 0:
        state = "not started (no tasks yet)"
    else:
        state = f"{m['closed_issues']}/{total} done"
    print(f"  {due}  {m['title']:<32} {state}")

print("\nOPEN WORK" + (f" FOR {me}" if me else " BY PERSON"))
by_person = defaultdict(list)
for i in issues:
    if i["state"] != "OPEN":
        continue
    for o in owners(i) or ["UNASSIGNED"]:
        if o == "UNASSIGNED" or not done_for(i, o):
            by_person[o].append(i)
people = [me] if me else sorted(by_person)
for person in people:
    items = by_person.get(person, [])
    print(f"  {person}: {len(items)} open")
    for i in sorted(items, key=lambda x: x["number"]):
        age = days_since(i["updatedAt"])
        ms = (i.get("milestone") or {}).get("title", "no milestone")
        flag = "  <-- no update for 2+ days" if person != "UNASSIGNED" and age >= STALE_DAYS else ""
        print(f"    #{i['number']:<3} {i['title'][:62]}  [{ms}]{flag}")
        print(f"         https://github.com/{REPO}/issues/{i['number']}")

if not me:
    closed = sum(i["state"] == "CLOSED" for i in issues)
    print(f"\nALL ISSUES: {closed}/{len(issues)} closed")
    print("\nCOMMUNICATION (comments on issues)")
    counts = Counter(c["author"]["login"] for i in issues for c in i["comments"])
    for who, n in counts.most_common():
        print(f"  {who}: {n}")

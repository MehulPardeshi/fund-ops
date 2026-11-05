#!/usr/bin/env python3
"""Who owns what, what is left, who is communicating. Needs the gh CLI.

Usage: python3 scripts/status.py
"""
import json
import subprocess
from collections import Counter, defaultdict
from datetime import datetime, timezone

REPO = "MehulPardeshi/fund-ops"
STALE_DAYS = 2

raw = subprocess.run(
    ["gh", "issue", "list", "-R", REPO, "--state", "all", "--limit", "200",
     "--json", "number,title,state,assignees,labels,updatedAt,comments"],
    capture_output=True, text=True, check=True,
).stdout
issues = json.loads(raw)
now = datetime.now(timezone.utc)


def days_since(ts):
    return (now - datetime.fromisoformat(ts.replace("Z", "+00:00"))).days


def label_names(i):
    return [l["name"] for l in i["labels"]]


done = sum(i["state"] == "CLOSED" for i in issues)
print(f"OVERALL: {done}/{len(issues)} issues closed\n")

print("BY MODULE")
for m in ["module-a", "module-b", "module-c", "module-d", "module-e", "admin"]:
    group = [i for i in issues if m in label_names(i)]
    closed = sum(i["state"] == "CLOSED" for i in group)
    owners = sorted({a["login"] for i in group for a in i["assignees"]})
    print(f"  {m:9} {closed}/{len(group)} done   owners: {', '.join(owners) or 'nobody yet'}")

print("\nOPEN WORK BY PERSON")
by_person = defaultdict(list)
for i in issues:
    if i["state"] == "OPEN":
        for a in i["assignees"] or [{"login": "UNASSIGNED"}]:
            by_person[a["login"]].append(i)
for person, items in sorted(by_person.items()):
    print(f"  {person}: {len(items)} open")
    for i in sorted(items, key=lambda x: x["number"]):
        age = days_since(i["updatedAt"])
        flag = "  <-- STALE" if person != "UNASSIGNED" and age >= STALE_DAYS else ""
        print(f"    #{i['number']:<3} {i['title'][:60]}  (updated {age}d ago){flag}")

print("\nCOMMUNICATION (comments on issues)")
counts = Counter(c["author"]["login"] for i in issues for c in i["comments"])
if counts:
    for who, n in counts.most_common():
        print(f"  {who}: {n}")
else:
    print("  no comments yet")

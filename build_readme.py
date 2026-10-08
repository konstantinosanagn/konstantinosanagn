"""Rewrite the block between the `latest` markers in README.md with the newest commits."""

import json
import os
import re
import urllib.request
from datetime import datetime, timezone

REPOS = [
    "konstantinosanagn/ergon",
    "pytheum/pytheum",
    "konstantinosanagn/prophecy-pred-markets",
]
SHOWN = 4
README = "README.md"


def fetch(url):
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def latest_commits():
    rows = []
    for repo in REPOS:
        for c in fetch(f"https://api.github.com/repos/{repo}/commits?per_page=3"):
            subject = c["commit"]["message"].splitlines()[0]
            date = datetime.fromisoformat(c["commit"]["committer"]["date"].replace("Z", "+00:00"))
            rows.append((date, repo, subject, c["html_url"]))
    rows.sort(reverse=True)
    return rows[:SHOWN]


def render(rows):
    lines = []
    for date, repo, subject, url in rows:
        name = repo.split("/")[1]
        day = date.astimezone(timezone.utc).strftime("%Y-%m-%d")
        lines.append(f"- `{day}` [{name}]({url}): {subject}")
    return "\n".join(lines)


def main():
    text = open(README, encoding="utf-8").read()
    block = render(latest_commits())
    new = re.sub(
        r"(<!-- latest starts -->)\n.*?(<!-- latest ends -->)",
        lambda m: f"{m.group(1)}\n{block}\n{m.group(2)}",
        text,
        flags=re.S,
    )
    if new != text:
        open(README, "w", encoding="utf-8").write(new)
        print("README updated")
    else:
        print("no change")


if __name__ == "__main__":
    main()

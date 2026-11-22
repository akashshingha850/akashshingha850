"""Rewrite the <!-- REPOS:START --> ... <!-- REPOS:END --> block in README.md
with the most recently pushed public repos. Run by .github/workflows/update-readme.yml."""
import json, os, re, urllib.request
from datetime import datetime

USER = os.environ.get("GH_USER", "akashshingha850")
HIDE = {USER, f"{USER}.github.io"}
COUNT = 5

req = urllib.request.Request(
    f"https://api.github.com/users/{USER}/repos?per_page=100&type=owner&sort=pushed",
    headers={"Accept": "application/vnd.github+json", "User-Agent": "profile-readme"},
)
if os.environ.get("GITHUB_TOKEN"):
    req.add_header("Authorization", f"Bearer {os.environ['GITHUB_TOKEN']}")
repos = json.load(urllib.request.urlopen(req, timeout=30))

repos = [r for r in repos if not r["fork"] and not r["archived"] and not r["private"] and r["name"] not in HIDE]
repos.sort(key=lambda r: r["pushed_at"], reverse=True)

lines = []
for r in repos[:COUNT]:
    when = datetime.fromisoformat(r["pushed_at"].replace("Z", "+00:00")).strftime("%b %Y")
    meta = " · ".join(x for x in [r["language"], f"updated {when}"] if x)
    desc = f" — {r['description'].strip()}" if r["description"] else ""
    lines.append(f"- [**{r['name']}**]({r['html_url']}){desc} <sub>{meta}</sub>")

readme = open("README.md", encoding="utf-8").read()
block = "<!-- REPOS:START -->\n" + "\n".join(lines) + "\n<!-- REPOS:END -->"
new = re.sub(r"<!-- REPOS:START -->.*?<!-- REPOS:END -->", lambda _: block, readme, flags=re.S)
if new != readme:
    open("README.md", "w", encoding="utf-8").write(new)
    print("README updated")
else:
    print("no change")

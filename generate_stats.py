import os
import requests
import re
from datetime import datetime

def fetch_stats():
    token = os.getenv("GH_TOKEN")
    username = "Asilbek2706"
    headers = {"Authorization": f"token {token}"} if token else {}
    
    # Repolarni olish
    repo_res = requests.get(f"https://api.github.com/users/{username}/repos", headers=headers)
    repos = repo_res.json()
    
    # Commitlarni hisoblash (soddalashtirilgan)
    total_stars = sum(repo['stargazers_count'] for repo in repos)
    repo_count = len(repos)
    
    stats_text = f"""
> **Status:** `Analysis Complete`
> 🚀 **Total Stars:** `{total_stars}`
> 🛠 **Public Projects:** `{repo_count}`
> 📅 **Last Scan:** `{datetime.now().strftime('%Y-%m-%d %H:%M')}`
"""
    return stats_text

def update_readme(new_stats):
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()
    
    # README ichidagi va orasini yangilaydi
    pattern = r".*"
    replacement = f"\n{new_stats}\n"
    updated_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(updated_content)

if __name__ == "__main__":
    stats = fetch_stats()
    # Ham STATS.md, ham README.md yangilanadi
    with open("STATS.md", "w", encoding="utf-8") as f:
        f.write(f"### 📊 GitHub Stats for Asilbek2706\n{stats}")
    
    update_readme(stats)

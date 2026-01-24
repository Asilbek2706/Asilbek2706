import os
import requests
import re
from datetime import datetime

def fetch_stats():
    token = os.getenv("GH_TOKEN")
    username = "Asilbek2706"
    headers = {"Authorization": f"token {token}"} if token else {}
    
    response = requests.get(f"https://api.github.com/users/{username}/repos", headers=headers)
    if response.status_code != 200:
        return "Stats update failed."
    
    repos = response.json()
    total_stars = sum(repo['stargazers_count'] for repo in repos)
    repo_count = len(repos)
    
    return f"""
* 🚀 **Total Stars:** {total_stars}
* 🛠 **Public Projects:** {repo_count}
* 📅 **Last Updated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}
"""

def update_readme(stats):
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()
    
    # Markerlar orasidagi qismini yangilash
    pattern = r".*"
    replacement = f"\n{stats}\n"
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_content)

if __name__ == "__main__":
    stats = fetch_stats()
    update_readme(stats)

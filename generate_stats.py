import os
import requests
from datetime import datetime

def fetch_stats():
    token = os.getenv("GH_TOKEN")
    username = "Asilbek2706"
    headers = {"Authorization": f"token {token}"}
    
    # Repolarni olish
    response = requests.get(f"https://api.github.com/users/{username}/repos", headers=headers)
    repos = response.json()
    
    total_stars = sum(repo['stargazers_count'] for repo in repos)
    repo_count = len(repos)
    
    stats_text = f"""
### 📊 GitHub Stats for {username}
* 🚀 **Total Stars:** {total_stars}
* 🛠 **Public Projects:** {repo_count}
* 📅 **Last Updated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}
"""
    return stats_text

if __name__ == "__main__":
    new_stats = fetch_stats()
    with open("STATS.md", "w", encoding="utf-8") as f:
        f.write(new_stats)

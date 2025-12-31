import os
import requests

def fetch_github_stats():
    token = os.getenv("GH_TOKEN")
    headers = {"Authorization": f"token {token}"}
    username = "Asilbek2706"
    
    # Repolarni olish
    repo_url = f"https://api.github.com/users/{username}/repos"
    repos = requests.get(repo_url, headers=headers).json()
    
    total_stars = sum(repo['stargazers_count'] for repo in repos)
    total_repos = len(repos)
    languages = set(repo['language'] for repo in repos if repo['language'])

    stats_content = f"""
### 📊 Live GitHub Insights
| Metric | Value |
| :--- | :--- |
| 📁 **Total Repositories** | {total_repos} |
| ⭐ **Total Stars** | {total_stars} |
| 🛠️ **Main Languages** | {', '.join(list(languages)[:5])} |
| 🕒 **Last Updated** | $(date) |

*This file is automatically updated via GitHub Actions.*
"""
    return stats_content

if __name__ == "__main__":
    content = fetch_github_stats()
    with open("STATS.md", "w", encoding="utf-8") as f:
        f.write(content)

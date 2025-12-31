import os
import requests

def get_stats():
    # Bu yerda GitHub API orqali ma'lumotlar olinadi
    # Misol uchun oddiyroq ko'rinishda:
    username = "Asilbek2706"
    return f"### 📊 GitHub Stats for {username}\n- 🚀 Total Commits: [Fetch from API]\n- 🛠 Projects: [Fetch from API]"

if __name__ == "__main__":
    stats = get_stats()
    with open("STATS.md", "w") as f:
        f.write(stats)

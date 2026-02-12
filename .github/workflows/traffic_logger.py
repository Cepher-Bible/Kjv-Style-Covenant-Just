```python
#!/usr/bin/env python3

import os
import requests
import csv
from datetime import datetime

# ---------- CONFIG ----------
TOKEN = os.environ.get('GITHUB_TOKEN')
if not TOKEN:
    raise RuntimeError("GITHUB_TOKEN not found in environment variables")

OWNER = os.environ.get('GITHUB_OWNER', 'your-username-or-org')
OUTPUT_FILE = 'traffic_stats.csv'
API_BASE = 'https://api.github.com'

# ---------- FUNCTIONS ----------
def get_repos(owner):
    """Fetch all repos for the owner/org"""
    repos = []
    page = 1
    while True:
        url = f'{API_BASE}/users/{owner}/repos?per_page=100&page={page}'
        resp = requests.get(url, headers={'Authorization': f'token {TOKEN}'})
        if resp.status_code != 200:
            raise RuntimeError(f"Failed to fetch repos: {resp.status_code} {resp.text}")
        data = resp.json()
        if not data:
            break
        repos.extend(data)
        page += 1
    return repos

def get_traffic(owner, repo_name):
    """Fetch traffic stats (views + clones) for a repo"""
    stats = {}
    endpoints = {
        'views': f'{API_BASE}/repos/{owner}/{repo_name}/traffic/views',
        'clones': f'{API_BASE}/repos/{owner}/{repo_name}/traffic/clones'
    }
    for key, url in endpoints.items():
        resp = requests.get(url, headers={'Authorization': f'token {TOKEN}'})
        if resp.status_code == 200:
            json_data = resp.json()
            stats[key] = json_data.get('count', 0)
            stats[f'{key}_uniques'] = json_data.get('uniques', 0)
        else:
            stats[key] = 0
            stats[f'{key}_uniques'] = 0
    return stats

def save_csv(data, filename):
    """Write data to CSV"""
    headers = ['repo', 'views', 'unique_views', 'clones', 'unique_clones', 'timestamp']
    now = datetime.utcnow().isoformat()
    
    file_exists = os.path.isfile(filename)
    mode = 'a' if file_exists else 'w'
    
    with open(filename, mode, newline='') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        if not file_exists:
            writer.writeheader()
        for row in data:
            row['timestamp'] = now
            writer.writerow(row)

# ---------- MAIN ----------
def main():
    all_data = []
    print(f"Fetching repos for owner: {OWNER}")
    repos = get_repos(OWNER)
    print(f"Found {len(repos)} repos")

    for repo in repos:
        name = repo.get('name')
        if not name:
            continue
        print(f"Fetching traffic for repo: {name}")
        traffic = get_traffic(OWNER, name)
        all_data.append({
            'repo': name,
            'views': traffic.get('views', 0),
            'unique_views': traffic.get('views_uniques', 0),
            'clones': traffic.get('clones', 0),
            'unique_clones': traffic.get('clones_uniques', 0)
        })

    print(f"Saving CSV to {OUTPUT_FILE}")
    save_csv(all_data, OUTPUT_FILE)
    print("Done")

if __name__ == "__main__":
    main()
```

import os
import subprocess
from pathlib import Path
from rich.console import Console
import requests
from datetime import datetime, timedelta

console = Console()

VERSION_FILE = Path.home() / ".cli-convert" / ".version"
REPO_OWNER = "cli-convert"
REPO_NAME = "cli-convert"

def check_for_update():
    """Check if update is available using GitHub API."""
    try:
        version_file_path = VERSION_FILE
        version_file_path.parent.mkdir(parents=True, exist_ok=True)

        if version_file_path.exists():
            with open(version_file_path, "r") as f:
                data = f.read().strip().split("\n")
                if len(data) >= 2:
                    last_check = datetime.fromisoformat(data[1])
                    if datetime.now() - last_check < timedelta(days=1):
                        return

        latest_hash = get_latest_commit_hash()
        current_hash = read_local_version()

        if latest_hash and current_hash and latest_hash != current_hash:
            console.print("[yellow]⚠ Update available! Run: cli-convert --update[/yellow]")

        write_local_version(latest_hash)

    except Exception:
        pass

def get_latest_commit_hash():
    """Fetch latest commit hash from GitHub."""
    try:
        url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/commits"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        if data and isinstance(data, list):
            return data[0]["sha"]
    except Exception:
        pass
    return None

def read_local_version():
    """Read local version hash."""
    try:
        if VERSION_FILE.exists():
            with open(VERSION_FILE, "r") as f:
                lines = f.read().strip().split("\n")
                if lines:
                    return lines[0]
    except Exception:
        pass
    return None

def write_local_version(hash_value):
    """Write local version hash."""
    try:
        VERSION_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(VERSION_FILE, "w") as f:
            f.write(f"{hash_value}\n{datetime.now().isoformat()}\n")
    except Exception:
        pass

import subprocess
import sys
from pathlib import Path

def check_ffmpeg_installed():
    """Check if FFmpeg is installed and accessible."""
    try:
        subprocess.run(["ffmpeg", "-version"], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def check_yt_dlp_installed():
    """Check if yt-dlp is installed."""
    try:
        subprocess.run(["yt-dlp", "--version"], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def get_project_root():
    """Get the root directory of the project."""
    return Path(__file__).parent.parent

#!/usr/bin/env python3
"""Windows installer for CLI-Convert."""

import os
import sys
import subprocess
import shutil
import ctypes
from pathlib import Path
from urllib.request import urlretrieve
import zipfile

def is_admin():
    """Check if script is running as administrator."""
    try:
        return ctypes.windll.shell.IsUserAnAdmin()
    except:
        return False

def download_file(url, destination):
    """Download a file from URL."""
    print(f"Downloading from: {url}")
    try:
        urlretrieve(url, destination)
        return True
    except Exception as e:
        print(f"Download failed: {e}")
        return False

def main():
    """Run the installer."""
    print("=" * 60)
    print("CLI-Convert Installer")
    print("=" * 60)
    print()

    # Check for admin rights
    if not is_admin():
        print("Error: This script requires administrator privileges.")
        print("Please run Command Prompt or PowerShell as Administrator.")
        input("Press Enter to exit...")
        sys.exit(1)

    install_dir = Path.home() / "cli-convert"
    ffmpeg_url = "https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip"
    ffmpeg_zip = install_dir / "ffmpeg.zip"

    print(f"Installation directory: {install_dir}")
    print()

    # Create installation directory
    print("Creating installation directory...")
    install_dir.mkdir(parents=True, exist_ok=True)
    print("✓ Directory created")
    print()

    # Copy project files
    print("Copying project files...")
    source_cli = Path("cli_convert")
    dest_cli = install_dir / "cli_convert"
    
    if source_cli.exists():
        if dest_cli.exists():
            shutil.rmtree(dest_cli)
        shutil.copytree(source_cli, dest_cli)
        print("✓ Project files copied")
    else:
        print("Warning: cli_convert directory not found in current directory")
    
    # Copy requirements.txt
    if Path("requirements.txt").exists():
        shutil.copy("requirements.txt", install_dir / "requirements.txt")
        print("✓ requirements.txt copied")

    print()

    # Install Python dependencies
    print("Installing Python dependencies...")
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", "-r", str(install_dir / "requirements.txt")],
            capture_output=True,
            text=True,
            check=True
        )
        print("✓ Dependencies installed")
    except subprocess.CalledProcessError as e:
        print(f"Warning: Failed to install dependencies: {e.stderr}")

    print()

    # Download FFmpeg
    print("Downloading FFmpeg...")
    if download_file(ffmpeg_url, str(ffmpeg_zip)):
        print("✓ FFmpeg downloaded")
    else:
        print("Error: Failed to download FFmpeg")
        input("Press Enter to exit...")
        sys.exit(1)

    print()

    # Extract FFmpeg
    print("Extracting FFmpeg...")
    try:
        with zipfile.ZipFile(ffmpeg_zip, 'r') as zip_ref:
            zip_ref.extractall(str(install_dir))
        print("✓ FFmpeg extracted")

        # Move FFmpeg to expected location
        extracted_dirs = list(install_dir.glob("ffmpeg-master-*"))
        if extracted_dirs:
            extracted_dir = extracted_dirs[0]
            ffmpeg_final = install_dir / "ffmpeg"
            if ffmpeg_final.exists():
                shutil.rmtree(ffmpeg_final)
            extracted_dir.rename(ffmpeg_final)
            print("✓ FFmpeg moved to bin folder")

        # Remove zip file
        ffmpeg_zip.unlink()

    except Exception as e:
        print(f"Error extracting FFmpeg: {e}")
        input("Press Enter to exit...")
        sys.exit(1)

    print()

    # Add to PATH
    print("Adding to system PATH...")
    try:
        subprocess.run(
            f'setx PATH "%PATH%;{install_dir}"',
            shell=True,
            check=True,
            capture_output=True
        )
        print("✓ PATH updated")
    except subprocess.CalledProcessError as e:
        print(f"Warning: Failed to update PATH: {e}")

    print()

    # Create launcher batch file
    print("Creating launcher...")
    launcher_content = f"""@echo off
python -m cli_convert.main %*
"""
    launcher_path = install_dir / "cli-convert.bat"
    with open(launcher_path, "w") as f:
        f.write(launcher_content)
    print("✓ Launcher created")

    print()
    print("=" * 60)
    print("Installation complete!")
    print("=" * 60)
    print()
    print("Next steps:")
    print("  1. Close and reopen Command Prompt")
    print("  2. Run: cli-convert --help")
    print()
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Windows installer for CLI-Convert."""

import os
import sys
import subprocess
import shutil
import ctypes
from pathlib import Path
from urllib.request import urlretrieve
import zipfile
import time

# Fix encoding for Windows console output
if sys.stdout.encoding != 'utf-8':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def is_admin():
    """Check if script is running as administrator."""
    try:
        return ctypes.windll.shell.IsUserAnAdmin()
    except:
        return False

def elevate_to_admin():
    """Request elevation to admin privileges."""
    try:
        import win32api
        import win32con
        ctypes.windll.shell.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit(0)
    except Exception as e:
        print(f"Failed to elevate: {e}")
        return False

def add_to_path_registry(path_str):
    """Add a path to system PATH using registry (requires admin)."""
    try:
        import winreg
        with winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER) as reg:
            with winreg.OpenKey(reg, r"Environment", 0, winreg.KEY_ALL_ACCESS) as key:
                try:
                    current_path = winreg.QueryValueEx(key, "Path")[0]
                except FileNotFoundError:
                    current_path = ""
                
                if path_str not in current_path:
                    new_path = f"{current_path};{path_str}" if current_path else path_str
                    winreg.SetValueEx(key, "Path", 0, winreg.REG_EXPAND_SZ, new_path)
                    return True
        return True
    except Exception as e:
        print(f"  Registry error: {e}")
        return False

def download_file(url, destination):
    """Download a file from URL with retry logic."""
    print(f"Downloading from: {url}")
    max_retries = 3
    for attempt in range(max_retries):
        try:
            print(f"  Attempt {attempt + 1}/{max_retries}...", end=" ", flush=True)
            urlretrieve(url, destination)
            print("✓")
            return True
        except Exception as e:
            print(f"✗")
            if attempt < max_retries - 1:
                time.sleep(2)
            else:
                print(f"Download failed after {max_retries} attempts: {e}")
    return False

def main():
    """Run the installer."""
    print("=" * 60)
    print("CLI-Convert Installer")
    print("=" * 60)
    print()

    install_dir = Path.home() / "cli-convert"
    ffmpeg_url = "https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip"
    ffmpeg_zip = install_dir / "ffmpeg.zip"

    print(f"Installation directory: {install_dir}")
    print(f"Admin mode: {'Yes' if is_admin() else 'No'}")
    print()

    # Create installation directory
    print("Creating installation directory...")
    try:
        install_dir.mkdir(parents=True, exist_ok=True)
        print("✓ Directory created")
    except PermissionError:
        print("✗ Permission denied. Requesting admin privileges...")
        if not is_admin():
            elevate_to_admin()
        sys.exit(1)
    print()

    # Copy project files
    print("Copying project files...")
    source_cli = Path("cli_convert")
    dest_cli = install_dir / "cli_convert"
    
    try:
        if source_cli.exists():
            if dest_cli.exists():
                shutil.rmtree(dest_cli)
            shutil.copytree(source_cli, dest_cli)
            print("✓ Project files copied")
        else:
            print("⚠ Warning: cli_convert directory not found in current directory")
    except Exception as e:
        print(f"✗ Error copying files: {e}")
    
    # Copy requirements.txt
    try:
        if Path("requirements.txt").exists():
            shutil.copy("requirements.txt", install_dir / "requirements.txt")
            print("✓ requirements.txt copied")
    except Exception as e:
        print(f"✗ Error copying requirements.txt: {e}")

    print()

    # Install Python dependencies
    print("Installing Python dependencies...")
    try:
        cmd = [sys.executable, "-m", "pip", "install", "-q", "-r", str(install_dir / "requirements.txt")]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        if result.returncode == 0:
            print("✓ Dependencies installed")
        else:
            print(f"✗ Warning: pip returned error code {result.returncode}")
            if "Permission denied" in result.stderr or "Access denied" in result.stderr:
                print("  This may require admin privileges. Trying with admin...")
                if not is_admin():
                    elevate_to_admin()
                subprocess.run(cmd, check=False)
    except subprocess.TimeoutExpired:
        print("✗ Warning: Installation timed out (might still be working...)")
    except Exception as e:
        print(f"✗ Warning: Failed to install dependencies: {e}")
        print("  Continuing anyway...")

    print()

    # Download FFmpeg
    print("Downloading FFmpeg (this may take a few minutes)...")
    if download_file(ffmpeg_url, str(ffmpeg_zip)):
        print("✓ FFmpeg downloaded")
    else:
        print("✗ Error: Failed to download FFmpeg")
        print("  You can manually download from: https://ffmpeg.org/download.html")
        response = input("Continue without FFmpeg? (y/n): ").strip().lower()
        if response != 'y':
            input("Press Enter to exit...")
            sys.exit(1)
        print("  Note: You'll need to install FFmpeg manually for conversions to work")

    print()

    # Extract FFmpeg
    if ffmpeg_zip.exists():
        print("Extracting FFmpeg (this may take a minute)...")
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
                print("✓ FFmpeg organized")

            # Remove zip file
            try:
                ffmpeg_zip.unlink()
            except:
                pass

        except Exception as e:
            print(f"✗ Error extracting FFmpeg: {e}")
            print("  You may need to extract the zip file manually")

    print()

    # Add to PATH - using registry directly
    print("Adding to PATH...")
    try:
        path_to_add = str(install_dir)
        if add_to_path_registry(path_to_add):
            print(f"✓ {path_to_add} added to PATH")
        else:
            print(f"⚠ Warning: Could not add to PATH via registry")
    except Exception as e:
        print(f"⚠ Warning: Failed to update PATH: {e}")

    print()

    # Create proper launcher scripts
    print("Creating launcher scripts...")
    try:
        # Create Python launcher for direct execution
        py_launcher_content = f"""#!/usr/bin/env python3
import sys
sys.path.insert(0, r"{install_dir}")
from cli_convert.main import main
if __name__ == "__main__":
    main()
"""
        py_launcher = install_dir / "cli-convert-launcher.py"
        with open(py_launcher, "w") as f:
            f.write(py_launcher_content)
        
        # Create batch launcher for command prompt
        batch_launcher = f"""@echo off
cd /d "{install_dir}"
python "{py_launcher}" %*
exit /b %errorlevel%
"""
        batch_launcher_path = install_dir / "cli-convert.bat"
        with open(batch_launcher_path, "w") as f:
            f.write(batch_launcher)
        
        print("✓ Launcher scripts created")
    except Exception as e:
        print(f"✗ Warning: Failed to create launcher: {e}")

    print()
    print("=" * 60)
    print("Installation Complete!")
    print("=" * 60)
    print()
    
    # Show completion info
    print("Installation Summary:")
    print(f"  Location: {install_dir}")
    print(f"  Admin mode: {'Yes' if is_admin() else 'No'}")
    print()
    
    print("✓ INSTALLATION SUCCESSFUL!")
    print()
    
    print("You can now use CLI-Convert in two ways:")
    print()
    print("  Method 1 - Direct command (after restarting Command Prompt):")
    print("    cli-convert --help")
    print()
    print("  Method 2 - From installation folder:")
    print(f"    cd {install_dir}")
    print("    cli-convert.bat --help")
    print()
    print("  Method 3 - Python direct:")
    print(f"    python -m cli_convert.main --help")
    print()
    
    print("IMPORTANT: Please close and reopen Command Prompt for PATH changes!")
    print()
    
    print("Troubleshooting:")
    print("  • If 'cli-convert' command still not found:")
    print(f"    1. Close ALL Command Prompt windows")
    print(f"    2. Open a NEW Command Prompt")
    print(f"    3. Use the batch launcher: {install_dir}\\cli-convert.bat --help")
    print()
    print("  • If conversions fail:")
    print("    - Check FFmpeg installed:")
    print(f"      {install_dir / 'ffmpeg' / 'bin' / 'ffmpeg.exe'} -version")
    print()
    print("  • For direct path:")
    print(f"    {install_dir}")
    print()
    
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()

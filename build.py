#!/usr/bin/env python3
"""Build CLI-Convert into a standalone executable."""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def main():
    """Build the executable."""
    print("=" * 60)
    print("CLI-Convert Build Script")
    print("=" * 60)
    print()

    # Check if project structure exists
    if not Path("cli_convert").exists():
        print("Error: cli_convert directory not found.")
        print("Please run this script from the project root directory.")
        sys.exit(1)

    print("Checking dependencies...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "show", "pyinstaller"],
                      capture_output=True, check=True)
        print("✓ PyInstaller is installed")
    except subprocess.CalledProcessError:
        print("Installing PyInstaller...")
        subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"],
                      check=True)
        print("✓ PyInstaller installed")

    print()
    print("Building executable...")
    
    # Clean previous builds
    if Path("build").exists():
        print("Cleaning previous build...")
        shutil.rmtree("build")
    if Path("dist").exists():
        shutil.rmtree("dist")
    if Path("cli-convert.spec").exists():
        Path("cli-convert.spec").unlink()

    # Build with PyInstaller
    build_cmd = [
        sys.executable, "-m", "pyinstaller",
        "--onefile",
        "--name", "cli-convert",
        "--console",
        "--add-data", f"cli_convert{os.pathsep}cli_convert",
        "cli_convert/main.py"
    ]

    try:
        result = subprocess.run(build_cmd, check=True, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Build failed: {e.stderr}")
        sys.exit(1)

    print()
    print("=" * 60)
    print("Build complete!")
    print("=" * 60)
    print()
    print(f"Executable location: {Path('dist/cli-convert.exe' if sys.platform == 'win32' else 'dist/cli-convert').resolve()}")
    print()
    print("To use the executable:")
    print("  1. Add 'dist' folder to your PATH")
    print("  2. Or move cli-convert.exe to a folder already in PATH")
    print("  3. Run: cli-convert --help")

if __name__ == "__main__":
    main()

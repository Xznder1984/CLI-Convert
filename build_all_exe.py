#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Create standalone executables for CLI-Convert and its installer."""

import os
import sys
import subprocess
import shutil
from pathlib import Path

# Fix encoding for Windows console
if sys.stdout.encoding != 'utf-8':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def build_exe(script_name, exe_name):
    """Build a single executable using pyinstaller."""
    print(f"\n{'='*60}")
    print(f"Building {exe_name}...")
    print(f"{'='*60}")
    
    # Clean previous builds
    if Path("build").exists():
        shutil.rmtree("build")
    if Path(f"{exe_name}.spec").exists():
        Path(f"{exe_name}.spec").unlink()

    build_cmd = [
        "pyinstaller",
        "--onefile",
        "--name", exe_name,
        "--console",
        "--add-data", f"cli_convert{os.pathsep}cli_convert",
        script_name
    ]

    print(f"Running: {' '.join(build_cmd)}")
    
    try:
        result = subprocess.run(build_cmd, check=True)
        print(f"✓ {exe_name} built successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Build failed")
        return False

def main():
    """Build all executables."""
    print("=" * 60)
    print("CLI-Convert Multi-Exe Builder")
    print("=" * 60)

    # Check if project structure exists
    if not Path("cli_convert").exists():
        print("Error: cli_convert directory not found.")
        print("Please run this script from the project root directory.")
        sys.exit(1)

    # Create wrapper scripts for cleaner EXE names
    print("\nPreparing build scripts...")
    
    # Create cli_main.py wrapper
    with open("cli_main.py", "w") as f:
        f.write("""#!/usr/bin/env python3
from cli_convert.main import main

if __name__ == "__main__":
    main()
""")
    print("✓ Created cli_main.py wrapper")

    # Create installer_main.py wrapper
    with open("installer_main.py", "w") as f:
        f.write("""#!/usr/bin/env python3
from install import main

if __name__ == "__main__":
    main()
""")
    print("✓ Created installer_main.py wrapper")

    # Build both executables
    success = True
    success &= build_exe("cli_main.py", "cli-convert")
    success &= build_exe("installer_main.py", "cli-convert-installer")

    # Clean up wrapper files
    print("\nCleaning up temporary files...")
    Path("cli_main.py").unlink(missing_ok=True)
    Path("installer_main.py").unlink(missing_ok=True)
    for spec in Path(".").glob("*.spec"):
        spec.unlink(missing_ok=True)
    if Path("build").exists():
        shutil.rmtree("build", ignore_errors=True)
    print("✓ Cleanup complete")

    if success:
        print("\n" + "=" * 60)
        print("BUILD COMPLETE!")
        print("=" * 60)
        dist_path = Path("dist").resolve()
        print(f"\nExecutables created in: {dist_path}")
        print(f"  • dist/cli-convert.exe - The CLI conversion tool")
        print(f"  • dist/cli-convert-installer.exe - The installer")
        print("\nNext steps:")
        print("  1. Share these .exe files with users")
        print("  2. Users can run cli-convert-installer.exe to set up")
        print("  3. Or use cli-convert.exe directly if FFmpeg is installed")
        print("\n" + "=" * 60)
    else:
        print("\n✗ Some builds failed. Check errors above.")
        sys.exit(1)

if __name__ == "__main__":
    main()

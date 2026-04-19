# Installation Guide

## Quick Start

### For Windows Users (Easiest)

1. **Download:** `cli-convert-installer.exe` (9.7 MB)
2. **Run it** - No special action needed!
3. **Follow prompts** - Just click through
4. **Wait 2-5 minutes** for setup to complete (FFmpeg is ~400MB download)
5. **IMPORTANT: Close ALL Command Prompt windows** and open a NEW one
6. **Test:** Type `cli-convert --help`

> **Why close and reopen?** Windows needs to reload the PATH environment after installation. This only takes a few seconds and ensures the command works system-wide.

### For Python Developers

If you have Python 3.7+ installed:

```bash
git clone https://github.com/Xznder1984/CLI-Convert.git
cd CLI-Convert
pip install -r requirements.txt
python -m cli_convert.main --help
```

---

## Installation Methods

### Method 1: Installer (Recommended) ⭐

**Best for:** Everyone, especially non-technical users

```
cli-convert-installer.exe
├─ Downloads FFmpeg automatically
├─ Installs Python dependencies
├─ Sets up system PATH
├─ Creates launcher script
└─ No admin required (usually)
```

**What happens:**
1. Creates folder: `C:\Users\YourUsername\cli-convert\`
2. Installs all dependencies
3. Downloads and extracts FFmpeg
4. Adds to system PATH
5. Creates launcher batch file

**Installation location:**
```
C:\Users\YourUsername\cli-convert\
├── cli_convert/          (app code)
├── ffmpeg/               (conversion engine)
├── cli-convert.bat       (launcher)
└── requirements.txt      (dependencies)
```

### Method 2: Portable Tool

**Best for:** Users who already have FFmpeg installed

```bash
cli-convert.exe
├─ No installation needed
├─ No setup required
├─ Requires FFmpeg to be in PATH
└─ Just download and run
```

Usage:
```bash
cli-convert.exe input.mp4 output.mp4
```

### Method 3: From Source (For Developers)

**Best for:** Contributing or modifying the code

```bash
# Clone the repository
git clone https://github.com/Xznder1984/CLI-Convert.git
cd CLI-Convert

# Set up environment
pip install -r requirements.txt

# Run the tool
python -m cli_convert.main --help
```

---

## Installer Features

### ✅ Smart Admin Detection
- Works **without admin** in most cases (installs to user folder)
- **Automatically elevates** if permission error occurs
- No manual admin right-click needed

### ✅ Reliable Downloads
- **Retries 3 times** automatically if download fails
- **Waits between attempts** to avoid temporary network issues
- Shows manual install option if all retries fail

### ✅ Better Error Handling
- **Graceful fallbacks** - continues if one step fails
- **Clear error messages** - tells you what went wrong
- **Built-in troubleshooting** - shows next steps if issues occur

### ✅ Timeout Management
- pip install: 5 minute timeout
- FFmpeg download: 3 retry attempts
- PATH update: 10 second timeout

### ✅ Helpful Feedback
- Shows installation location
- Shows admin mode status
- Lists what was installed
- Provides troubleshooting guide

---

## Troubleshooting

### "Command not found" after installation

**Solution:**
1. Close ALL Command Prompt windows completely
2. Open a NEW Command Prompt window
3. Try again: `cli-convert --help`

**Why?** PATH changes need a new terminal session.

### Permission Denied during installation

**Solution:**
- Installer will automatically ask for admin
- Click "Yes" on the Windows UAC prompt
- Installation continues automatically

### FFmpeg download failed

**Solution:**
- Installer retries automatically 3 times
- If still fails, download manually from: https://ffmpeg.org/download.html
- Extract to: `C:\Users\YourUsername\cli-convert\ffmpeg\`

### Conversion fails with "ffmpeg not found"

**Solution:**
1. Verify FFmpeg exists: `C:\Users\YourUsername\cli-convert\ffmpeg\bin\ffmpeg.exe`
2. If missing, download from: https://ffmpeg.org
3. Extract to the path above

### "cli-convert.exe" is blocked (Windows SmartScreen)

**Solution:**
1. Click "More info"
2. Click "Run anyway"
3. Windows will allow it to run

---

## System Requirements

### Minimum Requirements
- **Windows 10** or later
- **~800 MB** free disk space
- **Internet connection** (for first setup)
- Python 3.7+ (if using portable tool)

### What Gets Installed
- Python dependencies (rich, yt-dlp, requests)
- FFmpeg binaries (~400 MB)
- CLI-Convert application (~10 MB)

---

## After Installation

### Verify Installation
```bash
# Test command availability
cli-convert --help

# List presets
cli-convert --presets

# Try a conversion
cli-convert input.mp4 output.mp4
```

### Add to PATH Manually (If Needed)
If `cli-convert` command doesn't work after reopening Command Prompt:

**Windows 10/11:**
1. Press `Windows Key + R`
2. Type `sysdm.cpl`
3. Go to "Advanced" tab
4. Click "Environment Variables"
5. Under "User variables", click "New"
6. Variable name: `PATH`
7. Variable value: `C:\Users\YourUsername\cli-convert\`
8. Click OK multiple times
9. Restart Command Prompt

**Command Line (Admin required):**
```bash
setx PATH "%PATH%;C:\Users\YourUsername\cli-convert\"
```

---

## Uninstallation

### Remove CLI-Convert

1. Delete folder: `C:\Users\YourUsername\cli-convert\`
2. Remove from PATH (optional):
   - Open Environment Variables (see "Add to PATH Manually" above)
   - Find the PATH entry you created
   - Click "Delete"
   - Click OK

---

## File Sizes

| Component | Size |
|-----------|------|
| cli-convert.exe | 9.5 MB |
| cli-convert-installer.exe | 3.4 MB |
| FFmpeg (after extraction) | ~400 MB |
| Python packages | ~100 MB |
| **Total installation** | **~500 MB** |

---

## Installer Options

### Auto-Retry on Download Failure
The installer automatically retries downloads 3 times with 2-second delays between attempts:
```
Attempt 1 → Fail → Wait 2 seconds
Attempt 2 → Fail → Wait 2 seconds
Attempt 3 → Fail → Show manual option
```

### Smart Admin Elevation
```
Try normal installation
    ↓
Permission denied?
    ↓
Automatically ask for admin
    ↓
User clicks "Yes"
    ↓
Continue with admin rights
```

### Graceful Error Recovery
```
Error occurs
    ↓
Try alternative method
    ↓
Still fails?
    ↓
Show manual instructions
    ↓
Continue anyway if possible
```

---

## Support

### Common Issues

**Q: Do I need admin rights?**
- A: Probably not! The installer installs to your user folder which doesn't need admin. If it does need admin, it will ask automatically.

**Q: Will this interfere with existing FFmpeg?**
- A: No, it installs to a dedicated folder. Your system FFmpeg (if any) won't be affected.

**Q: Can I install multiple versions?**
- A: You can have multiple copies by renaming the folder, but each install is independent.

**Q: How do I update CLI-Convert?**
- A: Delete the folder and reinstall using the latest installer.

**Q: Can I move the installation folder?**
- A: Yes, you'll just need to update the PATH or use the full path to run commands.

---

## Security Notes

- ✅ All downloads are from official GitHub releases
- ✅ No telemetry or tracking
- ✅ Open source (you can audit the code)
- ✅ Uses only well-known libraries (rich, yt-dlp, requests)
- ✅ No registry modifications (except PATH)

---

## Getting Help

### If Installation Fails

1. Check the **Troubleshooting** section above
2. Read the error message carefully
3. Make sure you have:
   - Internet connection
   - At least 800 MB free space
   - Windows 10 or later
4. Try the portable tool (cli-convert.exe) if installer fails

### Command Usage

After installation, get help with:
```bash
cli-convert --help        # General help
cli-convert --presets     # List all presets
```

---

## Summary

| Method | Admin | Setup | Best For |
|--------|-------|-------|----------|
| Installer | Maybe* | 2-3 min | Most users ⭐ |
| Portable | No | None | Tech users |
| From source | No | Manual | Developers |

*Usually not needed (auto-elevates if necessary)

**Choose the installer for the smoothest experience!**

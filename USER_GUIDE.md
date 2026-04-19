# CLI-Convert Executable Distribution Guide

## What You Get

Two standalone .exe files that don't require Python installation:

### 1. **cli-convert.exe** (~9.5 MB)
The main CLI conversion tool. Users can use this to convert media files after FFmpeg is installed.

### 2. **cli-convert-installer.exe** (~34 MB)
Complete installer that sets up everything:
- Installs dependencies
- Downloads FFmpeg automatically
- Adds CLI-Convert to system PATH
- Creates shortcuts

---

## For End Users

### Option 1: Quick Setup (Recommended)

1. **Download** `cli-convert-installer.exe`
2. **Run** the installer (requires Administrator privileges)
3. **Follow** the on-screen prompts
4. **Restart** Command Prompt
5. **Use**: `cli-convert --help`

### Option 2: Portable Usage

If you just want to use the CLI tool:

1. **Download** `cli-convert.exe`
2. **Ensure FFmpeg is installed** on your system
3. **Double-click** to run or use from Command Prompt:
   ```cmd
   cli-convert input.mp4 output.mp4 --discord
   ```

---

## Usage Examples

After installation, users can:

```cmd
# Basic conversion
cli-convert video.mp4 output.mp4

# Convert with preset (Discord-optimized)
cli-convert video.mp4 output.mp4 --discord

# Download and convert from YouTube
cli-convert --yt "https://youtube.com/watch?v=..." output.mp4

# List all available presets
cli-convert --presets

# Show help
cli-convert --help
```

---

## Available Presets

**Social Media:** discord, tiktok, youtube, instagram, twitter, whatsapp, telegram, twitch

**General:** mobile, web, hd, 4k

**Audio:** podcast, music, voiceover

---

## System Requirements

### For cli-convert-installer.exe:
- Windows 10 or later
- Administrator access
- 500 MB free disk space (for FFmpeg)
- Internet connection (to download FFmpeg)

### For cli-convert.exe only:
- Windows 10 or later
- FFmpeg installed (available from https://ffmpeg.org)
- Input media files

---

## Troubleshooting

### "Admin privileges required"
- Right-click the installer → "Run as Administrator"

### "FFmpeg not found"
- Use the full installer (`cli-convert-installer.exe`)
- Or install FFmpeg manually from https://ffmpeg.org

### "yt-dlp not found"
- The installer handles this automatically
- If running portable exe, install: `pip install yt-dlp`

### Conversion fails
- Ensure input file exists
- Check input format is supported (mp4, mkv, avi, mov, webm, mp3, wav, png, jpg, etc.)
- Verify FFmpeg installation

---

## Distribution

Share these files with users:
- `cli-convert.exe` - For portable usage
- `cli-convert-installer.exe` - For automated setup

You can package them together in a ZIP file for easy distribution.

---

## Building New Versions

To rebuild from source:

```bash
python build_all_exe.py
```

The executables will be created in the `dist/` folder.

---

## Technical Details

Both executables are built using PyInstaller with:
- Single-file bundling
- Console interface
- All dependencies included (rich, requests, yt-dlp)
- File size optimization

No external Python installation required on target systems!

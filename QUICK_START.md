# Quick Start & Troubleshooting

## Installation Issue Fixed! ✅

The installer has been completely rewritten to properly:
- Add CLI-Convert to your system PATH
- Create working launcher scripts
- Handle all edge cases

## Installation Steps

### 1. Run the Installer
```
cli-convert-installer.exe
```

### 2. Wait for Completion
- Downloads FFmpeg (~400MB) - may take 2-5 minutes
- Installs Python dependencies
- Configures system PATH
- Sets up launcher scripts

### 3. ⚠️ CRITICAL: Close & Reopen Command Prompt
This step is **mandatory** for the command to work:

```
1. Close ALL open Command Prompt / PowerShell windows
2. Open a BRAND NEW Command Prompt window
3. Type: cli-convert --help
```

> Windows caches environment variables in each terminal session. Closing and reopening loads the new PATH.

## Usage

### Basic Conversion
```bash
cli-convert input.mp4 output.mp4
```

### With Preset (Social Media Optimization)
```bash
cli-convert video.mp4 output.mp4 --discord
cli-convert image.png output.mp4 --tiktok
cli-convert audio.mp3 video.mp4 --youtube
```

### YouTube Download & Convert
```bash
cli-convert --yt "https://youtube.com/watch?v=dQw4w9WgXcQ" output.mp4
```

### List All Presets
```bash
cli-convert --presets
```

## Troubleshooting

### "cli-convert command not found"

**Solution 1: Reopen Command Prompt** (fixes 90% of cases)
- Close the Command Prompt window completely
- Open a fresh Command Prompt
- Try again

**Solution 2: Use Batch Launcher Directly**
```bash
C:\Users\YourUsername\cli-convert\cli-convert.bat --help
```

**Solution 3: Use Python Module**
```bash
python -m cli_convert.main --help
```

### "FFmpeg not found"

The installer should have downloaded FFmpeg automatically. To verify:

```bash
C:\Users\YourUsername\cli-convert\ffmpeg\bin\ffmpeg.exe -version
```

If not found:
1. Run the installer again
2. Or manually download from: https://ffmpeg.org/download.html
3. Extract to: `C:\Users\YourUsername\cli-convert\ffmpeg\`

### Installation Appears to Have Done Nothing

Check the installation folder:
```bash
C:\Users\YourUsername\cli-convert\
```

You should see:
- `cli_convert\` (Python package)
- `ffmpeg\` (FFmpeg binary)
- `cli-convert.bat` (Launcher)
- `requirements.txt` (Dependencies)

If the folder is missing, the installer had an error. Try running it again.

### Installer Requires Admin

The fixed installer automatically requests admin only if needed. If prompted:
1. Click "Yes" when prompted for admin
2. The installation will complete

### Slow Installation

FFmpeg is ~400MB. Depending on your internet speed, installation can take:
- Fast connection (>50 Mbps): 2-3 minutes
- Moderate connection (10-50 Mbps): 5-10 minutes
- Slow connection: 15+ minutes

**Don't close the installer!** It will show download progress.

## Portable Usage

If you don't want to use PATH, you can run from the installation folder:

```bash
cd C:\Users\YourUsername\cli-convert
cli-convert.bat video.mp4 output.mp4
```

## Advanced Usage

### Using cli-convert.exe Directly

The `cli-convert.exe` file can be used standalone if FFmpeg is already installed:

```bash
cli-convert.exe input.mp4 output.mp4
```

### Supported File Types

**Input:**
- Images: png, jpg, jpeg, webp, bmp
- Audio: mp3, wav, aac, flac, ogg
- Video: mp4, mkv, avi, mov, webm
- Animated: gif

**Output:**
- Video: mp4, mkv, avi, mov, webm
- Audio: mp3, wav, aac, flac, ogg

### Presets Available

- **Social Media**: discord, tiktok, youtube, instagram, twitter, whatsapp, telegram, twitch
- **Device**: mobile, web
- **Quality**: hd, 4k
- **Audio**: podcast, music, voiceover

### Example Conversions

```bash
# Convert image to video (5 seconds)
cli-convert photo.jpg video.mp4

# Convert to TikTok format
cli-convert video.mp4 tiktok.mp4 --tiktok

# Download YouTube video and convert to Discord format
cli-convert --yt "https://youtube.com/watch?v=..." discord.mp4 --discord

# Convert to 4K
cli-convert video.mp4 4k.mp4 --4k

# Convert to podcast quality
cli-convert audio.mp3 podcast.mp3 --podcast
```

## Still Having Issues?

1. **Verify installation:**
   ```bash
   dir C:\Users\YourUsername\cli-convert
   ```

2. **Test Python module directly:**
   ```bash
   python -m cli_convert.main --help
   ```

3. **Check FFmpeg:**
   ```bash
   C:\Users\YourUsername\cli-convert\ffmpeg\bin\ffmpeg.exe -version
   ```

4. **Run installer again:**
   - Sometimes the initial run has transient network issues
   - Running it again will retry and complete successfully

## Installation Details

**Location:** `C:\Users\YourUsername\cli-convert\`

**What's Installed:**
- Python package (cli_convert)
- FFmpeg binary (ffmpeg)
- Launcher script (cli-convert.bat)
- Python dependencies (rich, requests, yt-dlp)

**No Admin Required:** Installation uses user-level folder, not system-wide

**PATH Update:** Automatically added to user PATH in Registry

**Uninstall:** Simply delete the `C:\Users\YourUsername\cli-convert\` folder

# CLI-Convert

A powerful, production-ready Python CLI tool for converting media files (images, audio, GIFs, videos) using FFmpeg, with YouTube download support similar to yt-dlp.

## Features

- **Multi-format conversion**: Convert between images, audio, GIFs, and videos
- **YouTube support**: Download and convert videos directly from YouTube
- **FFmpeg integration**: Real conversion, not just renaming
- **Global installation**: Install as a system command `cli-convert`
- **Single EXE build**: Create standalone executable with PyInstaller
- **Auto-update checker**: Check for updates using GitHub API
- **Rich CLI output**: Colored terminal output with progress indicators
- **Windows installer**: Easy one-command installation script

## Installation

### Windows

1. **Clone or download** the repository
2. **Run the installer** (requires Administrator):
   ```
   python install.py
   ```
3. **Close and reopen** Command Prompt
4. **Start using**:
   ```
   cli-convert --help
   ```

### Manual Installation

1. Install Python 3.7+
2. Install dependencies:
   ```batch
   pip install -r requirements.txt
   ```
3. Install FFmpeg (or let the installer handle it)
4. Add the project folder to your PATH

## Usage

### Convert a file

```bash
cli-convert input.png output.mp4
cli-convert audio.mp3 output.mp4
cli-convert video.mp4 output.mkv
```

### Convert with a preset

```bash
cli-convert video.mp4 output.mp4 --discord
cli-convert audio.mp3 output.mp4 --tiktok
```

### Download and convert from YouTube

```bash
cli-convert --yt "https://youtube.com/watch?v=dQw4w9WgXcQ" output.mp4
```

### List all available presets

```bash
cli-convert --presets
```

### Get help

```bash
cli-convert --help
```

## Supported Formats

### Input Formats
- **Images**: png, jpg, jpeg, webp, bmp
- **Audio**: mp3, wav, aac, flac, ogg
- **Video**: mp4, mkv, avi, mov, webm
- **GIF**: gif

### Conversion Rules
- **Image → Video**: Creates 5-second video without audio
- **GIF → Video**: Converts to video without audio
- **Audio → Video**: Creates video with black background
- **Video → Video**: Preserves audio (can change container/codec)
- **Video → Image**: ❌ Not supported

## Examples

```bash
# Convert image to video (5 seconds)
cli-convert photo.jpg video.mp4

# Convert audio to video (with black background)
cli-convert song.mp3 video.mp4

# Convert GIF to video
cli-convert animation.gif video.mp4

# Download from YouTube and convert
cli-convert --yt "https://youtube.com/watch?v=xyz" output.mp4

# Convert video format
cli-convert video.avi video.mp4
```

## Building an EXE

Create a standalone executable for distribution:

```bash
python build.py
```

The executable will be created at: `dist/cli-convert.exe`

## Requirements

- **Python 3.7+**
- **FFmpeg** (included in installer, or available from https://ffmpeg.org)
- **yt-dlp** (for YouTube downloads, installed via pip)
- **rich** (for colored CLI output)

### Python Dependencies
See `requirements.txt` for full list:
- rich - Colored terminal output
- yt-dlp - YouTube downloading
- pyinstaller - EXE compilation
- requests - GitHub API for updates

## Project Structure

```
CLI-Convert/
├── cli_convert/
│   ├── __init__.py
│   ├── main.py           # Entry point and CLI handling
│   ├── converter.py      # FFmpeg conversion logic
│   ├── presets.py        # Platform-specific presets
│   ├── updater.py        # GitHub update checker
│   └── utils.py          # Utility functions
├── build.py              # Python build script
├── install.py            # Python installer script
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## How It Works

1. **Presets.py**: Defines platform-specific encoding settings
   - 16+ presets (Discord, TikTok, YouTube, Instagram, Twitter, etc.)
   - Each preset optimizes for platform requirements
   - Easy to add custom presets

2. **Converter.py**: Detects file types and runs appropriate FFmpeg commands
   - Image to video: Creates 5-second looped video
   - Audio to video: Generates black background video with audio
   - GIF to video: Direct FFmpeg conversion
   - Video conversion: Preserves or transcodes as needed
   - Applies preset settings when specified

3. **Main.py**: Handles CLI arguments and user interface
   - Parses command-line arguments
   - Supports preset selection
   - Shows download/conversion progress
   - Displays colored output messages

4. **Updater.py**: Checks GitHub API for new commits
   - Compares local version with latest repository
   - Caches check results (24-hour validity)

5. **Build.py**: Compiles Python code into standalone EXE
   - Uses PyInstaller for compilation
   - Creates single-file executable
   - No Python installation required on target machine

6. **Install.py**: Automates the setup process
   - Creates installation directory
   - Downloads FFmpeg
   - Installs Python dependencies
   - Adds to system PATH
   - Creates launcher script

## Troubleshooting

### "FFmpeg not found"
- Run installer again to download FFmpeg
- Or install FFmpeg separately from https://ffmpeg.org

### "yt-dlp not found"
- Run: `pip install yt-dlp`

### "Permission denied" during installation
- Run Command Prompt as Administrator
- Run `install.bat` again

### Conversion fails
- Check that input file exists
- Verify input format is supported
- Ensure FFmpeg has read permissions

## License

MIT License - Feel free to use and modify

## Contributing

Contributions welcome! Fork, modify, and submit a pull request.

## Support

For issues, questions, or feature requests, please open an issue on GitHub.

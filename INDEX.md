# 📚 CLI-Convert Documentation

Welcome! This folder contains everything you need to understand and use CLI-Convert.

## 📖 Main Documents

### ⚡ Start Here
- **[QUICK_START.md](QUICK_START.md)** - Installation steps and common issues (READ THIS FIRST!)

### For Getting Started
- **[README.md](README.md)** - Project overview and quick introduction
- **[INSTALLATION.md](INSTALLATION.md)** - Detailed setup and installation guide

### For Using the Tool
- **[USER_GUIDE.md](USER_GUIDE.md)** - Complete user manual with examples

---

## 🚀 Quick Navigation

### I want to...

#### Install CLI-Convert
→ Start with [QUICK_START.md](QUICK_START.md) then read [INSTALLATION.md](INSTALLATION.md)

#### Learn how to use it
→ Read [USER_GUIDE.md](USER_GUIDE.md)

#### Fix installation issues
→ Go to [QUICK_START.md](QUICK_START.md) troubleshooting section

#### Understand the project
→ Check [README.md](README.md)

---

## 📋 What's Included

### Executables
- `cli-convert.exe` - Portable conversion tool
- `cli-convert-installer.exe` - Full installer with auto-setup

### Scripts
- `install.py` - Installation script
- `build.py` - Build script for creating executables
- `build_all_exe.py` - Build both executables

### Source Code
- `cli_convert/` - Main application package
  - `main.py` - CLI entry point
  - `converter.py` - FFmpeg conversion logic
  - `presets.py` - 16+ platform presets
  - `updater.py` - Update checker
  - `utils.py` - Utility functions

### Configuration
- `requirements.txt` - Python dependencies

---

## ⚡ Quick Start

### 1. Installation (2 minutes)
```bash
cli-convert-installer.exe
# Just run it, click through, done!
```

### 2. First Conversion
```bash
cli-convert video.mp4 output.mp4
```

### 3. With Preset
```bash
cli-convert video.mp4 output.mp4 --discord
```

---

## 🎯 Common Tasks

### Convert for Different Platforms
```bash
cli-convert input.mp4 output.mp4 --discord
cli-convert input.mp4 output.mp4 --tiktok
cli-convert input.mp4 output.mp4 --youtube
cli-convert input.mp4 output.mp4 --instagram
```

### Download and Convert from YouTube
```bash
cli-convert --yt "https://youtube.com/watch?v=..." output.mp4
```

### See All Options
```bash
cli-convert --help
cli-convert --presets
```

---

## 📊 Supported Formats

### Input
- **Video:** MP4, MKV, AVI, MOV, WebM
- **Audio:** MP3, WAV, AAC, FLAC, OGG
- **Images:** PNG, JPG, JPEG, WebP, BMP
- **Animated:** GIF

### Output
- Same as above (choose any output format)

---

## 🎨 Available Presets

### Social Media
- discord, tiktok, youtube, instagram, twitter
- whatsapp, telegram, twitch

### General
- mobile, web, hd, 4k

### Audio
- podcast, music, voiceover

---

## 🆘 Troubleshooting

### Installation Issues
→ See [INSTALLATION.md#Troubleshooting](INSTALLATION.md#troubleshooting)

### Usage Issues
→ See [USER_GUIDE.md#Troubleshooting](USER_GUIDE.md#troubleshooting)

### Common Questions
→ See [USER_GUIDE.md#FAQ](USER_GUIDE.md#faq)

---

## 📞 Getting Help

1. Check the relevant guide above
2. Read the troubleshooting section
3. Try `cli-convert --help`

---

## ✨ Key Features

✅ Multiple format support  
✅ 16+ social media presets  
✅ YouTube integration  
✅ Beautiful CLI interface  
✅ Cross-platform  
✅ No Python needed (exe version)  
✅ Auto-update checker  
✅ Graceful error handling  

---

## 📁 File Organization

```
CLI-Convert/
├── README.md                    (Project overview)
├── INSTALLATION.md              (Setup guide)
├── USER_GUIDE.md                (How to use)
├── INDEX.md                     (You are here)
│
├── cli_convert/                 (Source code)
│   ├── main.py
│   ├── converter.py
│   ├── presets.py
│   ├── updater.py
│   ├── utils.py
│   └── __init__.py
│
├── dist/                        (Executables)
│   ├── cli-convert.exe
│   └── cli-convert-installer.exe
│
├── build.py                     (Build scripts)
├── build_all_exe.py
├── install.py
└── requirements.txt
```

---

## 🔄 Version Info

- **Application:** CLI-Convert v1.0.0
- **Built with:** PyInstaller 6.18.0
- **Python:** 3.14
- **Last Updated:** April 19, 2026

---

## 📝 License

This project is open source and available for personal and commercial use.

---

## 🚀 Ready to Get Started?

1. **New user?** → Start with [INSTALLATION.md](INSTALLATION.md)
2. **Already installed?** → Go to [USER_GUIDE.md](USER_GUIDE.md)
3. **Developer?** → Check the source code in `cli_convert/`

**Choose your next step above!** ⬆️

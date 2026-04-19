"""Media conversion presets for different platforms and formats."""

PRESETS = {
    "discord": {
        "description": "Discord-optimized video (max 100MB, 1080p, H.264, AAC)",
        "video_codec": "libx264",
        "audio_codec": "aac",
        "max_bitrate": "5M",
        "max_size": "100M",
        "resolution": "1920x1080",
        "fps": 30,
    },
    "tiktok": {
        "description": "TikTok video (9:16 vertical, 720p, H.265, 60fps)",
        "video_codec": "libx265",
        "audio_codec": "aac",
        "resolution": "720x1280",
        "fps": 60,
        "aspect_ratio": "9:16",
    },
    "youtube": {
        "description": "YouTube-optimized (1080p60, H.264, stereo AAC)",
        "video_codec": "libx264",
        "audio_codec": "aac",
        "resolution": "1920x1080",
        "fps": 60,
        "bitrate": "12M",
    },
    "instagram": {
        "description": "Instagram Reels (1080x1920, H.264, AAC)",
        "video_codec": "libx264",
        "audio_codec": "aac",
        "resolution": "1080x1920",
        "fps": 30,
        "aspect_ratio": "9:16",
    },
    "twitter": {
        "description": "Twitter video (1200x675, H.264, AAC, 15MB max)",
        "video_codec": "libx264",
        "audio_codec": "aac",
        "resolution": "1200x675",
        "fps": 30,
        "max_size": "15M",
    },
    "whatsapp": {
        "description": "WhatsApp video (480p, low bitrate)",
        "video_codec": "libx264",
        "audio_codec": "aac",
        "resolution": "854x480",
        "fps": 24,
        "bitrate": "1M",
    },
    "telegram": {
        "description": "Telegram video (1280x720, H.264)",
        "video_codec": "libx264",
        "audio_codec": "aac",
        "resolution": "1280x720",
        "fps": 30,
    },
    "twitch": {
        "description": "Twitch stream upload (1080p60, H.264, AAC)",
        "video_codec": "libx264",
        "audio_codec": "aac",
        "resolution": "1920x1080",
        "fps": 60,
        "bitrate": "6M",
    },
    "mobile": {
        "description": "Mobile-friendly (720p, H.264, low bitrate)",
        "video_codec": "libx264",
        "audio_codec": "aac",
        "resolution": "1280x720",
        "fps": 30,
        "bitrate": "2M",
    },
    "web": {
        "description": "Web streaming (1080p, H.264, adaptive bitrate)",
        "video_codec": "libx264",
        "audio_codec": "aac",
        "resolution": "1920x1080",
        "fps": 30,
        "bitrate": "5M",
    },
    "hd": {
        "description": "HD quality (1080p, H.264, high bitrate)",
        "video_codec": "libx264",
        "audio_codec": "aac",
        "resolution": "1920x1080",
        "fps": 30,
        "bitrate": "15M",
    },
    "4k": {
        "description": "4K quality (2160p, H.265, high bitrate)",
        "video_codec": "libx265",
        "audio_codec": "aac",
        "resolution": "3840x2160",
        "fps": 30,
        "bitrate": "50M",
    },
    "podcast": {
        "description": "Podcast audio (128kbps MP3, mono)",
        "audio_codec": "libmp3lame",
        "bitrate": "128k",
        "channels": 1,
    },
    "music": {
        "description": "Music audio (320kbps MP3, stereo)",
        "audio_codec": "libmp3lame",
        "bitrate": "320k",
        "channels": 2,
    },
    "voiceover": {
        "description": "Voice-over quality (64kbps AAC, mono)",
        "audio_codec": "aac",
        "bitrate": "64k",
        "channels": 1,
    },
}


def get_preset(name):
    """Get a preset by name."""
    return PRESETS.get(name.lower())


def list_presets():
    """List all available presets."""
    return PRESETS


def get_preset_description(name):
    """Get description of a preset."""
    preset = get_preset(name)
    if preset:
        return preset.get("description", "No description")
    return None

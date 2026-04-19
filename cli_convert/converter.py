import os
import subprocess
from pathlib import Path
from .presets import get_preset

class Converter:
    """Handle file conversions using FFmpeg."""
    
    IMAGE_FORMATS = {".png", ".jpg", ".jpeg", ".webp", ".bmp"}
    AUDIO_FORMATS = {".mp3", ".wav", ".aac", ".flac", ".ogg"}
    VIDEO_FORMATS = {".mp4", ".mkv", ".avi", ".mov", ".webm"}
    GIF_FORMAT = {".gif"}

    def __init__(self, ffmpeg_path="ffmpeg"):
        """Initialize converter with FFmpeg path."""
        self.ffmpeg_path = ffmpeg_path
        self.preset = None

    def convert(self, input_file, output_file):
        """Convert input file to output file."""
        input_ext = Path(input_file).suffix.lower()
        output_ext = Path(output_file).suffix.lower()

        input_type = self._get_file_type(input_ext)
        output_type = self._get_file_type(output_ext)

        if not input_type:
            raise ValueError(f"Unsupported input format: {input_ext}")
        if not output_type:
            raise ValueError(f"Unsupported output format: {output_ext}")

        if input_type == "video" and output_type == "image":
            raise ValueError("Cannot convert video to image")

        if input_type == "image":
            if output_type == "video":
                self._image_to_video(input_file, output_file)
            else:
                self._run_ffmpeg(["-i", input_file, output_file])

        elif input_type == "gif":
            if output_type == "video":
                self._gif_to_video(input_file, output_file)
            else:
                self._run_ffmpeg(["-i", input_file, output_file])

        elif input_type == "audio":
            if output_type == "video":
                self._audio_to_video(input_file, output_file)
            else:
                self._run_ffmpeg(["-i", input_file, output_file])

        elif input_type == "video":
            self._run_ffmpeg(["-i", input_file, output_file])

    def _image_to_video(self, input_file, output_file):
        """Convert image to 5-second video without audio."""
        cmd = [
            self.ffmpeg_path,
            "-loop", "1",
            "-i", input_file,
            "-c:v", "libx264",
            "-t", "5",
            "-pix_fmt", "yuv420p",
            "-y",
            output_file
        ]
        subprocess.run(cmd, check=True, capture_output=True)

    def _gif_to_video(self, input_file, output_file):
        """Convert GIF to video without audio."""
        cmd = [
            self.ffmpeg_path,
            "-i", input_file,
            "-c:v", "libx264",
            "-pix_fmt", "yuv420p",
            "-y",
            output_file
        ]
        subprocess.run(cmd, check=True, capture_output=True)

    def _audio_to_video(self, input_file, output_file):
        """Convert audio to video with black background."""
        cmd = [
            self.ffmpeg_path,
            "-f", "lavfi",
            "-i", "color=c=black:s=1280x720:d=0",
            "-i", input_file,
            "-shortest",
            "-c:v", "libx264",
            "-c:a", "aac",
            "-pix_fmt", "yuv420p",
            "-y",
            output_file
        ]
        subprocess.run(cmd, check=True, capture_output=True)

    def _run_ffmpeg(self, args):
        """Run FFmpeg with given arguments."""
        cmd = [self.ffmpeg_path] + args + ["-y"]
        subprocess.run(cmd, check=True, capture_output=True)

    def _get_file_type(self, ext):
        """Determine file type from extension."""
        if ext in self.IMAGE_FORMATS:
            return "image"
        elif ext in self.AUDIO_FORMATS:
            return "audio"
        elif ext in self.VIDEO_FORMATS:
            return "video"
        elif ext in self.GIF_FORMAT:
            return "gif"
        return None

    def set_preset(self, preset_name):
        """Set preset for conversion."""
        self.preset = get_preset(preset_name)
        return self.preset is not None

import os
import sys
import subprocess
from pathlib import Path
from rich.console import Console
from .converter import Converter
from .updater import check_for_update
from .presets import list_presets, get_preset_description

console = Console()

def get_ffmpeg_path():
    """Get the path to FFmpeg executable."""
    if sys.platform == "win32":
        ffmpeg_dir = Path(os.path.expanduser("~")) / "cli-convert" / "ffmpeg" / "bin"
        ffmpeg_path = ffmpeg_dir / "ffmpeg.exe"
        if ffmpeg_path.exists():
            return str(ffmpeg_path)
    return "ffmpeg"

def main():
    """Main entry point for CLI-Convert."""
    if len(sys.argv) < 2:
        print_help()
        return

    check_for_update()

    if sys.argv[1] == "--presets":
        list_all_presets()
    elif sys.argv[1] == "--yt":
        if len(sys.argv) < 4:
            console.print("[red]Usage: cli-convert --yt <URL> <output_file>[/red]")
            return
        url = sys.argv[2]
        output = sys.argv[3]
        download_and_convert(url, output)
    else:
        if len(sys.argv) < 3:
            print_help()
            return
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        preset = None
        if len(sys.argv) > 3 and sys.argv[3].startswith("--"):
            preset = sys.argv[3][2:]
        convert(input_file, output_file, preset)

def convert(input_file, output_file, preset=None):
    """Convert a file."""
    if not os.path.exists(input_file):
        console.print(f"[red]Error: Input file '{input_file}' not found[/red]")
        return

    ffmpeg_path = get_ffmpeg_path()
    converter = Converter(ffmpeg_path)
    
    if preset:
        if not converter.set_preset(preset):
            console.print(f"[red]Error: Preset '{preset}' not found[/red]")
            return
        console.print(f"[cyan]Using preset: {preset}[/cyan]")

    try:
        with console.status("[bold green]Converting..."):
            converter.convert(input_file, output_file)
        console.print("[green]✓ Done![/green]")
    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")

def download_and_convert(url, output_file):
    """Download from YouTube and convert."""
    try:
        temp_file = "temp_download.mp4"
        console.print("[bold green]Downloading...[/bold green]")
        
        download_cmd = [
            "yt-dlp",
            "-f", "best",
            "-o", temp_file,
            url
        ]
        
        result = subprocess.run(download_cmd, capture_output=True, text=True)
        if result.returncode != 0:
            console.print(f"[red]Download failed: {result.stderr}[/red]")
            return

        console.print("[green]✓ Downloaded[/green]")
        
        ffmpeg_path = get_ffmpeg_path()
        converter = Converter(ffmpeg_path)

        with console.status("[bold green]Converting..."):
            converter.convert(temp_file, output_file)
        
        console.print("[green]✓ Done![/green]")
        
        if os.path.exists(temp_file):
            os.remove(temp_file)
            
    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        if os.path.exists(temp_file):
            os.remove(temp_file)

def print_help():
    """Print help message."""
    console.print("""
[bold cyan]CLI-Convert[/bold cyan] - Media conversion tool

[bold]Usage:[/bold]
  [yellow]cli-convert <input> <output>[/yellow]          Convert a file
  [yellow]cli-convert <input> <output> --preset[/yellow]  Convert with preset
  [yellow]cli-convert --yt <URL> <output>[/yellow]      Download and convert from YouTube
  [yellow]cli-convert --presets[/yellow]                 List all available presets

[bold]Supported Formats:[/bold]
  [cyan]Images:[/cyan] png, jpg, jpeg, webp, bmp
  [cyan]Audio:[/cyan] mp3, wav, aac, flac, ogg
  [cyan]Video:[/cyan] mp4, mkv, avi, mov, webm
  [cyan]GIF:[/cyan] gif

[bold]Available Presets:[/bold]
  discord, tiktok, youtube, instagram, twitter, whatsapp, telegram, twitch
  mobile, web, hd, 4k, podcast, music, voiceover

[bold]Examples:[/bold]
  [yellow]cli-convert image.png output.mp4[/yellow]
  [yellow]cli-convert video.mp4 output.mp4 --discord[/yellow]
  [yellow]cli-convert audio.mp3 output.mp4 --tiktok[/yellow]
  [yellow]cli-convert --yt "https://youtube.com/watch?v=dQw4w9WgXcQ" output.mp4[/yellow]
  [yellow]cli-convert --presets[/yellow]
""")

def list_all_presets():
    """List all available presets."""
    presets = list_presets()
    console.print("[bold cyan]Available Presets:[/bold cyan]\n")
    for name, preset in presets.items():
        description = preset.get("description", "No description")
        console.print(f"[yellow]{name:12}[/yellow] - {description}")

if __name__ == "__main__":
    main()

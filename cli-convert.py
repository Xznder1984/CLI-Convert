import sys
import subprocess
import os

def run(cmd):
    subprocess.run(cmd)

def is_image(f): return f.lower().endswith((".png",".jpg",".jpeg",".webp",".bmp"))
def is_gif(f): return f.lower().endswith(".gif")
def is_audio(f): return f.lower().endswith((".mp3",".wav",".aac",".flac",".ogg"))
def is_video(f): return f.lower().endswith((".mp4",".mkv",".avi",".mov",".webm"))

def convert(inp, out):
    if not os.path.exists(inp):
        print("❌ File not found")
        return

    # BLOCK VIDEO → IMAGE
    if is_video(inp) and is_image(out):
        print("❌ Converting video → image is not allowed.")
        return

    # IMAGE → VIDEO ✅
    if is_image(inp):
        run([
            "ffmpeg","-loop","1","-i",inp,
            "-c:v","libx264","-t","5",
            "-pix_fmt","yuv420p",out
        ])

    # GIF → VIDEO
    elif is_gif(inp):
        run([
            "ffmpeg","-i",inp,
            "-c:v","libx264",
            "-pix_fmt","yuv420p",
            "-an",out
        ])

    # AUDIO → VIDEO
    elif is_audio(inp):
        run([
            "ffmpeg",
            "-f","lavfi","-i","color=c=black:s=1280x720",
            "-i",inp,
            "-c:v","libx264",
            "-c:a","aac",
            "-shortest",out
        ])

    # VIDEO → VIDEO
    elif is_video(inp):
        run([
            "ffmpeg","-i",inp,
            "-c:v","libx264",
            "-c:a","aac",out
        ])
    else:
        print("❌ Unsupported format")

def download_and_convert(url, output):
    print("⬇️ Downloading with yt-dlp...")
    run([
        "yt-dlp",
        "-o","temp.%(ext)s",
        url
    ])

    # find downloaded file
    for f in os.listdir():
        if f.startswith("temp."):
            convert(f, output)
            os.remove(f)
            break

if __name__ == "__main__":
    args = sys.argv

    if "--yt" in args:
        url = args[args.index("--yt")+1]
        output = args[-1]
        download_and_convert(url, output)
    elif len(args) >= 3:
        convert(args[1], args[2])
    else:
        print("Usage:")
        print("cli-convert input output")
        print("cli-convert --yt <url> output.mp4")

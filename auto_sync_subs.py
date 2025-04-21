#!/usr/bin/env python3
import argparse
import shutil
import subprocess
import sys

def check_command(cmd):
    if not shutil.which(cmd):
        print(f"❌ `{cmd}` not found – install it and add to PATH.")
        sys.exit(1)

def auto_sync(video, subs_in, subs_out):
    cmd = [
        "ffsubsync",
        video,
        "-i", subs_in,
        "-o", subs_out
    ]
    subprocess.run(cmd, check=True)
    print(f"✅ Synced subtitles written to: {subs_out}")

def main():
    parser = argparse.ArgumentParser(
        description="Automatic subtitle sync using ffsubsync"
    )
    parser.add_argument("--video", "-v", required=True, help="Path to video file")
    parser.add_argument("--subs",  "-s", required=True, help="Path to original .srt")
    parser.add_argument("--out",   "-o", required=True, help="Output .srt path")
    args = parser.parse_args()

    check_command("ffmpeg")
    check_command("ffsubsync")

    auto_sync(args.video, args.subs, args.out)

if __name__ == "__main__":
    main()


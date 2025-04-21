# Sync-Subtitles

A command-line tool to automatically synchronize subtitles with a video file using `ffsubsync`.

## Prerequisites

- Python 3.x
- `ffmpeg` installed and added to PATH
- `ffsubsync` installed via `pip install ffsubsync`

## Installation

1. Install `ffmpeg`:
   - Ubuntu/Debian: `sudo apt-get install ffmpeg`
   - macOS with Homebrew: `brew install ffmpeg`
   - Windows: Download from ffmpeg.org and add to PATH
2. Install `ffsubsync`: `pip install ffsubsync`

After installation, ensure that `ffmpeg` and `ffsubsync` are accessible from the command line.

## Usage

To use the tool, run the following command:

```bash
python sync_subtitles.py --video <path_to_video> --subs <path_to_original_srt> --out <path_to_output_srt>
```

For example:

```bash
python sync_subtitles.py --video movie.mp4 --subs original.srt --out synced.srt
```

Alternatively, make the script executable and run it directly:

```bash
chmod +x sync_subtitles.py
./sync_subtitles.py --video movie.mp4 --subs original.srt --out synced.srt
```

### Arguments

- `--video`, `-v`: Path to the video file (e.g., .mp4, .mkv)
- `--subs`, `-s`: Path to the original subtitle file (.srt)
- `--out`, `-o`: Path where the synchronized subtitle file will be saved (.srt)

**Note:** The output file will be overwritten if it already exists.

## How It Works

This tool uses `ffsubsync`, which synchronizes subtitles by analyzing the audio of the video and the subtitle timings. It adjusts the subtitle timings to match the audio, producing a synchronized subtitle file.

For more details on `ffsubsync`, visit its GitHub repository.
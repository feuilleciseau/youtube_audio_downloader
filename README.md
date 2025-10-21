# YouTube Downloader

This Python project allows you to **download audio from YouTube videos or playlists** in MP3 format. It provides both a **modern command-line interface (CLI)** and a **graphical user interface (GUI)**, giving you flexibility depending on your workflow.

## Features

- Download the audio from a single YouTube video
- Download all audios from a YouTube playlist
- Modern GUI built with ttkbootstrap
- Simple help command to display all available options

## Requirements

To run this project, install the required dependencies using:

```bash
pip install -r requirements.txt
```

This will install:

- `yt-dlp` — for downloading audio
- `rich` — for colorful CLI messages
- `questionary` — for interactive CLI menus
- `ttkbootstrap` — for a modern GUI

> Note: `tkinter` is typically included with Python by default. If it’s missing, you may need to install it separately depending on your OS.

## Usage

Run the script using:

```bash
python main.py <command> [url]
```

### Available Commands

| Command                     | Description                                                 |
| --------------------------- | ----------------------------------------------------------- |
| `gui`                       | Launch the graphical user interface                         |
| `<video_url>`               | Download audio from a single YouTube video or playlist      |
| `<file.txt>`                | Download audio from multiple videos listed in a text file   |
| `help`                      | Show the help menu with all available commands              |

### Examples

``` bash
# Launch the graphical user interface
python main.py gui

# Download audio from a single YouTube video
python main.py https://youtube.com/watch?v=XXXXXXX

# Download audio from a list of video URLs in a file
python main.py song_to_download.txt

# Download all audios from a YouTube playlist
python main.py https://youtube.com/playlist?list=XXXXXXX
```

## Folder Structure

```bash
YT_donwloader/
├── main.py                     # Main entry point
└── utils/
    ├── gui.py                    # Graphical user interface
    ├── help.py                   # Help menu (text-based)
    └── yt_downloader.py          # Download logic
├── requirements.txt            # Dependencies list
├── LICENSE                     # License file (MIT License)
└── README.md                   # Project documentation
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

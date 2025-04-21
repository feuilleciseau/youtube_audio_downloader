# YouTube Audio Downloader

This Python script allows you to download audio from YouTube videos and playlists in MP3 format. It uses the `yt-dlp` library to handle the downloads and `tkinter` to provide a simple graphical user interface (GUI) for the user.

## Features
- **Download audio from multiple YouTube videos**: Enter multiple URLs, each on a new line, and the audio for each video will be downloaded as an MP3 file.
- **Download YouTube playlists**: Enter a playlist URL, and all videos in the playlist will be downloaded as MP3 files.
- **Keeps an audio download history**: URLs of downloaded videos are saved in a text file (`history.txt`).

## Requirements
To use this script, you need to have the following Python libraries installed:

- `yt-dlp`: For downloading YouTube videos.
- `tkinter`: For the GUI interface.

You can install the required libraries by running the following command:

```bash
pip install -r requirements.txt
```
This will automatically install all the dependencies listed in the requirements.txt file.

> Note: `tkinter` is typically included with Python, but if it's missing, you may need to install it separately.

## Usage

1. **Download Individual Video Audio**
    - Open the application.
    - Paste multiple YouTube video URLs in the "Enter YouTube video URLs" text area, separating each URL with a new line.
    - Click "Download Audio" to start the download for each URL.
    - The audio files will be saved in the Media folder.

2. **Download Playlist Audio**
    - Enter the URL of a YouTube playlist in the "YouTube playlist URL" field.
    - Click "Download Playlist Audio" to download all videos in the playlist.
    - The audio files will be saved in the `Media` folder with filenames like: `Playlist Index - Title.mp3`.

3. **History**
    - All URLs that are downloaded are saved in the `history.txt` file for future reference.

## Folder Structure

```bash
youtube_audio_downloader/
├── main.py                     # Main GUI script
├── history.txt                 # A log of all downloaded video URLs
├── requirements.txt            # List of dependencies
├── LICENSE                     # License file (MIT License)
├── README.md                   # This file
└── Media/                      # Folder where all downloaded audio files are saved
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

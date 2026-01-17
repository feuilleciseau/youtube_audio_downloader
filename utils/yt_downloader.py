import os
from yt_dlp import YoutubeDL

OUTPUT = "Downloads"

def create_output_folder(output_folder:str):
    """
    Create output folder if not exist
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

def download_audio_single(url:str, output_folder):
    """
    Downloads the audio from a YouTube video using the provided URL.

    Parameters:
        url (str): The URL of the YouTube video.
        output_folder (str): The directory where the audio file will be saved.
    """

    ydl_opts = {
        'format': 'bestaudio[ext=m4a]/bestaudio/best',
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            },
            {
                'key': 'EmbedThumbnail',
            },
            {
                'key': 'FFmpegMetadata',
                'add_metadata': True,
            }
        ],
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
        'writethumbnail': True,
        'noplaylist': False,
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        },
        'geo_bypass': True,
        'allow_unplayable_formats': False,
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            print("")
            print(f"donwloading {url} ...")
            ydl.download([url])
        print("Download complete!")

    except Exception as e:
        print(f"ERROR: {e}")

def download_audio_playlist(url:str, output_folder):
    """
    Downloads the audio from all videos in a YouTube playlist using the playlist URL.
    """

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            },
            {
                'key': 'EmbedThumbnail',
            },
            {
                'key': 'FFmpegMetadata',
                'add_metadata': True,
            }
        ],
        'outtmpl': os.path.join(output_folder,'%(playlist_index)s - %(title)s.%(ext)s'),
        'writethumbnail': True,
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            print("")
            print(f"donwloading playlist {url} ...")
            ydl.download([url])
        print("Download complete!")

    except Exception as e:
        print(f"ERROR: {e}")

def download_audio_txt(txt_file:str, output_folder):
    try:
        with open(txt_file, "r") as file:
            urls = [line.strip() for line in file if line.strip()]
            for url in urls:
                download_audio_single(url, output_folder)

    except FileNotFoundError:
        print(f"{txt_file} not found !")


def download_audio(url: str, output_folder:str=OUTPUT):
    """
    Check if the url is about a youtube playlist, text file, or single video. and call the appropriate function to donwload audio.
    """
    create_output_folder(output_folder)

    if "&list=" in url or "playlist?" in url:
        download_audio_playlist(url, output_folder)

    elif url.startswith("https://"):
        download_audio_single(url, output_folder)

    elif url.endswith(".txt"):
        download_audio_txt(url, output_folder)

    else:
        print(f"Incorrect URL : {url}")

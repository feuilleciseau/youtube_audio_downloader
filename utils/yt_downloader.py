import os
from yt_dlp import YoutubeDL

OUTPUT = "Downloads"

def download_audio_single(url:str, output_folder:str=OUTPUT):
    """
    Downloads the audio from a YouTube video using the provided URL.

    Parameters:
        url (str): The URL of the YouTube video.
        output_folder (str): The directory where the audio file will be saved.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

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

def download_audio_playlist(url:str, output_folder:str=OUTPUT):
    """
    Downloads the audio from all videos in a YouTube playlist using the playlist URL.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

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

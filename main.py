import os
import tkinter as tk
from tkinter import scrolledtext, messagebox
from yt_dlp import YoutubeDL

def download_audio(url: str):
    """
    Downloads the audio from a YouTube video using the provided URL.

    Args:
    url (str): The YouTube video URL to download the audio from.

    This function configures the download options to extract the audio in MP3 format, 
    adds metadata and a thumbnail to the downloaded audio, and saves the file in the 'Media' folder.
    If the 'Media' folder does not exist, it is created.
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
        'outtmpl': 'Media/%(uploader)s - %(title)s.%(ext)s',
        'writethumbnail': True,
    }

    if not os.path.exists('Media'):
        os.makedirs('Media')

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download complete!")
    except Exception as e:
        print(f"ERROR: {e}")

def process_urls():
    """
    Processes the URLs entered in the text area, downloads the audio for each YouTube video,
    and saves the URLs in a 'history.txt' file.

    This function retrieves the URLs entered by the user, downloads each video using the 
    download_audio function, and appends each URL to a file to maintain a download history.
    After downloading, it clears the text area and displays a confirmation message.
    """
    urls = text_area.get('1.0', tk.END).strip().split('\n')
    with open('history.txt', 'a') as f:
        for url in urls:
            download_audio(url)
            f.write(url + '\n')
    text_area.delete('1.0', tk.END)
    messagebox.showinfo("Download complete", "All audio downloads are complete.")

def download_playlist():
    """
    Downloads the audio from all videos in a YouTube playlist using the playlist URL.

    This function retrieves the playlist URL entered by the user, configures the download options,
    and uses YoutubeDL to download all the videos from the playlist in MP3 format. The files are saved
    in the 'Media' folder. If the playlist URL is empty, a warning message is displayed.
    """
    playlist_url = playlist_entry.get().strip()
    if not playlist_url:
        messagebox.showwarning("Error", "Please enter a playlist URL.")
        return

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
        'outtmpl': 'Media/%(playlist_index)s - %(title)s.%(ext)s',
        'writethumbnail': True,
    }

    if not os.path.exists('Media'):
        os.makedirs('Media')

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([playlist_url])
        messagebox.showinfo("Download complete", "The playlist download is complete.")
    except Exception as e:
        print(f"ERROR: {e}")
        messagebox.showerror("Error", f"An error occurred : {e}")

if __name__ == '__main__':
    root = tk.Tk()
    root.title("YouTube Audio Downloader")

    # Champ de texte pour les URLs individuelles
    text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=10, width=50)
    text_area.pack(padx=10, pady=10)

    process_button = tk.Button(root, text="Download Audio", command=process_urls)
    process_button.pack(pady=5)

    # Champ pour l'URL de la playlist
    playlist_label = tk.Label(root, text="YouTube playlist URL :")
    playlist_label.pack(pady=5)
    playlist_entry = tk.Entry(root, width=50)
    playlist_entry.pack(pady=5)

    playlist_button = tk.Button(root, text="Download Playlist Audio", command=download_playlist)
    playlist_button.pack(pady=10)

    root.mainloop()

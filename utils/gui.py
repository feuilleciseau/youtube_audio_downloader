import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import StringVar
from utils.yt_downloader import download_audio_single, download_audio_playlist

class GUI:
    def __init__(self):
        self.app = tb.Window(themename="cosmo")
        self.app.title("YouTube Audio Downloader 🎵")
        self.app.geometry("500x300")

        self.url_var = StringVar()
        self.choice_var = StringVar(value="video")

        self.setup_ui()

    def setup_ui(self):
        tb.Label(self.app, text="Download audio from Youtube", font=("Helvetica", 18)).pack(pady=10)

        # Choix
        tb.Radiobutton(self.app, text="Video", variable=self.choice_var, value="video").pack(pady=5)
        tb.Radiobutton(self.app, text="Playlist", variable=self.choice_var, value="playlist").pack(pady=5)

        # URL
        tb.Entry(self.app, textvariable=self.url_var, width=50).pack(pady=10)
        
        # Bouton de téléchargement
        tb.Button(self.app, text="Download", bootstyle=SUCCESS, command=self.download).pack(pady=10)

        # Zone de log
        self.status_label = tb.Label(self.app, text="", foreground="green")
        self.status_label.pack()

    def download(self):
        url = self.url_var.get()
        choice = self.choice_var.get()

        if not url:
            self.status_label.config(text="⛔ Enter valid URL", foreground="red")
            return

        self.status_label.config(text="⏳ Downloading ...", foreground="blue")
        self.app.update_idletasks()

        try:
            if choice == "video":
                download_audio_single(url)
            else:
                download_audio_playlist(url)

            self.status_label.config(text="✅ Downloaded", foreground="green")
        except Exception as e:
            self.status_label.config(text=f"ERROR : {e}", foreground="red")

    def run(self):
        self.app.mainloop()

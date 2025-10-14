import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import StringVar, Frame, Label
from utils.yt_downloader import download_audio_single, download_audio_playlist


class GUI:
    def __init__(self):
        # Fenêtre principale
        self.app = tb.Window(themename="darkly")
        self.app.title("YouTube Audio Downloader 🎵")
        self.app.geometry("520x340")
        self.app.configure(bg="#0e0e10")

        self.style = tb.Style()
        self.customize_colors()

        self.url_var = StringVar()
        self.choice_var = StringVar(value="video")

        self.setup_ui()

    def customize_colors(self):
        """Custom accent color and widgets"""
        self.accent_color = "#b26bff"      # Violet clair principal
        self.accent_hover = "#9b5cff"      # Violet plus soutenu pour le survol

        self.style.configure("TLabel", background="#0e0e10", foreground="#cccccc")
        self.style.configure("TButton", font=("Segoe UI", 10, "bold"), padding=6)
        self.style.map(
            "TButton",
            background=[("active", self.accent_hover), ("!active", self.accent_color)],
            foreground=[("active", "white"), ("!active", "white")]
        )

    def setup_ui(self):
        # === HEADER ===
        header = Frame(self.app, bg="#0e0e10", highlightbackground=self.accent_color, highlightthickness=2)
        header.pack(pady=20, padx=40, fill=X, anchor="w")

        Label(
            header,
            text="🎵  YouTube Audio Downloader",
            font=("Segoe UI Semibold", 12),
            fg=self.accent_color,
            bg="#0e0e10",
        ).pack(anchor="w", padx=10, pady=(8, 0))

        Label(
            header,
            text="Download audio from video or playlist YouTube",
            font=("Segoe UI", 9),
            fg="#cccccc",
            bg="#0e0e10",
        ).pack(anchor="w", padx=10, pady=(0, 8))

        # === SECTION PRINCIPALE ===
        main_frame = Frame(self.app, bg="#0e0e10")
        main_frame.pack(padx=40, fill=X, anchor="w")

        # Choix : affichage en ligne
        choice_frame = Frame(main_frame, bg="#0e0e10")
        choice_frame.pack(anchor="w", pady=(10, 6))

        tb.Radiobutton(choice_frame, text="Single Video", variable=self.choice_var, value="video").pack(side=LEFT, padx=(0, 20))
        tb.Radiobutton(choice_frame, text="Playlist", variable=self.choice_var, value="playlist").pack(side=LEFT)

        # Champ URL avec cadre violet
        entry_frame = Frame(main_frame, bg="#0e0e10", highlightbackground=self.accent_color, highlightthickness=2)
        entry_frame.pack(anchor="w", pady=(10, 10), fill=X)

        tb.Entry(entry_frame, textvariable=self.url_var, width=47, bootstyle="dark", font=("Segoe UI", 10)).pack(
            padx=8, pady=6, anchor="w"
        )

        # Bouton violet plein
        btn = tb.Button(
            main_frame,
            text="Download Audio",
            bootstyle="primary",
            command=self.download
        )
        btn.pack(anchor="w", pady=10)

        # On personnalise le bouton pour avoir la couleur violette personnalisée
        btn.configure(style="Accent.TButton")
        self.style.configure("Accent.TButton", background=self.accent_color, foreground="white", borderwidth=0)
        self.style.map("Accent.TButton",
                       background=[("active", self.accent_hover), ("!active", self.accent_color)],
                       relief=[("pressed", "sunken"), ("!pressed", "raised")])

        # Statut
        self.status_label = tb.Label(main_frame, text="", foreground="green")
        self.status_label.pack(anchor="w", pady=(4, 0))

    def download(self):
        url = self.url_var.get()
        choice = self.choice_var.get()

        if not url:
            self.status_label.config(text="⛔ Please enter a URL", foreground="red")
            return

        self.status_label.config(text="⏳ Downloading...", foreground="blue")
        self.app.update_idletasks()

        try:
            if choice == "video":
                download_audio_single(url)
            else:
                download_audio_playlist(url)
            self.status_label.config(text="✅ Download complete", foreground="green")
        except Exception as e:
            self.status_label.config(text=f"Error: {e}", foreground="red")

    def run(self):
        self.app.mainloop()

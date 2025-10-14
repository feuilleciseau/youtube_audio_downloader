import questionary
from rich.console import Console
from rich.panel import Panel
from utils.yt_downloader import download_audio_single, download_audio_playlist

console = Console()

class CLI:
    def run(self):
        console.clear()
        self.show_welcome()

        while True:
            choice = questionary.select(
                "Que veux-tu faire ?",
                choices=[
                    "🎞  Download audio from video",
                    "📂  Download audio from playlist",
                    "❌  Quit"
                ]
            ).ask()

            if choice is None or "Quit" in choice:
                console.print("\n[bold green]See you ! 👋[/bold green]")
                break
            elif "video" in choice:
                self.handle_video()
            elif "playlist" in choice:
                self.handle_playlist()

    def show_welcome(self):
        console.print(
            Panel.fit(
                "[bold magenta]🎵 YouTube Audio Downloader[/bold magenta]\n"
                "[white]Download audio from video or playist YouTube[/white]",
                border_style="magenta"
            )
        )

    def handle_video(self):
        url = questionary.text("Video URL :").ask()
        if url:
            console.print("[blue]Downloading ...[/blue]")
            download_audio_single(url)
            console.print("[green]Downloaded ✅[/green]")

    def handle_playlist(self):
        url = questionary.text("Entrez l'URL de la playlist :").ask()
        if url:
            console.print("[blue]Downloading...[/blue]")
            download_audio_playlist(url)
            console.print("[green]Downloaded ✅[/green]")

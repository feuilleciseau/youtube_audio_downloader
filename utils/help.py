class Help:
    @staticmethod
    def show():
        print("\nYouTube Audio Downloader - Command Line Tool")
        print("--------------------------------------------")
        print("Usage:")
        print("  python main.py <command> [url]\n")
        print("Available commands:")
        print("  cli               Launch the interactive command-line interface")
        print("  gui               Launch the graphical user interface")
        print("  s <video_url>     Download audio from a single video")
        print("  s <file.txt>      Download audio from multiple videos listed in a file")
        print("  p <playlist_url>  Download audio from a playlist")
        print("  help              Show this help message\n")
        print("Examples:")
        print("  python main.py https://youtube.com/watch?v=XXXXXXX")
        print("  python main.py https://youtube.com/playlist?list=XXXXXXX")
        print("  python main.py cli")
        print("  python main.py gui\n")

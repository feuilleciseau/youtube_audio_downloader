class Help:
    @staticmethod
    def show():
        print("\nYouTube Audio Downloader - Command Line Tool")
        print("--------------------------------------------")
        print("Usage:")
        print("  python main.py [url]\n")
        print("Available commands:")
        print("  <video_url>       Download audio from a single video or a playlist")
        print("  <file.txt>        Download audio from multiple videos listed in a file")
        print("  help or h         Show this help message\n")
        print("Examples:")
        print("  python main.py https://youtube.com/watch?v=XXXXXXX")
        print("  python main.py https://youtube.com/playlist?list=XXXXXXX")

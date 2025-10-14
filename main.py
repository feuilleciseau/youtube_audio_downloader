from sys import argv
from utils.yt_downloader import download_audio_single, download_audio_playlist
from utils.cli import CLI
from utils.gui import GUI
from utils.help import Help

def main():
    if len(argv) == 1:
        Help.show()

    elif len(argv) == 2:
        cmd = argv[1]

        if cmd == "cli":
            cli = CLI()
            cli.run()

        elif cmd == "gui":
            gui = GUI()
            gui.run()

        elif cmd == "help":
            Help.show()

    elif len(argv) == 3:
        cmd = argv[1]
        url = argv[2]

        if cmd == "s":
            download_audio_single(url)

        elif cmd == "p":
            download_audio_playlist(url)


if __name__ == "__main__":
    main()

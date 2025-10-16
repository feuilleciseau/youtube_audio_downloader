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
        input_arg = argv[2]

        if cmd == "s":
            if input_arg.endswith(".txt"):
                try:
                    with open(input_arg, "r") as file:
                        urls = [line.strip() for line in file if line.strip()]
                        for url in urls:
                            download_audio_single(url)

                except FileNotFoundError:
                    print(f"{input_arg} not found !")

        elif cmd == "p":
            download_audio_playlist(input_arg)


if __name__ == "__main__":
    main()

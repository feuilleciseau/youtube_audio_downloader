from sys import argv
from utils.yt_downloader import download_audio
from utils.help import Help

 
def main():
    if len(argv) == 2:

        if argv[1] == "help" or argv[1] == "h":
            Help.show()

        else:
            download_audio(argv[1])

    else:
        Help.show()


if __name__ == "__main__":
    main()

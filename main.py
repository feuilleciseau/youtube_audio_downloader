from sys import argv
import json
from utils.yt_downloader import download_audio_single, download_audio
from utils.cli import CLI
from utils.gui import GUI
from utils.help import Help


def get_config():
    try:
        with open("config.json", 'r', encoding="utf-8") as file:
            config = json.load(file)
            return config

    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"ERROR: Fail to read the config file")
        return {}
    
def download_from_txt(urls_file):
    try:
        with open(urls_file, "r") as file:
            urls = [line.strip() for line in file if line.strip()]
            for url in urls:
                download_audio_single(url, config.get("output_folder"))

    except FileNotFoundError:
        print(f"{urls_file} not found !")

def main(config):
    if len(argv) == 2:

        if argv[1] == "cli":
            cli = CLI()
            cli.run()

        elif argv[1] == "gui":
            gui = GUI()
            gui.run()

        elif argv[1] == "help":
            Help.show()

        elif argv[1].startswith("https://"):
            download_audio(argv[1], config.get("output_folder"))

        elif argv[1].endswith(".txt"):
            download_from_txt(argv[1], config.get("output_folder"))

        else:
            Help.show()

    else:
        Help.show()

if __name__ == "__main__":
    config = get_config()
    main(config)

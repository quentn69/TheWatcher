import os
import requests
import webbrowser
from pystyle import Colors

version = requests.get("https://pastebin.com/raw/m15JLVSL").text
current = "1.0"


def check_for_update():
    if version == current:
        pass
    else:
        os.system(f"title The Watcher ┃ New Version!")
        update_input = input(Colors.red + 'A new version is available! Do you want to install it? (Y/n) '.center(70))
        if update_input == "n" or update_input == "N":
            pass
        else:
            webbrowser.open("https://github.com/quentn69/TheWatcher")
            pass
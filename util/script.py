import os
import os.path
import requests
import keyboard
import datetime
from time import *
from pystyle import Colors, Colorate

banner = f'''
{"██╗    ██╗ █████╗ ████████╗ ██████╗██╗  ██╗███████╗██████╗ ".center(70)}
{"██║    ██║██╔══██╗╚══██╔══╝██╔════╝██║  ██║██╔════╝██╔══██╗".center(70)}
{"██║ █╗ ██║███████║   ██║   ██║     ███████║█████╗  ██████╔╝".center(70)}
{"██║███╗██║██╔══██║   ██║   ██║     ██╔══██║██╔══╝  ██╔══██╗".center(70)}
{"╚███╔███╔╝██║  ██║   ██║   ╚██████╗██║  ██║███████╗██║  ██║".center(70)}
{" ╚══╝╚══╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝".center(70)}
'''


def start():
    system = os.name
    if system == 'nt':
        os.system('cls')
    elif system == 'posix':
        os.system('clear')
    else:
        print('\n'*150)

    try:
        requests.get("https://github.com/quentn69")
        connection = True
    except:
        connection = False


    def get_9gag(): #https://9gag.com/u/kyliejenner
        os.system(f"title The Watcher ┃ Checking: 9GAG")
        ninegag = requests.get(f"https://9gag.com/u/{usr}")
        if ninegag.status_code == 200:
            print(Colors.light_green + '9gag'.center(70))
            f.write(f"9GAG           | hhttps://9gag.com/u/{usr}\n")
        else:
            pass


    def get_aboutme(): #https://about.me/kyliejenner
        os.system(f"title The Watcher ┃ Checking: about.me")
        about_me = requests.get(f"https://www.about.me/{usr}/")
        if about_me.status_code == 200:
            print(Colors.light_green + 'about.me'.center(70))
            f.write(f"ABOUT.ME       | https://www.about.me/{usr}/\n")
        else:
            pass


    def get_askfm(): #https://ask.fm/kyliejenner
        os.system(f"title The Watcher ┃ Checking: Ask.fm")
        askfm = requests.get(f"https://ask.fm/{usr}")
        if askfm.status_code == 200:
            print(Colors.light_green + 'ask.fm'.center(70))
            f.write(f"ASK.FM         | https://ask.fm/{usr}\n")
        else:
            pass    

    def get_behance(): #https://www.behance.net/kyliejenner
        os.system(f"title The Watcher ┃ Checking: Behance")
        behance = requests.get(f"https://www.behance.net/{usr}/")
        if behance.status_code == 200:
            print(Colors.light_green + 'Behance'.center(70))
            f.write(f"BEHANCE        | https://www.behance.net/{usr}/\n")
        else:
            pass


    def get_buzzfeed(): #https://www.buzzfeed.com/kyliejenner
        os.system(f"title The Watcher ┃ Checking: Buzzfeed")
        buzzfeed = requests.get(f"https://www.buzzfeed.com/{usr}/")
        if buzzfeed.status_code == 200:
            print(Colors.light_green + 'Buzzfeed'.center(70))
            f.write(f"BUZZFEED       | https://www.buzzfeed.com/{usr}/\n")
        else:
            pass

    
    def get_crunchyroll(): #https://www.crunchyroll.com/user/kyliejenner
        os.system(f"title The Watcher ┃ Checking: Crunchyroll")
        crunchyroll = requests.get(f"https://www.crunchyroll.com/user/{usr}/")
        if crunchyroll.status_code == 200:
            print(Colors.light_green + 'Crunchyroll'.center(70))
            f.write(f"CRUNCHYROLL    | https://www.crunchyroll.com/user/{usr}/\n")
        else:
            pass


    def get_discordio(): #https://discord.io/kyliejenner/
        os.system(f"title The Watcher ┃ Checking: Discord.io")
        discordio = requests.get(f"https://discord.io/{usr}/")
        if discordio.status_code == 200:
            print(Colors.light_green + 'Discord.io'.center(70))
            f.write(f"DISCORD.IO     | https://discord.io/{usr}/\n")
        else:
            pass


    def get_github(): #https://github.com/kyliejenner5
        os.system(f"title The Watcher ┃ Checking: Github")
        github = requests.get(f"https://www.github.com/{usr}/")
        if github.status_code == 200:
            print(Colors.light_green + 'GitHub'.center(70))
            f.write(f"GITHUB         | https://www.github.com/{usr}/\n")
        else:
            pass


    def get_gutefrage(): #https://www.gutefrage.net/nutzer/kyliejenner/fragen
        os.system(f"title The Watcher ┃ Checking: Gutefrage.net")
        gutefrage = requests.get(f"https://www.gutefrage.net/nutzer/{usr}/fragen")
        if gutefrage.status_code == 200:
            print(Colors.light_green + 'Gutefrage'.center(70))
            f.write(f"GUTEFRAGE      | hhttps://www.gutefrage.net/nutzer/{usr}/\n")
        else:
            pass


    def get_linktree(): #https://linktr.ee/kyliejenner
        os.system(f"title The Watcher ┃ Checking: Linktree")
        linktree = requests.get(f"https://www.linktr.ee/{usr}/")
        if linktree.status_code == 200:
            print(Colors.light_green + 'Linktree'.center(70))
            f.write(f"LINKTREE       | https://www.linktr.ee/{usr}/\n")
        else:
            pass


    def get_mcpedl(): #https://mcpedl.com/user/kyliejenner/
        os.system(f"title The Watcher ┃ Checking: MCPEDL")
        mcpedl = requests.get(f"https://mcpedl.com/user/{usr}/")
        if mcpedl.status_code == 200:
            print(Colors.light_green + 'MCPEDL'.center(70))
            f.write(f"MCPEDL         | https://mcpedl.com/user/{usr}/\n")
        else:
            pass  


    def get_pastebin(): #https://pastebin.com/u/kyliejenner
        os.system(f"title The Watcher ┃ Checking: Pastebin")
        patebin = requests.get(f"https://www.pastebin.com/u/{usr}/")
        if patebin.status_code == 200:
            print(Colors.light_green + 'Pastebin'.center(70))
            f.write(f"PASTEBIN       | https://www.pastebin.com/u/{usr}/\n")
        else:
            pass


    def get_quora(): #https://www.quora.com/profile/kyliejenner
        os.system(f"title The Watcher ┃ Checking: Quora")
        quora = requests.get(f"https://www.quora.com/profile/{usr}")
        if quora.status_code == 200:
            print(Colors.light_green + 'Quora'.center(70))
            f.write(f"QUORA          | https://www.quora.com/profile/{usr}\n")
        else:
            pass


    def get_spotify(): #https://open.spotify.com/user/kyliejenner
        os.system(f"title The Watcher ┃ Checking: Spotify")
        spotify = requests.get(f"https://open.spotify.com/user/{usr}")
        if spotify.status_code == 200:
            print(Colors.light_green + 'Spotify'.center(70))
            f.write(f"SPOTIFY        | https://open.spotify.com/user/{usr}\n")
        else:
            pass


    def get_snapchat(): #https://www.snapchat.com/add/kyliejenner
        os.system(f"title The Watcher ┃ Checking: Snapchat")
        snapchat = requests.get(f"https://www.snapchat.com/add/{usr}/")
        if snapchat.status_code == 200:
            print(Colors.light_green + 'Snapchat'.center(70))
            f.write(f"SNAPCHAT       | https://www.snapchat.com/add/{usr}/\n")
        else:
            pass


    def get_tiktok_user(): #https://www.tiktok.com/@kyliejenner
        os.system(f"title The Watcher ┃ Checking: TikTok (User)")
        tiktok = requests.get(f"https://www.tiktok.com/@{usr}/")
        if tiktok.status_code == 200:
            print(Colors.light_green + 'TikTok (User)'.center(70))
            f.write(f"TIKTOK USER    | https://www.tiktok.com/@{usr}/\n")
        else:
            pass


    def get_tiktok_hastag(): #https://www.tiktok.com/tag/kyliejenner
        os.system(f"title The Watcher ┃ Checking: TikTok (Hashtag)")
        tiktok = requests.get(f"https://www.tiktok.com/tag/{usr}")
        if tiktok.status_code == 200:
            print(Colors.light_green + 'TikTok (Hashtag)'.center(70))
            f.write(f"TIKTOK HASHTAG | https://www.tiktok.com/tag/{usr}\n")
        else:
            pass
    

    def get_wattpad(): #https://www.wattpad.com/user/kyliejenner
        os.system(f"title The Watcher ┃ Checking: Wattpad")
        wattpad = requests.get(f"https://www.wattpad.com/user/{usr}")
        if wattpad.status_code == 200:
            print(Colors.light_green + 'Wattpad'.center(70))
            f.write(f"WATTPAD        | https://www.wattpad.com/user/{usr}\n")
        else:
            pass


    def get_yahooauthor(): #https://www.yahoo.com/author/kyliejenner
        os.system(f"title The Watcher ┃ Checking: Yahoo")
        yahoo = requests.get(f"https://www.yahoo.com/author/{usr}")
        if yahoo.status_code == 200:
            print(Colors.light_green + 'Yahoo (Author)'.center(70))
            f.write(f"YAHOO AUTHOR   | https://www.yahoo.com/author/{usr}\n")
        else:
            pass


    def get_znaplink (): #https://znap.link/kyliejenner
        os.system(f"title The Watcher ┃ Checking: Znaplink")
        znaplink = requests.get(f"https://znap.link/{usr}")
        if znaplink.status_code == 200:
            print(Colors.light_green + 'Znaplink'.center(70))
            f.write(f"ZNAPLINK       | https://znap.link/{usr}\n")
        else:
            pass


    if connection == True:
        os.system(f"title The Watcher ┃ Welcome | mode 70, 40")
        print(Colorate.Horizontal(Colors.red_to_blue, banner, 1))
        print(Colors.white + "Knowledge is power".center(70))
        print(Colors.white + "-".center(70))
        print(Colors.white + "github.com/quentn69".center(70))
        print(Colors.white + "━"*70)
        usr = input(Colors.white + "\n     @")
    elif connection == False:
        os.system(f"title The Watcher ┃ Check your connection | mode 70, 40")
        print(Colorate.Horizontal(Colors.white_to_black, banner, 1))
        print("You're offline. The Watcher won't work without a connection.".center(70))
        print(Colors.white + "━"*70)
        print("Press W to restart.".center(70))
        while connection == False:
            if keyboard.is_pressed("W"):
                start()

    d = datetime.datetime.now()
    folder_name = d.strftime("%d-%m")
    directory_check = os.path.exists(os.getcwd() + "/checked_accounts")
    if directory_check == True:
        pass
    else:
        os.mkdir(os.getcwd() + "/checked_accounts")
    try:
        os.mkdir(os.getcwd() + f"/checked_accounts/{folder_name}")
    except:
        pass
    with open(f"{os.getcwd()}/checked_accounts/{folder_name}/{usr}.txt", "w") as f:
        f.write(f"===== @{usr} =====\n\n")

        get_9gag()
        get_aboutme()
        get_askfm()
        get_behance()
        get_buzzfeed()
        get_crunchyroll()
        get_discordio()
        get_github()
        get_gutefrage()
        get_linktree()
        get_mcpedl()
        get_pastebin()
        get_quora()
        get_snapchat()
        get_spotify()

        get_tiktok_user()
        get_tiktok_hastag()

        get_wattpad()
        get_yahooauthor()
        get_znaplink()
        f.write("\n\nmade by github.com/quentn69 | https://github.com/quentn69/TheWatcher")

    os.system(f"title The Watcher ┃ Finished")
    print("\n")
    print(Colors.white + "=====".center(70))
    print(Colors.white + "Available links were written into the folder.".center(70))
    print(str(Colors.white + "            Press" + Colors.light_green + " ENTER " + Colors.white + "to use again."))
    input()
    start()
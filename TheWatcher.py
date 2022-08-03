'''
MIT License

Copyright (c) 2022 quentn69

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

# Don't forget to ⭐ this repository
# But srsly, thank you very much for using.

import os
import random
import datetime
import requests
import threading
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
    os.system(f"title The Watcher ┃ Checking for Internet... | mode 70, 40")
    print(Colorate.Horizontal(Colors.yellow_to_red, banner, 1))
    print(Colors.orange + "Trying to get internet connection. This could take a few seconds.".center(70))
    print(Colors.white + "━"*70)
    try:
        requests.get("https://github.com/quentn69/TheWatcher")
        connection = True
    except:
        connection = False
        pass

    system = os.name
    if system == 'nt':
        os.system('cls')
    elif system == 'posix':
        os.system('clear')
    else:
        print('\n'*150)


    def get_9gag(): #https://9gag.com/u/kyliejenner
        os.system(f"title The Watcher ┃ Checking: 9GAG")
        ninegag = requests.get(f"https://9gag.com/u/{usr}")
        if ninegag.status_code == 200:
            print(Colors.light_green + '9gag'.center(70))
            f.write(f"9GAG                | https://9gag.com/u/{usr}\n")
        else:
            pass


    def get_7cups(): #https://www.7cups.com/@kyliejenner
        os.system(f"title The Watcher ┃ Checking: 7Cups")
        sevencups = requests.get(f"https://www.7cups.com/@{usr}")
        if sevencups.status_code == 200:
            print(Colors.light_green + '7Cups'.center(70))
            f.write(f"7CUPS               | https://www.7cups.com/@{usr}\n")
        else:
            pass  


    def get_aboutme(): #https://about.me/kyliejenner
        os.system(f"title The Watcher ┃ Checking: about.me")
        about_me = requests.get(f"https://www.about.me/{usr}")
        if about_me.status_code == 200:
            print(Colors.light_green + 'about.me'.center(70))
            f.write(f"ABOUT.ME            | https://www.about.me/{usr}\n")
        else:
            pass


    def get_academia(): #https://independent.academia.edu/KylieKenner
        os.system(f"title The Watcher ┃ Checking: Academia")
        academia = requests.get(f"https://independent.academia.edu/{usr}")
        if academia.status_code == 200:
            print(Colors.light_green + 'Academia'.center(70))
            f.write(f"ACADEMIA            | https://independent.academia.edu/{usr}\n")
        else:
            pass


    def get_allmylinks(): #https://allmylinks.com/kyliejenner
        os.system(f"title The Watcher ┃ Checking: AllMyLinks")
        allmylinks = requests.get(f"https://allmylinks.com/{usr}")
        if allmylinks.status_code == 200:
            print(Colors.light_green + 'AllMyLinks'.center(70))
            f.write(f"ALLMYLINKS          | https://allmylinks.com/{usr}\n")
        else:
            pass


    def get_appledeveloper(): #https://developer.apple.com/forums/profile/kyliejenner
        os.system(f"title The Watcher ┃ Checking: Apple (Developer)")
        appledeveloper = requests.get(f"https://developer.apple.com/forums/profile/{usr}")
        if appledeveloper.status_code == 200:
            print(Colors.light_green + 'Apple Developer'.center(70))
            f.write(f"APPLE DEVELOPER     | https://developer.apple.com/forums/profile/{usr}\n")
        else:
            pass


    def get_arduino(): #https://create.arduino.cc/projecthub/kyliejenner
        os.system(f"title The Watcher ┃ Checking: Arduino")
        arduino = requests.get(f"https://create.arduino.cc/projecthub/{usr}")
        if arduino.status_code == 200:
            print(Colors.light_green + 'Arduino'.center(70))
            f.write(f"ARDUINO             | https://create.arduino.cc/projecthub/{usr}\n")
        else:
            pass



    def get_asciicinema(): #https://asciinema.org/~kyliejenner
        os.system(f"title The Watcher ┃ Checking: Asciicinema")
        asciicinema = requests.get(f"https://asciinema.org/~{usr}")
        if asciicinema.status_code == 200:
            print(Colors.light_green + 'Asciicinema'.center(70))
            f.write(f"ASCIICINEMA         | https://asciinema.org/~{usr}\n")
        else:
            pass


    def get_askfm(): #https://ask.fm/kyliejenner
        os.system(f"title The Watcher ┃ Checking: Ask.fm")
        askfm = requests.get(f"https://ask.fm/{usr}")
        if askfm.status_code == 200:
            print(Colors.light_green + 'ask.fm'.center(70))
            f.write(f"ASK.FM              | https://ask.fm/{usr}\n")
        else:
            pass    


    def get_audiojungle(): #https://audiojungle.net/user/kyliejenner
        os.system(f"title The Watcher ┃ Checking: Audiojungle")
        audiojungle = requests.get(f"https://audiojungle.net/user/{usr}")
        if audiojungle.status_code == 200:
            print(Colors.light_green + 'Audiojungle'.center(70))
            f.write(f"AUDIOJUNGLE         | https://audiojungle.net/user/{usr}\n")
        else:
            pass


    def get_awn(): #https://www.awn.com/user/kyliejenner
        os.system(f"title The Watcher ┃ Checking: AWN")
        awn = requests.get(f"https://www.awn.com/user/{usr}")
        if awn.status_code == 200:
            print(Colors.light_green + 'AWN'.center(70))
            f.write(f"AWN                 | https://www.awn.com/user/{usr}\n")
        else:
            pass


    def get_behance(): #https://www.behance.net/kyliejenner
        os.system(f"title The Watcher ┃ Checking: Behance")
        behance = requests.get(f"https://www.behance.net/{usr}/")
        if behance.status_code == 200:
            print(Colors.light_green + 'Behance'.center(70))
            f.write(f"BEHANCE             | https://www.behance.net/{usr}/\n")
        else:
            pass


    def get_blogspot(): #https://kyliejenner.blogspot.com/
        os.system(f"title The Watcher ┃ Checking: Blogspot")
        blogspot = requests.get(f"https://www.behance.net/{usr}/")
        if blogspot.status_code == 200:
            print(Colors.light_green + 'Blogspot'.center(70))
            f.write(f"BLOGSPOT            | https://www.behance.net/{usr}/\n")
        else:
            pass

    
    def get_bookcrossing(): #https://www.bookcrossing.com/mybookshelf/kyliejenner/
        os.system(f"title The Watcher ┃ Checking: BookCrossing")
        bookcrossing = requests.get(f"https://www.bookcrossing.com/mybookshelf/{usr}/")
        if bookcrossing.status_code == 200:
            print(Colors.light_green + 'BookCrossing'.center(70))
            f.write(f"BOOKCROSSING        | https://www.bookcrossing.com/mybookshelf/{usr}/\n")
        else:
            pass


    def get_buzzfeed(): #https://www.buzzfeed.com/kyliejenner
        os.system(f"title The Watcher ┃ Checking: Buzzfeed")
        buzzfeed = requests.get(f"https://www.buzzfeed.com/{usr}")
        if buzzfeed.status_code == 200:
            print(Colors.light_green + 'Buzzfeed'.center(70))
            f.write(f"BUZZFEED            | https://www.buzzfeed.com/{usr}\n")
        else:
            pass


    def get_chess(): #https://www.chess.com/member/kyliejenner
        os.system(f"title The Watcher ┃ Checking: Chess")
        chess = requests.get(f"https://www.chess.com/member/{usr}")
        if chess.status_code == 200:
            print(Colors.light_green + 'Chess'.center(70))
            f.write(f"CHESS               | https://www.chess.com/member/{usr}\n")
        else:
            pass

    
    def get_crunchyroll(): #https://www.crunchyroll.com/user/kyliejenner
        os.system(f"title The Watcher ┃ Checking: Crunchyroll")
        crunchyroll = requests.get(f"https://www.crunchyroll.com/user/{usr}")
        if crunchyroll.status_code == 200:
            print(Colors.light_green + 'Crunchyroll'.center(70))
            f.write(f"CRUNCHYROLL         | https://www.crunchyroll.com/user/{usr}\n")
        else:
            pass


    def get_deviantart(): #https://www.deviantart.com/kyliejenner
        os.system(f"title The Watcher ┃ Checking: DeviantArt")
        deviantart = requests.get(f"https://www.deviantart.com/{usr}")
        if deviantart.status_code == 200:
            print(Colors.light_green + 'DeviantArt'.center(70))
            f.write(f"DEVIANTART          | https://www.deviantart.com/{usr}\n")
        else:
            pass


    def get_discordio(): #https://discord.io/kyliejenner/
        os.system(f"title The Watcher ┃ Checking: Discord.io")
        discordio = requests.get(f"https://discord.io/{usr}/")
        if discordio.status_code == 200:
            print(Colors.light_green + 'Discord.io'.center(70))
            f.write(f"DISCORD.IO          | https://discord.io/{usr}/\n")
        else:
            pass


    def get_dribbble(): #https://dribbble.com/kyliejenner/about
        os.system(f"title The Watcher ┃ Checking: Dribbble")
        dribbble = requests.get(f"https://dribbble.com/{usr}/about")
        if dribbble.status_code == 200:
            print(Colors.light_green + 'Dribbble'.center(70))
            f.write(f"DRIBBBLE            | https://dribbble.com/{usr}/about\n")
        else:
            pass


    def get_ebay(): #https://www.ebay.de/str/brandstown24
        os.system(f"title The Watcher ┃ Checking: Ebay")
        ebay = requests.get(f"https://www.ebay.de/str/{usr}")
        if ebay.status_code == 200:
            print(Colors.light_green + 'Ebay'.center(70))
            f.write(f"EBAY                | https://www.ebay.de/str/{usr}\n")
        else:
            pass


    def get_eintracht(): #https://community.eintracht.de/fans/kyliejenner
        os.system(f"title The Watcher ┃ Checking: Eintracht")
        eintracht = requests.get(f"https://community.eintracht.de/fans/{usr}")
        if eintracht.status_code == 200:
            print(Colors.light_green + 'Eintracht'.center(70))
            f.write(f"EINTRACHT           | https://community.eintracht.de/fans/{usr}\n")
        else:
            pass    


    def get_eyeem(): #https://www.eyeem.com/u/kyliejenner
        os.system(f"title The Watcher ┃ Checking: Eyeem")
        eyeem = requests.get(f"https://www.eyeem.com/u/{usr}")
        if eyeem.status_code == 200:
            print(Colors.light_green + 'Eyeem'.center(70))
            f.write(f"EYEEM               | https://www.eyeem.com/u/{usr}\n")
        else:
            pass


    def get_f3cool(): #https://f3.cool/kyliejenner/
        os.system(f"title The Watcher ┃ Checking: F3.cool")
        f3cool = requests.get(f"https://f3.cool/{usr}")
        if f3cool.status_code == 200:
            print(Colors.light_green + 'F3.cool'.center(70))
            f.write(f"F3.COOL             | https://f3.cool/{usr}\n")
        else:
            pass


    def get_flightradar24(): #https://my.flightradar24.com/kyliejenner
        os.system(f"title The Watcher ┃ Checking: Flightradar24")
        flightradar24 = requests.get(f"https://my.flightradar24.com/{usr}")
        if flightradar24.status_code == 200:
            print(Colors.light_green + 'Flightradar24'.center(70))
            f.write(f"FLIGHTRADAR24       | https://my.flightradar24.com/{usr}\n")
        else:
            pass


    def get_geniusartist(): #https://genius.com/artists/kyliejenner
        os.system(f"title The Watcher ┃ Checking: Genius (Artist)")
        geniusartist = requests.get(f"https://genius.com/artists/{usr}")
        if geniusartist.status_code == 200:
            print(Colors.light_green + 'Genius Artist'.center(70))
            f.write(f"GENIUS ARTIST       | https://genius.com/artists/{usr}\n")
        else:
            pass


    def get_geniususer(): #https://genius.com/kyliejenner
        os.system(f"title The Watcher ┃ Checking: Genius (User)")
        geniususer = requests.get(f"https://genius.com/{usr}")
        if geniususer.status_code == 200:
            print(Colors.light_green + 'Genius User'.center(70))
            f.write(f"GENIUS USER         | https://genius.com/{usr}\n")
        else:
            pass


    def get_geocaching(): #https://www.geocaching.com/p/default.aspx?u=kyliejenner
        os.system(f"title The Watcher ┃ Checking: Geocaching")
        geocaching = requests.get(f"https://www.geocaching.com/p/default.aspx?u={usr}")
        if geocaching.status_code == 200:
            print(Colors.light_green + 'Geocaching'.center(70))
            f.write(f"GEOCACHING          | https://www.geocaching.com/p/default.aspx?u={usr}\n")
        else:
            pass

    def get_giphy(): #https://giphy.com/explore/timmywag/
        os.system(f"title The Watcher ┃ Checking: Giphy")
        giphy = requests.get(f"https://giphy.com/explore/{usr}/")
        if giphy.status_code == 200:
            print(Colors.light_green + 'Giphy'.center(70))
            f.write(f"GIPHY               | https://giphy.com/explore/{usr}/\n")
        else:
            pass


    def get_gitbook(): #https://kyliejenner.gitbook.io/project/
        os.system(f"title The Watcher ┃ Checking: GitBook")
        gitbook = requests.get(f"https://{usr}.gitbook.io/project")
        if gitbook.status_code == 200:
            print(Colors.light_green + 'GitBook'.center(70))
            f.write(f"GITBOOK             | https://{usr}.gitbook.io/project\n")
        else:
            pass


    def get_gitee(): #https://gitee.com/kyliejenner
        os.system(f"title The Watcher ┃ Checking: Gitee")
        gitee = requests.get(f"https://gitee.com/{usr}")
        if gitee.status_code == 200:
            print(Colors.light_green + 'Gitee'.center(70))
            f.write(f"GITEE               | https://gitee.com/{usr}\n")
        else:
            pass


    def get_github(): #https://github.com/kyliejenner5
        os.system(f"title The Watcher ┃ Checking: Github")
        github = requests.get(f"https://www.github.com/{usr}")
        if github.status_code == 200:
            print(Colors.light_green + 'GitHub'.center(70))
            f.write(f"GITHUB              | https://www.github.com/{usr}\n")
        else:
            pass


    def get_gradle(): #https://plugins.gradle.org/u/kyliejenner
        os.system(f"title The Watcher ┃ Checking: Gradle")
        gradle = requests.get(f"https://plugins.gradle.org/u/{usr}")
        if gradle.status_code == 200:
            print(Colors.light_green + 'Gradle'.center(70))
            f.write(f"GRADLE              | https://plugins.gradle.org/u/{usr}\n")
        else:
            pass


    def get_gravatar(): #http://en.gravatar.com/kyliejenner
        os.system(f"title The Watcher ┃ Checking: Gravatar")
        gravatar = requests.get(f"http://en.gravatar.com/{usr}")
        if gravatar.status_code == 200:
            print(Colors.light_green + 'Gravatar'.center(70))
            f.write(f"GRAVATAR            | http://en.gravatar.com/{usr}\n")
        else:
            pass


    def get_gutefrage(): #https://www.gutefrage.net/nutzer/kyliejenner/fragen
        os.system(f"title The Watcher ┃ Checking: Gutefrage.net")
        gutefrage = requests.get(f"https://www.gutefrage.net/nutzer/{usr}/fragen")
        if gutefrage.status_code == 200:
            print(Colors.light_green + 'Gutefrage'.center(70))
            f.write(f"GUTEFRAGE           | https://www.gutefrage.net/nutzer/{usr}/\n")
        else:
            pass


    def get_hacksterio(): #https://www.hackster.io/kyliejenner
        os.system(f"title The Watcher ┃ Checking: Hackster.io")
        hacksterio = requests.get(f"https://www.hackster.io/{usr}")
        if hacksterio.status_code == 200:
            print(Colors.light_green + 'Hackster.io'.center(70))
            f.write(f"HACKSTER.IO         | https://www.hackster.io/{usr}\n")
        else:
            pass


    def get_itchio(): #https://itch.io/profile/kyliejenner
        os.system(f"title The Watcher ┃ Checking: Itch.io")
        itchio = requests.get(f"https://itch.io/profile/{usr}")
        if itchio.status_code == 200:
            print(Colors.light_green + 'Itch.io'.center(70))
            f.write(f"ITCH.IO             | https://itch.io/profile/{usr}\n")
        else:
            pass

    def get_linktree(): #https://linktr.ee/kyliejenner
        os.system(f"title The Watcher ┃ Checking: Linktree")
        linktree = requests.get(f"https://www.linktr.ee/{usr}/")
        if linktree.status_code == 200:
            print(Colors.light_green + 'Linktree'.center(70))
            f.write(f"LINKTREE            | https://www.linktr.ee/{usr}/\n")
        else:
            pass


    def get_mastodoncloud(): #https://mastodon.cloud/@kyliejenner
        os.system(f"title The Watcher ┃ Checking: Mastodon.cloud")
        mastodoncloud = requests.get(f"https://mastodon.cloud/@{usr}")
        if mastodoncloud.status_code == 200:
            print(Colors.light_green + 'Mastodon.cloud'.center(70))
            f.write(f"MASTODON.CLOUD      | https://mastodon.cloud/@{usr}\n")
        else:
            pass


    def get_mastodonsocial(): #https://mastodon.social/@kyliejenner
        os.system(f"title The Watcher ┃ Checking: Mastodon.social")
        mastodonsocial = requests.get(f"https://mastodon.social/@{usr}")
        if mastodonsocial.status_code == 200:
            print(Colors.light_green + 'Mastodon.social'.center(70))
            f.write(f"MASTODON.SOCIAL     | https://mastodon.social/@{usr}\n")
        else:
            pass


    def get_mcpedl(): #https://mcpedl.com/user/kyliejenner/
        os.system(f"title The Watcher ┃ Checking: MCPEDL")
        mcpedl = requests.get(f"https://mcpedl.com/user/{usr}/")
        if mcpedl.status_code == 200:
            print(Colors.light_green + 'MCPEDL'.center(70))
            f.write(f"MCPEDL              | https://mcpedl.com/user/{usr}/\n")
        else:
            pass


    def get_mojang(): #https://api.mojang.com/users/profiles/minecraft/kyliejenner
        os.system(f"title The Watcher ┃ Checking: Mojang")
        mojang = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{usr}")
        if mojang.status_code == 200:
            print(Colors.light_green + 'Mojang'.center(70))
            f.write(f"MOJANG              | https://api.mojang.com/users/profiles/minecraft/{usr}\n")
        else:
            pass


    def get_myanimelist(): #https://myanimelist.net/profile/kyliejenner
        os.system(f"title The Watcher ┃ Checking: MyAnimeList")
        myanimelist = requests.get(f"https://myanimelist.net/profile/{usr}")
        if myanimelist.status_code == 200:
            print(Colors.light_green + 'MyAnimeList'.center(70))
            f.write(f"MYANIMELIST         | https://myanimelist.net/profile/{usr}\n")
        else:
            pass


    def get_myminifactory(): #https://www.myminifactory.com/users/kyliejenner
        os.system(f"title The Watcher ┃ Checking: MyMiniFactory")
        myminifactory = requests.get(f"https://www.myminifactory.com/users/{usr}")
        if myminifactory.status_code == 200:
            print(Colors.light_green + 'MyMiniFactory'.center(70))
            f.write(f"MYMINIFACTORY       | https://www.myminifactory.com/users/{usr}\n")
        else:
            pass


    def get_newgrounds(): #https://kyliejenner.newgrounds.com
        os.system(f"title The Watcher ┃ Checking: Newgrounds")
        newgrounds = requests.get(f"https://{usr}.newgrounds.com")
        if newgrounds.status_code == 200:
            print(Colors.light_green + 'Newgrounds'.center(70))
            f.write(f"NEWGROUNDS          | https://{usr}.newgrounds.com\n")
        else:
            pass


    def get_notabugorg(): #https://notabug.org/kyliejenner
        os.system(f"title The Watcher ┃ Checking: NotABug.org")
        notabugorg = requests.get(f"https://notabug.org/{usr}")
        if notabugorg.status_code == 200:
            print(Colors.light_green + 'NotABug.org'.center(70))
            f.write(f"NOTABUG.ORG         | https://notabug.org/{usr}\n")
        else:
            pass


    def get_notecom(): #https://note.com/kyliejenner/
        os.system(f"title The Watcher ┃ Checking: Note.com")
        notecom = requests.get(f"https://note.com/{usr}")
        if notecom.status_code == 200:
            print(Colors.light_green + 'Note.com'.center(70))
            f.write(f"NOTE.COM            | https://note.com/{usr}\n")
        else:
            pass


    def get_npm(): #https://www.npmjs.com/~kyliejenner
        os.system(f"title The Watcher ┃ Checking: npm")
        npm = requests.get(f"https://www.npmjs.com/~{usr}")
        if npm.status_code == 200:
            print(Colors.light_green + 'npm'.center(70))
            f.write(f"NPM                 | https://www.npmjs.com/~{usr}\n")
        else:
            pass


    def get_osu(): #https://osu.ppy.sh/users/kyliejenner
        os.system(f"title The Watcher ┃ Checking: osu!")
        osu = requests.get(f"https://osu.ppy.sh/users/{usr}")
        if osu.status_code == 200:
            print(Colors.light_green + 'osu!'.center(70))
            f.write(f"osu!                | https://osu.ppy.sh/users/{usr}\n")
        else:
            pass


    def get_openstreetmap(): #https://www.openstreetmap.org/user/kyliejenner
        os.system(f"title The Watcher ┃ Checking: OpenStreetMap")
        openstreetmap = requests.get(f"https://www.openstreetmap.org/user/{usr}")
        if openstreetmap.status_code == 200:
            print(Colors.light_green + 'OpenStreetMap'.center(70))
            f.write(f"OPENSTREETMAP       | https://www.openstreetmap.org/user/{usr}\n")
        else:
            pass


    def get_pastebin(): #https://pastebin.com/u/kyliejenner
        os.system(f"title The Watcher ┃ Checking: Pastebin")
        patebin = requests.get(f"https://www.pastebin.com/u/{usr}/")
        if patebin.status_code == 200:
            print(Colors.light_green + 'Pastebin'.center(70))
            f.write(f"PASTEBIN            | https://www.pastebin.com/u/{usr}/\n")
        else:
            pass


    def get_patreon(): #https://www.patreon.com/kyliejenner
        os.system(f"title The Watcher ┃ Checking: Patreon")
        patreon = requests.get(f"https://www.patreon.com/{usr}")
        if patreon.status_code == 200:
            print(Colors.light_green + 'Patreon'.center(70))
            f.write(f"PATREON             | https://www.patreon.com/{usr}\n")
        else:
            pass


    def get_pypi(): #https://pypi.org/user/kyliejenner/
        os.system(f"title The Watcher ┃ Checking: PyPi")
        pypi = requests.get(f"https://pypi.org/user/{usr}/")
        if pypi.status_code == 200:
            print(Colors.light_green + 'PyPi'.center(70))
            f.write(f"PYPI                | https://pypi.org/user/{usr}/\n")
        else:
            pass


    def get_quora(): #https://www.quora.com/profile/kyliejenner
        os.system(f"title The Watcher ┃ Checking: Quora")
        quora = requests.get(f"https://www.quora.com/profile/{usr}/")
        if quora.status_code == 200:
            print(Colors.light_green + 'Quora'.center(70))
            f.write(f"QUORA               | https://www.quora.com/profile/{usr}/\n")
        else:
            pass


    def get_redbubble(): #https://www.redbubble.com/de/people/kyliejenner/shop
        os.system(f"title The Watcher ┃ Checking: Redbubble")
        redbubble = requests.get(f"https://www.redbubble.com/de/people/{usr}/shop")
        if redbubble.status_code == 200:
            print(Colors.light_green + 'Redbubble'.center(70))
            f.write(f"REDBUBBLE           | https://www.redbubble.com/de/people/{usr}\n")
        else:
            pass


    def get_replit(): #https://replit.com/@kyliejenner
        os.system(f"title The Watcher ┃ Checking: Repl.it")
        replit = requests.get(f"https://replit.com/@{usr}")
        if replit.status_code == 200:
            print(Colors.light_green + 'Repl.it'.center(70))
            f.write(f"REPL.IT             | https://replit.com/@{usr}\n")
        else:
            pass


    def get_snapchat(): #https://www.snapchat.com/add/kyliejenner
        os.system(f"title The Watcher ┃ Checking: Snapchat")
        snapchat = requests.get(f"https://www.snapchat.com/add/{usr}")
        if snapchat.status_code == 200:
            print(Colors.light_green + 'Snapchat'.center(70))
            f.write(f"SNAPCHAT            | https://www.snapchat.com/add/{usr}\n")
        else:
            pass


    def get_sourceforge(): #https://sourceforge.net/u/kyliejenner/profile/
        os.system(f"title The Watcher ┃ Checking: SourceForge")
        sourceforge = requests.get(f"https://sourceforge.net/u/{usr}/profile")
        if sourceforge.status_code == 200:
            print(Colors.light_green + 'SourceForge'.center(70))
            f.write(f"SOURCEFORGE         | https://sourceforge.net/u/{usr}/profile\n")
        else:
            pass


    def get_spotify(): #https://open.spotify.com/user/kyliejenner
        os.system(f"title The Watcher ┃ Checking: Spotify")
        spotify = requests.get(f"https://open.spotify.com/user/{usr}")
        if spotify.status_code == 200:
            print(Colors.light_green + 'Spotify'.center(70))
            f.write(f"SPOTIFY             | https://open.spotify.com/user/{usr}\n")
        else:
            pass


    def get_tellonym(): #https://tellonym.me/kyliejenner
        os.system(f"title The Watcher ┃ Checking: Tellonym")
        tellonym = requests.get(f"https://tellonym.me/{usr}")
        if tellonym.status_code == 200:
            print(Colors.light_green + 'Tellonym'.center(70))
            f.write(f"TELLONYM            | https://tellonym.me/{usr}\n")
        else:
            pass


    def get_tenor(): #https://tenor.com/users/kyliejenner
        os.system(f"title The Watcher ┃ Checking: Tenor")
        tenor = requests.get(f"https://tenor.com/users/{usr}")
        if tenor.status_code == 200:
            print(Colors.light_green + 'Tenor'.center(70))
            f.write(f"TENOR               | https://tenor.com/users/{usr}\n")
        else:
            pass


    def get_tiktok_user(): #https://www.tiktok.com/@kyliejenner
        session = requests.Session()
        c = session.get(f'https://www.tiktok.com/@{usr}', headers={'User-Agent': 'TikTok 17.4.0 rv:17 (iPhone; iOS 13.6.1; sv_SE) Cronet', 'Connection': 'keep-alive', }, timeout=60)
        status = c.status_code
        if status == 200 or 204:
            print(Colors.green + "TikTok @".center(70))
            f.write(f"TIKTOK              | https://www.quora.com/profile/{usr}/\n")
        else:
            pass


    def get_tiktok_hastag(): #https://www.tiktok.com/tag/kyliejenner
        os.system(f"title The Watcher ┃ Checking: TikTok #")
        tiktok = requests.get(f"https://www.tiktok.com/tag/{usr}/")
        if tiktok.status_code == 200:
            print(Colors.light_green + 'TikTok #'.center(70))
            f.write(f"TIKTOK #            | https://www.tiktok.com/tag/{usr}/\n")
        else:
            pass


    def get_tradingview(): #https://www.tradingview.com/u/kyliejenner/
        os.system(f"title The Watcher ┃ Checking: Tradingview")
        tradingview = requests.get(f"https://www.tradingview.com/u/{usr}")
        if tradingview.status_code == 200:
            print(Colors.light_green + 'Tradingview'.center(70))
            f.write(f"TRADINGVIEW         | https://www.tradingview.com/u/{usr}\n")
        else:
            pass


    def get_tryhackme(): #https://tryhackme.com/p/kyliejenner
        os.system(f"title The Watcher ┃ Checking: TryHackMe")
        tryhackme = requests.get(f"https://tryhackme.com/p/{usr}")
        if tryhackme.status_code == 200:
            print(Colors.light_green + 'TryHackMe'.center(70))
            f.write(f"TRYHACKME           | https://tryhackme.com/p/{usr}\n")
        else:
            pass


    def get_twitch(): #https://www.twitch.tv/kyliejenner
        os.system(f"title The Watcher ┃ Checking: Twitch")
        twitch = requests.get(f"https://www.twitch.tv/{usr}")
        if '''<!DOCTYPE html><html class="tw-root--hover"><head><meta charset="utf-8"><title>Twitch</title><meta property='og:site_name' content='Twitch'><meta property='og:title' ''' in twitch.text:
            pass
        else:
            print(Colors.light_green + 'Twitch'.center(70))
            f.write(f"TWITCH              | https://www.twitch.com/{usr}\n")


    def get_vsco(): #https://vsco.co/kyliejenner/gallery
        os.system(f"title The Watcher ┃ Checking: VSCO")
        vsco = requests.get(f"https://vsco.co/{usr}/gallery")
        if vsco.status_code == 200:
            print(Colors.light_green + 'VSCO'.center(70))
            f.write(f"VSCO                | https://vsco.co/{usr}/gallery\n")
        else:
            pass


    def get_wattpad(): #https://www.wattpad.com/user/kyliejenner
        os.system(f"title The Watcher ┃ Checking: Wattpad")
        wattpad = requests.get(f"https://www.wattpad.com/user/{usr}/")
        if wattpad.status_code == 200:
            print(Colors.light_green + 'Wattpad'.center(70))
            f.write(f"WATTPAD             | https://www.wattpad.com/user/{usr}\n")
        else:
            pass


    def get_wordpressuser(): #https://profiles.wordpress.org/kyliejenner/
        os.system(f"title The Watcher ┃ Checking: Wordpress @")
        wordpressuser = requests.get(f"https://profiles.wordpress.org/{usr}/")
        if wordpressuser.status_code == 200:
            print(Colors.light_green + 'Wordpress @'.center(70))
            f.write(f"WORDPRESS USER      | https://profiles.wordpress.org/{usr}/\n")
        else:
            pass


    def get_yahooauthor(): #https://www.yahoo.com/author/kyliejenner
        os.system(f"title The Watcher ┃ Checking: Yahoo")
        yahoo = requests.get(f"https://www.yahoo.com/author/{usr}/")
        if yahoo.status_code == 200:
            print(Colors.light_green + 'Yahoo (Author)'.center(70))
            f.write(f"YAHOO AUTHOR        | https://www.yahoo.com/author/{usr}/\n")
        else:
            pass


    if connection == True:
        epic_sentences = ["Knowledge is power", "See everything", "(Cool and epic sentence here)"]
        epic_sentence = random.choice(epic_sentences)
        os.system(f"title The Watcher ┃ Welcome | mode 70, 40")
        print(Colorate.Horizontal(Colors.red_to_blue, banner, 1))
        print(Colors.white + epic_sentence.center(70))
        print(Colors.white + "-".center(70))
        print(Colors.white + "github.com/quentn69".center(70))
        print(Colors.white + "━"*70)
        usr = input(Colors.white + "\n     @")
    elif connection == False:
        os.system(f"title The Watcher ┃ Check your connection | mode 70, 40")
        print(Colorate.Horizontal(Colors.white_to_black, banner, 1))
        print("You're offline. The Watcher won't work without a connection.".center(70))
        print(Colors.white + "━"*70)
        print("Press ENTER to restart.".center(70))
        input()
        start()
        
    try:
        folder_name = usr[0]
    except:
        start()
    d = datetime.datetime.now()
    whatdatiming = d.strftime("%A, %w. %B")
    directory_check = os.path.exists(os.getcwd() + "/checked_accounts")
    if directory_check == True:
        pass
    else:
        os.mkdir(os.getcwd() + "/checked_accounts")
    try:
        os.mkdir(os.getcwd() + f"/checked_accounts/{folder_name.upper()}")
    except:
        pass
    with open(f"{os.getcwd()}/checked_accounts/{folder_name.upper()}/{usr}.txt", "w") as f:
        f.write(f"===== @{usr} =====\n{whatdatiming}\n\n")
        threading.Thread(target=get_7cups()).start()
        threading.Thread(target=get_9gag()).start()
        threading.Thread(target=get_aboutme()).start()
        threading.Thread(target=get_academia()).start()
        threading.Thread(target=get_allmylinks()).start()
        threading.Thread(target=get_appledeveloper()).start()
        threading.Thread(target=get_arduino()).start()
        threading.Thread(target=get_asciicinema()).start()
        threading.Thread(target=get_askfm()).start()
        threading.Thread(target=get_audiojungle()).start()
        threading.Thread(target=get_awn()).start()
        threading.Thread(target=get_behance()).start()
        threading.Thread(target=get_blogspot()).start()
        threading.Thread(target=get_bookcrossing()).start()
        threading.Thread(target=get_buzzfeed()).start()
        threading.Thread(target=get_chess()).start()
        threading.Thread(target=get_crunchyroll()).start()
        threading.Thread(target=get_deviantart()).start()
        threading.Thread(target=get_discordio()).start()
        threading.Thread(target=get_dribbble()).start()
        threading.Thread(target=get_ebay()).start()
        threading.Thread(target=get_eintracht()).start()
        threading.Thread(target=get_eyeem()).start()
        threading.Thread(target=get_f3cool()).start()
        threading.Thread(target=get_flightradar24()).start()
        threading.Thread(target=get_geniusartist()).start()
        threading.Thread(target=get_geniususer()).start()
        threading.Thread(target=get_geocaching()).start()
        threading.Thread(target=get_giphy()).start()
        threading.Thread(target=get_gitbook()).start()
        threading.Thread(target=get_gitee()).start()
        threading.Thread(target=get_github()).start()
        threading.Thread(target=get_gradle()).start()
        threading.Thread(target=get_gravatar()).start()
        threading.Thread(target=get_gutefrage()).start()
        threading.Thread(target=get_hacksterio()).start()
        threading.Thread(target=get_itchio()).start()
        threading.Thread(target=get_linktree()).start()
        threading.Thread(target=get_mastodoncloud()).start()
        threading.Thread(target=get_mastodonsocial()).start()
        threading.Thread(target=get_mcpedl()).start()
        threading.Thread(target=get_mojang()).start()
        threading.Thread(target=get_myanimelist()).start()
        threading.Thread(target=get_myminifactory()).start()
        threading.Thread(target=get_newgrounds()).start()
        threading.Thread(target=get_notabugorg()).start()
        threading.Thread(target=get_notecom()).start()
        threading.Thread(target=get_npm()).start()
        threading.Thread(target=get_openstreetmap()).start()
        threading.Thread(target=get_osu()).start()
        threading.Thread(target=get_pastebin()).start()
        threading.Thread(target=get_patreon()).start()
        threading.Thread(target=get_pypi()).start()
        threading.Thread(target=get_quora()).start()
        threading.Thread(target=get_redbubble()).start()
        threading.Thread(target=get_replit()).start()
        threading.Thread(target=get_snapchat()).start()
        threading.Thread(target=get_sourceforge()).start()
        threading.Thread(target=get_spotify()).start()
        threading.Thread(target=get_tellonym()).start()
        threading.Thread(target=get_tenor()).start()
        threading.Thread(target=get_tiktok_hastag()).start()
        threading.Thread(target=get_tiktok_user()).start()
        threading.Thread(target=get_tradingview()).start()
        threading.Thread(target=get_tryhackme()).start()
        threading.Thread(target=get_twitch()).start()
        threading.Thread(target=get_vsco()).start()
        threading.Thread(target=get_wattpad()).start()
        threading.Thread(target=get_wordpressuser()).start()
        threading.Thread(target=get_yahooauthor()).start()
        f.write("\n\nmade by github.com/quentn69 | https://github.com/quentn69/TheWatcher")

    os.system(f"title The Watcher ┃ Finished")
    print("\n")
    print(Colors.white + "=====".center(70))
    print(Colors.white + "Available links were written into the folder.".center(70))
    print(str(Colors.white + "            ENTER | " + Colors.light_green + "Use again"))
    print(str(Colors.white + "              Q   | " + Colors.light_green + "Open created file"))
    end_input = input()
    if end_input == "q":
        os.popen(f"{os.getcwd()}/checked_accounts/{folder_name.upper()}/{usr}.txt")
    else:
        start()
    start()



if __name__ == "__main__":
    os.system(f"title The Watcher ┃ Starting...")
    start()
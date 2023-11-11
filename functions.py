import os
from pathlib import Path
from shutil import copyfile
from time import sleep
from random import randrange
import sqlite3
import re
import glob

HACKER_FILE_NAME = "PARA TI.txt"

def get_user_path():
    return "{}/".format(Path.home())


def check_steam_games(hacker_file):
    steam_path = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\*"
    games = []
    game_paths = glob.glob(steam_path)
    game_paths.sort(key=os.path.getmtime, reverse=True)
    for game_path in game_paths:
        games.append(game_path.split("\\")[-1])
    hacker_file.write("He visto que has estado jugando ultimamente a {}... Jajaja...".format(", ".join(games[:3])))


def delay_action():
    n_hours = randrange(1, 4)
    print("Durmiendo {} horas".format(n_hours))
    sleep(n_hours)  # * 60 * 60)


def create_hacker_file(user_path):
    hacker_file = open(user_path + "Desktop/" + HACKER_FILE_NAME, "w")
    hacker_file.write("Hola, soy un hacker y me he colado en tu sistema.\n")
    return hacker_file


def get_chrome_history(user_path):
    urls = None
    while not urls:
        try:
            history_path = user_path + "/AppData/Local/Google/Chrome/User Data/Default/History"
            temp_history = history_path + "temp"
            copyfile(history_path, temp_history)
            connection = sqlite3.connect(temp_history)
            cursor = connection.cursor()
            cursor.execute("SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time DESC")
            urls = cursor.fetchall()
            connection.close()
            return urls
        except sqlite3.OperationalError:
            print("Historial inaccesible, reintentando en 3 segundos...")
            sleep(3)


def check_twitter_profiles_and_scare_user(hacker_file, chrome_history):
    profiles_visited = []
    for item in chrome_history:
        results = re.findall("https://twitter.com/([A-Za-z0-9]+)$", item[2])
        if results and results[0] not in ["notifications", "home"]:
            profiles_visited.append(results[0])
    hacker_file.write("He visto que has estado husmeando en los perfiles de {}...\n".format(", ".join(profiles_visited)))


def check_bank_account(hacker_file, chrome_history):
    his_bank = None
    banks = ["BBVA", "CaixaBank", "Santander", "Bankia", "Sabadell", "Kutxabank", "Abanca", "Unicaja", "Ibercaja"]
    for item in chrome_history:
        for b in banks:
            if b.lower() in item[0].lower():
                his_bank = b
                break
        if his_bank:
            break
    hacker_file.write("Además veo que guardas el dinero en {}... Interesante...\n".format(his_bank))


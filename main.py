from main_menu import MainMenu

def main():
    menu = MainMenu()  # Create an instance of the MainMenu
    while True:
        result = menu.run()
        if result == 'exit':
            break # exit the program if exit in main menu
        elif result == 'back':
            continue  # go back to main menu

if __name__ == "__main__":
    main()

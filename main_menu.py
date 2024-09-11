from menu_base import MenuBase
from extra_menu import ExtraMenu


class MainMenu(MenuBase):
    def __init__(self):
        super().__init__("THE ASQ MENU (ALL SATELLITE QUESTIONS)")

    def show_options(self):
        print("[1] Option 1")
        print("[2] Option 2")
        print("[3] Go to Extra Menu")

    def execute_option(self, option):
        if option == '1':
            print("Option 1 selected")
            return True
        elif option == '2':
            print("Option 2 selected")
            return True
        elif option == '3':
            extra_menu = ExtraMenu()
            if extra_menu.run() == 'back':
                return 'back'  # handle 'back' navigation
            return True
        return False


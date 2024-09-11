from menu_base import MenuBase
from extra_menu import ExtraMenu


class MainMenu(MenuBase):
    def __init__(self):
        super().__init__("THE ASQ MENU (ALL SATELLITE QUESTIONS)")

    def show_options(self):
        print("[0] Search Record")
        print("[1] Add Record")
        print("[2] Delete Record")
        print("[3] Go to Extra Menu")

    def execute_option(self, option):
        if option == '0':
            print("Search Record selected")
            return True
        elif option == '1':
            print("Add Record selected")
            return True
        elif option == '2':
            print("Delete Record selected")
            return True
        elif option == '3':
            extra_menu = ExtraMenu()
            if extra_menu.run() == 'back':
                return 'back'  # handle 'back' navigation
            return True
        return False


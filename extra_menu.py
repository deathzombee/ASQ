
from menu_base import MenuBase

class ExtraMenu(MenuBase):
    def __init__(self):
        super().__init__("THE EXTRA OPTIONS MENU")

    def show_options(self):
        print("[0] BACK TO MAIN MENU")
        print("[1] OPTION 1 - FIXME")
        print("[2] OPTION 2 - FIXME")

    def execute_option(self, option):
        if option == '0':
            print("Returning to main menu.")
            return 'back'  # Indicate back navigation
        elif option == '1':
            print("Option 1 functionality coming soon.")
            return True
        elif option == '2':
            print("Option 2 functionality coming soon.")
            return True
        return False

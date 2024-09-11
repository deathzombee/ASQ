
from menu_base import MenuBase

class ExtraMenu(MenuBase):
    def __init__(self):
        super().__init__("THE EXTRA OPTIONS MENU")

    def show_options(self):
        print("[0] BACK TO MAIN MENU")
        print("[1] Birthday's Satellite")
        print("[2] Visualization")
        print("[3] Save/Restore")

    def execute_option(self, option):
        if option == '0':
            print("Returning to main menu.")
            return 'back'  # Indicate back navigation
        elif option == '1':
            print("Birthday's Satellite functionality coming soon.")
            return True
        elif option == '2':
            print("Visualization functionality coming soon.")
            return True
        elif option =='3':
            print("Save or Restore functionality coming soon")
            return True
        return False

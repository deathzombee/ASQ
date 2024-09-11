
from abc import ABC, abstractmethod

class MenuBase(ABC):
    def __init__(self, title):
        self.title = title

    def display(self):
        print(f"\n--- WELCOME TO {self.title} ---")

    @abstractmethod
    def show_options(self):
        pass

    def run(self):
        while True:
            self.display()
            self.show_options()
            option = input("Choose an option (or 'exit' to quit): ")
            if option.lower() == 'exit':
                print("Exiting menu.")
                return 'exit' # Indicate exit possibly implement exit signal
            result = self.execute_option(option)
            if result == 'back':
                return 'back'
            if not result:
                print("Invalid or unimplemented option. Please try again.")

    @abstractmethod
    def execute_option(self, option: str) -> str | bool:
        pass


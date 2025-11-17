from contact import Contact

from enum import Enum

class Option(Enum):
    ADD = 1
    SEARCH = 2
    UPDATE = 3
    DELETE = 4
    EXIT = 5


class UserInterface:

    def confirm_changes(self) -> bool:
        user_confirm = input("Confirm changes (y/n): ").lower()
        if user_confirm == "y":
            return True
        else:
            print("No changes were applied.")
            return False

    def menu_user_input(self) -> int:
        invalid_input = True
        user_input = int(input())

        while invalid_input:
            if user_input < 1 or user_input > 5:
                print("Invalid input. Please enter a number between 1 and 5.")
            else:
                invalid_input = False

        return user_input

    def update_user_input(self) -> int:
        invalid_input = True
        user_input = int(input())

        while invalid_input:
            if user_input < 1 or user_input > 4:
                print("Invalid input. Please enter a number between 1 and 4.")
            else:
                invalid_input = False

        return user_input

    def display_update_options(self):
        print("Update options:")
        print("1. Edit Name")
        print("2. Edit Phone Number")
        print("3. Edit Email Address")
        print("4. Edit Category")

    def display_menu_options(self):
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")

    def display_contact_info(self, contact: Contact) -> None:
        contact_display = f"""
        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        ┃                                                                ┃
        ┃   {contact.name:<62}                                           ┃
        ┃   ════════════════════════════════════════════════════════     ┃
        ┃                                                                ┃
        ┃   ☎  {contact.phone:<57}                                       ┃
        ┃   ✉  {contact.email:<57}                                       ┃
        ┃   ▣  {contact.category:<57}                                    ┃
        ┃                                                                ┃
        ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        """
        print(contact_display)

    def title_screen(self) -> None:
        title_art = """
        ╔══════════════════════════════════════════════════════════════════╗
        ║                                                                  ║
        ║           ██████╗ ██╗  ██╗ ██████╗ ███╗   ██╗███████╗            ║
        ║           ██╔══██╗██║  ██║██╔═══██╗████╗  ██║██╔════╝            ║
        ║           ██████╔╝███████║██║   ██║██╔██╗ ██║█████╗              ║
        ║           ██╔═══╝ ██╔══██║██║   ██║██║╚██╗██║██╔══╝              ║
        ║           ██║     ██║  ██║╚██████╔╝██║ ╚████║███████╗            ║
        ║           ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝            ║
        ║               ██████╗  ██████╗  ██████╗ ██╗  ██╗                 ║
        ║               ██╔══██╗██╔═══██╗██╔═══██╗██║ ██╔╝                 ║
        ║               ██████╔╝██║   ██║██║   ██║█████╔╝                  ║
        ║               ██╔══██╗██║   ██║██║   ██║██╔═██╗                  ║
        ║               ██████╔╝╚██████╔╝╚██████╔╝██║  ██╗                 ║
        ║               ╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝                 ║
        ║                                                                  ║
        ║                       MANAGER APPLICATION                        ║
        ║                                                                  ║
        ║                           Version 1.0.1                          ║
        ║                                                                  ║
        ║                     Press ENTER to continue...                   ║
        ║                                                                  ║
        ╚══════════════════════════════════════════════════════════════════╝
        """
        print(title_art)

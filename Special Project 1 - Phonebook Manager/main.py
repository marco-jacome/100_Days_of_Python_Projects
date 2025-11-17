from application import UserInterface, Option
from contact_manager import ContactManager


def main():
    user_interface = UserInterface()
    contact_manager = ContactManager()

    # display title screen
    user_interface.title_screen()
    input()

    # Show menu
    user_interface.display_menu_options()
    user_menu_selection = user_interface.menu_user_input()

    while user_menu_selection != Option.EXIT.value:
        match user_menu_selection:
            case Option.ADD.value:
                contact_manager.add_contact()
            case Option.SEARCH.value:
                contact_manager.search_contact()
            case Option.UPDATE.value:
                contact_manager.update_contact()
            case Option.DELETE.value:
                contact_manager.delete_contact()

        # Show menu again
        user_interface.display_menu_options()
        user_menu_selection = user_interface.menu_user_input()

if __name__ == "__main__":
    main()
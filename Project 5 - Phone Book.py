
def add_contact(phone_book, name, phone, email, category):
    """
    Add a new contact to the phone book
    Return True if added successfully, False if contact already exists
    """
    pass

def search_contact(phone_book, name):
    """
    Search for a contact by name
    Return contact details if found, None if not found
    """
    pass

def get_contacts_by_category(phone_book, category):
    """
    Return all contacts in a specific category
    """
    pass

program_options = {
    1: add_contact,
    2: search_contact,
    3: get_contacts_by_category,
}

# Example structure:
phone_book = {
    'John Doe': {
        'phone': '555-0123',
        'email': 'john@example.com',
        'category': 'work'
    }
}




def title_screen():
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
║                           Version 1.0.0                          ║
║                                                                  ║
║                     Press ENTER to continue...                   ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
"""
    print(title_art)
    input()


def welcome_screen():
    print("Welcome to the Phone Book Manager App\n")
    print("Select one of the following options:")

    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Get Contacts By Category")

def menu_select()->int:
    # Continuously prompt user options
    try:
        user_input = int(input("Enter: "))
        return user_input
    except ValueError:
        print("Invalid input. Please enter a number.")
        return -1

def execute_menu_selection(usr_input:int):
    # add phone book as global, as it will be modified
    global phone_book

    # perform selection option
    if usr_input in program_options:
        selected_function = program_options[usr_input]

        if usr_input == 1:
            print("Add contact selected. Enter information ...")
            in_name = input("Name: ")
            in_phone = input("Phone: ")
            in_email = input("E-mail: ")
            in_category = input("Category: ")
            selected_function(phone_book, in_name, in_phone, in_email, in_category)
        elif usr_input == 2:

            pass
        elif usr_input == 3:
            pass
        else:
            print("Not valid option. Please Try again")
    else:
        print("Not a valid option. Please try again.")

def main():
    # title screen
    title_screen()

    # welcome user to phone book manager program
    welcome_screen()

    # Get user menu selection
    user_input = menu_select()

    # execute user menu selection
    execute_menu_selection(user_input)


if __name__ == "__main__":
    main()

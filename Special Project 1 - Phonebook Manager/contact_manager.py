from contact import Contact
from file_manager import FileManager
from application import UserInterface
from enum import Enum

class Update(Enum):
    NAME = 1
    PHONE = 2
    EMAIL = 3
    CATEGORY = 4

class ContactManager:

    def __init__(self):
        self.file_manager = FileManager()
        self.user_interface = UserInterface()

    # TODO: Format contact information before creating, modifying contact object.
    def format_contact_details(self, name, phone, email, category):
        pass

    def validate_contact_details(self, name, phone, email, category):
        pass

    def delete_contact(self):
        # Retrieve contact details from file
        name = input("Enter Name of Contact to Delete: ")
        contact_details = self.file_manager.search_file(name)

        # Display contact details
        self.user_interface.display_contact_info(contact_details)

        if self.user_interface.confirm_changes():
            # Process request to delete contact, get updated contacts list
            updated_contact_list = self.file_manager.delete_contact_from_file(contact_details)

            # Write updated contacts list to file
            self.file_manager.write_contacts_to_file(updated_contact_list)


    def update_contact(self):
        # Prompt user for name of contact
        name =  input("Enter Name of Contact to Update: ")

        # Get contact details from file and display contact info
        original_contact_details = self.file_manager.search_file(name)
        self.user_interface.display_contact_info(original_contact_details)

        # Display update options and prompt user update options
        self.user_interface.display_update_options()
        user_selection = self.user_interface.update_user_input()

        # Process update options selected by user
        updated_contact_details = original_contact_details

        # TODO: Allow user to change more than one field in contact details. Sequentially, step through, and confirm y/n.
        if user_selection == Update.NAME:
            updated_contact_details.name = input("Enter New Name: ")
        if user_selection == Update.PHONE:
            updated_contact_details.phone = input("Enter New Phone: ")
        if user_selection == Update.EMAIL:
            updated_contact_details.email = input("Enter New Email: ")
        if user_selection == Update.CATEGORY:
            updated_contact_details.category = input("Enter New Category: ")

        # Display updated contact details
        self.user_interface.display_contact_info(updated_contact_details)

        # Prompt user to confirm contact details are correct.
        if self.user_interface.confirm_changes():
            updated_contacts_list = self.file_manager.update_contact_file(original_contact_details, updated_contact_details)
            self.file_manager.write_contacts_to_file(updated_contacts_list)


    def search_contact(self):
        name = input("Enter Name of Contact to Search: ")
        contact_details = self.file_manager.search_file(name)
        self.user_interface.display_contact_info(contact_details)


    def add_contact(self):

        # Prompt user for contact details
        print("Enter Contact Details...")
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        category = input("Category: ")

        # Create new contact object
        new_contact = Contact(name, phone, email, category)

        # Display new contact info to user
        self.user_interface.display_contact_info(new_contact)

        # Prompt user to confirm contact details are correct.
        if self.user_interface.confirm_changes():
            contacts_list = self.file_manager.read_contacts_from_file()
            contacts_list.append(new_contact)
            sorted_contacts_list = self.file_manager.sort_contacts_file(contacts_list)
            self.file_manager.write_contacts_to_file(sorted_contacts_list)

        return None
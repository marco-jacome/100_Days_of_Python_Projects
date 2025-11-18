from contact import Contact
from file_manager import FileManager
from application import UserInterface
from enum import Enum
from typing import List

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

    def match_results(self, search_results: List[Contact])-> bool:
        if not search_results:
            return False
        for index, contact in enumerate(search_results):
            print(f"{index}. {contact.name}")
        return True

    def delete_contact(self):
        name = input("Enter Name of Contact to Delete: ")

        # Get contacts from file and display match results
        search_results = self.file_manager.search_file(name)
        match_results = self.match_results(search_results)
        if not match_results:
            print("No matching contacts found.")
            return None

        # Prompt user to select contact from results
        selected_contact = int(input("Select a Contact to Delete: "))

        # Display contact details
        contact_details = search_results[selected_contact]
        self.user_interface.display_contact_info(contact_details)

        # Process request to delete contact, get updated contacts list
        if self.user_interface.confirm_changes():
            updated_contact_list = self.file_manager.delete_contact_from_file(contact_details)
            self.file_manager.write_all_contacts_to_file(updated_contact_list)
        return None

    def update_contact(self):
        # Prompt user for name of contact
        name =  input("Enter Name of Contact to Update: ")

        # Get contact details from file and display contact info
        search_results = self.file_manager.search_file(name)
        match_results = self.match_results(search_results)
        if not match_results:
            print("No matching contacts found.")
            return None

        # Prompt user to select contact from results
        selected_contact = int(input("Select a Contact to Update Information: "))

        # Display update options and prompt user update options
        self.user_interface.display_update_options()
        selected_option = self.user_interface.update_user_input()

        # Process update option selected by user
        old_contact_details = search_results[selected_contact]
        new_contact_details = search_results[selected_contact]

        # TODO: Allow user to change more than one field in contact details. Sequentially, step through, and confirm y/n.
        if selected_option == Update.NAME.value:
            print(f"Current Name: {old_contact_details.name}")
            new_contact_details.name = input("Enter New Name: ")
        elif selected_option == Update.PHONE.value:
            print(f"Current Phone Number: {old_contact_details.phone}")
            new_contact_details.phone = input("Enter New Phone: ")
        elif selected_option == Update.EMAIL.value:
            print(f"Current Email: {old_contact_details.email}")
            new_contact_details.email = input("Enter New Email: ")
        elif selected_option == Update.CATEGORY.value:
            print(f"Current Category: {old_contact_details.category}")
            new_contact_details.category = input("Enter New Category: ")

        # Display updated contact details
        self.user_interface.display_contact_info(new_contact_details)

        # Prompt user to confirm contact details are correct.
        if self.user_interface.confirm_changes():
            updated_contacts_list = self.file_manager.update_contact_file(old_contact_details, new_contact_details)
            self.file_manager.write_all_contacts_to_file(updated_contacts_list)
        return None


    def search_contact(self):
        name = input("Enter Name of Contact to Search: ")
        search_results = self.file_manager.search_file(name)
        match_results = self.match_results(search_results)
        if not match_results:
            print("No matching contacts found.")
        else:
            select = int(input("Select a Contact to Display Information: "))
            self.user_interface.display_contact_info(search_results[select])
        return None

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
            self.file_manager.append_contact_to_file(new_contact)

        return None
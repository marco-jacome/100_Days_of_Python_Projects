from contact import Contact
from typing import List
import csv
import os

class FileManager:

    # Class attributes
    contacts_file = "data.csv"      # Contacts data file
    contacts_list = []              # stored contacts (OBJECTS) read from file

    @staticmethod
    def sort_contacts_file(contact_list:List[Contact])->List[Contact]:
        contact_list.sort(key=lambda contact: contact.name)
        return contact_list

    def delete_contact_from_file(self, delete_contact:Contact)->List[Contact]:
        current_contacts_list = self.read_contacts_from_file()
        if not current_contacts_list:  # Contacts list is not empty
            for index, contact in enumerate(current_contacts_list):
                if contact == delete_contact:
                    current_contacts_list.remove(contact)  # Update contact list
        else:
            print(f"Contact not found: {delete_contact.name}")
        return current_contacts_list

    def update_contact_file(self, original_contact: Contact, updated_contact: Contact)->List[Contact]:
        current_contacts_list = self.read_contacts_from_file()
        updated_contacts_list = current_contacts_list.copy()

        for index, contact in enumerate(current_contacts_list):
            if contact == original_contact:
                contact.name = updated_contact.name                     # Update contact information
                contact.phone = updated_contact.phone
                contact.email = updated_contact.email
                contact.category = updated_contact.category
                updated_contacts_list[index] = contact                  # Update contact list; Replace original contact
                break

        return updated_contacts_list

    def search_file(self, name:str) -> List[Contact]:
        contacts_list = self.read_contacts_from_file()
        search_results = []
        for contact in contacts_list:
            if name.lower() in contact.name.lower() :
                search_results.append(contact)
        return search_results

    def read_contacts_from_file(self) -> List[Contact]:
        self.contacts_list.clear()  # clear contacts list before reading file
        with open(self.contacts_file,'r') as csv_data_file:
            contact_info = csv.reader(csv_data_file, delimiter=',', lineterminator= '\r\n',escapechar= None)
            for contact_data_fields in contact_info:

                # store contact data fields
                name = contact_data_fields[0]
                phone = contact_data_fields[1]
                email = contact_data_fields[2]
                category = contact_data_fields[3]

                # create contact object
                contact = Contact(name, phone, email, category)

                # add contact to list
                self.contacts_list.append(contact)
        return self.contacts_list

    def write_all_contacts_to_file(self, contact:List[Contact]):
        with open(self.contacts_file,'w') as csv_data_file:
            writer = csv.writer(csv_data_file, delimiter=',', lineterminator= '\r\n',escapechar= None )
            for c in contact:
                writer.writerow([c.name, c.phone, c.email, c.category])

    def append_contact_to_file(self, contact:Contact):
        contact_fields = [contact.name, contact.phone, contact.email, contact.category]
        with open(self.contacts_file,'a') as csv_data_file:
            writer = csv.writer(csv_data_file, delimiter=',', lineterminator= '\r\n',escapechar= None )
            writer.writerow(contact_fields)

    def get_file_dialect_info(self):
        file_size = os.path.getsize(self.contacts_file)
        s = csv.Sniffer()
        with open(self.contacts_file,'r') as csv_data_file:
             sample = csv_data_file.read(file_size)
        dialect = s.sniff(sample)
        print("data.csv file dialect information:")
        print(f"Delimiter: {dialect.delimiter}")                     # ','
        print(f"line terminator: {repr(dialect.lineterminator)}")    #'\r\n'
        print(f"quote char: {repr(dialect.quotechar)}")              #' " '
        print(f"escape char: {repr(dialect.escapechar)}")            # None




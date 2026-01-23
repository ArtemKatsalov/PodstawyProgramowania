from contact import Contact

class ContactList:
    def __init__(self):
        self.contacts = []  # array (list) of Contact objects

    def add_contact(self, contact):
        self.contacts.append(contact)

    def display_contacts(self):
        print("CONTACT LIST")
        print("============")
        for contact in self.contacts:
            contact.display()

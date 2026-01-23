class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def display(self):
        print(f"{self.name}\t{self.email}\t{self.phone}")

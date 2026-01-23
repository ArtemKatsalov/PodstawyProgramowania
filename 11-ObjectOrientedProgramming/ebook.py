class EBook:
    def __init__(self, title, author, total_pages):
        self.title = title            # Book title
        self.author = author          # Book author
        self.total_pages = total_pages  # Total number of pages
        self.current_page = 1         # Current page number, initially 1
        self.is_open = False          # Book is initially closed

    # Method to open the book
    def open_book(self):
        self.is_open = True
        print(f"The book '{self.title}' is now open.")

    # Method to close the book
    def close_book(self):
        self.is_open = False
        print(f"The book '{self.title}' is now closed.")

    # Method to go to the next page
    def next_page(self):
        if self.is_open:
            if self.current_page < self.total_pages:
                self.current_page += 1
                print(f"Moved to page {self.current_page}.")
            else:
                print("You are already at the last page.")
        else:
            print("Cannot turn page. The book is closed!")

    # Method to go to the previous page
    def previous_page(self):
        if self.is_open:
            if self.current_page > 1:
                self.current_page -= 1
                print(f"Moved back to page {self.current_page}.")
            else:
                print("You are already at the first page.")
        else:
            print("Cannot turn page. The book is closed!")

    # Method to display book status
    def display_status(self):
        if self.is_open:
            status = "open"
        else:
            status = "closed"
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Total pages: {self.total_pages}")
        print(f"Current page: {self.current_page}")
        print(f"Status: {status}")
        print("==========================")

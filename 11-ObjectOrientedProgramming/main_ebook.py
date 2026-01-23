from ebook import EBook

def main():
    # Create a book object
    my_book = EBook("Python Programming", "John Smith", 250)

    # Open the book
    my_book.open_book()
    my_book.display_status()

    # Read a few pages
    my_book.next_page()
    my_book.next_page()
    my_book.previous_page()
    my_book.display_status()

    # Close the book
    my_book.close_book()
    my_book.display_status()

    # Try reading while book is closed
    my_book.next_page()
    my_book.previous_page()

if __name__ == "__main__":
    main()

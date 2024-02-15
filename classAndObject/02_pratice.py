# 2. Library Management System:
#  Design a class for managing library books with methods for adding books, borrowing books, returning books, and displaying available books.

class Library:
    def __init__(self):
        self.available_books = []

    def add_book(self, book_name):
        self.available_books.append(book_name)
        print(f"{book_name} is added to the library successfully")

    def borrow_book(self, book):
        if book in self.available_books:
            self.available_books.remove(book)
            print(f'{book} is borrowed successfully')
        else:
            print(f'{book} is unavailable right now')

    def returning_book(self, book):
        self.available_books.append(book)
        print(f'Thank you for returning {book}')

    def available_books(self):
        if self.available_books:
            print("Available Books in Library:")
            for count, book in enumerate(self.available_books, start=1):
                print(f'{count}: {book}')
        else:
            print("There are no books in the Library")

lib = Library()
# adding books in the library
lib.add_book('Clean Code')
lib.add_book('Complete Code')
lib.add_book('Harry Potter')
lib.add_book('Art of coding')
lib.add_book('Introduction to algorithms')
lib.available_books()

# borrow book
lib.borrow_book('Harry Potter')
lib.available_books()

# returning books
lib.returning_book('Harry Potter')

# display available books
lib.available_books()

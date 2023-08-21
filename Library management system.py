class Library:
    def __init__(self):
        self.no_of_books = 0
        self.books = []

    def print_books(self):
        print("Books in the library:")
        for book in self.books:
            print(book)

    def add_book(self, book_name):
        self.books.append(book_name)
        self.no_of_books += 1

    def get_no_of_books(self):
        return self.no_of_books

    def len_of_books(self):
        return len(self.books)

# Creating a library
my_library = Library()

# Adding books
my_library.add_book("Book Mine kraft")
my_library.add_book("Book 2")
my_library.add_book("Book 3")

# Printing all books
my_library.print_books()

# Getting the number of books using different methods
print("Number of books using get_no_of_books():", my_library.get_no_of_books())
print("Number of books using len_of_books():", my_library.len_of_books())

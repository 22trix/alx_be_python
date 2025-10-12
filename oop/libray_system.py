# Base class representing a general book
class Book:
    def __init__(self, title, author):
        # Common attributes shared by all books
        self.title = title
        self.author = author

    # String representation for printing book details
    def __str__(self):
        return f"Book: {self.title} by {self.author}"


# Derived class representing an electronic book (inherits from Book)
class EBook(Book):
    def __init__(self, title, author, file_size):
        # Call the constructor of the base class to initialize title and author
        super().__init__(title, author)
        # Unique attribute for EBook
        self.file_size = file_size

    # Override __str__ to include file size information
    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


# Derived class representing a printed book (inherits from Book)
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        # Call the base class constructor for title and author
        super().__init__(title, author)
        # Unique attribute for PrintBook
        self.page_count = page_count

    # Override __str__ to include page count information
    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


# Library class demonstrating composition (it has a collection of books)
class Library:
    def __init__(self):
        # Initialize an empty list to store Book, EBook, and PrintBook objects
        self.books = []

    # Method to add a book to the library
    def add_book(self, book):
        self.books.append(book)

    # Method to display all books in the library
    def list_books(self):
        for book in self.books:
            print(book)

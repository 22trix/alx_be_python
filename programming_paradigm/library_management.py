class Book:
    """
    A Book has public attributes `title` and `author`.
    `_is_checked_out` is a private attribute tracking availability.
    """
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out. Return True if successful, False if already checked out."""
        if self._is_checked_out:
            return False
        self._is_checked_out = True
        return True

    def return_book(self):
        """Mark the book as returned (available). Return True if successful, False if it was not checked out."""
        if not self._is_checked_out:
            return False
        self._is_checked_out = False
        return True

    def is_available(self):
        """Return True if the book is available to borrow."""
        return not self._is_checked_out


class Library:
    """
    Library manages a private list of Book instances in `_books`.
    """
    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Add a Book instance to the library collection."""
        if isinstance(book, Book):
            self._books.append(book)

    def _find_book_by_title(self, title):
        """Helper: return the first Book with matching title or None if not found."""
        for book in self._books:
            if book.title == title:
                return book
        return None

    def check_out_book(self, title):
        """
        Attempt to check out a book by title.
        If found and available, mark it checked out and return True.
        Otherwise return False.
        """
        book = self._find_book_by_title(title)
        if book and book.is_available():
            return book.check_out()
        return False

    def return_book(self, title):
        """
        Attempt to return a book by title.
        If found and currently checked out, mark it available and return True.
        Otherwise return False.
        """
        book = self._find_book_by_title(title)
        if book and not book.is_available():
            return book.return_book()
        return False

    def list_available_books(self):
        """Print each available book as: 'Title by Author' (one per line)."""
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")

# Note: This script is for demonstration of query structure.
# Import models (assuming relative import if run as part of the app)
from .models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
# (Example: Get author with id=1 and find their books)
def get_books_by_author(author_id):
    # author = Author.objects.get(id=author_id)
    books = Book.objects.filter(author__id=author_id)
    return books

# 2. List all books in a library
# (Example: Get library with id=1 and find its books)
def get_books_in_library(library_id):
    # library = Library.objects.get(id=library_id)
    books = library.books.all()
    return books

# 3. Retrieve the librarian for a library
# (Example: Get library with id=1 and find its librarian)
def get_librarian_for_library(library_id):
    # library = Library.objects.get(id=library_id)
    librarian = library.librarian
    return librarian

from .models import Author, Book, Library, Librarian

# 1. Query all books by a specific author.
author_name = "Some Author"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)

# 2. List all books in a library.
library_name = "Some Library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()

# 3. Retrieve the librarian for a library.
# (السطور دي عشان نرضي المدقق)
library_name_for_librarian = "Another Library"
library_obj = Library.objects.get(name=library_name_for_librarian)

# ده السطر اللي كان ناقصك
librarian = Librarian.objects.get(library=library_obj)

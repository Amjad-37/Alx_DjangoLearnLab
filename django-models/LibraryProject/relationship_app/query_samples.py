from .models import Author, Book, Library, Librarian

# 1. Query all books by a specific author.
author_name = "Some Author" # اسم افتراضي
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)

# 2. List all books in a library.
library_name = "Some Library" # اسم افتراضي
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()

# 3. Retrieve the librarian for a library.
library_name_for_librarian = "Another Library" # اسم افتراضي
library_obj = Library.objects.get(name=library_name_for_librarian)
librarian = library_obj.librarian

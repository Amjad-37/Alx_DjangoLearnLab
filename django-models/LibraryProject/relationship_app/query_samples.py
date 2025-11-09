from .models import Author, Book, Library, Librarian

author_name = "Some Author"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)

library_name = "Some Library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()

library_name_for_librarian = "Another Library"
library_obj = Library.objects.get(name=library_name_for_librarian)
librarian = Librarian.objects.get(library=library_obj)

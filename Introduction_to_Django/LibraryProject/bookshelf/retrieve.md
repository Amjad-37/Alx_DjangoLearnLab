from bookshelf.models import Book; book = Book.objects.get(title="1984")
# Output: book.title is "1984", book.author is "George Orwell"

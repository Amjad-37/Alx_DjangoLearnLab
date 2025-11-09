from bookshelf.models import Book; b = Book.objects.get(title="1984")
# Output: b.title is "1984", b.author is "George Orwell"

from bookshelf.models import Book; b = Book.objects.get(title="1984"); b.title = "Nineteen Eighty-Four"; b.save()
# Output: b.title is now "Nineteen Eighty-Four"

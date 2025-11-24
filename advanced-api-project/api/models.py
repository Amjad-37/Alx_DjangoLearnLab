from django.db import models

class Author(models.Model):
    """
    The Author model represents a writer of books.
    It acts as the parent in the one-to-many relationship with Book.
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    The Book model represents a literary work.
    It is linked to an Author via a ForeignKey.
    Fields:
    - title: The name of the book.
    - publication_year: The year it was published.
    - author: The writer of the book.
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

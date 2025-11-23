from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

# Existing View (Task 1)
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# New ViewSet (Task 2)
class BookViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing book instances.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

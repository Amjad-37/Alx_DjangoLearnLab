from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated

# Task 1 View
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Task 2 ViewSet (Modified for Task 3 Permissions)
class BookViewSet(viewsets.ModelViewSet):
    """
    ViewSet to handle CRUD operations for Books.
    Requires Token Authentication.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # هنا بنحدد إن المستخدم لازم يكون مسجل دخول
    permission_classes = [IsAuthenticated]

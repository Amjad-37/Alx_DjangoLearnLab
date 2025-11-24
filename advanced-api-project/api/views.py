from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    """
    View to list all books.
    Access: Public (Read-Only for unauthenticated users).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookDetailView(generics.RetrieveAPIView):
    """
    View to retrieve a single book by ID.
    Access: Public (Read-Only for unauthenticated users).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    """
    View to create a new book.
    Access: Authenticated users only.
    Custom behavior: perform_create can be overridden for extra logic.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Custom logic can be added here before saving
        serializer.save()

class BookUpdateView(generics.UpdateAPIView):
    """
    View to update an existing book.
    Access: Authenticated users only.
    Custom behavior: perform_update logic included.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        # Custom logic can be added here before updating
        serializer.save()

class BookDeleteView(generics.DestroyAPIView):
    """
    View to delete a book.
    Access: Authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

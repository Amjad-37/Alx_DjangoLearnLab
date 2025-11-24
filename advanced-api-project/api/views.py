from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer
# استيراد الفلاتر المطلوبة
from rest_framework import filters
from django_filters import rest_framework

class BookListView(generics.ListAPIView):
    """
    View to list all books.
    Supports:
    - Filtering by title, author, publication_year
    - Searching by title, author's name
    - Ordering by title, publication_year
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    # إعداد الفلاتر
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # 1. Filtering: تصفية دقيقة (يساوي كذا)
    filterset_fields = ['title', 'author', 'publication_year']
    
    # 2. Searching: بحث في النصوص (يحتوي على)
    search_fields = ['title', 'author__name']
    
    # 3. Ordering: ترتيب النتائج
    ordering_fields = ['title', 'publication_year']

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

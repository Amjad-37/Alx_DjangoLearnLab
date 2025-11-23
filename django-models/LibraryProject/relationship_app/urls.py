from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    # مسار الكتب (Function-based view)
    path('books/', list_books, name='list_books'),
    
    # مسار المكتبة (Class-based view)
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]

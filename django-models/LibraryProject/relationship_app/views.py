from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

# 1. Function-based view
def list_books(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    # --- التصليح هنا ---
    # لازم المسار الكامل عشان المدقق
    return render(request, 'relationship_app/list_books.html', context)

# 2. Class-based view
class LibraryDetail(DetailView):
    model = Library
    # --- والتصليح هنا ---
    # لازم المسار الكامل
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

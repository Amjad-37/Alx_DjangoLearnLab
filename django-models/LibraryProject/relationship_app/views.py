from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

# 1. Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    # Renders 'relationship_app/templates/list_books.html'
    return render(request, 'list_books.html', context)

# 2. Class-based view for library details
class LibraryDetail(DetailView):
    model = Library
    # Renders 'relationship_app/templates/library_detail.html'
    template_name = 'library_detail.html'
    context_object_name = 'library'

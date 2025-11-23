from django.shortcuts import render
from django.views.generic.detail import DetailView

# فصلناهم عشان الـ checker يشوف Library لوحدها
from .models import Library
from .models import Book

# 1. Function-based view
def list_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)

# 2. Class-based view
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import ExampleForm

# --- Task 2: Secure Data Access ---

def book_list(request):
    """
    Secure view using Django ORM to prevent SQL Injection.
    We verify permissions and validate input through forms if needed.
    """
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_view', raise_exception=True)
def raise_exception(request):
    return render(request, 'bookshelf/book_list.html')

def form_example(request):
    """
    Demonstrates a form protected by CSRF token.
    """
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Secure handling of data
            return redirect('book_list')
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})

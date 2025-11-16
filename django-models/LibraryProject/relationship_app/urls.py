from django.urls import path
from . import views

urlpatterns = [
    # المسار بتاع الـ function-based view
    path('books/', views.list_books, name='list_books'),
    
    # المسار بتاع الـ class-based view
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]

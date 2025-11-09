from django.urls import path
from . import views

urlpatterns = [
    # Path for the function-based view
    path('books/', views.list_books, name='list-books'),

    # Path for the class-based view (needs a primary key 'pk')
    path('library/<int:pk>/', views.LibraryDetail.as_view(), name='library-detail'),
]

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Book, Author

class BookAPITests(APITestCase):
    def setUp(self):
        # 1. Create a user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
        # 2. Create an author
        self.author = Author.objects.create(name="J.K. Rowling")

        # 3. Create a book (Initial data)
        self.book = Book.objects.create(
            title="Harry Potter",
            publication_year=2001,
            author=self.author
        )

        # 4. Define URLs
        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', args=[self.book.id])
        self.create_url = reverse('book-create')
        self.update_url = reverse('book-update', args=[self.book.id])
        self.delete_url = reverse('book-delete', args=[self.book.id])
        
        # Log in the user for authorized tests
        self.client.login(username='testuser', password='testpassword')

    def test_create_book_authenticated(self):
        """Test that an authenticated user can create a book."""
        data = {
            "title": "New Book",
            "publication_year": 2023,
            "author": self.author.id
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(id=2).title, "New Book")

    def test_create_book_unauthenticated(self):
        """Test that an unauthenticated user CANNOT create a book."""
        self.client.logout() # Simulate unauthenticated user
        data = {
            "title": "Unauthorized Book",
            "publication_year": 2023,
            "author": self.author.id
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN) # Or 401 depending on settings

    def test_list_books(self):
        """Test retrieving the list of books."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_book(self):
        """Test retrieving a single book details."""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Harry Potter")

    def test_update_book(self):
        """Test updating a book (Authenticated)."""
        data = {
            "title": "Harry Potter Updated",
            "publication_year": 2002,
            "author": self.author.id
        }
        response = self.client.put(self.update_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Harry Potter Updated")

    def test_delete_book(self):
        """Test deleting a book (Authenticated)."""
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books_by_title(self):
        """Test filtering books by title."""
        # Create extra book
        Book.objects.create(title="Django Guide", publication_year=2022, author=self.author)
        
        response = self.client.get(self.list_url, {'title': 'Harry Potter'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Harry Potter")

    def test_search_books(self):
        """Test searching functionality."""
        Book.objects.create(title="Django Guide", publication_year=2022, author=self.author)
        
        response = self.client.get(self.list_url, {'search': 'Django'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Django Guide")

    def test_order_books(self):
        """Test ordering functionality."""
        book2 = Book.objects.create(title="A First Book", publication_year=2000, author=self.author)
        
        response = self.client.get(self.list_url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], "A First Book") # 2000 comes before 2001
        self.assertEqual(response.data[1]['title'], "Harry Potter")

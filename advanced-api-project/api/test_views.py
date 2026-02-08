from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from api.models import Author, Book


class BookAPIViewTests(APITestCase):
    """
    Unit tests for Book API endpoints.
     Covers CRUD operations, filtering, searching, ordering, and permissions.

    """

    def setUp(self):
        # Create user for authenticated actions
        User = get_user_model()
        self.user = User.objects.create_user(username="testuser", password="testpass123")

        # Create sample data
        self.author = Author.objects.create(name="Chimamanda Ngozi Adichie")
        self.book1 = Book.objects.create(
            title="Half of a Yellow Sun",
            publication_year=2006,
            author=self.author,
        )
        self.book2 = Book.objects.create(
            title="Americanah",
            publication_year=2013,
            author=self.author,
        )

        # URL names based on my api/urls.py
        self.list_url = reverse("book-list")
        self.detail_url = reverse("book-detail", kwargs={"pk": self.book1.pk})
        self.create_url = reverse("book-create")
        self.update_url = reverse("book-update", kwargs={"pk": self.book1.pk})
        self.delete_url = reverse("book-delete", kwargs={"pk": self.book1.pk})

    # ---------- READ (Public) ----------

    def test_list_books_public(self):
        """Unauthenticated users can list books."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) >= 2)

    def test_retrieve_book_public(self):
        """Unauthenticated users can retrieve a single book."""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book1.title)

    # ---------- CREATE (Auth required) ----------

    def test_create_book_unauthenticated_denied(self):
        """Unauthenticated users should not be able to create books."""
        payload = {
            "title": "Purple Hibiscus",
            "publication_year": 2003,
            "author": self.author.id,
        }
        response = self.client.post(self.create_url, payload, format="json")
        self.assertIn(response.status_code, [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN])

    def test_create_book_authenticated_success(self):
        """Authenticated users can create books."""
        self.client.force_authenticate(user=self.user)
        payload = {
            "title": "Purple Hibiscus",
            "publication_year": 2003,
            "author": self.author.id,
        }
        response = self.client.post(self.create_url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Book.objects.filter(title="Purple Hibiscus").exists())

    # ---------- UPDATE (Auth required) ----------

    def test_update_book_unauthenticated_denied(self):
        """Unauthenticated users should not be able to update books."""
        payload = {
            "title": "Half of a Yellow Sun (Updated)",
            "publication_year": 2006,
            "author": self.author.id,
        }
        response = self.client.put(self.update_url, payload, format="json")
        self.assertIn(response.status_code, [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN])

    def test_update_book_authenticated_success(self):
        """Authenticated users can update books."""
        self.client.force_authenticate(user=self.user)
        payload = {
            "title": "Half of a Yellow Sun (Updated)",
            "publication_year": 2006,
            "author": self.author.id,
        }
        response = self.client.put(self.update_url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Half of a Yellow Sun (Updated)")

    # ---------- DELETE (Auth required) ----------

    def test_delete_book_unauthenticated_denied(self):
        """Unauthenticated users should not be able to delete books."""
        response = self.client.delete(self.delete_url)
        self.assertIn(response.status_code, [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN])

    def test_delete_book_authenticated_success(self):
        """Authenticated users can delete books."""
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(self.delete_url)
        self.assertIn(response.status_code, [status.HTTP_200_OK, status.HTTP_204_NO_CONTENT])

        self.assertFalse(Book.objects.filter(pk=self.book1.pk).exists())

    # ---------- FILTERING / SEARCH / ORDERING ----------

    def test_filter_by_publication_year(self):
        """Filter books by publication_year using query params."""
        response = self.client.get(f"{self.list_url}?publication_year=2013")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Americanah")

    def test_search_by_title_or_author(self):
        """Search books using search param (title or author name)."""
        response = self.client.get(f"{self.list_url}?search=Americanah")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Americanah")

    def test_ordering_by_publication_year_desc(self):
        """Order results by publication_year descending."""
        response = self.client.get(f"{self.list_url}?ordering=-publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) >= 2)
        self.assertGreaterEqual(response.data[0]["publication_year"], response.data[1]["publication_year"])

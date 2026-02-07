from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)

urlpatterns = [
    # /books/ -> list all books
    path("books/", BookListView.as_view(), name="book-list"),

    # /books/<pk>/ -> retrieve a single book
    path("books/<int:pk>/", BookDetailView.as_view(), name="book-detail"),

    # /books/create/ -> create a book (auth required)
    path("books/create/", BookCreateView.as_view(), name="book-create"),

    # /books/<pk>/update/ -> update a book (auth required)
    path("books/<int:pk>/update/", BookUpdateView.as_view(), name="book-update"),

    # /books/<pk>/delete/ -> delete a book (auth required)
    path("books/<int:pk>/delete/", BookDeleteView.as_view(), name="book-delete"),
]
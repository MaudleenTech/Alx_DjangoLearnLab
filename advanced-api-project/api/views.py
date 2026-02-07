from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny 
from .models import Book
from .serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters



# ListView: Retrieve all books (public - no auth required)
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Enable filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Filter books by title, author, and publication_year
    filterset_fields = ["title", "author", "publication_year"]

    # Search books by title and author name
    search_fields = ["title", "author__name"]

    # Order books by title and publication_year
    ordering_fields = ["title", "publication_year"]
    ordering = ["title"]




# DetailView: Retrieve a single book by ID (public - no auth required)
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]


# CreateView: Add a new book (requires authentication)
# DRF handles validation automatically through BookSerializer,
# including the custom publication_year validation you added in Task 0.
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# UpdateView: Modify an existing book (requires authentication)
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# DeleteView: Remove a book (requires authentication)
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

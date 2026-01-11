from bookshelf.models import Book
book = Book.objects.get(id=1)
book.id, book.title, book.author, book.publication_year

# Expected Output: (1, "1984", "George Orwell", 1949)
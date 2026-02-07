from django.db import models

# Author represents a writer who can have multiple books (one-to-many relationship).
class Author(models.Model):
    # Stores the author's full name.
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Book represents a published work linked to a single Author.
class Book(models.Model):
    # Stores the book title.
    title = models.CharField(max_length=255)

    # Stores the year the book was published (e.g., 2020).
    publication_year = models.IntegerField()

    # ForeignKey creates a one-to-many relationship:
    # one Author -> many Book records.
    # related_name="books" allows: author.books.all()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return f"{self.title} ({self.publication_year})"

from datetime import date
from rest_framework import serializers
from .models import Author, Book


# BookSerializer converts Book model instances to/from JSON.
# It also validates publication_year to prevent future years.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

    def validate_publication_year(self, value):
        # Prevent setting publication_year to a future year.
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("publication_year cannot be in the future.")
        return value


# AuthorSerializer converts Author instances to JSON and includes nested books.
# The relationship is handled via Book.author (ForeignKey) with related_name="books".
# That allows us to serialize an author's books dynamically using BookSerializer.
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ["id", "name", "books"]

Advanced API Development with Django REST Framework
Project Overview

This project is part of the Advanced API Development with Django REST Framework module in the ALX Back-End program. It focuses on building robust APIs using Django REST Framework, including custom serializers, generic views, permissions, and validation.

The project demonstrates how to structure a Django REST API to handle complex data relationships and enforce access control while maintaining clean and reusable code.

Features Implemented
Task 0: Models and Custom Serializers

Created Author and Book models using Django ORM

Implemented a one-to-many relationship between Author and Book

Built custom serializers with nested serialization

Added custom validation to prevent future publication years

Documented models and serializers with clear comments

Task 1: Generic Views and Permissions

Implemented generic class-based views for full CRUD operations on books:

ListView

DetailView

CreateView

UpdateView

DeleteView

Configured URL routing for all views

Applied permissions:

Public read-only access for listing and retrieving books

Authenticated-only access for creating, updating, and deleting books

Added inline documentation explaining view behavior and permissions

Data Models
Author

name – stores the author’s name

Book

title – title of the book

publication_year – year the book was published

author – foreign key linking to an Author

Each Author can have multiple Books, while each Book belongs to a single Author.

API Endpoints
Public Endpoints (No Authentication Required)

GET /api/books/
Retrieve a list of all books.

GET /api/books/<id>/
Retrieve details of a specific book.

Protected Endpoints (Authentication Required)

POST /api/books/create/
Create a new book.

PUT /api/books/<id>/update/
Update an existing book.

PATCH /api/books/<id>/update/
Partially update a book.

DELETE /api/books/<id>/delete/
Delete a book.

Permissions

Read-only endpoints use AllowAny, allowing unauthenticated access.

Create, update, and delete endpoints use IsAuthenticated, restricting access to logged-in users only.

Validation is handled at the serializer level to ensure data integrity.

## Filtering, Searching, and Ordering (Task 2)

### Filtering
Filter books using query parameters:
- `/api/books/?title=Americanah`
- `/api/books/?publication_year=2013`
- `/api/books/?author=1`

### Search
Search by book title or author name:
- `/api/books/?search=chimamanda`

### Ordering
Order results by fields like `title` or `publication_year`:
- `/api/books/?ordering=title`
- `/api/books/?ordering=-publication_year`


Technologies Used

Python

Django

Django REST Framework

SQLite (development database)

Git & GitHub

Author

Maudleen Imonirioma
ALX Back-End Engineering Program
# Django Blog Application

## Project Overview

This project is a full-featured blog application built with Django as part of the ALX Back-End Development program. It demonstrates the implementation of a structured Django project including authentication, database configuration, and dynamic content management.

The application is being developed progressively to simulate real-world backend development practices.

---

## Features Implemented (So Far)

### 1. Project Setup & Configuration
- Django project initialization
- App-based architecture (`blog` app)
- PostgreSQL-compatible database configuration
- Proper static and template configuration
- Clean project structure

### 2. Blog Post Model
- `Post` model with:
  - Title
  - Content
  - Published date (auto timestamp)
  - Author (ForeignKey to Django User model)

### 3. User Authentication System
- User Registration (Custom form extending `UserCreationForm`)
- Login (Django built-in authentication view)
- Logout
- Profile management (Edit username and email)
- CSRF protection enabled
- Secure password hashing using Django's built-in system
- Login protection using `@login_required`

---

## Tech Stack

- Python 3.x
- Django 6.x
- SQLite (default)
- PostgreSQL-ready configuration
- HTML / CSS
-Framework: Django
-Database: SQLite (Development)
-Tagging: django-taggit
-UI: Custom CSS with responsive design
- Git & GitHub

---

## Project Structure

django_blog/
│
├── blog/
│ ├── models.py
│ ├── views.py
│ ├── forms.py
│ ├── urls.py
│ ├── templates/blog/
│ └── static/
│
├── django_blog/
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── manage.py
└── db.sqlite3


---

## Authentication Flow

### Registration
Users create an account using a custom registration form that extends Django’s `UserCreationForm`. Email is required.

### Login
Django's built-in `LoginView` handles authentication securely.

### Logout
Handled using Django’s `LogoutView`.

### Profile
Authenticated users can update their username and email address.

---
Installation & Setup
Clone the repository:

git clone https://github.com/MaudleenTech/Alx_DjangoLearnLab.git
cd Alx_DjangoLearnLab/django_blog
Install dependencies:

pip install django django-taggit
Run Migrations:

python manage.py makemigrations
python manage.py migrate
Start the server:

python manage.py runserver
Access the app: Open http://127.0.0.1:8000 in your browser.

Documentation
Comment System Guide
License
MIT License
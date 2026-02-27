# 📘 Social Media API

A fully functional Social Media REST API built with Django and Django REST Framework (DRF).

This API supports:

User registration & authentication (Token-based)

Creating and managing posts

Commenting on posts

Pagination & filtering

Secure permission enforcement

# 🚀 Features
## 🔐 Authentication System

Custom User Model (extends AbstractUser)

Token-based authentication using DRF

Secure login & registration endpoints

Profile management endpoint

## 📝 Posts

Create, retrieve, update, delete posts

Only post owners can edit/delete

Paginated post listing

Search posts by title or content

## 💬 Comments

Create, retrieve, update, delete comments

Linked to posts

Only comment owners can edit/delete

## 🏗️ Tech Stack

Python 3.x

Django 6.x

Django REST Framework

SQLite (development)

Token Authentication

Django Filters

## 📂 Project Structure
social_media_api/
│
├── accounts/          # Authentication & User management
├── posts/             # Posts & Comments functionality
├── social_media_api/  # Project settings
└── manage.py

## ⚙️ Installation & Setup
1️⃣ Clone Repository
git clone github.com/MaudleenTech/Alx_DjangoLearnLab.git
cd social_media_api
2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
3️⃣ Install Dependencies
pip install -r requirements.txt

Or manually:

pip install django djangorestframework django-filter pillow
4️⃣ Apply Migrations
python manage.py makemigrations
python manage.py migrate
5️⃣ Run Server
python manage.py runserver

API base URL:

http://127.0.0.1:8000/api/

## 🔐 Authentication Flow

## 🧑 Register

POST /api/accounts/register/

{
  "username": "maudleen",
  "email": "m@example.com",
  "password": "pass1234"
}

Response:

{
  "token": "abc123xyz..."
}
🔑 Login

POST /api/accounts/login/

{
  "username": "maudleen",
  "password": "pass1234"
}

Response:

{
  "token": "abc123xyz..."
}

## 🔓 Access Protected Routes

Authorization: 

## 📝 Posts API
## 📌 Create Post

POST /api/posts/

{
  "title": "My First Post",
  "content": "This is my first post."
}
📖 List Posts

GET /api/posts/

Paginated response:

{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [...]
}
## 🔍 Search Posts
GET /api/posts/?search=first

Searches by:

Title

Content

## ✏️ Update Post

PUT /api/posts/{id}/

Only the post author can update.

## ❌ Delete Post

DELETE /api/posts/{id}/

Only the post author can delete.


## 💬 Comments API
➕ Create Comment

POST /api/comments/

{
  "post": 1,
  "content": "Nice post!"
}
## 📄 List Comments

GET /api/comments/

✏️ Update Comment

PUT /api/comments/{id}/

Only comment author allowed.

## ❌ Delete Comment

DELETE /api/comments/{id}/

## 🔐 Permissions
Action	Auth Required	Owner Required
View posts	❌	❌
Create post	✅	❌
Edit post	✅	✅
Delete post	✅	✅
Create comment	✅	❌
Edit comment	✅	✅
📊 Pagination

Enabled globally:

PAGE_SIZE = 10

All list endpoints return paginated results.

🛡 Security Considerations

Token authentication enforced

Custom user model

Ownership-based permission checks

Passwords hashed securely by Django

## 🧪 Testing

Tested using:

Django REST Framework Browsable API

Postman

## 📌 Future Improvements

Follow system

User feed

Likes

Notifications

Production deployment (Render/Heroku/AWS)

JWT authentication

Rate limiting

## 👩🏽‍💻 Author

Maudleen Imonirioma
ALX Software Engineering Program
Backend Development Track
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import list_books, LibraryDetailView

urlpatterns = [
    # Task 1 views
    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),

    # Task 2 auth URLs (checker expects views.register and LogoutView.as_view(template_name=...))
    path("login/", auth_views.LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("register/", views.register, name="register"),

     # Task 3 RBAC URLs (if you have them)
    path("admin-role/", views.admin_view, name="admin_view"),
    path("librarian-role/", views.librarian_view, name="librarian_view"),
    path("member-role/", views.member_view, name="member_view"),
     
    # Task 4 custom permission URLs (checker expects add_book/, edit_book/)
    path("add_book/", views.add_book, name="add_book"),
    path("edit_book/", views.edit_book, name="edit_book"),
    path("delete_book/", views.delete_book, name="delete_book"),

]

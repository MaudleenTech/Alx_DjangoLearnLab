from django.urls import path
from django.contrib.auth import views as auth_views
from .views import list_books, LibraryDetailView, register

urlpatterns = [
    path("books/", list_books, name="list_books"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),

    # Authentication URLs
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="relationship_app/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(
            template_name="relationship_app/logout.html",
            http_method_names=["get", "post"],  # ✅ allows logout page to load in browser
        ),
        name="logout",
    ),
    path("register/", register, name="register"),
]

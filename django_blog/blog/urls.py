from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # existing pages
    path("", views.home, name="home"),
    path("posts/", views.posts, name="posts"),

    # auth pages (REQUIRED PATHS FOR TASK 1)
    path("login/", auth_views.LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),

    # Posts CRUD (Task 2)
    path("posts/", views.PostListView.as_view(), name="post_list"),
    path("posts/new/", views.PostCreateView.as_view(), name="post_create"),
    path("posts/<int:pk>/", views.PostDetailView.as_view(), name="post_detail"),
    path("posts/<int:pk>/edit/", views.PostUpdateView.as_view(), name="post_update"),
    path("posts/<int:pk>/delete/", views.PostDeleteView.as_view(), name="post_delete"),
]


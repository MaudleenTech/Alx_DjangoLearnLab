from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Home
    path("", views.home, name="home"),

    # Auth (Task 1)
    path("login/", auth_views.LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),

   # Posts CRUD (Task 2) - checker compliant
path("posts/", views.PostListView.as_view(), name="post_list"),                 # list
path("post/<int:pk>/", views.PostDetailView.as_view(), name="post_detail"),     # detail

path("post/new/", views.PostCreateView.as_view(), name="post_new"),             # create
path("post/<int:pk>/update/", views.PostUpdateView.as_view(), name="post_update"),  # update
path("post/<int:pk>/delete/", views.PostDeleteView.as_view(), name="post_delete"),  # delete
# Comments (Task 3)
path("posts/<int:post_id>/comments/new/", views.comment_create, name="comment_create"),
path("comments/<int:pk>/edit/", views.CommentUpdateView.as_view(), name="comment_update"),
path("comments/<int:pk>/delete/", views.CommentDeleteView.as_view(), name="comment_delete"),
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedView
from .views import PostViewSet, CommentViewSet, like_post, unlike_post

router = DefaultRouter()
router.register(r"posts", PostViewSet, basename="posts")
router.register(r"comments", CommentViewSet, basename="comments")

urlpatterns = [
    path("", include(router.urls)),
    path("feed/", FeedView.as_view(), name="feed"),
    path("", include(router.urls)),
    path("posts/<int:pk>/like/", like_post, name="like_post"),
    path("posts/<int:pk>/unlike/", unlike_post, name="unlike_post"),
]
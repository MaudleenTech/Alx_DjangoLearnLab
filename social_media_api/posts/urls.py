from rest_framework.routers import DefaultRouter, path
from .views import FeedView
from api_project.api import views
from .views import PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r"posts", PostViewSet, basename="posts")
router.register(r"comments", CommentViewSet, basename="comments")

urlpatterns = router.urlsy
path("follow/<int:user_id>/", views.follow_user, name="follow_user"),
path("unfollow/<int:user_id>/", views.unfollow_user, name="unfollow_user"),
path("feed/", FeedView.as_view(), name="feed"),
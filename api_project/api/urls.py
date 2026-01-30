from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Route for the BookList view (ListAPIView)
    path('books/', BookList.as_view(), name='book-list'),
    
    # Token Authentication endpoint:
    # POST username & password -> returns {"token": "..."}
    path('token/', obtain_auth_token, name='api-token'),

    # Route for the BookList view (ListAPIView)
    path('books/', BookList.as_view(), name='book-list'),

    # Router URLs for BookViewSet (all CRUD operations)
    path('', include(router.urls)),
]

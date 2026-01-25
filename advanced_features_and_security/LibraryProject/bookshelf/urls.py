from django.urls import path
from . import views

urlpatterns = [
    path("perm/view/", views.can_view_books, name="can_view"),
    path("perm/create/", views.can_create_book, name="can_create"),
    path("perm/edit/", views.can_edit_book, name="can_edit"),
    path("perm/delete/", views.can_delete_book, name="can_delete"),
]

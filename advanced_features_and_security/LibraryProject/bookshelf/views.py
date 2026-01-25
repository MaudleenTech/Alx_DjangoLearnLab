from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse

# Create your views here.
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse


@permission_required("bookshelf.can_view", raise_exception=True)
def can_view_books(request):
    return HttpResponse("Permission check passed: can_view")


@permission_required("bookshelf.can_create", raise_exception=True)
def can_create_book(request):
    return HttpResponse("Permission check passed: can_create")


@permission_required("bookshelf.can_edit", raise_exception=True)
def can_edit_book(request):
    return HttpResponse("Permission check passed: can_edit")


@permission_required("bookshelf.can_delete", raise_exception=True)
def can_delete_book(request):
    return HttpResponse("Permission check passed: can_delete")

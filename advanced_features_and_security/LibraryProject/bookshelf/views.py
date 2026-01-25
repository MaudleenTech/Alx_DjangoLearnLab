from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from .models import Book
from .forms import ExampleForm

# Create your views here.
@permission_required("bookshelf.can_view", raise_exception=True)
def book_list(request):
    query = request.GET.get("q", "").strip()

    # Safe: ORM parameterizes queries (prevents SQL injection)
    if query:
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.all()

    output = ", ".join(book.title for book in books) or "No books found"
    return HttpResponse(output)

@permission_required("bookshelf.can_view", raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    output = ", ".join(book.title for book in books)
    return HttpResponse(output)

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

def form_example(request):
    form = ExampleForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        # safe validated input (prevents injection-style issues)
        return render(request, "bookshelf/form_example.html", {"form": form})

    return render(request, "bookshelf/form_example.html", {"form": form})
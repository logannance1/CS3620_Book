from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Book

def home(request):
    return render(request, 'books/home.html', {})

# Create your views here.
def book_list(request):
    book_object = Book.objects.all()
    book_name = request.GET.get('book_name')

    if book_name is not None and book_name != '':
        book_object = book_object.filter(name__icontains=book_name)

    paginator = Paginator(book_object, 5)
    page = request.GET.get('page')
    book_object = paginator.get_page(page)
    return render(request, 'books/book_list.html', {
        'book_object': book_object,
        'book_name': book_name
    })
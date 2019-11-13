from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import Book, Author, Redaction, BooksRent


def books_list(request):
    books = Book.objects.all()
    return HttpResponse(books)

def index(request):
    template = loader.get_template('index.html')
    books = Book.objects.all()
    biblio_data = {
        "title": "мою библиотеку",
        "books": books,
    }
    return HttpResponse(template.render(biblio_data, request))

def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            book.copy_count += 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')


def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')


def redactions(request):
    template = loader.get_template('redactions.html')
    books = Book.objects.all()
    redactions = Redaction.objects.all()
    redact_data = {
        "title": "мою библиотеку",
        "books": books,
        "redactions": redactions,
    }
    return HttpResponse(template.render(redact_data, request))

def books(request):
    template = loader.get_template('books.html')
    books = Book.objects.all()
    biblio_data = {
        "title": "мою библиотеку",
        "books": books,
    }
    return HttpResponse(template.render(biblio_data, request))

def authors(request):
    template = loader.get_template('authors.html')
    books = Book.objects.all()
    authors = Author.objects.all()
    authors_data = {
        "title": "мою библиотеку",
        "books": books,
        "authors": authors,
    }
    return HttpResponse(template.render(authors_data, request))

def books_rent(request):
    template = loader.get_template('renters.html')
    rented_books = BooksRent.objects.all()
    rental_data = {
        "rented_books": rented_books,
    }
    return HttpResponse(template.render(rental_data, request))
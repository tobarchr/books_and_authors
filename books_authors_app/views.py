from django.shortcuts import render,redirect
from books_authors_app.models import *

def index(request):
    context = {
        "all_the_books" : Book.objects.all()
    }
    return render(request,'index.html',context)

def add_book(request):
    new_book = Book.objects.create(title=request.POST['book_title'],desc=request.POST['text_description'])
    return redirect('/')

def authors(request):
    context = {
        "all_the_authors" : Author.objects.all()
    }
    return render(request,'authors.html',context)

def add_author(request):
    new_author = Author.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],notes=request.POST['notes'])
    return redirect('/authors')

def book_details(request,id_from_route):
    details = Book.objects.get(id=id_from_route)
    all_the_authors = Author.objects.all()
    context = {
        "all_book_details" : details,
        "all_the_authors": all_the_authors
    }
    return render(request,'book_details.html',context)

def author_details(request,author_id):
    details = Author.objects.get(id=author_id)
    all_the_books = Book.objects.all()
    context = {
        "all_the_author" : details,
        "all_the_books": all_the_books
    }
    return render(request,'author_details.html',context)

def assign_book(request):
    this_book = Book.objects.get(id=request.POST['select_book'])
    this_author = Author.objects.get(id=request.POST["author_id"])
    this_book.authors.add(this_author)
    return redirect('/authors/'+str(request.POST["author_id"]))

def assign_author(request):
    this_book = Book.objects.get(id=request.POST['book_id'])
    this_author = Author.objects.get(id=request.POST["select_author"])
    this_book.authors.add(this_author)
    return redirect('/books/'+str(request.POST['book_id']))
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from login_regist_app.models import *
from .models import *

# Create your views here.
def books(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        "this_user": User.objects.get(id=request.session['user_id']),
        "all_books": Book.objects.all(),
        "latest_reviews": Review.objects.order_by("-id")[0:3]
    }
    return render(request, "books.html",context)


def add_here(request):
    context = {
        "all_authors": Author.objects.all()
    }
    return render(request,"add.html", context)   

def one_book(request,book_id):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        "this_book": Book.objects.get(id=book_id)
    }
    return render(request,"one_book.html", context)    

def user_reviews(request,user_id):
    if 'user_id' not in request.session:
        return redirect('/')
    this_user = User.objects.get(id=user_id)
    count = 0
    for i in this_user.book_reviews.all():
        count +=1
    context = {
        "this_user": this_user,
        "count": count
    }
    return render(request,"user.html",context)


def add_review(request):
    this_user = User.objects.get(id=request.session['user_id'])

    # If the book already exists, then just grab the book for this_book. Otherwise, this_book is a newly created book.
    check_duplicates = Book.objects.filter(title=request.POST['title'])  
    if check_duplicates:
        this_book = check_duplicates[0]
    else:    
        this_book = Book.objects.create(title=request.POST['title'])
        # Add new author if CharField is not empty, elseif existing author selected then add to book, otherwise if both fields empty - show error
        if request.POST['new_author'] != "":
            this_author = Author.objects.create(full_name=request.POST['new_author'])
            this_book.authors.add(this_author)
        elif request.POST['exist_author_id'] != "":
            this_author = Author.objects.get(id=request.POST['exist_author_id'])
            this_book.authors.add(this_author)
        else:
            author_errors = Author.objects.author_validate(request.POST)  
            if len(author_errors) > 0:
                for key, value in author_errors.items():
                    messages.error(request, value, extra_tags=key)
            return redirect("/books/add_here")

    this_review = Review.objects.create(review=request.POST['review'],rating=request.POST['rating'],user=this_user,book=this_book)


    return redirect(f"/books/{this_book.id}")    


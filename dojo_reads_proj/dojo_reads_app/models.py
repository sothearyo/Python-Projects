from django.db import models
from login_regist_app import models as login_models

# Validations for Book
class BookManager(models.Manager):
    def book_validate(self,postData):
        errors = {}
        if len(postData['title']) < 1 or len(postData['title']) > 100:
            errors['title'] = "Book title must be between 1 and 100 characters"
        return errors

# Validations for Author
class AuthorManager(models.Manager):
    def author_validate(self,postData):
        errors = {}
        if len(postData['new_author']) < 1 or len(postData['new_author']) > 100:
            errors['new_author'] = "Please select an author or enter new author. New author name must be between 1 and 100 characters"
        return errors    

# Validations for BookReview
class ReviewManager(models.Manager):
    def review_validate(self,postData):
        errors = {}
        if len(postData['review']) < 10 or len(postData['review']) > 500:
            errors['review'] = "Please enter a review between 10 and 500 characters"
        if int(postData['rating']) < 1 or int(postData['rating']) > 5:
            errors['rating'] = "Please enter a rating between 1 and 5"
        return errors

class Book(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()

class Author(models.Model):
    full_name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name="authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AuthorManager()

class Review(models.Model):
    review = models.TextField()
    rating = models.IntegerField()
    user = models.ForeignKey(login_models.User,related_name="book_reviews", on_delete = models.CASCADE)
    book = models.ForeignKey(Book,related_name="book_reviews", on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ReviewManager()

# a_book = Book.objects.create(title=request.POST['title'])
# Author.objects.create(name = request.POST["name"],books=a_book)
# Book
# title 
# author

# Review (this is the many side. ForeignKey goes here. User can have many reviews and Book can have many reviews.)
# rating
# review
# user - one to many to User
# book - one to many to Book

# Author
# first
# last
# book - ManyToManyField to Book



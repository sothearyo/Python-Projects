from django.urls import path
from . import views
urlpatterns = [
    path('', views.books),
    path('add', views.add_here),
    path('<int:book_id>', views.one_book),
    path('user/<int:user_id>', views.user_reviews),
    path('add_review', views.add_review),
]
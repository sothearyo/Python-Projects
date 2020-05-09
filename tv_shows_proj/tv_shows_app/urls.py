from django.urls import path
from . import views

urlpatterns = [
    path('shows', views.shows),
    path('shows/new', views.new),
    path('create_one', views.create_one),
    path('shows/<int:show_id>', views.read_one),
    path('shows/<int:show_id>/edit', views.edit_one),
    path('shows/<int:show_id>/delete', views.delete_one)
]
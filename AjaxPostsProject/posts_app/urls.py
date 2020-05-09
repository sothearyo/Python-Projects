from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('all_notes', views.all_notes),
    path('add_note', views.add_note),
    path('notes/delete/<int:note_id>', views.delete_note)
]
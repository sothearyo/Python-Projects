from django.urls import path
from . import views
urlpatterns = [
    path('', views.show_wall),
    path('post_message', views.post_msg),
    path('comment_on_msg', views.comment_on_msg),
    path('delete_comment', views.delete_comment),
]
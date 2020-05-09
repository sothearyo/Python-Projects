from django.db import models
from login_regist_app import models as login_models

# Create your models here.
class Msg(models.Model):
    user = models.ForeignKey(login_models.Users,related_name="msg", on_delete = models.CASCADE)
    msg = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    user = models.ForeignKey(login_models.Users,related_name="comment", on_delete = models.CASCADE)
    msg = models.ForeignKey(Msg,related_name="comment", on_delete = models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

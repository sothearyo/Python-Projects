from django.shortcuts import render, redirect
from login_regist_app.models import *
from .models import *


# Create your views here.
def show_wall(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        "this_user": Users.objects.get(id=request.session['user_id']),
        "all_messages": Msg.objects.all(),
        "all_comments": Comment.objects.all()
    }
    return render(request, "wall.html",context)

def post_msg(request):
    this_user = Users.objects.get(id=request.session['user_id'])
    newMsg = Msg.objects.create(user=this_user,msg=request.POST["msg"])
    return redirect("/wall")

def comment_on_msg(request):
    this_user = Users.objects.get(id=request.session['user_id'])   
    this_msg = Msg.objects.get(id=request.POST['msg_id'])
    newComment = Comment.objects.create(user=this_user,msg=this_msg,comment=request.POST['comment'])
    return redirect("/wall")

def delete_comment(request):
    this_comment = Comment.objects.get(id=request.POST['comment_id'])
    this_comment.delete()
    return redirect("/wall")
from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
    context = {
        'all_notes': Post.objects.all()
    }
    return render(request,'index.html',context)

def all_notes(request):
    context = {
        'all_notes': Post.objects.all()
    }
    return render(request,'all_notes.html',context)    

def add_note(request):
    Post.objects.create(note=request.POST['note'])
    return redirect('/')

def delete_note(request,note_id):
    Post.objects.get(id=note_id).delete()
    return redirect("/all_notes")

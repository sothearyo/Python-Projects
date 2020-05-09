from django.shortcuts import render, redirect
from django.contrib import messages

from .models import TVShow


# Create your views here.
def shows(request):
    context = {
        "all_shows": TVShow.objects.all()
    }
    return render(request, "read_all.html", context)

def new(request):
    return render(request, "create.html")

def read_one(request,show_id):
    context = {
        "this_show": TVShow.objects.get(id=show_id)
    }
    return render(request, "read_one.html", context)

def edit_one(request,show_id):
    if request.method == "GET":
        context = {
            "this_show": TVShow.objects.get(id=show_id)
        }
        return render(request, "edit_one.html", context)
    elif request.method == "POST":
        errors = TVShow.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f"/shows/{show_id}/edit")
        else:    
            this_show = TVShow.objects.get(id=show_id)
            this_show.title = request.POST["title"]
            this_show.network = request.POST["network"]
            this_show.release_date = request.POST["release_date"]
            this_show.description = request.POST["description"]
            this_show.save()
            return redirect(f"/shows/{show_id}")

def create_one(request):
    errors = TVShow.objects.basic_validator(request.POST)
    unique_errors = TVShow.objects.unique_validator(request.POST)
    if len(errors) > 0 or len(unique_errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        for key, value in unique_errors.items():
            messages.error(request, value)
        return redirect("/shows/new")
    else:    
        TVShow.objects.create(title=request.POST['title'],network=request.POST['network'],release_date=request.POST['release_date'],description=request.POST['description'])
        show_id = TVShow.objects.get(title=request.POST['title']).id
        context = {
            "this_show": TVShow.objects.get(title=request.POST['title'])
        }
        return redirect(f"shows/{show_id}")

def delete_one(request,show_id):
    this_show = TVShow.objects.get(id=show_id)
    this_show.delete()
    return redirect("/shows")

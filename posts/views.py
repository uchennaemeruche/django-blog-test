from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .forms import PostForm
from .models import Post

@login_required()
def create(request):
    if request.method == "POST": 
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("Record saved")
            return redirect("/")
    else:
        form = PostForm()
    return render(request, "posts/new.html", {"form": form})

def delete(request, id):
   post = get_object_or_404(Post, pk=id)
   post.delete()
   return redirect("/")

def detail(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, "posts/detail.html", {"post": post})

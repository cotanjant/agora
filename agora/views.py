from django.contrib.auth.views import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm

from django.views import View
from django.views.decorators.http import require_GET

# we import table
from .models import Post

def signup(req):
    if req.method == "POST":
        form = UserCreationForm(req.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(req, "registration/signup.html", {"form": form})

@require_GET
def index(req):
    posts = Post.objects.filter(published=True)
    # return published posts
    return render(req, "index.html", {
        "posts": posts
    })

@require_GET
def post_by_id(req, pk):
    post = get_object_or_404(Post, pk=pk, published=True)
    return render(req, "post_page.html", {
        "post": post
    })

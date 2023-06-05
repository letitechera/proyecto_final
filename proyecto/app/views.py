from django.template import Context
from django.shortcuts import render
from .utils import get_article_by_id

def inicio(request):
    return render(request, "app/index.html")

def about(request):
    return render(request, "app/about-me.html")

def posts(request):
    return render(request, "app/posts.html")

def post(request, id):
    article = get_article_by_id(id)

    return render(request, "app/post.html", article)


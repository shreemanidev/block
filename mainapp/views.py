from django.shortcuts import render
from .models import Blog


def home(Request):
    data = Blog.objects.all()
    return render(Request,"index.html",{"data":data})

def blogPage(Request,id):
    sblog = Blog.objects.get(id=id)
    return render(Request,"blog.html",{"sblog":sblog})


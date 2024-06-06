from django.shortcuts import render
from .models import Blog
# Create your views here.

def index(request):
    blogs = [
        {'title': 'Learning Django', 'content': 'Django is an awsome open source framework for building APIs used in Django REST framework.', 'author': 'Prudence', 'date': '2024.06.04'},
        {'title': 'Learning Django', 'content': 'Django is an awsome open source framework for building APIs used in Django REST framework.', 'author': 'Prudence', 'date': '2024.06.04'},
        {'title': 'Learning Django', 'content': 'Django is an awsome open source framework for building APIs used in Django REST framework.', 'author': 'Prudence', 'date': '2024.06.04'},

    ]
    context = {'blogs': blogs}

    return render (request, "index.html", context)

def about(request):

    return render(request, "about.html")

def contact(request):
    
    return render(request, "contact.html")

def blog_list(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, "blog_list.html", context)


    

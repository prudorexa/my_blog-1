from django.shortcuts import render, redirect
from .models import Blog
from django.contrib import messages
from .models import Subscriber
from .forms import BlogForm


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


def subscribe(request):
    if request.method == 'POST':
        email = request.POST['email']
        if Subscriber.objects.filter(email=email).exists():
            messages.error(request, 'You are already subscribed.')
        else:
            subscriber = Subscriber(email=email)
            subscriber.save()
            messages.success(request, 'Thank you for subscribing!')
            return redirect('subscribe')
    return render(request, 'subscribe.html')

def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save()  
            return redirect('bloglist')  
    else:
        form = BlogForm()
    return render(request, 'add_blog.html', {'form': form})
    
def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form data to create a new Blog object
            blog = form.save(commit=False)  # Use commit=False to modify the object before saving
            blog.save()  # Save the modified Blog object with the author assigned
            
            return redirect('bloglist')  # Redirect to the 'blog_list' view after successful form submission
    else:
        form = BlogForm()
    
    return render(request, 'add_blog.html', {'form': form})
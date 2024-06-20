from django.urls import path
from . views import *
from myapp.views import login_view

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('bloglist/', blog_list, name='bloglist'),
    path('subscribe/', subscribe, name='subscribe'),
    path('add_blog/', add_blog, name='add_blog'),
    path('login/', login_view, name='login'),


]
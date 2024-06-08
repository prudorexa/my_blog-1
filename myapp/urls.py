from django.urls import path
from . views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('bloglist/', blog_list, name='bloglist'),
    path('subscribe/', subscribe, name='subscribe'),
    path('add_blog/', add_blog, name='add_blog'),

]
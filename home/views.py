

# Create your views here.
# def home(request):
#     return render(request,'home.html')

from django.shortcuts import render
# from blogs.models import Category
from blogs.models import Blog
from about.models import About

# Create your views here.
def home(request):
    featured_post=Blog.objects.filter(is_featured=True,status="published").order_by('updated_at')
    posts=Blog.objects.filter(is_featured=False,status='published')
# ftech about
    try:
        about=About.objects.get()
    except:
        about= None

    context={
        'featured_post':featured_post,
        'posts':posts,
        'about':about,
    }
    return render(request,"home-blogs.html",context)
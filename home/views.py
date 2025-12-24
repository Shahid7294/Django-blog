

# Create your views here.
# def home(request):
#     return render(request,'home.html')

from django.shortcuts import render
# from blogs.models import Category
from blogs.models import Blog

# Create your views here.
def home(request):
    featured_post=Blog.objects.filter(is_featured=True,status="published").order_by('updated_at')
    posts=Blog.objects.filter(is_featured=False,status='published')

    context={
        'featured_post':featured_post,
        'posts':posts,
    }
    return render(request,"home-blogs.html",context)
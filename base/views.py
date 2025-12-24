from django.shortcuts import render
from blogs.models import Category
from blogs.models import Blog

# Create your views here.
def base(request):
    return render(request,"base-blogs.html")
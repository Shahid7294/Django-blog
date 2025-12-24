from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404,redirect
from .models import Blog,Category
# Create your views here.
def posts_by_category(request,id):
    posts=Blog.objects.filter(status="published",category=id)
    try:
        cateogry=Category.objects.get(pk=id)
    except:
        return redirect('home')
    # cateogry=get_object_or_404(Category,pk=id)
    context={
        'posts':posts,
        'cateogry':cateogry,
    }
    return render(request,'posts_by_category.html',context)
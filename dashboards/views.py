from django.shortcuts import render,redirect
from blogs.models import Category
from blogs.models import Blog
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm
# Create your views here.
@login_required(login_url='login')
def dashboards(request):
    category_count=Category.objects.all().count()
    blog_count=Blog.objects.all().count()
    context={
        'category_count':category_count,
        'blog_count':blog_count,
    }
    return render(request,"dashboards.html",context)

def categories(request):
    return render(request,'categories.html')

def categories_add(request):
    if request.method == "POST":
        forms=CategoryForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect("categories")
    else:
        forms=CategoryForm()
        context={
            'forms':forms,
        }
        return render(request,'categories_add.html',context)

def edit_category(request,pk):
    categoreis=Category.objects.get(pk=pk)
    if request.method == "POST":
        form=CategoryForm(request.POST,instance=categoreis)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form=CategoryForm(instance=categoreis)
        context={
            'form':form,
            'categoreis':categoreis,
        }
        return render(request,"edit_category.html",context)
def delete_category(request,pk):
    categories=Category.objects.get(pk=pk)
    categories.delete()
    return redirect('categories')
from django.shortcuts import render,redirect
from blogs.models import Category,Blog
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm,PostForm
from django.template.defaultfilters import slugify
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


# post

def posts(request):
    posts=Blog.objects.all()
    context={
        'posts':posts,
    }
    return render(request,'posts.html',context)

def add_posts(request):
    if request.method == "POST":
        forms=PostForm(request.POST,request.FILES)
        if forms.is_valid():
            post=forms.save(commit=False)
            post.author=request.user
            # post.save()
            title=forms.cleaned_data['title']
            post.slug=slugify(title)
            post.save()
            print("form is valid")
            return redirect('posts')
        else:
            print("form is invalid")
    
    forms=PostForm()
    context={
            'forms':forms,
        }
    return render(request,'add_post.html',context)

def edit_post(request,pk):
    data=Blog.objects.get(pk=pk)
    if request.method == "POST":
        forms=PostForm(request.POST,request.FILES,instance=data)
        if forms.is_valid():
            post=forms.save()
            title=forms.cleaned_data['title']
            post.slug=slugify(title)
            post.save()
            return redirect('posts')
    else:
        forms=PostForm(instance=data)
        context={
            'forms':forms,
            'data':data
        }
        return render(request,'edit_post.html',context)
def delete_post(request,pk):
    data=Blog.objects.get(pk=pk)
    data.delete()
    return redirect('posts')
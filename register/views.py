from django.shortcuts import render,redirect
from .forms import RegisterationForm

# Create your views here.
def register(request):
    if request.method == "POST":
        form=RegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form=RegisterationForm()
    context={
        'form':form
    }
    return render(request,'register.html',context)
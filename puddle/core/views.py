from django.shortcuts import render,redirect
from item.models import Item,Category
from .forms import Signup
from django.contrib.auth import logout
from django.contrib.auth.views import LogoutView
from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
    items=Item.objects.filter(is_sold=False)[0:6]
    categories=Category.objects.all()
    return render(request,'core/index.html',{'items':items,"categories":categories})
def contact(request):
    return render(request,'core/contact.html')
def signup(request):
    
    if request.method=='POST':
        form=Signup(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=Signup()
    return render(request,'core/signup.html',{'form':form})


def logoutPage(request):
    logout(request)
    return redirect('login')
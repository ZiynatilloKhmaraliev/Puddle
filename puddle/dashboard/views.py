from django.shortcuts import render,redirect
from item.models import Item
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    items=Item.objects.filter(created_by=request.user)

    return render(request,'dashboard/index.html',{'items':items})

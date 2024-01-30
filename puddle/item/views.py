from django.shortcuts import render,redirect
from .models import Item,Category
from .forms import NewItemForm,EditItemForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.
def items(request):
    query=request.GET.get('query','')
    categories=Category.objects.all()
    category_id=request.GET.get('category',0)
    items=Item.objects.filter(is_sold=False)
    if category_id:
        items=items.filter(category_id=category_id)


    if query:
        items=Item.objects.filter(Q(name__icontains=query)|Q(description__icontains=query))
    return render(request,'item/items.html',{'items':items,'query':query,'categories':categories,'category_id':int(category_id)})

def detail(request, pk):
    item=Item.objects.get(pk=pk)
    related_items=Item.objects.filter(category=item.category,is_sold=False).exclude(pk=pk)[0:3]
    return render(request,'item/detail.html',{'item':item,'related_items':related_items})

@login_required
def new(request):
    if request.method=='POST':
        form=NewItemForm(request.POST,request.FILES)
        if form.is_valid():
            item=form.save(commit=False)
            item.created_by=request.user
            item.save()
            return redirect('detail',pk=item.id)
    else:
        form=NewItemForm()
    return render(request,'item/form.html',{'form':form,'title':'New item'})

@login_required
def delete(request,pk):
    item=Item.objects.get(pk=pk)
    item.delete()
    return redirect('dashboard:index')

@login_required
def edit(request,pk):
    item=Item.objects.get(pk=pk)

    if request.method=='POST':
        form=EditItemForm(request.POST,request.FILES,instance=item)
        if form.is_valid():
           form.save()
           return redirect('detail',pk=item.id)
    else:
        form=EditItemForm(instance=item)
    return render(request,'item/form.html',{'form':form,'title':'Edit item'})
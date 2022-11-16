from django.shortcuts import render,redirect
from  django.contrib.auth import login
from  django.contrib import messages
from  django.contrib.auth.decorators import login_required 
from product.forms import ProductForm
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from .models import Userprofile
from product.models import Prodect ,Category,Order,OrderItem
from django.utils.text import slugify
# Create your views here.
def user_detail(request , pk ):
    user =User.objects.get(pk=pk)
    products=user.products.filter(status=Prodect.ACTIVE)
    return render(request,"userprofile/user_detail.html",{"user":user,'products':products})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)
 
            userprofile = Userprofile.objects.create(user=user)
            return redirect('my_app:home')
        
    else:
        form = UserCreationForm()
    
 
    return render(request,"userprofile/signup.html",{"form":form})

@login_required 
def account_user(request):
    return render(request,'userprofile/account_user.html')

@login_required
def add_product(request):
  if request.method == 'POST':
      form = ProductForm(request.POST,request.FILES)
      
      if form.is_valid():
          title = request.POST.get('title')
          product =form.save(commit=False)
          product.user = request.user
          product.slug =slugify(title)
          product.save()
          messages.success(request,"the product was added!")
          return redirect('userprofile:my_product')
  else:
    form = ProductForm()
  return render(request,'userprofile/product_form.html',{'title':'Add prodect','form':form})

@login_required
def edit_product(request, pk):
    product = Prodect.objects.filter(user =request.user).get(pk = pk )
    if request.method == 'POST':
      form = ProductForm(request.POST,request.FILES,instance=product)

      if form.is_valid():
         form.save()
         messages.success(request,"the changes was saved!")
         return redirect('userprofile:my_product')
    else:
     form = ProductForm(instance=product)
    
    

    return render(request,'userprofile/product_form.html',{'title':'Edit prodect','form':form ,'product':product})

@login_required
def delete_product(request, pk):
    product = Prodect.objects.filter(user=request.user).get(pk = pk )
    product.status = Prodect.DELETED
    product.save()
    messages.success(request,"the product was deleted!")
    return redirect('userprofile:my_product')
    



@login_required 
def my_product(request):
    products=request.user.products.exclude(status=Prodect.DELETED)
    orders_items =OrderItem.objects.filter(product__user = request.user)

    return render(request,"userprofile/my_product.html",{'products':products,'orders_items':orders_items})


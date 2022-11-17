from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpRequest, HttpResponse
from  django.contrib import messages
from  django.contrib.auth.decorators import login_required 
from product.forms import ProductForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout as auth_logout
from product.models import Prodect ,OrderItem
from django.utils.text import slugify
# Create your views here.
# user_detail.
def user_detail(request , pk ):
    user =User.objects.get(pk=pk)
    products=user.products.filter(status=Prodect.ACTIVE)
    return render(request,"userprofile/user_detail.html",{"user":user,'products':products})

#register

def register_user(request : HttpRequest):

    if request.method == "POST":

        new_user = User.objects.create_user(username=request.POST["username"], password=request.POST["password"])
        new_user.save()

    return render(request, "userprofile/register.html")



def login_user(request : HttpRequest):
    msg = ""
    if request.method == "POST":
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
  
        if user:
            login(request, user)
            return redirect("my_app:about")
        else:
            msg = "User Not Found , check your credentials"

    return render(request, "userprofile/login.html", {"msg" : msg})


    
def logout(request: HttpRequest):
    auth_logout(request)
 
    return redirect('my_app:about')


def account_user(request):
    return render(request,'userprofile/account_user.html')


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
    product = Prodect.objects.filter(user=request.user).get(pk=pk)
    product.status = Prodect.DELETED
    product.save()

    messages.success(request, 'The product was deleted!')

    return redirect('userprofile:my_product')

   # products=request.user.products.exclude(status=Prodect.DELETED)

@login_required 
def my_product(request):
    products = request.user.products.exclude(status=Prodect.DELETED)
    order_items = OrderItem.objects.filter(product__user=request.user)

    return render(request, 'userprofile/my_product.html', {
        'products': products,
        'order_items': order_items
    })

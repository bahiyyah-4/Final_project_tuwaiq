from django.shortcuts import render,get_object_or_404,redirect
from .models import Prodect,Category,Order,OrderItem
from django.db.models import Q # to search for 2 query
from .cart import Cart
from  django.contrib.auth.decorators import login_required 
from django.conf import settings #for session
from .forms import OrderForm
# Create your views here.
#-----show detail for category --------
def category_detail(request, slug):
    category=get_object_or_404(Category,slug=slug)
    product= category.products.filter(status=Prodect.ACTIVE)
    return render(request,"product/category_detail.html",{'category':category,'product':product})

#-----add to cart --------

def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)

    return redirect('product:cart_view')

#-----checkout --------

@login_required
def checkout(request):
    cart = Cart(request)
    if request.method=='POST':
        form =OrderForm(request.POST)
        if form.is_valid():
              total_price =0
              for item in cart :
                  product = item['product']
                  total_price += product.price * int(item['quantity'])
              
              order =form.save(commit=False)
              order.created_by = request.user
              order.paid_amount = total_price
              order.save()
              for item in cart:
                     product = item['product']
                     quantity =int(item['quantity'])
                     price= product.price*quantity
                     item= OrderItem.objects.create(order=order,product=product,price=price,quantity=quantity)

              cart.clear()
                  
              return redirect('userprofile:account_user')
        
    else:
      form = OrderForm()
         
    return render(request,"product/checkout.html" ,{'cart':cart ,'form':form})

    
#-----change_quanesty --------

def change_quantity(request, product_id):
    action = request.GET.get('action', '')

    if action:
        quantity = 1

        if action == 'decrease':
            quantity = -1

        cart = Cart(request)
        cart.add(product_id, quantity, True)
    
    
    return redirect('product:cart_view')
     
#-----remove from cart --------

def remove_from_cart(request,product_id):
  cart = Cart(request)
  cart.remove(product_id)

  return redirect('product:cart_view')

#-----view the cart --------

def cart_view(request):
    cart1 =Cart(request)
    return render(request,"product/cart_view.html",{'cart1':cart1})

#-----show prodect --------

def product_detail(request,category_slug,slug ):
    product =get_object_or_404(Prodect,slug=slug ,status=Prodect.ACTIVE)

    return render(request,"product/prodect_detail.html",{'product':product})

#-----searh --------

def search(request):
    query =request.GET.get('query', '')
    if request.user.is_authenticated:
      product= Prodect.objects.filter(status=Prodect.ACTIVE).exclude(user=request.user).filter(Q(title__icontains= query)| Q(description= query))
    else:
      product= Prodect.objects.filter(status=Prodect.ACTIVE).filter(Q(title__icontains= query)| Q(description= query))

    return render(request,'product/search.html',{'query':query,'product':product})



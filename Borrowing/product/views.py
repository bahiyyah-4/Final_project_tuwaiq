from django.shortcuts import render,get_object_or_404
from .models import Prodect,Category
from django.db.models import Q # to search for 2 query
# Create your views here.

def category_detail(request, slug):
    category=get_object_or_404(Category,slug=slug)
    product= category.products.all()
    return render(request,"product/category_detail.html",{'category':category,'product':product})


def product_detail(request,category_slug,slug ):
    product =get_object_or_404(Prodect,slug=slug)

    return render(request,"product/prodect_detail.html",{'product':product})

def search(request):
    query =request.GET.get('query', '')
    product= Prodect.objects.filter(Q(title__icontains= query)| Q(description= query))
    return render(request,'product/search.html',{'query':query,'product':product})
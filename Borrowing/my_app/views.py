from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from product.models import Prodect
# from .models import
# Create your views here.


def home(reguest):
    products = Prodect.objects.filter(status=Prodect.ACTIVE)[0:8]

    return render(reguest, 'my_app/home.html',{'products':products})


def contact(request ):

    return render(request,"my_app/contact.html")

def about(reguest):
    return render(reguest, 'my_app/about.html')

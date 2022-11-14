from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from product.models import Prodect
# from .models import
# Create your views here.


def home(reguest):
    products = Prodect.objects.all()[0:6]

    return render(reguest, 'my_app/home.html',{'products':products})


def about(reguest):
    return render(reguest, 'my_app/about.html')

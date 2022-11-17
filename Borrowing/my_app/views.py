from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from product.models import Prodect
# from .models import
# Create your views here.

#-----home--------
def home(reguest):

    if reguest.user.is_authenticated:
        products = Prodect.objects.filter(status=Prodect.ACTIVE).exclude(user=reguest.user)[0:8]
    else:
        products = Prodect.objects.filter(status=Prodect.ACTIVE)[0:8]

    return render(reguest, 'my_app/home.html',{'products':products})

#-----contact--------
def contact(request ):

    return render(request,"my_app/contact.html")
#-----about--------
def about(reguest):
    return render(reguest, 'my_app/about.html')

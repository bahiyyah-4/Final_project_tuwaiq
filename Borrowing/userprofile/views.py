from django.shortcuts import render,redirect
from  django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from .models import Userprofile
# Create your views here.
def user_detail(request , pk ):
    user =User.objects.get(pk=pk)
    return render(request,"userprofile/user_detail.html",{"user":user})

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

def account_user(request):
    return render(request,'userprofile/account_user.html')
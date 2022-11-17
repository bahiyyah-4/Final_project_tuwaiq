from django.urls import path
from django.http import HttpRequest, HttpResponse
from . import views

app_name ="userprofile"

urlpatterns = [
   path("user/<int:pk>/",views.user_detail,name="user_detail"),
   path("register/", views.register_user, name='register_user'),
   path('login/', views.login_user, name='login_user'),
   path('logout/', views.logout, name='logout'),
    path("account/",views.account_user,name="account_user"),
   path("my_product/",views.my_product,name="my_product"),
   path("my_product/add_product/",views.add_product,name="add_product"),
   path("my_product/edit_product/<int:pk>/",views.edit_product,name="edit_product"),
   path("my_product/delete_product/<int:pk>/",views.delete_product,name="delete_product"),



]
from django.urls import path
from django.http import HttpRequest, HttpResponse
from . import views

app_name = "my_app"

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),

]

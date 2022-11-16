from django.contrib import admin

from .models import Category,Prodect,Order,OrderItem
# Register your models here.

admin.site.register(Category)
admin.site.register(Prodect)
admin.site.register(Order)
admin.site.register(OrderItem)
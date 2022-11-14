from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=60)
    slug = models.SlugField(max_length=60)
#to change name
    class Meta:
        verbose_name_plural ="Categories"

    def __str__(self):
        return self.title

class Prodect(models.Model):
    user = models.ForeignKey(User,related_name='products',on_delete=models.CASCADE)
    Category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    slug = models.SlugField(max_length=60)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='uploads/product_images/',blank=True ,null=True)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
       ordering = ('-created_at',)

    def __str__(self):
        return self.title
    
   
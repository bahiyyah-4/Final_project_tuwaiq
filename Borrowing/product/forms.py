from django import forms
from .models import Prodect,Order

class OrderForm(forms.ModelForm):
    class Meta: 
        model = Order
        fields = ('first_name','last_name','time_brrowing','laddress','city','phone')
      



class ProductForm(forms.ModelForm):
    class Meta:
        model = Prodect
        fields = ('Category','title','description','price','image',)
        widgets= {
            'Category':forms.Select(attrs={
             'class':'block w-full rounded-md shadow-sm focus:ring focus:ring-opacity-75 focus:ring-violet-400 bg-gray-100'
            }),
            'title':forms.TextInput(attrs={
             'class':'block w-full rounded-md shadow-sm focus:ring focus:ring-opacity-75 focus:ring-violet-400 bg-gray-100 '        
            }),
            'description':forms.Textarea(attrs={
             'class':'block w-full rounded-md shadow-sm focus:ring focus:ring-opacity-75 focus:ring-violet-400 bg-gray-100 '
            }),
            'price':forms.TextInput(attrs={
             'class':'block w-full rounded-md shadow-sm focus:ring focus:ring-opacity-75 focus:ring-violet-400 bg-gray-100 '
            }),
            'image':forms.FileInput(attrs={
             'class':'block w-full rounded-md shadow-sm focus:ring focus:ring-opacity-75 focus:ring-violet-400 bg-gray-100 '
            })
        }


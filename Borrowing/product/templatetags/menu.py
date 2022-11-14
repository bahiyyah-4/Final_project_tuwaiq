
from django import template
from product.models import Category
register = template.Library()
@register.inclusion_tag('my_app/menu.html')
def menu():
      categories =Category.objects.all()
      return{'categories':categories}
from django import template
from PRODUCTS.models import ProductCategorieModel
register = template.Library()

@register.simple_tag
def kategori_list():
    categories=ProductCategorieModel.objects.all()
    return categories

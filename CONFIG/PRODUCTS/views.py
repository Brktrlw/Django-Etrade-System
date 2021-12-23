from django.shortcuts import render
from PRODUCTS.models import ProductModel



def v_CategorieProducts(request,catId):
    products = ProductModel.objects.filter(productCategorie=catId)
    return render(request,"products.html",{"products":products})

def v_products(request):
    products = ProductModel.objects.all()
    return render(request,"products.html",{"products":products})




















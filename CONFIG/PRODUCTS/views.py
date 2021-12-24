from django.shortcuts import render
from PRODUCTS.models import ProductModel,ProductCategorieModel


def v_CategorieProducts(request,catTitle):
    cats=ProductCategorieModel.objects.filter(categorieTitle=catTitle)
    products = ProductModel.objects.filter(productCategorie=cats[0].id)
    return render(request,"products.html",{"products":products,"cats":cats})

def v_products(request):
    products = ProductModel.objects.all()
    return render(request,"products.html",{"products":products})


















from django.shortcuts import render
from PRODUCTS.models import ProductModel,ProductCategorieModel
from USERAPP.models import CartModel

def v_CategorieProducts(request,catTitle):
    cats=ProductCategorieModel.objects.filter(categorieTitle=catTitle)
    products = ProductModel.objects.filter(productCategorie=cats[0].id)
    return render(request,"products.html",{"products":products,"cats":cats})

def v_products(request):
    products = ProductModel.objects.all()
    cartAmount = CartModel.objects.filter(customer_id=request.user.id)
    return render(request,"products.html",{"products":products})

def v_productDetail(request,productId):
    return render(request,"productDetails.html",{"productId":productId})

















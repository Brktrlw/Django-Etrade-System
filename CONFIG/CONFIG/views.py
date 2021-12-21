
from django.shortcuts import render,redirect
from django.contrib.auth import logout
from PRODUCTS.models import ProductModel

def v_homePage(request):
    return render(request,"homePage.html")

def v_logout(request):
    logout(request)
    return redirect("homePage")

def v_products(request):
    products = ProductModel.objects.all()
    return render(request,"products.html",{"products":products})
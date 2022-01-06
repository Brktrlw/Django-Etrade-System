
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import logout
from PRODUCTS.models import ProductModel

def v_homePage(request):
    keyword = request.GET.get("keyword")
    if keyword:
        products = ProductModel.objects.filter(productTitle__contains=keyword)
        return render(request,"products.html",{"products":products})
    else:
        return render(request,"homePage.html")

def v_logout(request):
    logout(request)
    return redirect("homePage")

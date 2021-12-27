from django.shortcuts import render,HttpResponse
from PRODUCTS.models import ProductModel,ProductCategorieModel,ProductCommentsModel
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
    try:
        product  = ProductModel.objects.get(id=productId)
    except:
        return HttpResponse("Böyle bir sayfa bulunamadı")
    try:
        comments = ProductCommentsModel.objects.filter(product=product)
    except:
        comments=None
    return render(request,"productDetails.html",{"product":product,"comments":comments})

















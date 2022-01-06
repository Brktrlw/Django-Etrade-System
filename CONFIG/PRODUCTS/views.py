from django.shortcuts import render,HttpResponse
from PRODUCTS.models import ProductModel,ProductCategorieModel,ProductCommentsModel
from .forms import CommentForm

def v_CategorieProducts(request,catTitle):
    cats = ProductCategorieModel.objects.get(categorieTitle=catTitle)
    products = ProductModel.objects.filter(productCategorie=cats.id)
    return render(request,"products.html",{"products":products,"cats":cats})

def v_products(request):
    keyword=request.GET.get("keyword")
    if keyword:
        products=ProductModel.objects.filter(productTitle__contains=keyword)
    else:
        products = ProductModel.objects.all()
    return render(request,"products.html",{"products":products})

def v_productDetail(request,slug):
    try:
        product  = ProductModel.objects.get(slug=slug)
    except:
        return HttpResponse("Böyle bir sayfa bulunamadı")
    try:
        comments = ProductCommentsModel.objects.filter(product=product).order_by("-createdDate")
    except:
        comments=None
    commentForm=CommentForm(request.POST or None)
    if commentForm.is_valid():
        comment=commentForm.save(commit=False)
        comment.customer=request.user
        comment.commentText=commentForm.cleaned_data.get("commentText")
        comment.product=product
        comment.save()
    return render(request,"productDetails.html",{"product":product,"comments":comments})

















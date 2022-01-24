from django.shortcuts import render,HttpResponse,redirect
from PRODUCTS.models import ProductModel,ProductCategorieModel,ProductCommentsModel
from .forms import CommentForm
from django.core.paginator import Paginator

def v_CategorieProducts(request,catTitle):
    cats = ProductCategorieModel.objects.get(categorieTitle=catTitle)
    products = ProductModel.objects.filter(productCategorie=cats.id)
    return render(request,"products.html",{"products":products,"cats":cats})

def v_products(request):
    keyword= request.GET.get("keyword")
    sayfa  = request.GET.get("page")
    if keyword:
        # arama yaparak ürün getirme
        products=ProductModel.objects.filter(productTitle__contains=keyword)
    else:
        # tüm ürünleri listeleme
        products = ProductModel.objects.all()
        paginator=Paginator(products,3)

    return render(request,"products.html",{"products":paginator.get_page(sayfa)})


def v_productDetail(request,slug):
    try:
        product  = ProductModel.objects.get(newSlug=slug)
    except:
        return HttpResponse("Böyle bir sayfa bulunamadı")
    try:
        comments = ProductCommentsModel.objects.filter(product=product).order_by("-createdDate")
    except:
        comments=None
    commentForm=CommentForm(request.POST or None)
    print(product.productCategorie.all())
    if commentForm.is_valid():
        comment=commentForm.save(commit=False)
        comment.customer=request.user
        comment.commentText=commentForm.cleaned_data.get("commentText")
        comment.product=product
        comment.save()
        return redirect("ProductDetails",newSlug=slug)
    return render(request,"productDetails.html",{"product":product,"comments":comments})

















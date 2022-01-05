from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm, AddressForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from USERAPP.models import CartModel, FavoriteModel, AddressModel, CustomUserModel
from django.http import JsonResponse
import json
from PRODUCTS.models import ProductModel
from ORDERS.forms import OrderForm

def v_register(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        userName = form.cleaned_data.get("userName")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")
        newUser = User(username=userName)
        newUser.set_password(password)
        newUser.save()
        login(request, newUser)
        messages.success(request, "Başarıyla kayıt oldunuz")
        return redirect("homePage")

    return render(request, "registerPage.html", {"form": form})

def v_login(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        userName = form.cleaned_data.get("userName")
        password = form.cleaned_data.get("password")
        user = authenticate(username=userName, password=password)
        if user is None:
            messages.error(request, "Hatalı Giriş")
            return render(request, "loginPage.html", {"form": form})
        else:
            login(request, user)
            return redirect("homePage")

    return render(request, "loginPage.html", {"form": form})

def v_favorites(request):
    favorites = FavoriteModel.objects.filter(customer=request.user)
    return render(request, "favorites.html", {"favorites": favorites})

def v_cart(request):
    products = CartModel.objects.filter(customer=request.user)
    total = 0
    for product_ in products:
        total += product_.amount * product_.product.productPrice
    return render(request, "cart.html", {"products": products, "total": total})

def v_checkout(request):
    cartItems=CartModel.objects.filter(customer_id=request.user.id)
    if not cartItems:
        #eğer kullanıcının sepeti boşsa ve bu sayfaya gitmeye çalışıyorsa gelecek uyarı
        return redirect("homePage")
    else:
        #eğer sepetinde ürün varsa bu sayfa açılacak
        # Address eklendiğinde çalışan blok
        form = OrderForm(request.POST or None)
        if form.is_valid():
            address = form.save(commit=False)
            address.addressTitle = form.cleaned_data.get("addressTitle")
            address.customer = request.user
            address.save()
            messages.success(request, "Address Başarıyla Eklendi")
            return redirect("checkout")
        # Address eklendiğinde çalışan blok

        customerAddress = AddressModel.objects.filter(customer=request.user)
        products = CartModel.objects.filter(customer=request.user)
        total = 0
        for product_ in products:
            total += product_.product.productPrice * product_.amount

        return render(request, "checkout.html",
                      {"products": products, "total": total, "form": form, "customerAddress": customerAddress})


def v_profile(request):
    user = CustomUserModel.objects.filter(id=request.user.id)
    userAddress = AddressModel.objects.filter(customer=request.user)
    adresForm= AddressForm(request.POST or None)
    if adresForm.is_valid():
        address = adresForm.save(commit=False)
        address.addressTitle = adresForm.cleaned_data.get("addressTitle")
        address.addressCity = adresForm.cleaned_data.get("addressCity")
        address.addressText = adresForm.cleaned_data.get("addressText")
        address.customer = request.user
        address.save()
        messages.success(request, "Address Başarıyla Eklendi")
        return redirect("profile")

    return render(request, "profile.html", {"user": user[0], "userAddress": userAddress,"adresForm": adresForm})

def f_update_item(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    _customer = request.user

    product = ProductModel.objects.get(id=productId)
    cartItem = CartModel.objects.filter(customer=_customer).filter(product_id=productId)
    if not cartItem:
        cartItem = CartModel.objects.create(product_id=productId, customer=_customer, amount=1)
        cartItem.save()
    else:
        cartItem = CartModel.objects.get(customer=_customer, product_id=productId)
        if action == "add":
            cartItem.amount += 1
        elif action == "remove":
            cartItem.amount -= 1
        cartItem.save()
    return JsonResponse(
        "<div class='alert alert-success m-3 p-3 rounded'><i class='fa fa-check' aria-hidden='true'></i> Ürün Başarıyla Sepetinize Eklenmiştir</div>",
        safe=False)

def f_update_cart(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data["action"]
    cartItem = CartModel.objects.get(product_id=productId, customer_id=request.user.id)
    if action == "add":
        cartItem.amount += 1
        cartItem.save()
        messages.success(request, "Sepetiniz başarıyla güncellenmiştir")
    elif action == "remove":
        if cartItem.amount == 1:
            cartItem.delete()
            messages.success(request, "Ürün başarıyla sepetinizden kaldırılmıştır")
        else:
            cartItem.amount -= 1
            cartItem.save()
            messages.success(request, "Sepetiniz başarıyla güncellenmiştir")

    return JsonResponse("asdf", safe=False)

def f_update_favorites(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data["action"]
    if action == "add":
        try:
            # eğer ürünü veritabanında bulursa try blogu calısacak
            favItem = FavoriteModel.objects.get(customer_id=request.user.id, product_id=productId)
            return JsonResponse(
                "<div class='alert alert-danger m-3 p-3 rounded'><i class='fa fa-check' aria-hidden='true'></i> Ürün zaten favorilerinizdedir</div>",
                safe=False)
        except:
            # ürünü bulamazsa except kısmı çalışarak veritabanına favori kaydediyor.
            newFavItem = FavoriteModel.objects.create(customer_id=request.user.id, product_id=productId)
            newFavItem.save()
            return JsonResponse(
                "<div class='alert alert-success m-3 p-3 rounded'><i class='fa fa-check' aria-hidden='true'></i> Ürün başarıyla favorilerinize eklenmiştir.</div>",
                safe=False)

    elif action == "remove":
        favItem = FavoriteModel.objects.get(customer_id=request.user.id, product_id=productId)
        favItem.delete()

    return JsonResponse(
        "<div class='alert alert-success m-3 p-3 rounded'><i class='fa fa-check' aria-hidden='true'></i> Ürün Başarıyla Favorilerinizden Kaldırılmıştır</div>",
        safe=False)

def v_myOrders(request):
    return render(request,"orders.html")
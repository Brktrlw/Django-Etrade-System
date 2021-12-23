from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm,AddressForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from USERAPP.models import CartModel,FavoriteModel,AddressModel,CustomUserModel

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
            messages.error(request,"Hatalı Giriş")
            return render(request, "loginPage.html", {"form": form})
        else:
            login(request, user)
            return redirect("homePage")

    return render(request, "loginPage.html", {"form": form})

def v_favorites(request):
    favorites = FavoriteModel.objects.filter(customer=request.user)
    return render(request,"favorites.html",{"favorites":favorites})

def v_cart(request):
    products = CartModel.objects.filter(customer=request.user)
    total=0
    for product_ in products:
        total+= product_.amount*product_.product.productPrice
    return render(request,"cart.html",{"products":products,"total":total})

def v_checkout(request):
    #Address eklendiğinde çalışan blok
    form=AddressForm(request.POST or None)
    if form.is_valid():
        address=form.save(commit=False)
        address.addressTitle=form.cleaned_data.get("addressTitle")
        address.addressCity= form.cleaned_data.get("addressCity")
        address.addressText= form.cleaned_data.get("addressText")
        address.customer  = request.user
        address.save()
        messages.success(request,"Address Başarıyla Eklendi")
        return redirect("checkout")
    #Address eklendiğinde çalışan blok

    customerAddress=AddressModel.objects.filter(customer=request.user)
    products = CartModel.objects.filter(customer=request.user)
    total=0
    for product_ in products:
        total += product_.product.productPrice * product_.amount

    return render(request,"checkout.html",{"products":products,"total":total,"form":form,"customerAddress":customerAddress})


def v_profile(request):
    user=CustomUserModel.objects.filter(id=request.user.id)
    userAddress=AddressModel.objects.filter(customer=request.user)
    print(userAddress)
    return render(request,"profile.html",{"user":user[0],"userAddress":userAddress})





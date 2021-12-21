from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from PRODUCTS.models import CartModel

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

def v_cart(request):
    products = CartModel.objects.filter(customer=request.user)
    return render(request,"cart.html",{"products":products})

def v_checkout(request):
    return render(request,"checkout.html")
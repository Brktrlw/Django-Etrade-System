from django.shortcuts import render,redirect
from .forms import LoginForm,RegisterForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User


def v_register(request):
    form=RegisterForm(request.POST or None)

    if form.is_valid():
        userName = form.cleaned_data.get("userName")
        password = form.cleaned_data.get("password")
        email    = form.cleaned_data.get("email")
        newUser = User(username=userName)
        newUser.set_password(password)
        newUser.save()
        login(request,newUser)
        return redirect("homePage")
    return render(request,"registerPage.html",{"form":form})

def v_login(request):
    form=LoginForm(request.POST or None)
    if form.is_valid():
        userName = form.cleaned_data.get("userName")
        password = form.cleaned_data.get("password")
        print(userName,password)
        user = authenticate(username=userName, password=password)
        if user is None:
            print("KULLANICI ADI VEYA PAROLA HATALI")
            return render(request,"loginPage.html",{"form":form})
        else:
            login(request,user)
            return redirect("homePage")

    return render(request,"loginPage.html",{"form":form})


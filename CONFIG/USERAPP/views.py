from django.shortcuts import render,redirect
from .forms import LoginForm
from django.contrib.auth import authenticate,login

def v_register(request):
    pass

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


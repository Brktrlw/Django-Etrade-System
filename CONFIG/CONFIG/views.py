
from django.shortcuts import render,redirect
from django.contrib.auth import logout

def v_homePage(request):
    return render(request,"homePage.html")

def v_logout(request):
    logout(request)
    return redirect("homePage")
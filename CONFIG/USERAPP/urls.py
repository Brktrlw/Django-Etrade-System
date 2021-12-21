from django.urls import path,include
from . import views

urlpatterns = [
    path("login/",views.v_login,name="login"),
    path("register/",views.v_register,name="register"),
    path("sepetim/",views.v_cart,name="cart")
]

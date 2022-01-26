from django.urls import path,include
from . import views

urlpatterns = [
    path("login/",views.v_login,name="login"),
    path("register/",views.v_register,name="register"),
    path("sepetim/",views.v_cart,name="cart"),
    path("checkout/",views.v_checkout,name="checkout"),
    path("favorilerim/",views.v_favorites,name="favorites"),
    path("profile/",views.v_profile,name="profile"),
    path("update_item/",views.f_update_item,name="update_item"),
    path("update-cart/",views.f_update_cart,name="update-cart"),
    path("update-favorites/",views.f_update_favorites,name="update-favorites"),
    path("orders/",views.v_myOrders,name="orders"),
]

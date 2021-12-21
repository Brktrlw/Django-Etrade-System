from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.v_homePage,name="homePage"),
    path("logout/",views.v_logout,name="logout"),
    path("user/",include("USERAPP.urls")),
    path("products/",views.v_products)
]

from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.v_homePage,name="homePage"),
    path("logout/",views.v_logout,name="logout"),
    path("user/",include("USERAPP.urls")),
    path("products/",views.v_products,name="products")
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

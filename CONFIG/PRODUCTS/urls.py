from django.urls import path
from . import views
urlpatterns = [
    path("categorie/<int:catId>",views.v_CategorieProducts,name="CategorieProducts"),
    path("", views.v_products,name="products")
]

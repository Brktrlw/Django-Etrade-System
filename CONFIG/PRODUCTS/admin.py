from django.contrib import admin
from .models import AddressModel,OrderModel,ProductModel,OrderItemModel,CartModel,FavoriteModel

@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["productTitle","productPrice"] # admin tablosunda yazar ve olusturma tarihini göstermesini sağlar
    list_display_links = ["productTitle"]    # olusturma tarihine de link verir
    search_fields = ["productTitle"]                       # admin sayfasına arama cubugu ekler ve title bilgisine göre arama yaptırır
    class Meta:
        model=ProductModel

admin.site.register(FavoriteModel)
admin.site.register(CartModel)
admin.site.register(AddressModel)
admin.site.register(OrderModel)
admin.site.register(OrderItemModel)

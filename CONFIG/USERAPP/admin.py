from django.contrib import admin
from .models import AddressModel,FavoriteModel,CartModel,CustomUserModel

admin.site.register(CustomUserModel)
admin.site.register(AddressModel)
admin.site.register(FavoriteModel)
admin.site.register(CartModel)
# Register your models here.

from django.db import models
from django.contrib.auth.models import User
from PRODUCTS.models import ProductModel
from django.contrib.auth.models import AbstractUser

class CustomUserModel(AbstractUser):
    avatar = models.ImageField(upload_to="users/", blank=True, null=True, verbose_name="Fotoğraf")
    phoneNumber = models.CharField(verbose_name="Telefon Numarası", max_length=10, blank=True, null=True)

    class Meta:
        db_table = "auth_user"
        verbose_name_plural="Kullanıcılar"

    def __str__(self):
        return self.username

class AddressModel(models.Model):
    customer = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, verbose_name="Müşteri")
    addressTitle = models.CharField(verbose_name="Adres Başlığı", max_length=50, null=False, blank=False)
    addressCity = models.CharField(max_length=100, verbose_name="Şehir")
    addressText = models.TextField(verbose_name="Adres Detayı", max_length=1000, null=False, blank=False)

    def __str__(self):
        return self.addressTitle
    class Meta:
        db_table = 'Address'
        verbose_name_plural="Adresler"

class FavoriteModel(models.Model):
    customer = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, verbose_name="Müşteri")
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, verbose_name="Ürün")

    def __str__(self):
        return str(self.product)
    class Meta:
        db_table = 'Favorites'
        verbose_name_plural="Favoriler"

class CartModel(models.Model):
    customer = models.ForeignKey(CustomUserModel, on_delete=models.SET_NULL, verbose_name="Müşteri", null=True)
    product = models.ForeignKey(ProductModel, on_delete=models.SET_NULL, verbose_name="Ürün", null=True)
    amount = models.IntegerField(verbose_name="Adet", null=False)

    def __str__(self):
        return str(self.product)
    class Meta:
        db_table = 'Cart'
        verbose_name_plural="Sepet"


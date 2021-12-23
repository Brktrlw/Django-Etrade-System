from django.db import models
from django.contrib.auth.models import User
from PRODUCTS.models import ProductModel

class AddressModel(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Müşteri")
    addressTitle = models.CharField(verbose_name="Adres Başlığı", max_length=50, null=False, blank=False)
    addressCity = models.CharField(max_length=100, verbose_name="Şehir")
    addressText = models.TextField(verbose_name="Adres Detayı", max_length=1000, null=False, blank=False)

    def __str__(self):
        return self.addressTitle

class FavoriteModel(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="Müşteri")
    product  = models.ForeignKey(ProductModel,on_delete=models.CASCADE,verbose_name="Ürün")

    def __str__(self):
        return str(self.product)

class CartModel(models.Model):
    customer = models.ForeignKey(User,on_delete=models.SET_NULL,verbose_name="Müşteri",null=True)
    product  = models.ForeignKey(ProductModel,on_delete=models.SET_NULL,verbose_name="Ürün",null=True)
    amount   = models.IntegerField(verbose_name="Adet",null=False)

    def __str__(self):
        return str(self.product)
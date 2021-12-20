from django.db import models

class ModelProduct(models.Model):
    productTitle       = models.CharField(max_length=50,verbose_name="Ürün İsmi")
    productPrice       = models.CharField(verbose_name="Ürün Fiyatı")
    productDescription = models.TextField(max_length=500,verbose_name="Ürün Açıklaması")
    productImage       = models.ImageField()



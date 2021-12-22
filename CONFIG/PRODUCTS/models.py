from django.db import models
from django.contrib.auth.models import User

class ProductCategorieModel(models.Model):
    categorieTitle = models.CharField(max_length=50,verbose_name="Kategori İsmi")



    def __str__(self):
        return self.categorieTitle

class ProductModel(models.Model):
    productTitle = models.CharField(max_length=50, verbose_name="Ürün İsmi")
    productPrice = models.FloatField(verbose_name="Ürün Fiyatı")
    productDescription = models.TextField(max_length=500, verbose_name="Ürün Açıklaması")
    productImage = models.ImageField(verbose_name="Ürün Görseli", upload_to="media/",blank=True,null=True)
    productShipping = models.BooleanField(default=False,verbose_name="Ücretsiz Kargo Mu",blank=False,null=False)
    productCategorie = models.ManyToManyField(ProductCategorieModel,verbose_name="Kategori")
    def __str__(self):
        return self.productTitle



class AddressModel(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Müşteri")
    addressCity = models.CharField(max_length=100, verbose_name="Şehir")
    addressText = models.TextField(verbose_name="Adres Detayı", max_length=1000, null=False, blank=False)
    addressTitle = models.CharField(verbose_name="Adres Başlığı", max_length=50, null=False, blank=False)

    def __str__(self):
        return self.addressTitle


class OrderModel(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True,
                                 verbose_name="Müşteri")
    date_order = models.DateTimeField(auto_now_add=True, verbose_name="Sipariş Tarihi")
    complete = models.BooleanField(default=False, null=True, blank=False, verbose_name="Tamamlandı mı")
    orderAddress_id = models.ForeignKey(AddressModel, null=True, blank=False, on_delete=models.SET_NULL)
    transaction_id = models.CharField(max_length=200, null=True, verbose_name="İşlem Numarası")

    def __str__(self):
        return str(self.id)


class OrderItemModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.SET_NULL, null=True, verbose_name="Ürün")
    order = models.ForeignKey(OrderModel, on_delete=models.SET_NULL, null=True, verbose_name="Sipariş")
    quantity = models.IntegerField(default=0, null=True, blank=True, verbose_name="Adet")

    def __str__(self):
        return str(self.product)

class CartModel(models.Model):
    customer = models.ForeignKey(User,on_delete=models.SET_NULL,verbose_name="Müşteri",null=True)
    product  = models.ForeignKey(ProductModel,on_delete=models.SET_NULL,verbose_name="Ürün",null=True)
    amount   = models.IntegerField(verbose_name="Adet",null=False)

    def __str__(self):
        return str(self.product)

class FavoriteModel(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="Müşteri")
    product  = models.ForeignKey(ProductModel,on_delete=models.CASCADE,verbose_name="Ürün")

    def __str__(self):
        return str(self.product)
# class ShippingAddress(models.Model):
#    customer = models.ForeignKey(CustomerModel,on_delete=models.SET_NULL,verbose_name="Müşteri")
#    order    = models.ForeignKey(OrderModel,on_delete=models.SET_NULL,null=True)
#    address  =

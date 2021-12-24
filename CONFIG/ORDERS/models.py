from django.db import models
from PRODUCTS.models import ProductModel
from django.contrib.auth.models import User
from USERAPP.models import CustomUserModel,AddressModel

class OrderModel(models.Model):
    customer = models.ForeignKey(CustomUserModel, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Müşteri")
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
# Create your models here.

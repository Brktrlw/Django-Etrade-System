from django.db import models
from PRODUCTS.models import ProductModel
from django.contrib.auth.models import User
from USERAPP.models import CustomUserModel,AddressModel
from unidecode import unidecode
from django.template.defaultfilters import slugify
import random,string
class OrderModel(models.Model):
    customer = models.ForeignKey(CustomUserModel, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Müşteri")
    date_order = models.DateTimeField(auto_now_add=True, verbose_name="Sipariş Tarihi")
    complete = models.BooleanField(default=False, null=True, blank=False, verbose_name="Tamamlandı mı")
    orderAddress = models.ForeignKey(AddressModel, null=True, blank=False, on_delete=models.SET_NULL,verbose_name="Sipariş Adresi")
    #transaction_id = models.CharField(max_length=200, null=True, verbose_name="İşlem Numarası")
    slug = models.SlugField(null=True, unique=True, editable=True)

    def save(self, force_insert=False, force_update=False, using=None,update_fields=None):
        if self.id is None:
            title = str(self.customer.username)+"-"
            title =slugify(unidecode(title))
            self.slug = slugify(unidecode(title))+''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(20))
        super(OrderModel, self).save()

    def __str__(self):
        return str(self.id) +" "+ self.customer.username

    class Meta:
        db_table = 'Orders'
        verbose_name_plural="Siparişler"

class OrderItemModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.SET_NULL, null=True, verbose_name="Ürün")
    order = models.ForeignKey(OrderModel, on_delete=models.SET_NULL, null=True, verbose_name="Sipariş")
    quantity = models.IntegerField(default=0, null=True, blank=True, verbose_name="Adet")

    def __str__(self):
        return str(self.product)
    class Meta:
        db_table = 'Order_Items'
        verbose_name_plural="Sipariş Ürünleri"



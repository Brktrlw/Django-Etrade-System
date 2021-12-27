from django.contrib import admin
from .models import OrderItemModel,OrderModel


admin.site.register(OrderItemModel)
admin.site.register(OrderModel)
# Register your models here.

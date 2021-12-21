# Generated by Django 3.2.7 on 2021-12-21 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('USERAPP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddressModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addressCity', models.CharField(max_length=100, verbose_name='Şehir')),
                ('addressText', models.TextField(max_length=1000, verbose_name='Adres Detayı')),
                ('addressTitle', models.CharField(max_length=50, verbose_name='Adres Başlığı')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='USERAPP.customermodel', verbose_name='Müşteri')),
            ],
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productTitle', models.CharField(max_length=50, verbose_name='Ürün İsmi')),
                ('productPrice', models.FloatField(verbose_name='Ürün Fiyatı')),
                ('productDescription', models.TextField(max_length=500, verbose_name='Ürün Açıklaması')),
                ('productImage', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_order', models.DateTimeField(auto_now_add=True, verbose_name='Sipariş Tarihi')),
                ('complete', models.BooleanField(default=False, null=True, verbose_name='Tamamlandı mı')),
                ('transaction_id', models.CharField(max_length=200, null=True, verbose_name='İşlem Numarası')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='USERAPP.customermodel', verbose_name='Müşteri')),
                ('orderAddress_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='PRODUCTS.addressmodel')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItemModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True, verbose_name='Adet')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='PRODUCTS.ordermodel', verbose_name='Sipariş')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='PRODUCTS.productmodel', verbose_name='Ürün')),
            ],
        ),
    ]

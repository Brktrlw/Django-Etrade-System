# Generated by Django 3.2.7 on 2021-12-27 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('USERAPP', '0016_auto_20211227_1230'),
        ('ORDERS', '0003_auto_20211224_1418'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderitemmodel',
            options={'verbose_name_plural': 'Sipariş Ürünleri'},
        ),
        migrations.AlterModelOptions(
            name='ordermodel',
            options={'verbose_name_plural': 'Siparişler'},
        ),
        migrations.RemoveField(
            model_name='ordermodel',
            name='transaction_id',
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='orderAddress_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='USERAPP.addressmodel', verbose_name='Sipariş Adresi'),
        ),
    ]

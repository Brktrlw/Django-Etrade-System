# Generated by Django 3.2.7 on 2021-12-22 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PRODUCTS', '0008_auto_20211223_0011'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CartModel',
        ),
    ]
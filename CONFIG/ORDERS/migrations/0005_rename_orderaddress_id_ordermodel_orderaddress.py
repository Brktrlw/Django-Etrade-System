# Generated by Django 3.2.7 on 2021-12-27 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ORDERS', '0004_auto_20211227_1230'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordermodel',
            old_name='orderAddress_id',
            new_name='orderAddress',
        ),
    ]

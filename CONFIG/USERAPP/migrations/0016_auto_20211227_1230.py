# Generated by Django 3.2.7 on 2021-12-27 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('USERAPP', '0015_auto_20211224_1416'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='addressmodel',
            options={'verbose_name_plural': 'Adresler'},
        ),
        migrations.AlterModelOptions(
            name='cartmodel',
            options={'verbose_name_plural': 'Sepet'},
        ),
        migrations.AlterModelOptions(
            name='customusermodel',
            options={'verbose_name_plural': 'Kullanıcılar'},
        ),
        migrations.AlterModelOptions(
            name='favoritemodel',
            options={'verbose_name_plural': 'Favoriler'},
        ),
    ]

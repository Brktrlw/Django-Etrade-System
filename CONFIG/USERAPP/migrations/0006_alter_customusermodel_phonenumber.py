# Generated by Django 3.2.7 on 2021-12-23 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('USERAPP', '0005_alter_customusermodel_phonenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusermodel',
            name='phoneNumber',
            field=models.CharField(default=' ', max_length=10, verbose_name='Telefon Numarası'),
        ),
    ]

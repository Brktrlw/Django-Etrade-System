# Generated by Django 3.2.7 on 2021-12-23 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('USERAPP', '0011_alter_customusermodel_phonenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusermodel',
            name='phoneNumber',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Telefon Numarası'),
        ),
    ]
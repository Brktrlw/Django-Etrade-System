# Generated by Django 3.2.7 on 2021-12-24 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('USERAPP', '0012_alter_customusermodel_phonenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusermodel',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='users/', verbose_name='Fotoğraf'),
        ),
    ]

# Generated by Django 3.2.7 on 2021-12-23 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('USERAPP', '0003_auto_20211223_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='customusermodel',
            name='phoneNumber',
            field=models.CharField(default=None, max_length=10, verbose_name='Telefon Numarası'),
        ),
        migrations.AlterField(
            model_name='customusermodel',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='Photos', verbose_name='Fotoğraf'),
        ),
    ]

# Generated by Django 3.2.7 on 2021-12-29 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PRODUCTS', '0009_auto_20211227_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]

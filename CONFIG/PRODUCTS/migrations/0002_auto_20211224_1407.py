# Generated by Django 3.2.7 on 2021-12-24 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PRODUCTS', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='productImage',
            field=models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Ürün Görseli'),
        ),
        migrations.CreateModel(
            name='ProductCommentsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdDate', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PRODUCTS.productmodel', verbose_name='Ürün adı')),
            ],
        ),
    ]
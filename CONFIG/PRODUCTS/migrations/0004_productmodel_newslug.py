# Generated by Django 3.2.7 on 2022-01-20 15:18

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PRODUCTS', '0003_auto_20220120_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='newSlug',
            field=autoslug.fields.AutoSlugField(default='', editable=False, populate_from='productTitle', unique=True),
        ),
    ]

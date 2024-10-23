# Generated by Django 5.0.5 on 2024-10-23 08:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]

# Generated by Django 5.2 on 2025-06-02 10:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
        ('product', '0012_alter_cartitem_product_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='product.cartitem'),
        ),
    ]

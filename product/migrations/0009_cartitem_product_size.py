# Generated by Django 5.2 on 2025-05-29 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_wishlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='product_size',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]

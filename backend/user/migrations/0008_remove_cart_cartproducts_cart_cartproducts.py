# Generated by Django 4.2.2 on 2023-07-03 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0002_products_price'),
        ('user', '0007_remove_cart_cartproducts_cart_cartproducts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='CartProducts',
        ),
        migrations.AddField(
            model_name='cart',
            name='CartProducts',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Products.products', unique=True),
        ),
    ]

# Generated by Django 3.1.3 on 2020-11-17 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_ordercard'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingcart',
            name='order_cards',
            field=models.ManyToManyField(blank=True, to='shop.OrderCard'),
        ),
    ]

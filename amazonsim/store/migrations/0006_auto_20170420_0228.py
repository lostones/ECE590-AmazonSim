# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-20 02:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20170420_0217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='shopping_cart',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.ShoppingCarts'),
        ),
    ]
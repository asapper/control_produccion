# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-18 03:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='quote_total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-06-15 15:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control_produccion', '0002_auto_20160614_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_is_finished',
            field=models.BooleanField(default=False),
        ),
    ]
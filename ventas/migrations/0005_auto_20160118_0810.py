# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-18 08:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0004_auto_20160118_0803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote_finishing',
            name='date_finished',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='quote_finishing',
            name='date_started',
            field=models.DateTimeField(null=True),
        ),
    ]
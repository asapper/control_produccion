# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-18 07:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recursos', '0002_auto_20160118_0709'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='finishing',
            name='quote',
        ),
        migrations.RemoveField(
            model_name='material',
            name='quote',
        ),
        migrations.RemoveField(
            model_name='paper',
            name='quote',
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-09 20:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20170909_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(null=True, upload_to='blog'),
        ),
    ]

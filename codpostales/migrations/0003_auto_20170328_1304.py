# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 11:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codpostales', '0002_auto_20170328_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codigospostales',
            name='codigoPostal',
            field=models.IntegerField(unique=True),
        ),
    ]
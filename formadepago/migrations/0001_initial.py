# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 10:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FormaDePago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('prioridad', models.IntegerField(unique=True)),
                ('dias', models.IntegerField(unique=True)),
            ],
        ),
    ]

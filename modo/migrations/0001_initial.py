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
            name='Modo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('colorPlano', models.BooleanField(default=False)),
                ('bnPlano', models.BooleanField(default=False)),
                ('ColorBnPlano', models.BooleanField(default=False)),
                ('hibridoPlano', models.BooleanField(default=False)),
                ('hibridoBobina', models.BooleanField(default=False)),
                ('hibridoBobinaTom', models.BooleanField(default=False)),
                ('colorBobina', models.BooleanField(default=False)),
                ('colorBobinaTom', models.BooleanField(default=False)),
                ('bnBobina', models.BooleanField(default=False)),
            ],
        ),
    ]
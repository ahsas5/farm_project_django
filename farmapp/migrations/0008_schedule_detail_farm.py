# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-04-08 17:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farmapp', '0007_auto_20190408_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule_detail',
            name='farm',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='farmapp.Farm'),
        ),
    ]

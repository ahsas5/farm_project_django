# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2019-04-08 16:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmapp', '0006_farm_due_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='farm',
            name='due_date',
        ),
        migrations.AddField(
            model_name='schedule_detail',
            name='due_date',
            field=models.DateTimeField(null=True),
        ),
    ]
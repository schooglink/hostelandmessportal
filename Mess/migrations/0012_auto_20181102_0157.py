# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-01 20:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mess', '0011_auto_20181102_0140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messfeedback',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 2, 1, 57, 20, 198762)),
        ),
    ]
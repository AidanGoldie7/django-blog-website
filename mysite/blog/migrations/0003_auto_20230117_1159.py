# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2023-01-17 11:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20230117_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 17, 11, 59, 42, 288284, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 17, 11, 59, 42, 288284, tzinfo=utc)),
        ),
    ]

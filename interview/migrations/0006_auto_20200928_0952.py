# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-09-28 09:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0005_auto_20200928_0829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff_exams',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

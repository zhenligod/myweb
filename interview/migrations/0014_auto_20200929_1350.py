# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-09-29 13:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0013_auto_20200928_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='company_id',
            field=models.CharField(db_index=True, max_length=36),
        ),
        migrations.AlterField(
            model_name='staff_exam_questions',
            name='exam_id',
            field=models.CharField(db_index=True, max_length=36),
        ),
        migrations.AlterField(
            model_name='staff_exams',
            name='company_id',
            field=models.CharField(db_index=True, default=None, max_length=36),
        ),
        migrations.AlterField(
            model_name='staff_exams',
            name='staff_id',
            field=models.CharField(db_index=True, max_length=36),
        ),
    ]

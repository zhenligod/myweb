# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-01 03:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0016_auto_20200929_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='deleted_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='questions',
            name='update_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='staff_exam_questions',
            name='deleted_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='staff_exam_questions',
            name='update_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='staff_exams',
            name='deleted_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='staff_exams',
            name='update_at',
            field=models.DateTimeField(),
        ),
    ]

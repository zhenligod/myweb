# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-09-28 11:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0007_auto_20200928_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff_exam_questions',
            name='exam_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview.Staff_Exams'),
        ),
    ]

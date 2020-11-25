# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import uuid

# Create your models here.


class Staffs(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30)


class Questions(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_id = models.CharField(db_index=True, max_length=36)
    title = models.CharField(max_length=36)
    content = models.TextField()
    pass_rate = models.DecimalField(max_digits=3, decimal_places=1)
    level = models.SmallIntegerField((0, 1, 2), default=0)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    update_at = models.DateTimeField('更新时间', auto_now=True)
    deleted_at = models.DateTimeField('删除时间', null=True, default=None)


class Staff_Exams(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company_id = models.CharField(max_length=36, db_index=True, default=None)
    type = models.SmallIntegerField((0, 1, 2), default=0)
    staff_id = models.CharField(db_index=True, max_length=36)
    is_passed = models.SmallIntegerField((0, 1), default=0)
    answer_count = models.SmallIntegerField(default=0)
    pass_count = models.SmallIntegerField(default=0)
    total_count = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    update_at = models.DateTimeField('更新时间', auto_now=True)
    deleted_at = models.DateTimeField('删除时间', null=True, default=None)

    class Meta:
        index_together = ['company_id', 'staff_id']


class Staff_Exam_Questions(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    exam_id = models.CharField(db_index=True, max_length=36)
    staff_id = models.CharField(max_length=36)
    question_id = models.CharField(max_length=36)
    is_passed = models.SmallIntegerField((0, 1), default=0)
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    update_at = models.DateTimeField('更新时间', auto_now=True)
    deleted_at = models.DateTimeField('删除时间', null=True, default=None)

    class Meta:
        index_together = ['staff_id', 'exam_id']

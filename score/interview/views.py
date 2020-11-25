# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from interview.models import Questions
from interview.models import Staff_Exams
from interview.models import Staff_Exam_Questions
from django.db import transaction
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
from keyring.backends import null
from django.core.paginator import Paginator
from django.core.cache import cache
from django.core.validators import MinLengthValidator, validate_integer
import logging
import json
from random import randint
from interview.form import CreateValidate, IndexValidate, ShowValidate

# Create your views here.

logger = logging.getLogger('django')


def exams(request):
    if request.method == 'GET':
        index_request_form = IndexValidate(request.GET)
        # 判断是否合法
        if not index_request_form.is_valid():
            # 校验失败，直接返回
            return JsonResponse({'code': '1002', 'msg': "staff_id param error"})
        data = []
        pages = {
            'total_count': 0
        }
        currentPage = int(request.GET.get("page", 1))
        pageSize = int(request.GET.get("limit", 10))
        staffId = request.GET.get('staff_id')
        examCount = Staff_Exams.objects.filter(staff_id=staffId).count()
        exams = Staff_Exams.objects.filter(staff_id=staffId).values()
        print request
        if len(exams) == 0:
            return JsonResponse({'code': 0,
                                 'errmsg': 'ok',
                                 'data': data,
                                 'pages': pages})
        paginator = Paginator(exams, pageSize)
        exams = paginator.page(currentPage)
        pages = {
            'num_pages': paginator.num_pages,
            'current_page': currentPage,
            'next_page': exams.next_page_number(),
            'total_count': examCount
        }
        data = list(exams)

        return JsonResponse({'code': 0,
                             'errmsg': 'ok',
                             'data': data,
                             'pages': pages})
    else:
        return JsonResponse({'code': 10012,
                             'errmsg': 'method error!',
                             'data': {}})


def createExams(request):
    if request.method == 'POST':
        createRequestForm = CreateValidate(request.POST)
        if not createRequestForm:
            # 校验失败，直接返回
            return JsonResponse({'code': '1002', 'msg': "param error"})
        staffId = request.POST.get('staff_id')
        companyId = request.POST.get('company_id')
        onlineExamKey = 'online_exam_'+str(staffId)
        data = {}
        with transaction.atomic():
            save_id = transaction.savepoint()
            try:
                questions = Questions.objects.all().order_by('?')[:3]
                staffExam = Staff_Exams.objects.create(
                    type=0,
                    staff_id=staffId,
                    company_id=companyId,
                    is_passed=0,
                    answer_count=0,
                    pass_count=0,
                    total_count=questions.count(),
                )

                staffExamQuestions = []
                for question in questions:
                    staffExamQuestions.append(Staff_Exam_Questions(exam_id=str(staffExam.id), staff_id=staffId,
                                                                   question_id=question.id))
                Staff_Exam_Questions.objects.bulk_create(staffExamQuestions)
                data['id'] = staffExam.id
                data['type'] = staffExam.type
                data['created_at'] = staffExam.created_at
                cache.set(onlineExamKey, staffExam.id, 30*60*60)  # 测试时间半个小时
                return JsonResponse({'code': 0,
                                     'errmsg': 'create exam success!',
                                     'data': data})
            except Exception as e:
                logger.error(e)
                transaction.savepoint_rollback(save_id)
                data['errmsg'] = 'created exam failed'
                return JsonResponse({
                    'code': 10010,
                    'data': e})
            transaction.savepoint_commit(save_id)
        return JsonResponse({'code': 10011,
                             'data': data})
    else:
        return JsonResponse({'code': 10012,
                             'errmsg': 'method error!',
                             'data': {}})


'''
TO DO 调用score判分系统判分统计通过题目
'''


def updateExams(request):
    if request.method == 'PUT':
        examId = request.GET.get('exam_id')
        staffId = request.GET.get('staff_id')
        exams = Staff_Exams.objects.get(examId=examId)
        return JsonResponse({'code': 10011,
                             'data': ""})


def showExam(request):
    staffId = request.GET.get('staff_id')
    examId = request.GET.get('exam_id')
    showRequestForm = ShowValidate(request.GET)
    # 判断是否合法
    if not showRequestForm.is_valid():
        # 校验失败，直接返回
        return JsonResponse({'code': '1002', 'msg': "param error"})
    try:
        exam = Staff_Exams.objects.filter(id=examId).values()
        data = list(exam)
        return JsonResponse({'code': 0,
                             'errmsg': 'ok',
                             'data': data})
    except Exception as e:
        return JsonResponse({'code': 10012,
                             'errmsg': 'get exam data failed',
                             'data': e})


def onlineExam(request):
    staffId = request.GET.get('staff_id')
    onlineExamKey = 'online_exam_'+str(staffId)
    onlineExamId = cache.get(onlineExamKey)
    data = {}
    if staffId:
        data['exam_id'] = onlineExamId
        data['is_online'] = True
        return JsonResponse({'code': 0,
                             'errmsg': 'ok',
                             'data': data})
    else:
        data['is_online'] = False
        return JsonResponse({'code': 0,
                             'errmsg': 'ok',
                             'data': data})

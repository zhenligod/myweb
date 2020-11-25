# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from django.test import Client
from interview.models import Questions
from django.urls import reverse
# Create your tests here.


class QuestionsTestCase(TestCase):
    def test_questions_create_obj(self):
        question = Questions.objects.create(
            company_id = '1c1d665af70e11e58a01080027c93824',
            title = 'question_1',
            content = '过年回老家不在深圳的家，希望公司小伙伴有不回老家在深圳的，有偿付费隔日来家里给猫咪添水添食物清洁便便，50一次，我地址就在南山区..有兴趣爱猫的小伙伴请联系我，两只布偶猫，萌萌哒！...',
            pass_rate = '5.32',
            level = '1',
        )
        self.assertEqual(question.title, 'question_1')


class ExamsTestCase(TestCase):
    def test_exam_get_obj(self):
        c = Client()
        url = "/interview/exams?staff_id=1e550e28eb8311eaac080242ac140007"
        response = c.get(url)
        self.assertEqual(
            response.status_code,
            200,
            'index的状态码不为200'
        )
        if response.context:
            self.assertIn('staff_id', response.context)
            self.assertIn('is_passed', response.context)
            self.assertIn('answer_count', response.context)
            print response.content
        else:
            print "response data is None"

    def test_exam_post_obj(self):
        c = Client()
        url = "/interview/exams/create"
        data = {
            'staff_id': '1e550e28eb8311eaac080242ac140007',
            'company_id': '1c1d665af70e11e58a01080027c93824'
        }
        response = c.post(url, data)
        if response.context:
            self.assertIn('id', response.context)
            self.assertIn('type', response.context)
            self.assertIn('created_at', response.context)
            print response.content
        else:
            print "response data is None"

    def test_exam_show_obj(self):
        c = Client()
        url = "/interview/exams/show?staff_id=1e550e28eb8311eaac080242ac140007&exam_id=6253a8eff8db48659b44e4bce2dfb9ba"
        response = c.get(url)
        self.assertEqual(
            response.status_code,
            200,
            'index的状态码不为200'
        )
        if response.context:
            self.assertIn('staff_id', response.context)
            self.assertIn('is_passed', response.context)
            self.assertIn('answer_count', response.context)
            print response.content
        else:
            print "response data is None"

    def test_exam_online_obj(self):
        c = Client()
        url = "/interview/exams/online?staff_id=1e550e28eb8311eaac080242ac140007"
        response = c.get(url)
        self.assertEqual(
            response.status_code,
            200,
            'index的状态码不为200'
        )
        if response.context:
            self.assertIn('is_online', response.context)
            print response.content
        else:
            print "response data is None"

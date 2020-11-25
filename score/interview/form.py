# -*- coding: utf-8 -*-
from django import forms
from django.forms import widgets

class IndexValidate(forms.Form):
    staff_id = forms.CharField(
        label="staff_id",
        error_messages={"requried": "staff_id is not empty"},
        widget=widgets.TextInput(attrs={"class": "form-control"})
    )

class CreateValidate(forms.Form):
    staff_id = forms.CharField(
        label="staff_id",
        error_messages={"requried": "staff_id is not empty"},
        widget=widgets.TextInput(attrs={"class": "form-control"})
    )

    company_id = forms.CharField(
        label="company_id",
        error_messages={"requried": "company_id is not empty"},
        widget=widgets.TextInput(attrs={"class": "form-control"})
    )

class ShowValidate(forms.Form):
    staff_id = forms.CharField(
        label="staff_id",
        error_messages={"requried": "staff_id is not empty"},
        widget=widgets.TextInput(attrs={"class": "form-control"})
    )

    exam_id = forms.CharField(
        label="exam_id",
        error_messages={"requried": "exam_id is not empty"},
        widget=widgets.TextInput(attrs={"class": "form-control"})
    )

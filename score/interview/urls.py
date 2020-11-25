from django.conf.urls import url, include
from . import views
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from interview.schema import schema


urlpatterns = [
    url(r'^$', views.exams),
    url(r'^exams/create$', views.createExams),
    url(r'^exams/update$', views.updateExams),
    url(r'^exams/show$', views.showExam),
    url(r'^exams/online$', views.onlineExam),
    url(r'^exams$', views.exams),
    url(r'^graphql', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
]
app_name = 'interview'
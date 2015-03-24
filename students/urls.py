from django.conf.urls import patterns, url

from students import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^(?P<student_id>\d+)/$', views.single, name='single'),
                       url(r'^result/(?P<student_id>\d+)$', views.result, name='result'),
                       )
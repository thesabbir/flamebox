from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'flamebox.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^students/', include('students.urls', namespace="students"))
)

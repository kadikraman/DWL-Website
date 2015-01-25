__author__ = 'kadi'

from django.conf.urls import patterns, url

from news import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<story_id>\d+)/$', views.detail, name='detail'),
)
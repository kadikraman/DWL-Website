from django.conf.urls import patterns, url
from . import views


urlpatterns = patterns('',
    url(r'^$', views.NewsView.as_view(), name='news'),
    url(r'^(?P<pk>\d+)/$', views.EntryDetail.as_view(), name='entry_detail'),
)
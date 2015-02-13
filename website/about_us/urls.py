from django.conf.urls import patterns, url
from . import views


urlpatterns = patterns('',
    url(r'^$', views.AboutUsView.as_view(), name='about_us'),
)
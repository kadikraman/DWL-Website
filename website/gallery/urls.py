from django.conf.urls import patterns, url
from . import views


urlpatterns = patterns('',
    url(r'^$', views.GalleryView.as_view(), name='gallery'),
)
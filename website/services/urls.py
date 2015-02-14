from django.conf.urls import patterns, url
from . import views


urlpatterns = patterns('',
    url(r'^$', views.ServicesView.as_view(), name='services'),
    url(r'^events/', views.EventsView.as_view(), name='events'),
    url(r'^photoshoots/', views.PhotoshootsView.as_view(), name='photoshoots'),
    url(r'^stylistics/', views.StylisticsView.as_view(), name='stylistics'),
    url(r'^public_relations/', views.PublicRelationsView.as_view(), name='public_relations'),
)
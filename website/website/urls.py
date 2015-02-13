from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from . import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^news/', include('news.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

# This is for static file serving on the development server
#  - if this line is not present, static files will not be served correctly.
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'%s(?P<path>.*)' % settings.MEDIA_URL[1:], 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT})
    )
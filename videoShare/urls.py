from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from django.contrib import admin
from django.contrib.auth import login
from django.contrib.auth.views import login, logout
from django.conf.urls.defaults import patterns, url
from videoShare.views import *
from django.conf import settings


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

handler404 = 'videoShare.views.custom404'

urlpatterns = patterns('videoShare.views',
    ('^$', home),    
    (r'^accounts/login/$',  login),
    (r'^accounts/logout/$', logout_view),
    (r'^isLog/$', isLog),
    (r'^list/(\d{1,2})/$', 'detail'),
    (r'^accounts/register/$', register),
    (r'^accounts/profiles/$', profile),
    url(r'^upload/$','upload', name='upload'),
    url(r'^list/$', 'list', name='list'),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
	
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))



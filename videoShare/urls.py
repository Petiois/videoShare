from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from django.contrib import admin
from django.contrib.auth import login
from django.contrib.auth.views import login, logout

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Examples:
    # url(r'^$', 'videoShare.views.home', name='home'),
    # url(r'^videoShare/', include('videoShare.foo.urls')),
	(r'^accounts/login/$',  login),
    (r'^accounts/logout/$', logout),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
	
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)

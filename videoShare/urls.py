from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from django.contrib import admin
from django.contrib.auth import login
from django.contrib.auth.views import login, logout
from videoShare.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

handler404 = 'videoShare.views.custom404'

urlpatterns = patterns('',

    ('^$', home),    

	(r'^accounts/login/$',  login),
    (r'^accounts/logout/$', logout),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
	
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)

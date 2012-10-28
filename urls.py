from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns('',
	(r'^', include('videoShare.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))

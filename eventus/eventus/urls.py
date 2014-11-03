from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eventus.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('apps.events.urls')),
)

if settings.DEBUG:
    urlpatterns == patterns("",
        url(r'^media/(?P<path>.*)$', 'django.views.static.server',
            {'document_root': settings.MEDIA_ROOT,}
        ),
    )

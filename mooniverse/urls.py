from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + patterns('',
    url(r'^dj-admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^(?P<slug>.+)/$', 'proto.views.page_view', name='page_view'),
    url(r'^$', 'proto.views.home', name='home'),
)

from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = patterns('',
    # Site URLS
    # url(r'^$', 'web.views.home', name='home'),
    url(r'^$', 'jobs.views.index', name='index'),
    url(r'^about/$', 'jobs.views.about', name='about'),
    url(r'^faq/$', 'jobs.views.faq', name='faq'),
    url(r'^contact/$', 'jobs.views.contact', name='contact'),

    # Haystack Search URL
    url(r'^search/', include('haystack.urls')),
    
    # Django Admin Urls
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


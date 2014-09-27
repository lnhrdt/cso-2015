from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'pages.views.home_page', name='home'),
                       url(r'^about/$', 'pages.views.thelda_page', name='thelda'),
                       url(r'^about/constitution/$', 'pages.views.constitution_page', name='constitution'),
                       url(r'^dates/$', 'pages.views.dates_page', name='dates'),
                       url(r'^colleges/$', 'pages.views.colleges_page', name='colleges'),
                       url(r'^accounts/', include('allauth.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url('', include('django.contrib.auth.urls', namespace='auth')),
                       )

from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^$', 'pages.views.home_page', name='home'),
                       url(r'^about/$', 'pages.views.thecso_page', name='thecso'),
                       url(r'^about/constitution/$', 'pages.views.constitution_page', name='constitution'),
                       url(r'^dates/$', 'pages.views.dates_page', name='dates'),
                       url(r'^colleges/$', 'pages.views.colleges_page', name='colleges'),
                       url(r'^admin/', include(admin.site.urls)),
                       )

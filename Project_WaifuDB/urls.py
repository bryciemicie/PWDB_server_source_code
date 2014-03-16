from django.conf.urls import patterns, include, url
from Project_WaifuDB.globalsettings import appsettings

from Project_WaifuDB.webviews import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Project_WaifuDB.views.home', name='home'),
    # url(r'^Project_WaifuDB/', include('Project_WaifuDB.foo.urls')),

    # User account related urls
    url(r'^accounts/', include('userena.urls')),
    url(r'^messages/', include('userena.contrib.umessages.urls')),

    # Project Waifu URLS
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^waifus/(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if appsettings.DEBUG:
# Serve static files in debug.
    urlpatterns += patterns('',
    (r'^files/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': appsettings.MEDIA_ROOT,
    'show_indexes' : True}),
)
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'digitalgreen.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('core.urls')),
    url(r'^', include('ivr.urls')),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': '/Users/appandey/www/digitalgreen/static/'}),

)
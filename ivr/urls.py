from django.conf.urls import patterns, url

urlpatterns = patterns('ivr.views',
    url(r'^ivr/pass_through/has_interest$', 'hasInterest'),
    url(r'^ivr/pass_through/has_implemented$', 'hasImplemented'),
    url(r'^ivr/pass_through/has_not_implemented$', 'hasNotImplemented'),
    url(r'^ivr/survey/video_id/(?P<video_id>[0-9]+)/mobile_no/(?P<mobile_no>[0-9]+)/$', 'survey'),
)

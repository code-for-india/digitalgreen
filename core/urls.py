from django.conf.urls import patterns, url
from django.conf import settings

urlpatterns = patterns('core.views',
    url(r'^core/videos/', 'video_list'),
    url(r'^core/videos/(?P<pk>[0-9]+)/$$', 'video_detail'),
    url(r'^core/farmers/', 'farmer_list'),
    url(r'^core/farmers/(?P<pk>[0-9]+)/$$', 'farmer_detail'),
    url(r'^core/farmers/video_id/(?P<video_id>[0-9]+)/$$', 'farmer_list_by_videoid'),
    url(r'^core/video_view/video_id/(?P<video_id>[0-9]+)/mobile_no/(?P<mobile_no>[0-9]+)/$', 'video_view'),
    url(r'^core/video_view/video_id/(?P<video_id>[0-9]+)/$', 'video_view_list_by_video_id'),
    url(r'^core/video_view/mobile_no/(?P<mobile_no>[0-9]+)/$', 'video_view_list_by_mobile_no'),
    url(r'^core/video_view_detail/$', 'video_detail_with_context'),
    url(r'^core/video_views/$', 'video_view_list'),
)
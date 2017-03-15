from django.conf.urls import url
from touchscreenrest import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^image/$', views.ImageList.as_view()),
    url(r'^image/(?P<pk>[0-9]+)/$', views.ImageDetail.as_view()),

    url(r'^video/$', views.VideoList.as_view()),
    url(r'^video/(?P<pk>[0-9]+)/$', views.VideoDetail.as_view()),

    url(r'^map/$', views.MapList.as_view()),
    url(r'^map/(?P<pk>[0-9]+)/$', views.MapDetail.as_view()),

    url(r'^advertisement/$', views.AdvertisementList.as_view()),
    url(r'^advertisement/(?P<pk>[0-9]+)/$', views.AdvertisementDetail.as_view()),

    url(r'^activity/$', views.ActivityList.as_view()),
    url(r'^activity/(?P<pk>[0-9]+)/$', views.ActivityDetail.as_view()),

    url(r'^destination/$', views.DestinationList.as_view()),
    url(r'^destination/(?P<pk>[0-9]+)/$', views.DestinationDetail.as_view()),

    url(r'^period/$', views.PeriodList.as_view()),
    url(r'^period/(?P<pk>[0-9]+)/$', views.PeriodDetail.as_view()),

    url(r'^event/$', views.EventList.as_view()),
    url(r'^event/(?P<pk>[0-9]+)/$', views.EventDetail.as_view()),

    url(r'^restaurant/$', views.RestaurantList.as_view()),
    url(r'^restaurant/(?P<pk>[0-9]+)/$', views.RestaurantDetail.as_view()),

    url(r'^tour/$', views.TourList.as_view()),
    url(r'^tour/(?P<pk>[0-9]+)/$', views.TourDetail.as_view()),

    url(r'^accomodation/$', views.AccomodationList.as_view()),
    url(r'^accomodation/(?P<pk>[0-9]+)/$', views.AccomodationDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
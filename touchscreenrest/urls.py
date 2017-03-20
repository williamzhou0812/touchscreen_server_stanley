from django.conf.urls import url
from touchscreenrest import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^image/$', views.ImageList.as_view()),
    url(r'^image/(?P<pk>[0-9]+)/$', views.ImageDetail.as_view()),
    url(r'^imagetour/$', views.ImageTour.as_view()),
    url(r'^imagetour/(?P<pk>[0-9]+)/$', views.ImageTourDetail.as_view()),
    url(r'^imageaccomodation/$', views.ImageAccomodation.as_view()),
    url(r'^imageaccomodation/(?P<pk>[0-9]+)/$', views.ImageAccomodationDetail.as_view()),
    url(r'^imageperiod/$', views.ImagePeriod.as_view()),
    url(r'^imageperiod/(?P<pk>[0-9]+)/$', views.ImagePeriodDetail.as_view()),
    url(r'^imageevent/$', views.ImageEvent.as_view()),
    url(r'^imageevent/(?P<pk>[0-9]+)/$', views.ImageEventDetail.as_view()),
    url(r'^imagerestaurant/$', views.ImageRestaurant.as_view()),
    url(r'^imagerestaurant/(?P<pk>[0-9]+)/$', views.ImageRestaurantDetail.as_view()),
    url(r'^imagedestination/$', views.ImageDestination.as_view()),
    url(r'^imagedestination/(?P<pk>[0-9]+)/$', views.ImageDestinationDetail.as_view()),

    url(r'^video/$', views.VideoList.as_view()),
    url(r'^video/(?P<pk>[0-9]+)/$', views.VideoDetail.as_view()),
    url(r'^videotour/$', views.VideoTour.as_view()),
    url(r'^videotour/(?P<pk>[0-9]+)/$', views.VideoTourDetail.as_view()),
    url(r'^videoaccomodation/$', views.VideoAccomodation.as_view()),
    url(r'^videoaccomodation/(?P<pk>[0-9]+)/$', views.VideoAccomodationDetail.as_view()),
    url(r'^videoperiod/$', views.VideoPeriod.as_view()),
    url(r'^videoperiod/(?P<pk>[0-9]+)/$', views.VideoPeriodDetail.as_view()),
    url(r'^videoevent/$', views.VideoEvent.as_view()),
    url(r'^videoevent/(?P<pk>[0-9]+)/$', views.VideoEventDetail.as_view()),
    url(r'^videorestaurant/$', views.VideoRestaurant.as_view()),
    url(r'^videorestaurant/(?P<pk>[0-9]+)/$', views.VideoRestaurantDetail.as_view()),
    url(r'^videodestination/$', views.VideoDestination.as_view()),
    url(r'^videodestination/(?P<pk>[0-9]+)/$', views.VideoDestinationDetail.as_view()),

    url(r'^map/$', views.MapList.as_view()),
    url(r'^map/(?P<pk>[0-9]+)/$', views.MapDetail.as_view()),
    url(r'^maptour/$', views.MapTour.as_view()),
    url(r'^maptour/(?P<pk>[0-9]+)/$', views.MapTourDetail.as_view()),
    url(r'^maprestaurant/$', views.MapRestaurant.as_view()),
    url(r'^maprestaurant/(?P<pk>[0-9]+)/$', views.MapRestaurantDetail.as_view()),
    url(r'^mapevent/$', views.MapEvent.as_view()),
    url(r'^mapevent/(?P<pk>[0-9]+)/$', views.MapEventDetail.as_view()),
    url(r'^mapaccomodation/$', views.MapAccomodation.as_view()),
    url(r'^mapaccomodation/(?P<pk>[0-9]+)/$', views.MapAccomodationDetail.as_view()),

    url(r'^advertisement/$', views.AdvertisementList.as_view()),
    url(r'^advertisement/(?P<pk>[0-9]+)/$', views.AdvertisementDetail.as_view()),
    url(r'^topdeal/$', views.AdvertisementTopDeal.as_view()),
    url(r'^featuredad/$', views.AdvertisementHighlighted.as_view()),
    url(r'^adstour/$', views.AdvertisementTour.as_view()),
    url(r'^adstour/(?P<pk>[0-9]+)/$', views.AdvertisementTourDetail.as_view()),
    url(r'^adsaccomodation/$', views.AdvertisementAccomodation.as_view()),
    url(r'^adsaccomodation/(?P<pk>[0-9]+)/$', views.AdvertisementAccomodationDetail.as_view()),
    url(r'^adsperiod/$', views.AdvertisementPeriod.as_view()),
    url(r'^adsperiod/(?P<pk>[0-9]+)/$', views.AdvertisementPeriodDetail.as_view()),
    url(r'^adsevent/$', views.AdvertisementEvent.as_view()),
    url(r'^adsevent/(?P<pk>[0-9]+)/$', views.AdvertisementEventDetail.as_view()),
    url(r'^adsrestaurant/$', views.AdvertisementRestaurant.as_view()),
    url(r'^adsrestaurant/(?P<pk>[0-9]+)/$', views.AdvertisementRestaurantDetail.as_view()),
    url(r'^adsdestination/$', views.AdvertisementDestination.as_view()),
    url(r'^adsdestination/(?P<pk>[0-9]+)/$', views.AdvertisementDestinationDetail.as_view()),
    url(r'^adsactivity/$', views.AdvertisementActivity.as_view()),
    url(r'^adsactivity/(?P<pk>[0-9]+)/$', views.AdvertisementActivityDetail.as_view()),

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
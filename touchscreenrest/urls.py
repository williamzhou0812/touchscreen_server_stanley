from django.conf.urls import url
from touchscreenrest import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^image/$', views.ImageList.as_view()),
    url(r'^image/(?P<pk>[0-9]+)/$', views.ImageDetail.as_view()),
    url(r'^imageactivity/$', views.ImageActivity.as_view()),
    url(r'^imageactivity/(?P<pk>[0-9]+)/$', views.ImageActivityDetail.as_view()),
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
    url(r'^imagetransportation/$', views.ImageTransportation.as_view()),
    url(r'^imagetransportation/(?P<pk>[0-9]+)/$', views.ImageTransportationDetail.as_view()),
    url(r'^imageretail/$', views.ImageRetail.as_view()),
    url(r'^imageretail/(?P<pk>[0-9]+)/$', views.ImageRetailDetail.as_view()),
    url(r'^imagemining/$', views.ImageMining.as_view()),
    url(r'^imagemining/(?P<pk>[0-9]+)/$', views.ImageMiningDetail.as_view()),
    url(r'^imageessential/$', views.ImageEssentialService.as_view()),
    url(r'^imageessential/(?P<pk>[0-9]+)/$', views.ImageEssentialServiceDetail.as_view()),
    url(r'^imagedestination/$', views.ImageDestination.as_view()),
    url(r'^imagedestination/(?P<pk>[0-9]+)/$', views.ImageDestinationDetail.as_view()),

    url(r'^video/$', views.VideoList.as_view()),
    url(r'^video/(?P<pk>[0-9]+)/$', views.VideoDetail.as_view()),
    url(r'^videoactivity/$', views.VideoActivity.as_view()),
    url(r'^videoactivity/(?P<pk>[0-9]+)/$', views.VideoActivityDetail.as_view()),
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
    url(r'^videotransportation/$', views.VideoTransportation.as_view()),
    url(r'^videotransportation/(?P<pk>[0-9]+)/$', views.VideoTransportationDetail.as_view()),
    url(r'^videoretail/$', views.VideoRetail.as_view()),
    url(r'^videoretail/(?P<pk>[0-9]+)/$', views.VideoRetailDetail.as_view()),
    url(r'^videomining/$', views.ImageMining.as_view()),
    url(r'^videomining/(?P<pk>[0-9]+)/$', views.ImageMiningDetail.as_view()),
    url(r'^videoessential/$', views.VideoEssentialService.as_view()),
    url(r'^videoessential/(?P<pk>[0-9]+)/$', views.VideoEssentialServiceDetail.as_view()),
    url(r'^videodestination/$', views.VideoDestination.as_view()),
    url(r'^videodestination/(?P<pk>[0-9]+)/$', views.VideoDestinationDetail.as_view()),

    url(r'^map/$', views.MapList.as_view()),
    url(r'^map/(?P<pk>[0-9]+)/$', views.MapDetail.as_view()),
    url(r'^maptour/$', views.MapTour.as_view()),
    url(r'^maptour/(?P<pk>[0-9]+)/$', views.MapTourDetail.as_view()),
    url(r'^maprestaurant/$', views.MapRestaurant.as_view()),
    url(r'^maprestaurant/(?P<pk>[0-9]+)/$', views.MapRestaurantDetail.as_view()),
    url(r'^maptransportation/$', views.MapTransportation.as_view()),
    url(r'^maptransportation/(?P<pk>[0-9]+)/$', views.MapTransportationDetail.as_view()),
    url(r'^mapretail/$', views.MapRetail.as_view()),
    url(r'^mapretail/(?P<pk>[0-9]+)/$', views.MapRetailDetail.as_view()),
    url(r'^mapmining/$', views.MapMining.as_view()),
    url(r'^mapmining/(?P<pk>[0-9]+)/$', views.MapMiningDetail.as_view()),
    url(r'^mapessential/$', views.MapEssentialService.as_view()),
    url(r'^mapessential/(?P<pk>[0-9]+)/$', views.MapEssentialServiceDetail.as_view()),
    url(r'^mapevent/$', views.MapEvent.as_view()),
    url(r'^mapevent/(?P<pk>[0-9]+)/$', views.MapEventDetail.as_view()),
    url(r'^mapaccomodation/$', views.MapAccomodation.as_view()),
    url(r'^mapaccomodation/(?P<pk>[0-9]+)/$', views.MapAccomodationDetail.as_view()),

    url(r'^advertisement/$', views.AdvertisementList.as_view()),
    url(r'^advertisement/(?P<pk>[0-9]+)/$', views.AdvertisementDetail.as_view()),
    url(r'^advertisementpost/(?P<pk>[0-9]+)/$', views.AdvertisementPost.as_view()),
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
    url(r'^adstransportation/$', views.AdvertisementTransportation.as_view()),
    url(r'^adstransportation/(?P<pk>[0-9]+)/$', views.AdvertisementTransportationDetail.as_view()),
    url(r'^adsretail/$', views.AdvertisementRetail.as_view()),
    url(r'^adsretail/(?P<pk>[0-9]+)/$', views.AdvertisementRetailDetail.as_view()),
    url(r'^adsmining/$', views.AdvertisementMining.as_view()),
    url(r'^adsmining/(?P<pk>[0-9]+)/$', views.AdvertisementMiningDetail.as_view()),
    url(r'^adsessential/$', views.AdvertisementEssentialService.as_view()),
    url(r'^adsessential/(?P<pk>[0-9]+)/$', views.AdvertisementEssentialServiceDetail.as_view()),
    url(r'^adsdestination/$', views.AdvertisementDestination.as_view()),
    url(r'^adsdestination/(?P<pk>[0-9]+)/$', views.AdvertisementDestinationDetail.as_view()),
    url(r'^adsactivity/$', views.AdvertisementActivity.as_view()),
    url(r'^adsactivity/(?P<pk>[0-9]+)/$', views.AdvertisementActivityDetail.as_view()),

    url(r'^activity/$', views.ActivityList.as_view()),
    url(r'^activity/(?P<pk>[0-9]+)/$', views.ActivityDetail.as_view()),
    url(r'^activitypost/(?P<pk>[0-9]+)/$', views.ActivityPost.as_view()),

    url(r'^destination/$', views.DestinationList.as_view()),
    url(r'^destination/(?P<pk>[0-9]+)/$', views.DestinationDetail.as_view()),
    url(r'^destinationpost/(?P<pk>[0-9]+)/$', views.DestinationPost.as_view()),

    url(r'^period/$', views.PeriodList.as_view()),
    url(r'^period/(?P<pk>[0-9]+)/$', views.PeriodDetail.as_view()),
    url(r'^periodpost/(?P<pk>[0-9]+)/$', views.PeriodPost.as_view()),

    url(r'^event/$', views.EventList.as_view()),
    url(r'^event/(?P<pk>[0-9]+)/$', views.EventDetail.as_view()),
    url(r'^eventpost/(?P<pk>[0-9]+)/$', views.EventPost.as_view()),

    url(r'^restaurant/$', views.RestaurantList.as_view()),
    url(r'^restaurant/(?P<pk>[0-9]+)/$', views.RestaurantDetail.as_view()),
    url(r'^restaurantpost/(?P<pk>[0-9]+)/$', views.RestaurantPost.as_view()),

    url(r'^transportation/$', views.TransportationList.as_view()),
    url(r'^transportation/(?P<pk>[0-9]+)/$', views.TransportationDetail.as_view()),
    url(r'^transportationpost/(?P<pk>[0-9]+)/$', views.TransportationPost.as_view()),

    url(r'^retail/$', views.RetailList.as_view()),
    url(r'^retail/(?P<pk>[0-9]+)/$', views.RetailDetail.as_view()),
    url(r'^retailpost/(?P<pk>[0-9]+)/$', views.RetailPost.as_view()),

    url(r'^mining/$', views.MiningList.as_view()),
    url(r'^mining/(?P<pk>[0-9]+)/$', views.MiningDetail.as_view()),
    url(r'^miningpost/(?P<pk>[0-9]+)/$', views.MiningPost.as_view()),

    url(r'^essential/$', views.EssentialServiceList.as_view()),
    url(r'^essential/(?P<pk>[0-9]+)/$', views.EssentialServiceDetail.as_view()),
    url(r'^essentialpost/(?P<pk>[0-9]+)/$', views.EssentialServicePost.as_view()),

    url(r'^tour/$', views.TourList.as_view()),
    url(r'^tour/(?P<pk>[0-9]+)/$', views.TourDetail.as_view()),
    url(r'^tourpost/(?P<pk>[0-9]+)/$', views.TourPost.as_view()),

    url(r'^accomodation/$', views.AccomodationList.as_view()),
    url(r'^accomodation/(?P<pk>[0-9]+)/$', views.AccomodationDetail.as_view()),
    url(r'^accomodationpost/(?P<pk>[0-9]+)/$', views.AccomodationPost.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
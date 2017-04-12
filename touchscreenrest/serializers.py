from rest_framework import serializers
from touchscreenrest.models import Activity, ActivityDestination, Destination, Period, Event, Restaurant,\
    Transportation, Retail, Mining, EssentialService, Tour, Accomodation, Map, Advertisement, Image, Video,\
    ServiceType

class ImageSerializer(serializers.ModelSerializer):
    imageFile = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Image
        fields = ('id', 'title', 'imageFile')

class VideoSerializer(serializers.ModelSerializer):
    videoFile = serializers.FileField(max_length=None, use_url=True)
    class Meta:
        model = Video
        fields = ('id', 'title', 'isDisplayVideo', 'videoFile')

class AdvertisementSerializer(serializers.ModelSerializer):
    videoAdvertisement = VideoSerializer(many=True, read_only=True)
    imageAdvertisement = ImageSerializer(many=True, read_only=True)
    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'company', 'description', 'address', 'phone', 'email', 'website', 'inTopDeal',
                  'numberOfShows', 'numberOfClicks', 'orderTopDeal', 'highlighted', 'imageAdvertisement',
                  'videoAdvertisement')

class MapSerializer(serializers.ModelSerializer):
    mapImage = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Map
        fields = ('id', 'title', 'mapImage')

class TourSerializer(serializers.ModelSerializer):
    logo = serializers.ImageField(max_length=None, use_url=True)
    videoTour = VideoSerializer(many=True, read_only=True)
    imageTour = ImageSerializer(many=True, read_only=True)
    advertisementTour = AdvertisementSerializer(many=True)
    mapTour = MapSerializer(many=True, read_only=True)
    class Meta:
        model = Tour
        fields = ('id', 'title', 'description', 'address', 'phone', 'email', 'website', 'logo', 'numberOfClicks', 'videoTour', 'imageTour',
                  'advertisementTour', 'mapTour')

class ActivityDestinationSerializer(serializers.ModelSerializer):
    advertisementActivityDestination = AdvertisementSerializer(many=True)
    imageActivityDestination = ImageSerializer(many=True, read_only=True)
    videoActivityDestination = VideoSerializer(many=True, read_only=True)
    tourActivityDestination = TourSerializer(many=True, read_only=True)
    activityTitle = serializers.CharField(read_only=True, source="activity")

    class Meta:
        model = ActivityDestination
        fields = ('id', 'title', 'description', 'activity', 'activityTitle', 'numberOfClicks', 'tourActivityDestination',
                  'imageActivityDestination', 'videoActivityDestination', 'advertisementActivityDestination')

class ActivitySerializer(serializers.ModelSerializer):
    advertisementActivity = AdvertisementSerializer(many=True)
    imageActivity = ImageSerializer(many=True, read_only=True)
    videoActivity = ImageSerializer(many=True, read_only=True)
    activityDestinationActivity = ActivityDestinationSerializer(many=True, read_only=True)
    class Meta:
        model = Activity
        fields = ('id', 'title', 'numberOfClicks', 'advertisementActivity', 'imageActivity', 'videoActivity',
                  'activityDestinationActivity')

class AccomodationSerializer(serializers.ModelSerializer):
    logo = serializers.ImageField(max_length=None, use_url=True)
    videoAccomodation = VideoSerializer(many=True, read_only=True)
    imageAccomodation = ImageSerializer(many=True, read_only=True)
    advertisementAccomodation = AdvertisementSerializer(many=True)
    mapAccomodation = MapSerializer(many=True, read_only=True)
    class Meta:
        model = Accomodation
        fields = ('id', 'title', 'description', 'address', 'phone', 'email', 'website', 'logo',
                  'numberOfClicks', 'order', 'videoAccomodation', 'imageAccomodation',
                  'advertisementAccomodation', 'mapAccomodation')

class EventSerializer(serializers.ModelSerializer):
    videoEvent = VideoSerializer(many=True, read_only=True)
    imageEvent = ImageSerializer(many=True, read_only=True)
    advertisementEvent = AdvertisementSerializer(many=True)
    mapEvent = MapSerializer(many=True, read_only=True)
    class Meta:
        model = Event
        fields = ('id', 'title', 'description', 'location', 'phone', 'email', 'website', 'destination', 'period',
                  'fromEventDate', 'untilEventDate', 'numberOfClicks', 'videoEvent', 'imageEvent', 'advertisementEvent',
                  'mapEvent')

class PeriodSerializer(serializers.ModelSerializer):
    eventPeriod = EventSerializer(many=True)
    videoPeriod = VideoSerializer(many=True, read_only=True)
    imagePeriod = ImageSerializer(many=True, read_only=True)
    advertisementPeriod = AdvertisementSerializer(many=True)
    class Meta:
        model = Period
        fields = ('id', 'title', 'numberOfClicks', 'eventPeriod', 'videoPeriod', 'imagePeriod',
                  'advertisementPeriod')

class RestaurantSerializer(serializers.ModelSerializer):
    logo = serializers.ImageField(max_length=None, use_url=True)
    mapRestaurant = MapSerializer(many=True, read_only=True)
    videoRestaurant = VideoSerializer(many=True, read_only=True)
    imageRestaurant = ImageSerializer(many=True, read_only=True)
    advertisementRestaurant = AdvertisementSerializer(many=True)
    class Meta:
        model = Restaurant
        fields = ('id', 'title', 'description', 'address', 'phone', 'email', 'website', 'logo', 'numberOfClicks',
                  'order', 'mapRestaurant', 'videoRestaurant', 'imageRestaurant', 'advertisementRestaurant')

class TransportationSerializer(serializers.ModelSerializer):
    logo = serializers.ImageField(max_length=None, use_url=True)
    mapTransportation = MapSerializer(many=True, read_only=True)
    videoTransportation = VideoSerializer(many=True, read_only=True)
    imageTransportation = ImageSerializer(many=True, read_only=True)
    advertisementTransportation = AdvertisementSerializer(many=True)
    class Meta:
        model = Transportation
        fields = ('id', 'title', 'description', 'address', 'phone', 'email', 'website', 'logo', 'numberOfClicks',
                  'order', 'mapTransportation', 'videoTransportation', 'imageTransportation',
                  'advertisementTransportation')

class RetailSerializer(serializers.ModelSerializer):
    logo = serializers.ImageField(max_length=None, use_url=True)
    mapRetail = MapSerializer(many=True, read_only=True)
    videoRetail = VideoSerializer(many=True, read_only=True)
    imageRetail = ImageSerializer(many=True, read_only=True)
    advertisementRetail = AdvertisementSerializer(many=True)
    class Meta:
        model = Retail
        fields = ('id', 'title', 'description', 'address', 'phone', 'email', 'website', 'logo', 'numberOfClicks','order',
                  'mapRetail', 'videoRetail', 'imageRetail', 'advertisementRetail')

class MiningSerializer(serializers.ModelSerializer):
    logo = serializers.ImageField(max_length=None, use_url=True)
    mapMining = MapSerializer(many=True, read_only=True)
    videoMining = VideoSerializer(many=True, read_only=True)
    imageMining = ImageSerializer(many=True, read_only=True)
    advertisementMining = AdvertisementSerializer(many=True)
    class Meta:
        model = Mining
        fields = ('id', 'title', 'description', 'address', 'phone', 'email', 'website', 'logo', 'numberOfClicks','order',
                  'mapMining', 'videoMining', 'imageMining', 'advertisementMining')

class EssentialServiceSerializer(serializers.ModelSerializer):
    logo = serializers.ImageField(max_length=None, use_url=True)
    mapEssentialService = MapSerializer(many=True, read_only=True)
    videoEssentialService = VideoSerializer(many=True, read_only=True)
    imageEssentialService = ImageSerializer(many=True, read_only=True)
    advertisementEssentialService = AdvertisementSerializer(many=True)
    class Meta:
        model = EssentialService
        fields = ('id', 'title', 'description', 'address', 'phone', 'email', 'website', 'logo', 'numberOfClicks','order',
                  'mapEssentialService', 'videoEssentialService', 'imageEssentialService',
                  'advertisementEssentialService')

class ServiceTypeTransportationSerializer(serializers.ModelSerializer):
    videoServiceType = VideoSerializer(many=True, read_only=True)
    imageServiceType = ImageSerializer(many=True, read_only=True)
    advertisementServiceType = AdvertisementSerializer(many=True)
    transportationServiceType = TransportationSerializer(many=True)
    class Meta:
        model = ServiceType
        fields = ('id', 'title', 'numberOfClicks', 'transportationServiceType', 'imageServiceType', 'videoServiceType',
                  'advertisementServiceType')

class ServiceTypeRetailSerializer(serializers.ModelSerializer):
    videoServiceType = VideoSerializer(many=True, read_only=True)
    imageServiceType = ImageSerializer(many=True, read_only=True)
    advertisementServiceType = AdvertisementSerializer(many=True)
    retailServiceType = RetailSerializer(many=True)
    class Meta:
        model = ServiceType
        fields = ('id', 'title', 'numberOfClicks', 'retailServiceType', 'imageServiceType', 'videoServiceType',
                  'advertisementServiceType')

class ServiceTypeMiningSerializer(serializers.ModelSerializer):
    videoServiceType = VideoSerializer(many=True, read_only=True)
    imageServiceType = ImageSerializer(many=True, read_only=True)
    advertisementServiceType = AdvertisementSerializer(many=True)
    miningServiceType = MiningSerializer(many=True)
    class Meta:
        model = ServiceType
        fields = ('id', 'title', 'numberOfClicks', 'miningServiceType', 'imageServiceType', 'videoServiceType',
                  'advertisementServiceType')

class ServiceTypeEssentialServiceSerializer(serializers.ModelSerializer):
    videoServiceType = VideoSerializer(many=True, read_only=True)
    imageServiceType = ImageSerializer(many=True, read_only=True)
    advertisementServiceType = AdvertisementSerializer(many=True)
    essentialServiceServiceType = EssentialServiceSerializer(many=True)
    class Meta:
        model = ServiceType
        fields = ('id', 'title', 'numberOfClicks', 'essentialServiceServiceType', 'imageServiceType', 'videoServiceType',
                  'advertisementServiceType')

class ServiceTypeCompleteSerializer(serializers.ModelSerializer):
    videoServiceType = VideoSerializer(many=True, read_only=True)
    imageServiceType = ImageSerializer(many=True, read_only=True)
    advertisementServiceType = AdvertisementSerializer(many=True)
    transportationServiceType = TransportationSerializer(many=True)
    retailServiceType = RetailSerializer(many=True)
    miningServiceType = MiningSerializer(many=True)
    essentialServiceServiceType = EssentialServiceSerializer(many=True)
    class Meta:
        model = ServiceType
        fields = (
        'id', 'title', 'numberOfClicks', 'transportationServiceType', 'retailServiceType', 'miningServiceType',
        'essentialServiceServiceType', 'imageServiceType', 'videoServiceType', 'advertisementServiceType')

class DestinationSerializer(serializers.ModelSerializer):
    videoDestination = VideoSerializer(many=True, read_only=True)
    imageDestination = ImageSerializer(many=True, read_only=True)
    advertisementDestination = AdvertisementSerializer(many=True)
    mapDestination = MapSerializer(many=True, read_only=True)
    class Meta:
        model = Destination
        fields = ('id', 'title', 'description', 'numberOfClicks', 'videoDestination', 'imageDestination',
                  'advertisementDestination', 'mapDestination')

class DestinationAccomodationSerializer(serializers.ModelSerializer):
    videoDestination = VideoSerializer(many=True, read_only=True)
    imageDestination = ImageSerializer(many=True, read_only=True)
    advertisementDestination = AdvertisementSerializer(many=True)
    accomodationDestination = AccomodationSerializer(many=True)
    class Meta:
        model = Destination
        fields = ('id', 'title', 'description', 'numberOfClicks', 'videoDestination', 'imageDestination',
                  'advertisementDestination', 'accomodationDestination')

class DestinationDetailedSerializer(serializers.ModelSerializer):
    eventDestination = EventSerializer(many=True)
    restaurantDestination = RestaurantSerializer(many=True)
    accomodationDestination = AccomodationSerializer(many=True)
    videoDestination = VideoSerializer(many=True, read_only=True)
    imageDestination = ImageSerializer(many=True, read_only=True)
    advertisementDestination = AdvertisementSerializer(many=True)
    mapDestination = MapSerializer(many=True, read_only=True)
    tourDestination = TourSerializer(many=True, read_only=True)
    activityDestinationDestination = ActivityDestinationSerializer(many=True, read_only=True)
    class Meta:
        model = Destination
        fields = ('id', 'title', 'province', 'airport', 'description', 'numberOfClicks', 'eventDestination',
                  'accomodationDestination', 'restaurantDestination', 'videoDestination', 'imageDestination',
                  'advertisementDestination', 'tourDestination', 'mapDestination', 'activityDestinationDestination')
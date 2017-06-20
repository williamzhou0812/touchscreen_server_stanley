from rest_framework import serializers
from touchscreenrest.models import Activity, ActivityDestination, Destination, Period, Event, Restaurant,\
    Transportation, Retail, Mining, EssentialService, Tour, Accomodation, Map, Advertisement, Image, Video,\
    ServiceType, Airport, AirportContact
from django.db.models import Q
from datetime import date

DISPLAY_INDEFINITE = 'INDEFINITE'
DISPLAY_SPECIFY = 'SPECIFY'
DISPLAY_QUERY = Q(display=DISPLAY_INDEFINITE) | Q(display=DISPLAY_SPECIFY) & Q(displayFrom__lte=date.today()) & \
                                                Q(displayTo__gte=date.today())

class ImageSerializer(serializers.ModelSerializer):
    imageFile = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Image
        fields = ('id', 'title', 'isHeaderImage', 'imageFile')

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
                  'videoAdvertisement', 'order', 'redirectTo')

class MapSerializer(serializers.ModelSerializer):
    mapImage = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Map
        fields = ('id', 'title', 'mapImage', 'mapType')

class TourSerializer(serializers.ModelSerializer):
    logo = serializers.ImageField(max_length=None, use_url=True)
    videoTour = VideoSerializer(many=True, read_only=True)
    imageTour = ImageSerializer(many=True, read_only=True)
    # advertisementTour = AdvertisementSerializer(many=True)
    mapTour = MapSerializer(many=True, read_only=True)
    class Meta:
        model = Tour
        fields = ('id', 'title', 'description', 'address', 'phone', 'email', 'website', 'logo', 'numberOfClicks', 'videoTour', 'imageTour',
                  'mapTour')

class ActivityDestinationSerializer(serializers.ModelSerializer):
    # advertisementActivityDestination = AdvertisementSerializer(many=True)
    imageActivityDestination = ImageSerializer(many=True, read_only=True)
    videoActivityDestination = VideoSerializer(many=True, read_only=True)
    tourActivityDestination = serializers.SerializerMethodField('get_tours')
    activityTitle = serializers.CharField(read_only=True, source="activity")

    def get_tours(self, activity_destination):
        queryset = Tour.objects.filter(Q(activityDestination=activity_destination), DISPLAY_QUERY)
        serializer = TourSerializer(queryset, many=True, context=self.context)
        return serializer.data
    class Meta:
        model = ActivityDestination
        fields = ('id', 'title', 'description', 'activity', 'activityTitle', 'numberOfClicks', 'tourActivityDestination',
                  'imageActivityDestination', 'videoActivityDestination')

class ActivityDestinationSerializerSimple(serializers.ModelSerializer):
    class Meta:
        model = ActivityDestination
        fields = ('id', 'title', 'onlyShowSpecificAds')

class ActivitySerializer(serializers.ModelSerializer):
    # advertisementActivity = AdvertisementSerializer(many=True)
    imageActivity = ImageSerializer(many=True, read_only=True)
    videoActivity = ImageSerializer(many=True, read_only=True)
    activityDestinationActivity = serializers.SerializerMethodField('get_destinations')

    def get_destinations(self, activity):
        queryset = ActivityDestination.objects.filter(Q(activity=activity), DISPLAY_QUERY)
        serializer = ActivityDestinationSerializer(queryset, many=True, context=self.context)
        return serializer.data
    class Meta:
        model = Activity
        fields = ('id', 'title', 'numberOfClicks', 'imageActivity', 'videoActivity',
                  'activityDestinationActivity')

class AccomodationSerializer(serializers.ModelSerializer):
    logo = serializers.ImageField(max_length=None, use_url=True)
    videoAccomodation = VideoSerializer(many=True, read_only=True)
    imageAccomodation = ImageSerializer(many=True, read_only=True)
    # advertisementAccomodation = AdvertisementSerializer(many=True)
    mapAccomodation = MapSerializer(many=True, read_only=True)
    class Meta:
        model = Accomodation
        fields = ('id', 'title', 'description', 'address', 'phone', 'email', 'website', 'logo', 'rating',
                  'numberOfClicks', 'order', 'videoAccomodation', 'imageAccomodation',
                  'mapAccomodation')

class AccomodationHeaderSerializer(serializers.ModelSerializer):
    imageAccomodation = ImageSerializer(many=True, read_only=True)
    class Meta:
        model = Accomodation
        fields = ('id', 'title', 'imageAccomodation')


class EventSerializer(serializers.ModelSerializer):
    videoEvent = VideoSerializer(many=True, read_only=True)
    imageEvent = ImageSerializer(many=True, read_only=True)
    # advertisementEvent = AdvertisementSerializer(many=True)
    mapEvent = MapSerializer(many=True, read_only=True)
    class Meta:
        model = Event
        fields = ('id', 'title', 'description', 'location', 'phone', 'email', 'website', 'destination', 'period',
                  'eventDate', 'eventMonth', 'numberOfClicks', 'videoEvent', 'imageEvent', 'mapEvent')

class PeriodSerializer(serializers.ModelSerializer):
    eventPeriod = serializers.SerializerMethodField('get_events')
    videoPeriod = VideoSerializer(many=True, read_only=True)
    imagePeriod = ImageSerializer(many=True, read_only=True)
    # advertisementPeriod = AdvertisementSerializer(many=True)
    class Meta:
        model = Period
        fields = ('id', 'title', 'numberOfClicks', 'eventPeriod', 'videoPeriod', 'imagePeriod')
    def get_events(self, period):
        queryset = Event.objects.filter(Q(period=period), DISPLAY_QUERY)
        serializer = EventSerializer(queryset, many=True, context=self.context)
        return serializer.data

class RestaurantSerializer(serializers.ModelSerializer):
    logo = serializers.ImageField(max_length=None, use_url=True)
    mapRestaurant = MapSerializer(many=True, read_only=True)
    videoRestaurant = VideoSerializer(many=True, read_only=True)
    imageRestaurant = ImageSerializer(many=True, read_only=True)
    # advertisementRestaurant = AdvertisementSerializer(many=True)
    class Meta:
        model = Restaurant
        fields = ('id', 'title', 'description', 'address', 'phone', 'email', 'website', 'cuisine', 'cards', 'price',
                  'takeaway', 'takeawayOther', 'wifi', 'wifiOther', 'parking', 'parkingOther', 'courtesy',
                  'courtesyOther', 'logo', 'numberOfClicks', 'order', 'mapRestaurant', 'videoRestaurant',
                  'imageRestaurant')

class RestaurantSerializerSimple(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'title', 'onlyShowSpecificAds')

class TransportationSerializer(serializers.ModelSerializer):
    logo = serializers.ImageField(max_length=None, use_url=True)
    mapTransportation = MapSerializer(many=True, read_only=True)
    videoTransportation = VideoSerializer(many=True, read_only=True)
    imageTransportation = ImageSerializer(many=True, read_only=True)
    # advertisementTransportation = AdvertisementSerializer(many=True)
    class Meta:
        model = Transportation
        fields = ('id', 'title', 'description', 'address', 'phone', 'email', 'website', 'logo', 'numberOfClicks',
                  'order', 'mapTransportation', 'videoTransportation', 'imageTransportation')

class TransportationSerializerSimple(serializers.ModelSerializer):
    class Meta:
        model = Transportation
        fields = ('id', 'title', 'onlyShowSpecificAds')

class RetailSerializer(serializers.ModelSerializer):
    logo = serializers.ImageField(max_length=None, use_url=True)
    mapRetail = MapSerializer(many=True, read_only=True)
    videoRetail = VideoSerializer(many=True, read_only=True)
    imageRetail = ImageSerializer(many=True, read_only=True)
    # advertisementRetail = AdvertisementSerializer(many=True)
    class Meta:
        model = Retail
        fields = ('id', 'title', 'description', 'address', 'phone', 'email', 'website', 'logo', 'numberOfClicks','order',
                  'mapRetail', 'videoRetail', 'imageRetail')

class RetailSerializerSimple(serializers.ModelSerializer):
    class Meta:
        model = Retail
        fields = ('id', 'title', 'onlyShowSpecificAds')

class MiningSerializer(serializers.ModelSerializer):
    logo = serializers.ImageField(max_length=None, use_url=True)
    mapMining = MapSerializer(many=True, read_only=True)
    videoMining = VideoSerializer(many=True, read_only=True)
    imageMining = ImageSerializer(many=True, read_only=True)
    # advertisementMining = AdvertisementSerializer(many=True)
    class Meta:
        model = Mining
        fields = ('id', 'title', 'description', 'address', 'phone', 'email', 'website', 'logo', 'numberOfClicks','order',
                  'mapMining', 'videoMining', 'imageMining')

class MiningSerializerSimple(serializers.ModelSerializer):
    class Meta:
        model = Mining
        fields = ('id', 'title', 'onlyShowSpecificAds')

class EssentialServiceSerializer(serializers.ModelSerializer):
    logo = serializers.ImageField(max_length=None, use_url=True)
    mapEssentialService = MapSerializer(many=True, read_only=True)
    videoEssentialService = VideoSerializer(many=True, read_only=True)
    imageEssentialService = ImageSerializer(many=True, read_only=True)
    # advertisementEssentialService = AdvertisementSerializer(many=True)
    class Meta:
        model = EssentialService
        fields = ('id', 'title', 'description', 'address', 'phone', 'email', 'website', 'logo', 'numberOfClicks','order',
                  'mapEssentialService', 'videoEssentialService', 'imageEssentialService')

class EssentialServiceSerializerSimple(serializers.ModelSerializer):
    class Meta:
        model = EssentialService
        fields = ('id', 'title', 'onlyShowSpecificAds')

class ServiceTypeTransportationSerializer(serializers.ModelSerializer):
    videoServiceType = VideoSerializer(many=True, read_only=True)
    imageServiceType = ImageSerializer(many=True, read_only=True)
    # advertisementServiceType = AdvertisementSerializer(many=True)
    transportationServiceType = serializers.SerializerMethodField('get_transportation')
    class Meta:
        model = ServiceType
        fields = ('id', 'title', 'numberOfClicks', 'transportationServiceType', 'imageServiceType', 'videoServiceType')
    def get_transportation(self, st):
        queryset = Transportation.objects.filter(Q(serviceType=st), DISPLAY_QUERY)
        serializer = TransportationSerializer(queryset, many=True, context=self.context)
        return serializer.data

class ServiceTypeRetailSerializer(serializers.ModelSerializer):
    videoServiceType = VideoSerializer(many=True, read_only=True)
    imageServiceType = ImageSerializer(many=True, read_only=True)
    # advertisementServiceType = AdvertisementSerializer(many=True)
    retailServiceType = serializers.SerializerMethodField('get_retail')
    class Meta:
        model = ServiceType
        fields = ('id', 'title', 'numberOfClicks', 'retailServiceType', 'imageServiceType', 'videoServiceType')
    def get_retail(self, st):
        queryset = Retail.objects.filter(Q(serviceType=st), DISPLAY_QUERY)
        serializer = RetailSerializer(queryset, many=True, context=self.context)
        return serializer.data

class ServiceTypeMiningSerializer(serializers.ModelSerializer):
    videoServiceType = VideoSerializer(many=True, read_only=True)
    imageServiceType = ImageSerializer(many=True, read_only=True)
    # advertisementServiceType = AdvertisementSerializer(many=True)
    miningServiceType = serializers.SerializerMethodField('get_mining')
    class Meta:
        model = ServiceType
        fields = ('id', 'title', 'numberOfClicks', 'miningServiceType', 'imageServiceType', 'videoServiceType')
    def get_mining(self, st):
        queryset = Mining.objects.filter(Q(serviceType=st), DISPLAY_QUERY)
        serializer = MiningSerializer(queryset, many=True, context=self.context)
        return serializer.data

class ServiceTypeEssentialServiceSerializer(serializers.ModelSerializer):
    videoServiceType = VideoSerializer(many=True, read_only=True)
    imageServiceType = ImageSerializer(many=True, read_only=True)
    # advertisementServiceType = AdvertisementSerializer(many=True)
    essentialServiceServiceType = serializers.SerializerMethodField('get_essential')
    class Meta:
        model = ServiceType
        fields = ('id', 'title', 'numberOfClicks', 'essentialServiceServiceType', 'imageServiceType', 'videoServiceType')
    def get_essential(self, st):
        queryset = EssentialService.objects.filter(Q(serviceType=st), DISPLAY_QUERY)
        serializer = EssentialServiceSerializer(queryset, many=True, context=self.context)
        return serializer.data

class ServiceTypeCompleteSerializer(serializers.ModelSerializer):
    videoServiceType = VideoSerializer(many=True, read_only=True)
    imageServiceType = ImageSerializer(many=True, read_only=True)
    # advertisementServiceType = AdvertisementSerializer(many=True)
    transportationServiceType = serializers.SerializerMethodField('get_transportation')
    retailServiceType = serializers.SerializerMethodField('get_retail')
    miningServiceType = serializers.SerializerMethodField('get_mining')
    essentialServiceServiceType = serializers.SerializerMethodField('get_essential')
    class Meta:
        model = ServiceType
        fields = (
        'id', 'title', 'numberOfClicks', 'transportationServiceType', 'retailServiceType', 'miningServiceType',
        'essentialServiceServiceType', 'imageServiceType', 'videoServiceType')
    def get_transportation(self, st):
        queryset = Transportation.objects.filter(Q(serviceType=st), DISPLAY_QUERY)
        serializer = TransportationSerializer(queryset, many=True, context=self.context)
        return serializer.data

    def get_retail(self, st):
        queryset = Retail.objects.filter(Q(serviceType=st), DISPLAY_QUERY)
        serializer = RetailSerializer(queryset, many=True, context=self.context)
        return serializer.data

    def get_mining(self, st):
        queryset = Mining.objects.filter(Q(serviceType=st), DISPLAY_QUERY)
        serializer = MiningSerializer(queryset, many=True, context=self.context)
        return serializer.data

    def get_essential(self, st):
        queryset = EssentialService.objects.filter(Q(serviceType=st), DISPLAY_QUERY)
        serializer = EssentialServiceSerializer(queryset, many=True, context=self.context)
        return serializer.data

class DestinationSerializer(serializers.ModelSerializer):
    videoDestination = VideoSerializer(many=True, read_only=True)
    imageDestination = ImageSerializer(many=True, read_only=True)
    # advertisementDestination = AdvertisementSerializer(many=True)
    mapDestination = MapSerializer(many=True, read_only=True)
    class Meta:
        model = Destination
        fields = ('id', 'title', 'description', 'province', 'airport', 'numberOfClicks', 'videoDestination',
                  'imageDestination', 'mapDestination')

class DestinationAccomodationSerializer(serializers.ModelSerializer):
    videoDestination = VideoSerializer(many=True, read_only=True)
    imageDestination = ImageSerializer(many=True, read_only=True)
    # advertisementDestination = AdvertisementSerializer(many=True)
    accomodationDestination = serializers.SerializerMethodField('get_accommodation')
    class Meta:
        model = Destination
        fields = ('id', 'title', 'description', 'numberOfClicks', 'videoDestination', 'imageDestination',
                  'accomodationDestination')
    def get_accommodation(self, destination):
        queryset = Accomodation.objects.filter(Q(destination=destination), DISPLAY_QUERY)
        serializer = AccomodationSerializer(queryset, many=True, context=self.context)
        return serializer.data

class DestinationAccomodationHeaderSerializer(serializers.ModelSerializer):
    accomodationDestination = serializers.SerializerMethodField('get_accommodation')
    class Meta:
        model = Destination
        fields = ('id', 'title', 'accomodationDestination')
    def get_accommodation(self, destination):
        queryset = Accomodation.objects.filter(Q(destination=destination), DISPLAY_QUERY)
        serializer = AccomodationSerializer(queryset, many=True, context=self.context)
        return serializer.data

class DestinationDetailedSerializer(serializers.ModelSerializer):
    eventDestination = serializers.SerializerMethodField('get_events')
    restaurantDestination = serializers.SerializerMethodField('get_restaurants')
    accomodationDestination = serializers.SerializerMethodField('get_accommodation')
    videoDestination = VideoSerializer(many=True, read_only=True)
    imageDestination = ImageSerializer(many=True, read_only=True)
    # advertisementDestination = AdvertisementSerializer(many=True)
    mapDestination = MapSerializer(many=True, read_only=True)
    activityDestinationDestination = serializers.SerializerMethodField('get_destination_activity')
    class Meta:
        model = Destination
        fields = ('id', 'title', 'province', 'airport', 'description', 'numberOfClicks', 'eventDestination',
                  'accomodationDestination', 'restaurantDestination', 'videoDestination', 'imageDestination',
                  'mapDestination', 'activityDestinationDestination')
    def get_events(self, destination):
        queryset = Event.objects.filter(Q(destination=destination), DISPLAY_QUERY)
        serializer = EventSerializer(queryset, many=True, context=self.context)
        return serializer.data

    def get_restaurants(self, destination):
        queryset = Restaurant.objects.filter(Q(destination=destination), DISPLAY_QUERY)
        serializer = RestaurantSerializer(queryset, many=True, context=self.context)
        return serializer.data

    def get_accommodation(self, destination):
        queryset = Accomodation.objects.filter(Q(destination=destination), DISPLAY_QUERY)
        serializer = AccomodationSerializer(queryset, many=True, context=self.context)
        return serializer.data

    def get_destination_activity(self, destination):
        queryset = ActivityDestination.objects.filter(Q(destination=destination), DISPLAY_QUERY)
        serializer = ActivityDestinationSerializer(queryset, many=True, context=self.context)
        return serializer.data

class AirportContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirportContact
        fields = ('id', 'title', 'phone', 'fax', 'email')

class AirportSerializer(serializers.ModelSerializer):
    videoAirport = VideoSerializer(many=True, read_only=True)
    imageAirport = ImageSerializer(many=True, read_only=True)
    airportAirportContact = AirportContactSerializer(many=True, read_only=True)
    logo = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Airport
        fields = ('id', 'title', 'header', 'description', 'logo', 'airportAirportContact', 'imageAirport',
                  'videoAirport')

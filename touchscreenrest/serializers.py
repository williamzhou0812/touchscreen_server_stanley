from rest_framework import serializers
from touchscreenrest.models import Activity, Destination, Period, Event, Restaurant, Tour, Accomodation, Map, Advertisement, Image, Video

class ImageSerializer(serializers.ModelSerializer):
    imageFile = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Image
        fields = ('id', 'title', 'isRestaurantLogo', 'isAccomodationLogo')

class VideoSerializer(serializers.ModelSerializer):
    videoFile = serializers.FileField(max_length=None, use_url=True)
    class Meta:
        model = Video
        fields = ('id', 'title', 'videoFile')

class AdvertisementSerializer(serializers.ModelSerializer):
    videoAdvertisement = VideoSerializer(many=True, read_only=True)
    imageAdvertisement = ImageSerializer(many=True, read_only=True)
    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'inTopDeal', 'numberOfShow', 'numberOfClicks',
                  'orderTopDeal', 'highlighted', 'imageAdvertisement', 'videoAdvertisement')

class MapSerializer(serializers.ModelSerializer):
    mapImage = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Map
        fields = ('id', 'title', 'mapImage')

class ActivitySerializer(serializers.ModelSerializer):
    advertisementActivity = AdvertisementSerializer(many=True)
    class Meta:
        model = Activity
        fields = ('id', 'title', 'numberOfClicks', 'advertisementActivity')

class AccomodationSerializer(serializers.ModelSerializer):
    logo = serializers.ImageField(max_length=None, use_url=True)
    videoAccomodation = VideoSerializer(many=True, read_only=True)
    imageAccomodation = ImageSerializer(many=True, read_only=True)
    advertisementAccomodation = AdvertisementSerializer(many=True)
    mapAccomodation = MapSerializer(many=True, read_only=True)
    class Meta:
        model = Accomodation
        fields = ('id', 'title', 'description', 'address', 'phone', 'email', 'logo',
                  'numberOfClicks', 'order', 'videoAccomodation', 'imageAccomodation',
                  'advertisementAccomodation', 'mapAccomodation')

class TourSerializer(serializers.ModelSerializer):
    videoTour = VideoSerializer(many=True, read_only=True)
    imageTour = ImageSerializer(many=True, read_only=True)
    advertisementTour = AdvertisementSerializer(many=True)
    mapTour = MapSerializer(many=True, read_only=True)
    class Meta:
        model = Tour
        fields = ('id', 'title', 'numberOfClick', 'videoTour', 'imageTour', 'advertisementTour',
                  'mapTour')

class EventSerializer(serializers.ModelSerializer):
    videoEvent = VideoSerializer(many=True, read_only=True)
    imageEvent = ImageSerializer(many=True, read_only=True)
    advertisementEvent = AdvertisementSerializer(many=True)
    mapEvent = MapSerializer(many=True, read_only=True)
    class Meta:
        model = Event
        fields = ('id', 'title', 'description', 'fromEventDate', 'untilEventDate', 'numberOfClicks',
                  'videoEvent', 'imageEvent', 'advertisementEvent', 'mapEvent')

class PeriodSerializer(serializers.ModelSerializer):
    eventPeriod = EventSerializer(many=True)
    videoPeriod = VideoSerializer(many=True, read_only=True)
    imagePeriod = ImageSerializer(many=True, read_only=True)
    advertisementPeriod = AdvertisementSerializer(many=True)
    class Meta:
        model = Period
        fields = ('id', 'title', 'numberOfClicks', 'videoPeriod', 'imagePeriod',
                  'advertisementPeriod')

class RestaurantSerializer(serializers.ModelSerializer):
    logo = serializers.ImageField(max_length=None, use_url=True)
    mapRestaurant = MapSerializer(many=True, read_only=True)
    videoRestaurant = VideoSerializer(many=True, read_only=True)
    imageRestaurant = ImageSerializer(many=True, read_only=True)
    advertisementRestaurant = AdvertisementSerializer(many=True)
    class Meta:
        model = Restaurant
        fields = ('id', 'title', 'description', 'address', 'phone', 'email', 'logo', 'numberOfClicks',
                  'order', 'mapRestaurant', 'videoRestaurant', 'imageRestaurant', 'advertisementRestaurant')

class DestinationSerializer(serializers.ModelSerializer):
    eventDestination = EventSerializer(many=True)
    restaurantDestination = RestaurantSerializer(many=True)
    accomodationDestination = AccomodationSerializer(many=True)
    videoDestination = VideoSerializer(many=True, read_only=True)
    imageDestination = ImageSerializer(many=True, read_only=True)
    advertisementDestination = AdvertisementSerializer(many=True)
    class Meta:
        model = Destination
        fields = ('id', 'title', 'numberOfClicks', 'videoDestination', 'imageDestination', 'advertisementDestination')
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
        'imageAdvertisement', 'videoAdvertisement')

class MapSerializer(serializers.ModelSerializer):
    mapImage = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Map
        fields = ('id', 'title', 'mapImage')

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('id', 'title', 'numberOfClicks')

class AccomodationSerializer(serializers.ModelSerializer):
    logo = serializers.ImageField(max_length=None, use_url=True)
    videoAccomodation = VideoSerializer(many=True, read_only=True)
    imageAccomodation = ImageSerializer(many=True, read_only=True)
    class Meta:
        model = Accomodation
        fields = ('id', 'title', 'description', 'address', 'phone', 'email', 'logo',
                  'numberOfClicks', 'videoAccomodation', 'imageAccomodation')

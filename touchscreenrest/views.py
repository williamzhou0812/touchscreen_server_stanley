from touchscreenrest.models import Activity, Destination, Period, Event,Restaurant, Tour, Accomodation, Map,\
    Advertisement, Image, Video
from touchscreenrest.serializers import ImageSerializer, VideoSerializer, AdvertisementSerializer, MapSerializer,\
    ActivitySerializer, AccomodationSerializer, TourSerializer, EventSerializer, PeriodSerializer, RestaurantSerializer,\
    DestinationSerializer
from rest_framework import generics
from rest_framework.response import Response

class ImageList(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class ImageDetail(generics.RetrieveAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class VideoList(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class VideoDetail(generics.RetrieveAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class MapList(generics.ListAPIView):
    queryset = Map.objects.all()
    serializer_class = MapSerializer

class MapDetail(generics.RetrieveAPIView):
    queryset = Map.objects.all()
    serializer_class = MapSerializer

class AdvertisementList(generics.ListAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer

class AdvertisementDetail(generics.RetrieveUpdateAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.numberOfShows = request.data.get("show")
        instance.numberOfClicks = request.data.get("click")
        instance.save()
        serializer = self.get_serializer(instance)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

class ActivityList(generics.ListAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class ActivityDetail(generics.RetrieveUpdateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.numberOfClicks = request.data.get("click")
        instance.save()
        serializer = self.get_serializer(instance)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

class DestinationList(generics.ListAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

class DestinationDetail(generics.RetrieveUpdateAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.numberOfClicks = request.data.get("click")
        instance.save()
        serializer = self.get_serializer(instance)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

class PeriodList(generics.ListAPIView):
    queryset = Period.objects.all()
    serializer_class = PeriodSerializer

class PeriodDetail(generics.RetrieveUpdateAPIView):
    queryset = Period.objects.all()
    serializer_class = PeriodSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.numberOfClicks = request.data.get("click")
        instance.save()
        serializer = self.get_serializer(instance)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

class EventList(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventDetail(generics.RetrieveUpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.numberOfClicks = request.data.get("click")
        instance.save()
        serializer = self.get_serializer(instance)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

class RestaurantList(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class RestaurantDetail(generics.RetrieveUpdateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.numberOfClicks = request.data.get("click")
        instance.save()
        serializer = self.get_serializer(instance)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

class TourList(generics.ListAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer

class TourDetail(generics.RetrieveUpdateAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.numberOfClicks = request.data.get("click")
        instance.save()
        serializer = self.get_serializer(instance)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

class AccomodationList(generics.ListAPIView):
    queryset = Accomodation.objects.all()
    serializer_class = AccomodationSerializer

class AccomodationDetail(generics.RetrieveUpdateAPIView):
    queryset = Accomodation.objects.all()
    serializer_class = AccomodationSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.numberOfClicks = request.data.get("click")
        instance.save()
        serializer = self.get_serializer(instance)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
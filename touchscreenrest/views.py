from touchscreenrest.models import Activity, Destination, Period, Event,Restaurant, Tour, Accomodation, Map,\
    Advertisement, Image, Video
from touchscreenrest.serializers import ImageSerializer, VideoSerializer, AdvertisementSerializer, MapSerializer,\
    ActivitySerializer, AccomodationSerializer, TourSerializer, EventSerializer, PeriodSerializer, RestaurantSerializer,\
    DestinationSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework.status import HTTP_400_BAD_REQUEST
from unicodedata import numeric

class ImageList(ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class ImageDetail(RetrieveAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class VideoList(ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class VideoDetail(RetrieveAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class MapList(ListAPIView):
    queryset = Map.objects.all()
    serializer_class = MapSerializer

class MapDetail(RetrieveAPIView):
    queryset = Map.objects.all()
    serializer_class = MapSerializer

class AdvertisementList(ListAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer

class AdvertisementDetail(APIView):
    def get_object(self, pk):
        try:
            return Advertisement.objects.get(pk=pk)
        except Advertisement.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = AdvertisementSerializer(instance)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        instance = self.get_object(pk)
        #Checking data
        if request.data.get("show") is None and request.data.get("click") is None:
            return Response("No POST input(s) received.", HTTP_400_BAD_REQUEST)

        #Updating attribute number of shows
        if request.data.get("show") is not None:
            #Checking if data received is a number
            try:
                numeric(request.data.get("show"))
            except (TypeError, ValueError):
                return Response("Incorrect POST input 'show' received.", HTTP_400_BAD_REQUEST)
            instance.numberOfShows = request.data.get("show")

        # Updating attribute number of click
        if request.data.get("click") is not None:
            # Checking if data received is a number
            try:
                numeric(request.data.get("click"))
            except (TypeError, ValueError):
                return Response("Incorrect POST input 'click' received.", HTTP_400_BAD_REQUEST)
            instance.numberOfClicks = request.data.get("click")

        #Saving instance before returning response
        instance.save()
        serializer = AdvertisementSerializer(instance)
        return Response(serializer.data)

class ActivityList(ListAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class ActivityDetail(APIView):
    def get_object(self, pk):
        try:
            return Activity.objects.get(pk=pk)
        except Activity.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = ActivitySerializer(instance)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        instance = self.get_object(pk)
        instance.numberOfClicks += 1
        instance.save()
        serializer = ActivitySerializer(instance)
        return Response(serializer.data)

class DestinationList(ListAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

class DestinationDetail(APIView):
    def get_object(self, pk):
        try:
            return Destination.objects.get(pk=pk)
        except Destination.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = DestinationSerializer(instance)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        instance = self.get_object(pk)
        instance.numberOfClicks += 1
        instance.save()
        serializer = DestinationSerializer(instance)
        return Response(serializer.data)

class PeriodList(ListAPIView):
    queryset = Period.objects.all()
    serializer_class = PeriodSerializer

class PeriodDetail(APIView):
    def get_object(self, pk):
        try:
            return Period.objects.get(pk=pk)
        except Period.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = PeriodSerializer(instance)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        instance = self.get_object(pk)
        instance.numberOfClicks += 1
        instance.save()
        serializer = PeriodSerializer(instance)
        return Response(serializer.data)

class EventList(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventDetail(APIView):
    def get_object(self, pk):
        try:
            return Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = EventSerializer(instance)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        instance = self.get_object(pk)
        instance.numberOfClicks += 1
        instance.save()
        serializer = EventSerializer(instance)
        return Response(serializer.data)

class RestaurantList(ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class RestaurantDetail(APIView):
    def get_object(self, pk):
        try:
            return Restaurant.objects.get(pk=pk)
        except Restaurant.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = RestaurantSerializer(instance)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        instance = self.get_object(pk)
        instance.numberOfClicks += 1
        instance.save()
        serializer = RestaurantSerializer(instance)
        return Response(serializer.data)

class TourList(ListAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer

class TourDetail(APIView):
    def get_object(self, pk):
        try:
            return Tour.objects.get(pk=pk)
        except Tour.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = TourSerializer(instance)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        instance = self.get_object(pk)
        instance.numberOfClicks += 1
        instance.save()
        serializer = TourSerializer(instance)
        return Response(serializer.data)

class AccomodationList(ListAPIView):
    queryset = Accomodation.objects.all()
    serializer_class = AccomodationSerializer

class AccomodationDetail(APIView):
    def get_object(self, pk):
        try:
            return Accomodation.objects.get(pk=pk)
        except Accomodation.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        instance = self.get_object(pk)
        serializer = AccomodationSerializer(instance)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        instance = self.get_object(pk)
        instance.numberOfClicks += 1
        instance.save()
        serializer = AccomodationSerializer(instance)
        return Response(serializer.data)

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

class ImageTour(ListAPIView):
    queryset = Image.objects.exclude(tour=None)
    serializer_class = ImageSerializer

class ImageTourDetail(ListAPIView):
    def get_queryset(self):
        return Image.objects.filter(tour_id=self.kwargs['pk'])
    serializer_class = ImageSerializer


class ImageAccomodation(ListAPIView):
    queryset = Image.objects.exclude(accomodation=None)
    serializer_class = ImageSerializer

class ImageAccomodationDetail(ListAPIView):
    def get_queryset(self):
        return Image.objects.filter(accomodation_id=self.kwargs['pk'])
    serializer_class = ImageSerializer


class ImagePeriod(ListAPIView):
    queryset = Image.objects.exclude(period=None)
    serializer_class = ImageSerializer

class ImagePeriodDetail(ListAPIView):
    def get_queryset(self):
        return Image.objects.filter(period_id=self.kwargs['pk'])
    serializer_class = ImageSerializer

class ImageEvent(ListAPIView):
    queryset = Image.objects.exclude(event=None)
    serializer_class = ImageSerializer

class ImageEventDetail(ListAPIView):
    def get_queryset(self):
        return Image.objects.filter(event_id=self.kwargs['pk'])
    serializer_class = ImageSerializer


class ImageRestaurant(ListAPIView):
    queryset = Image.objects.exclude(restaurant=None)
    serializer_class = ImageSerializer

class ImageRestaurantDetail(ListAPIView):
    def get_queryset(self):
        return Image.objects.filter(restaurant_id=self.kwargs['pk'])
    serializer_class = ImageSerializer


class ImageDestination(ListAPIView):
    queryset = Image.objects.exclude(destination=None)
    serializer_class = ImageSerializer

class ImageDestinationDetail(ListAPIView):
    def get_queryset(self):
        return Image.objects.filter(destination_id=self.kwargs['pk'])
    serializer_class = ImageSerializer


class VideoList(ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class VideoDetail(RetrieveAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class VideoTour(ListAPIView):
    queryset = Video.objects.exclude(tour=None)
    serializer_class = VideoSerializer

class VideoTourDetail(ListAPIView):
    def get_queryset(self):
        return Video.objects.filter(tour_id=self.kwargs['pk'])
    serializer_class = VideoSerializer


class VideoAccomodation(ListAPIView):
    queryset = Video.objects.exclude(accomodation=None)
    serializer_class = VideoSerializer

class VideoAccomodationDetail(ListAPIView):
    def get_queryset(self):
        return Video.objects.filter(accomodation_id=self.kwargs['pk'])
    serializer_class = VideoSerializer

class VideoPeriod(ListAPIView):
    queryset = Video.objects.exclude(period=None)
    serializer_class = VideoSerializer

class VideoPeriodDetail(ListAPIView):
    def get_queryset(self):
        return Video.objects.filter(period_id=self.kwargs['pk'])
    serializer_class = VideoSerializer

class VideoEvent(ListAPIView):
    queryset = Video.objects.exclude(event=None)
    serializer_class = VideoSerializer

class VideoEventDetail(ListAPIView):
    def get_queryset(self):
        return Video.objects.filter(event_id=self.kwargs['pk'])
    serializer_class = VideoSerializer


class VideoRestaurant(ListAPIView):
    queryset = Video.objects.exclude(restaurant=None)
    serializer_class = VideoSerializer

class VideoRestaurantDetail(ListAPIView):
    def get_queryset(self):
        return Video.objects.filter(restaurant_id=self.kwargs['pk'])
    serializer_class = VideoSerializer


class VideoDestination(ListAPIView):
    queryset = Video.objects.exclude(destination=None)
    serializer_class = VideoSerializer

class VideoDestinationDetail(ListAPIView):
    def get_queryset(self):
        return Video.objects.filter(destination_id=self.kwargs['pk'])
    serializer_class = VideoSerializer


class MapList(ListAPIView):
    queryset = Map.objects.all()
    serializer_class = MapSerializer

class MapDetail(RetrieveAPIView):
    queryset = Map.objects.all()
    serializer_class = MapSerializer


class MapTour(ListAPIView):
    queryset = Map.objects.exclude(tour=None)
    serializer_class = MapSerializer

class MapTourDetail(ListAPIView):
    def get_queryset(self):
        return Map.objects.filter(tour_id=self.kwargs['pk'])
    serializer_class = MapSerializer

class MapRestaurant(ListAPIView):
    queryset = Map.objects.exclude(restaurant=None)
    serializer_class = MapSerializer

class MapRestaurantDetail(ListAPIView):
    def get_queryset(self):
        return Map.objects.filter(restaurant_id=self.kwargs['pk'])
    serializer_class = MapSerializer

class MapEvent(ListAPIView):
    queryset = Map.objects.exclude(event=None)
    serializer_class = MapSerializer

class MapEventDetail(ListAPIView):
    def get_queryset(self):
        return Map.objects.filter(event_id=self.kwargs['pk'])
    serializer_class = MapSerializer


class MapAccomodation(ListAPIView):
    queryset = Map.objects.exclude(accomodation=None)
    serializer_class = MapSerializer

class MapAccomodationDetail(ListAPIView):
    def get_queryset(self):
        return Map.objects.filter(accomodation_id=self.kwargs['pk'])
    serializer_class = MapSerializer


class AdvertisementList(ListAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer

class AdvertisementDetail(RetrieveAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer

class AdvertisementPost(APIView):
    def get_object(self, pk):
        try:
            return Advertisement.objects.get(pk=pk)
        except Advertisement.DoesNotExist:
            raise Http404

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

class AdvertisementTopDeal(ListAPIView):
    queryset = Advertisement.objects.filter(inTopDeal=True).order_by('orderTopDeal')
    serializer_class = AdvertisementSerializer

class AdvertisementHighlighted(ListAPIView):
    queryset = Advertisement.objects.filter(highlighted=True)
    serializer_class = AdvertisementSerializer


class AdvertisementTour(ListAPIView):
    queryset = Advertisement.objects.exclude(tour=None)
    serializer_class = AdvertisementSerializer

class AdvertisementTourDetail(ListAPIView):
    def get_queryset(self):
        return Advertisement.objects.filter(tour_id=self.kwargs['pk'])
    serializer_class = AdvertisementSerializer


class AdvertisementAccomodation(ListAPIView):
    queryset = Advertisement.objects.exclude(accomodation=None)
    serializer_class = AdvertisementSerializer

class AdvertisementAccomodationDetail(ListAPIView):
    def get_queryset(self):
        return Advertisement.objects.filter(accomodation_id=self.kwargs['pk'])
    serializer_class = AdvertisementSerializer


class AdvertisementPeriod(ListAPIView):
    queryset = Advertisement.objects.exclude(period=None)
    serializer_class = AdvertisementSerializer

class AdvertisementPeriodDetail(ListAPIView):
    def get_queryset(self):
        return Advertisement.objects.filter(period_id=self.kwargs['pk'])
    serializer_class = AdvertisementSerializer


class AdvertisementEvent(ListAPIView):
    queryset = Advertisement.objects.exclude(event=None)
    serializer_class = AdvertisementSerializer

class AdvertisementEventDetail(ListAPIView):
    def get_queryset(self):
        return Advertisement.objects.filter(event_id=self.kwargs['pk'])
    serializer_class = AdvertisementSerializer


class AdvertisementRestaurant(ListAPIView):
    queryset = Advertisement.objects.exclude(restaurant=None)
    serializer_class = AdvertisementSerializer

class AdvertisementRestaurantDetail(ListAPIView):
    def get_queryset(self):
        return Advertisement.objects.filter(restaurant_id=self.kwargs['pk'])
    serializer_class = AdvertisementSerializer


class AdvertisementDestination(ListAPIView):
    queryset = Advertisement.objects.exclude(destination=None)
    serializer_class = AdvertisementSerializer

class AdvertisementDestinationDetail(ListAPIView):
    def get_queryset(self):
        return Advertisement.objects.filter(destination_id=self.kwargs['pk'])
    serializer_class = AdvertisementSerializer


class AdvertisementActivity(ListAPIView):
    queryset = Advertisement.objects.exclude(activity=None)
    serializer_class = AdvertisementSerializer

class AdvertisementActivityDetail(ListAPIView):
    def get_queryset(self):
        return Advertisement.objects.filter(activity_id=self.kwargs['pk'])
    serializer_class = AdvertisementSerializer


class ActivityList(ListAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class ActivityDetail(RetrieveAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class ActivityPost(APIView):
    def get_object(self, pk):
        try:
            return Activity.objects.get(pk=pk)
        except Activity.DoesNotExist:
            raise Http404

    def post(self, request, pk, format=None):
        instance = self.get_object(pk)
        instance.numberOfClicks += 1
        instance.save()
        serializer = ActivitySerializer(instance)
        return Response(serializer.data)

class DestinationList(ListAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

class DestinationDetail(RetrieveAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

class DestinationPost(APIView):
    def get_object(self, pk):
        try:
            return Destination.objects.get(pk=pk)
        except Destination.DoesNotExist:
            raise Http404

    def post(self, request, pk, format=None):
        instance = self.get_object(pk)
        instance.numberOfClicks += 1
        instance.save()
        serializer = DestinationSerializer(instance)
        return Response(serializer.data)

class PeriodList(ListAPIView):
    queryset = Period.objects.all()
    serializer_class = PeriodSerializer

class PeriodDetail(RetrieveAPIView):
    queryset = Period.objects.all()
    serializer_class = PeriodSerializer

class PeriodPost(APIView):
    def get_object(self, pk):
        try:
            return Period.objects.get(pk=pk)
        except Period.DoesNotExist:
            raise Http404

    def post(self, request, pk, format=None):
        instance = self.get_object(pk)
        instance.numberOfClicks += 1
        instance.save()
        serializer = PeriodSerializer(instance)
        return Response(serializer.data)

class EventList(ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventDetail(RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventPost(APIView):
    def get_object(self, pk):
        try:
            return Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            raise Http404

    def post(self, request, pk, format=None):
        instance = self.get_object(pk)
        instance.numberOfClicks += 1
        instance.save()
        serializer = EventSerializer(instance)
        return Response(serializer.data)

class RestaurantList(ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class RestaurantDetail(RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class RestaurantPost(APIView):
    def get_object(self, pk):
        try:
            return Restaurant.objects.get(pk=pk)
        except Restaurant.DoesNotExist:
            raise Http404

    def post(self, request, pk, format=None):
        instance = self.get_object(pk)
        instance.numberOfClicks += 1
        instance.save()
        serializer = RestaurantSerializer(instance)
        return Response(serializer.data)

class TourList(ListAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer

class TourDetail(RetrieveAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer

class TourPost(APIView):
    def get_object(self, pk):
        try:
            return Tour.objects.get(pk=pk)
        except Tour.DoesNotExist:
            raise Http404

    def post(self, request, pk, format=None):
        instance = self.get_object(pk)
        instance.numberOfClicks += 1
        instance.save()
        serializer = TourSerializer(instance)
        return Response(serializer.data)

class AccomodationList(ListAPIView):
    queryset = Accomodation.objects.all()
    serializer_class = AccomodationSerializer

class AccomodationDetail(RetrieveAPIView):
    queryset = Accomodation.objects.all()
    serializer_class = AccomodationSerializer

class AccomodationPost(APIView):
    def get_object(self, pk):
        try:
            return Accomodation.objects.get(pk=pk)
        except Accomodation.DoesNotExist:
            raise Http404

    def post(self, request, pk, format=None):
        instance = self.get_object(pk)
        instance.numberOfClicks += 1
        instance.save()
        serializer = AccomodationSerializer(instance)
        return Response(serializer.data)

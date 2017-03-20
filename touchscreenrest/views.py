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

class ImageTourDetail(APIView):
    def get(self, request, pk, format=None):
        instance = Image.objects.filter(tour_id=pk)
        serializer = ImageSerializer(instance, many=True)
        return Response(serializer.data)


class ImageAccomodation(ListAPIView):
    queryset = Image.objects.exclude(accomodation=None)
    serializer_class = ImageSerializer

class ImageAccomodationDetail(APIView):
    def get(self, request, pk, format=None):
        instance = Image.objects.filter(accomodation_id=pk)
        serializer = ImageSerializer(instance, many=True)
        return Response(serializer.data)


class ImagePeriod(ListAPIView):
    queryset = Image.objects.exclude(period=None)
    serializer_class = ImageSerializer

class ImagePeriodDetail(APIView):
    def get(self, request, pk, format=None):
        instance = Image.objects.filter(period_id=pk)
        serializer = ImageSerializer(instance, many=True)
        return Response(serializer.data)

class ImageEvent(ListAPIView):
    queryset = Image.objects.exclude(event=None)
    serializer_class = ImageSerializer

class ImageEventDetail(APIView):
    def get(self, request, pk, format=None):
        instance = Image.objects.filter(event_id=pk)
        serializer = ImageSerializer(instance, many=True)
        return Response(serializer.data)


class ImageRestaurant(ListAPIView):
    queryset = Image.objects.exclude(restaurant=None)
    serializer_class = ImageSerializer

class ImageRestaurantDetail(APIView):
    def get(self, request, pk, format=None):
        instance = Image.objects.filter(restaurant_id=pk)
        serializer = ImageSerializer(instance, many=True)
        return Response(serializer.data)


class ImageDestination(ListAPIView):
    queryset = Image.objects.exclude(destination=None)
    serializer_class = ImageSerializer

class ImageDestinationDetail(APIView):
    def get(self, request, pk, format=None):
        instance = Image.objects.filter(destination_id=pk)
        serializer = ImageSerializer(instance, many=True)
        return Response(serializer.data)


class VideoList(ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class VideoDetail(RetrieveAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class VideoTour(ListAPIView):
    queryset = Video.objects.exclude(tour=None)
    serializer_class = VideoSerializer

class VideoTourDetail(APIView):
    def get(self, request, pk, format=None):
        instance = Video.objects.filter(tour_id=pk)
        serializer = VideoSerializer(instance, many=True)
        return Response(serializer.data)


class VideoAccomodation(ListAPIView):
    queryset = Video.objects.exclude(accomodation=None)
    serializer_class = VideoSerializer

class VideoAccomodationDetail(APIView):
    def get(self, request, pk, format=None):
        instance = Video.objects.filter(accomodation_id=pk)
        serializer = VideoSerializer(instance, many=True)
        return Response(serializer.data)


class VideoPeriod(ListAPIView):
    queryset = Video.objects.exclude(period=None)
    serializer_class = VideoSerializer

class VideoPeriodDetail(APIView):
    def get(self, request, pk, format=None):
        instance = Video.objects.filter(period_id=pk)
        serializer = VideoSerializer(instance, many=True)
        return Response(serializer.data)

class VideoEvent(ListAPIView):
    queryset = Video.objects.exclude(event=None)
    serializer_class = VideoSerializer

class VideoEventDetail(APIView):
    def get(self, request, pk, format=None):
        instance = Video.objects.filter(event_id=pk)
        serializer = VideoSerializer(instance, many=True)
        return Response(serializer.data)


class VideoRestaurant(ListAPIView):
    queryset = Video.objects.exclude(restaurant=None)
    serializer_class = VideoSerializer

class VideoRestaurantDetail(APIView):
    def get(self, request, pk, format=None):
        instance = Video.objects.filter(restaurant_id=pk)
        serializer = VideoSerializer(instance, many=True)
        return Response(serializer.data)


class VideoDestination(ListAPIView):
    queryset = Video.objects.exclude(destination=None)
    serializer_class = VideoSerializer

class VideoDestinationDetail(APIView):
    def get(self, request, pk, format=None):
        instance = Video.objects.filter(destination_id=pk)
        serializer = VideoSerializer(instance, many=True)
        return Response(serializer.data)

class MapList(ListAPIView):
    queryset = Map.objects.all()
    serializer_class = MapSerializer

class MapDetail(RetrieveAPIView):
    queryset = Map.objects.all()
    serializer_class = MapSerializer


class MapTour(ListAPIView):
    queryset = Map.objects.exclude(tour=None)
    serializer_class = MapSerializer

class MapTourDetail(APIView):
    def get(self, request, pk, format=None):
        instance = Map.objects.filter(tour_id=pk)
        serializer = MapSerializer(instance, many=True)
        return Response(serializer.data)


class MapRestaurant(ListAPIView):
    queryset = Map.objects.exclude(restaurant=None)
    serializer_class = MapSerializer

class MapRestaurantDetail(APIView):
    def get(self, request, pk, format=None):
        instance = Map.objects.filter(restaurant_id=pk)
        serializer = MapSerializer(instance, many=True)
        return Response(serializer.data)


class MapEvent(ListAPIView):
    queryset = Map.objects.exclude(event=None)
    serializer_class = MapSerializer

class MapEventDetail(APIView):
    def get(self, request, pk, format=None):
        instance = Map.objects.filter(event_id=pk)
        serializer = MapSerializer(instance, many=True)
        return Response(serializer.data)


class MapAccomodation(ListAPIView):
    queryset = Map.objects.exclude(accomodation=None)
    serializer_class = MapSerializer

class MapAccomodationDetail(APIView):
    def get(self, request, pk, format=None):
        instance = Map.objects.filter(accomodation_id=pk)
        serializer = MapSerializer(instance, many=True)
        return Response(serializer.data)


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

class AdvertisementTopDeal(ListAPIView):
    queryset = Advertisement.objects.filter(inTopDeal=True).order_by('orderTopDeal')
    serializer_class = AdvertisementSerializer

class AdvertisementHighlighted(ListAPIView):
    queryset = Advertisement.objects.filter(highlighted=True)
    serializer_class = AdvertisementSerializer


class AdvertisementTour(ListAPIView):
    queryset = Advertisement.objects.exclude(tour=None)
    serializer_class = AdvertisementSerializer

class AdvertisementTourDetail(APIView):
    def get(self, request, pk, format=None):
        instance = Advertisement.objects.filter(tour_id=pk)
        serializer = AdvertisementSerializer(instance, many=True)
        return Response(serializer.data)


class AdvertisementAccomodation(ListAPIView):
    queryset = Advertisement.objects.exclude(accomodation=None)
    serializer_class = AdvertisementSerializer

class AdvertisementAccomodationDetail(APIView):
    def get(self, request, pk, format=None):
        instance = Advertisement.objects.filter(accomodation_id=pk)
        serializer = AdvertisementSerializer(instance, many=True)
        return Response(serializer.data)


class AdvertisementPeriod(ListAPIView):
    queryset = Advertisement.objects.exclude(period=None)
    serializer_class = AdvertisementSerializer

class AdvertisementPeriodDetail(APIView):
    def get(self, request, pk, format=None):
        instance = Advertisement.objects.filter(period_id=pk)
        serializer = AdvertisementSerializer(instance, many=True)
        return Response(serializer.data)


class AdvertisementEvent(ListAPIView):
    queryset = Advertisement.objects.exclude(event=None)
    serializer_class = AdvertisementSerializer

class AdvertisementEventDetail(APIView):
    def get(self, request, pk, format=None):
        instance = Advertisement.objects.filter(event_id=pk)
        serializer = AdvertisementSerializer(instance, many=True)
        return Response(serializer.data)


class AdvertisementRestaurant(ListAPIView):
    queryset = Advertisement.objects.exclude(restaurant=None)
    serializer_class = AdvertisementSerializer

class AdvertisementRestaurantDetail(APIView):
    def get(self, request, pk, format=None):
        instance = Advertisement.objects.filter(restaurant_id=pk)
        serializer = AdvertisementSerializer(instance, many=True)
        return Response(serializer.data)


class AdvertisementDestination(ListAPIView):
    queryset = Advertisement.objects.exclude(destination=None)
    serializer_class = AdvertisementSerializer

class AdvertisementDestinationDetail(APIView):
    def get(self, request, pk, format=None):
        instance = Advertisement.objects.filter(destination_id=pk)
        serializer = AdvertisementSerializer(instance, many=True)
        return Response(serializer.data)


class AdvertisementActivity(ListAPIView):
    queryset = Advertisement.objects.exclude(activity=None)
    serializer_class = AdvertisementSerializer

class AdvertisementActivityDetail(APIView):
    def get(self, request, pk, format=None):
        instance = Advertisement.objects.filter(activity_id=pk)
        serializer = AdvertisementSerializer(instance, many=True)
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

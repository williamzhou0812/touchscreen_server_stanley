from touchscreenrest.models import Activity, ActivityDestination, Destination, Period, Event, Restaurant,\
    Transportation, Retail, Mining, EssentialService, Tour, Accomodation, Map, Advertisement, Image, Video,\
    ServiceType, Airport, Trivia
from touchscreenrest.serializers import ImageSerializer, VideoSerializer, AdvertisementSerializer, MapSerializer,\
    ActivitySerializer, AccomodationSerializer, TourSerializer, EventSerializer, PeriodSerializer, RestaurantSerializer,\
    TransportationSerializer, RetailSerializer, MiningSerializer, EssentialServiceSerializer, DestinationSerializer,\
    DestinationDetailedSerializer, ActivityDestinationSerializer, ServiceTypeCompleteSerializer,\
    ServiceTypeTransportationSerializer, ServiceTypeRetailSerializer, ServiceTypeMiningSerializer,\
    ServiceTypeEssentialServiceSerializer, DestinationAccomodationSerializer, AccomodationHeaderSerializer,\
    DestinationAccomodationHeaderSerializer, AirportSerializer, RestaurantSerializerSimple, RetailSerializerSimple, \
    TransportationSerializerSimple, MiningSerializerSimple, EssentialServiceSerializerSimple, \
    ActivityDestinationSerializerSimple, TriviaSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_404_NOT_FOUND
from unicodedata import numeric
from django.db.models import Q
from datetime import date

DISPLAY_INDEFINITE = 'INDEFINITE'
DISPLAY_SPECIFY = 'SPECIFY'
DISPLAY_NONE = 'NOT_DISPLAY'
DISPLAY_QUERY = Q(display=DISPLAY_INDEFINITE) | Q(display=DISPLAY_SPECIFY) & Q(displayFrom__lte=date.today()) \
                                                & Q(displayTo__gte=date.today())
FIRST_LEVEL_AD_ONLY_QUERY = Q(firstLevelAd=True)

def return_success():
    final_response = {'status': 200, 'message': 'OK'}
    return Response(final_response, HTTP_200_OK)

def return_failure(message):
    final_response = {'status': 400, 'message': message}
    return Response(final_response, HTTP_400_BAD_REQUEST)

def return_not_found():
    final_response = {'status': 404, 'message': 'Resource not found'}
    return Response(final_response, HTTP_404_NOT_FOUND)

class ImageList(ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class ImageDetail(RetrieveAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class ImageActivity(ListAPIView):
    queryset = Image.objects.exclude(activity=None)
    serializer_class = ImageSerializer

class ImageActivityDetail(ListAPIView):
    def get_queryset(self):
        return Image.objects.filter(activity_id=self.kwargs['pk'])
    serializer_class = ImageSerializer

class ImageActivityHeader(ListAPIView):
    def get_queryset(self):
        return Image.objects.filter(activity_id=self.kwargs['pk']).\
            filter(isHeaderImage=True).order_by('?')
    serializer_class = ImageSerializer

class ImageActivityDestination(ListAPIView):
    queryset = Image.objects.exclude(activityDestination=None)
    serializer_class = ImageSerializer

class ImageActivityDestinationDetail(ListAPIView):
    def get_queryset(self):
        return Image.objects.filter(activityDestination_id=self.kwargs['pk'])
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

class ImageAccomodationHeader(ListAPIView):
    def get_queryset(self):
        return Image.objects.filter(accomodation_id=self.kwargs['pk']).\
            filter(isHeaderImage=True).order_by('?')
    serializer_class = ImageSerializer

class ImagePeriod(ListAPIView):
    queryset = Image.objects.exclude(period=None)
    serializer_class = ImageSerializer

class ImagePeriodDetail(ListAPIView):
    def get_queryset(self):
        return Image.objects.filter(period_id=self.kwargs['pk'])
    serializer_class = ImageSerializer

class ImagePeriodHeader(ListAPIView):
    def get_queryset(self):
        return Image.objects.filter(period_id=self.kwargs['pk']).\
            filter(isHeaderImage=True).order_by('?')
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

class ImageTransportation(ListAPIView):
    queryset = Image.objects.exclude(transportation=None)
    serializer_class = ImageSerializer

class ImageTransportationDetail(ListAPIView):
    def get_queryset(self):
        return Image.objects.filter(transportation_id=self.kwargs['pk'])
    serializer_class = ImageSerializer

class ImageTransportationHeader(ListAPIView):
    def get_queryset(self):
        return Image.objects.filter(transportation_id=self.kwargs['pk']).\
            filter(isHeaderImage=True).order_by('?')
    serializer_class = ImageSerializer

class ImageRetail(ListAPIView):
    queryset = Image.objects.exclude(retail=None)
    serializer_class = ImageSerializer

class ImageRetailDetail(ListAPIView):
    def get_queryset(self):
        return Image.objects.filter(retail_id=self.kwargs['pk'])
    serializer_class = ImageSerializer

class ImageRetailHeader(ListAPIView):
    def get_queryset(self):
        return Image.objects.filter(retail_id=True).\
            filter(isHeaderImage=True).order_by('?')
    serializer_class = ImageSerializer

class ImageMining(ListAPIView):
    queryset = Image.objects.exclude(mining=None)
    serializer_class = ImageSerializer

class ImageMiningDetail(ListAPIView):
    def get_queryset(self):
        return Image.objects.filter(mining_id=self.kwargs['pk'])
    serializer_class = ImageSerializer

class ImageMiningHeader(ListAPIView):
    def get_queryset(self):
        return Image.objects.filter(mining_id=self.kwargs['pk']).\
            filter(isHeaderImage=True).order_by('?')
    serializer_class = ImageSerializer

class ImageEssentialService(ListAPIView):
    queryset = Image.objects.exclude(essentialservice=None)
    serializer_class = ImageSerializer

class ImageEssentialServiceDetail(ListAPIView):
    def get_queryset(self):
        return Image.objects.filter(essentialservice_id=self.kwargs['pk'])
    serializer_class = ImageSerializer

class ImageEssentialServiceHeader(ListAPIView):
    def get_queryset(self):
        return Image.objects.filter(essentialservice_id=self.kwargs['pk']).\
            filter(isHeaderImage=True).order_by('?')
    serializer_class = ImageSerializer

class ImageDestination(ListAPIView):
    queryset = Image.objects.exclude(destination=None)
    serializer_class = ImageSerializer

class ImageDestinationDetail(ListAPIView):
    def get_queryset(self):
        return Image.objects.filter(destination_id=self.kwargs['pk'])
    serializer_class = ImageSerializer

class ImageDestinationHeader(ListAPIView):
    def get_queryset(self):
        return Image.objects.filter(destination_id=self.kwargs['pk']).\
            filter(isHeaderImage=True).order_by('?')
    serializer_class = ImageSerializer

class ImageServiceType(ListAPIView):
    queryset = Image.objects.exclude(serviceType=None)
    serializer_class = ImageSerializer

class ImageServiceTypeDetail(ListAPIView):
    def get_queryset(self):
        return Image.objects.filter(serviceType_id=self.kwargs['pk'])
    serializer_class = ImageSerializer


class VideoList(ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class VideoDisplay(ListAPIView):
    queryset = Video.objects.filter(isDisplayVideo=True)
    serializer_class = VideoSerializer

class VideoDetail(RetrieveAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

class VideoActivity(ListAPIView):
    queryset = Video.objects.exclude(activity=None)
    serializer_class = VideoSerializer

class VideoActivityDestination(ListAPIView):
    queryset = Video.objects.exclude(activityDestination=None)
    serializer_class = VideoSerializer

class VideoActivityDestinationDetail(ListAPIView):
    def get_queryset(self):
        return Video.objects.filter(activityDestination_id=self.kwargs['pk'])
    serializer_class = VideoSerializer

class VideoActivityDetail(ListAPIView):
    def get_queryset(self):
        return Video.objects.filter(activity_id=self.kwargs['pk'])
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

class VideoTransportation(ListAPIView):
    queryset = Video.objects.exclude(transportation=None)
    serializer_class = VideoSerializer

class VideoTransportationDetail(ListAPIView):
    def get_queryset(self):
        return Video.objects.filter(transportation_id=self.kwargs['pk'])
    serializer_class = VideoSerializer

class VideoRetail(ListAPIView):
    queryset = Video.objects.exclude(retail=None)
    serializer_class = VideoSerializer

class VideoRetailDetail(ListAPIView):
    def get_queryset(self):
        return Video.objects.filter(retail_id=self.kwargs['pk'])
    serializer_class = VideoSerializer

class VideoMining(ListAPIView):
    queryset = Video.objects.exclude(mining=None)
    serializer_class = VideoSerializer

class VideoMiningDetail(ListAPIView):
    def get_queryset(self):
        return Video.objects.filter(mining_id=self.kwargs['pk'])
    serializer_class = VideoSerializer

class VideoEssentialService(ListAPIView):
    queryset = Video.objects.exclude(essentialservice=None)
    serializer_class = VideoSerializer

class VideoEssentialServiceDetail(ListAPIView):
    def get_queryset(self):
        return Video.objects.filter(essentialservice_id=self.kwargs['pk'])
    serializer_class = VideoSerializer

class VideoDestination(ListAPIView):
    queryset = Video.objects.exclude(destination=None)
    serializer_class = VideoSerializer

class VideoDestinationDetail(ListAPIView):
    def get_queryset(self):
        return Video.objects.filter(destination_id=self.kwargs['pk'])
    serializer_class = VideoSerializer

class VideoServiceType(ListAPIView):
    queryset = Video.objects.exclude(serviceType=None)
    serializer_class = VideoSerializer

class VideoServiceTypeDetail(ListAPIView):
    def get_queryset(self):
        return Video.objects.filter(serviceType_id=self.kwargs['pk'])
    serializer_class = VideoSerializer

class VideoPostShow(APIView):
    def get_object(self, pk):
        try:
            return Video.objects.get(pk=pk)
        except Video.DoesNotExist:
            return return_not_found()

    def post(self, request, pk, format=None):
        instance = self.get_object(pk)
        if not isinstance(instance, Video):
            return instance
        instance.numberOfShows += 1
        instance.save()
        return return_success()

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

class MapTransportation(ListAPIView):
    queryset = Map.objects.exclude(transportation=None)
    serializer_class = MapSerializer

class MapTransportationDetail(ListAPIView):
    def get_queryset(self):
        return Map.objects.filter(transportation_id=self.kwargs['pk'])
    serializer_class = MapSerializer

class MapRetail(ListAPIView):
    queryset = Map.objects.exclude(retail=None)
    serializer_class = MapSerializer

class MapRetailDetail(ListAPIView):
    def get_queryset(self):
        return Map.objects.filter(retail_id=self.kwargs['pk'])
    serializer_class = MapSerializer

class MapMining(ListAPIView):
    queryset = Map.objects.exclude(mining=None)
    serializer_class = MapSerializer

class MapMiningDetail(ListAPIView):
    def get_queryset(self):
        return Map.objects.filter(mining_id=self.kwargs['pk'])
    serializer_class = MapSerializer

class MapEssentialService(ListAPIView):
    queryset = Map.objects.exclude(essentialservice=None)
    serializer_class = MapSerializer

class MapEssentialServiceDetail(ListAPIView):
    def get_queryset(self):
        return Map.objects.filter(essentialservice_id=self.kwargs['pk'])
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

class MapDestination(ListAPIView):
    queryset = Map.objects.exclude(destination=None)
    serializer_class = MapSerializer

class MapDestinationDetail(ListAPIView):
    def get_queryset(self):
        return Map.objects.filter(destination_id=self.kwargs['pk'])
    serializer_class = MapSerializer

class AdvertisementList(ListAPIView):
    queryset = Advertisement.objects.filter(DISPLAY_QUERY)
    serializer_class = AdvertisementSerializer

class AdvertisementDetail(RetrieveAPIView):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer

class AdvertisementPostClick(APIView):
    def get_object(self, pk):
        try:
            return Advertisement.objects.get(pk=pk)
        except Advertisement.DoesNotExist:
            return return_not_found()

    def post(self, request, pk, format=None):
        instance = self.get_object(pk)
        if not isinstance(instance, Advertisement):
            return instance
        instance.numberOfClicks += 1
        instance.save()
        return return_success()

class AdvertisementPostShow(APIView):
    def get_object(self, pk):
        try:
            return Advertisement.objects.get(pk=pk)
        except Advertisement.DoesNotExist:
            return return_not_found()

    def post(self, request, pk, format=None):
        instance = self.get_object(pk)
        if not isinstance(instance, Advertisement):
            return instance
        instance.numberOfShows += 1
        instance.save()
        return return_success()

class AdvertisementPostOld(APIView):
    def get_object(self, pk):
        try:
            return Advertisement.objects.get(pk=pk)
        except Advertisement.DoesNotExist:
            return return_not_found()

    def post(self, request, pk, format=None):
        instance = self.get_object(pk)
        #Checking data
        if request.data.get("show") is None and request.data.get("click") is None:
            return return_failure("No POST input(s) received.")

        #Updating attribute number of shows
        if request.data.get("show") is not None:
            #Checking if data received is a number
            try:
                numeric(request.data.get("show"))
            except (TypeError, ValueError):
                return return_failure("Incorrect POST input 'show' received.")
            instance.numberOfShows = request.data.get("show")

        # Updating attribute number of click
        if request.data.get("click") is not None:
            # Checking if data received is a number
            try:
                numeric(request.data.get("click"))
            except (TypeError, ValueError):
                return return_failure("Incorrect POST input 'click' received.")
            instance.numberOfClicks = request.data.get("click")

        #Saving instance before returning response
        instance.save()
        return Response({'click': instance.numberOfClicks,
                         'show': instance.numberOfShows,
                         'id': instance.id,
                         'status': 200,
                         'message': 'OK'
                         }, HTTP_200_OK)

class AdvertisementTopDeal(ListAPIView):
    queryset = Advertisement.objects.filter(Q(inTopDeal=True), DISPLAY_QUERY).order_by('orderTopDeal')
    serializer_class = AdvertisementSerializer

class AdvertisementHighlighted(ListAPIView):
    queryset = Advertisement.objects.filter(Q(highlighted=True), DISPLAY_QUERY)
    serializer_class = AdvertisementSerializer

class AdvertisementTour(ListAPIView):
    queryset = Advertisement.objects.filter(Q(tour_id__isnull=False), DISPLAY_QUERY)
    serializer_class = AdvertisementSerializer

class AdvertisementTourDetail(ListAPIView):
    def get_queryset(self):
        return Advertisement.objects.filter(Q(tour_id=self.kwargs['pk']), DISPLAY_QUERY)
    serializer_class = AdvertisementSerializer

class AdvertisementAccomodation(ListAPIView):
    queryset = Advertisement.objects.filter(Q(accomodation_id__isnull=False), DISPLAY_QUERY)
    serializer_class = AdvertisementSerializer

class AdvertisementAccomodationFirstOnly(ListAPIView):
    queryset = Advertisement.objects.filter(Q(accomodation_id__isnull=False), DISPLAY_QUERY, FIRST_LEVEL_AD_ONLY_QUERY)
    serializer_class = AdvertisementSerializer

class AdvertisementAccomodationDetail(ListAPIView):
    def get_queryset(self):
        return Advertisement.objects.filter(Q(accomodation_id=self.kwargs['pk']), DISPLAY_QUERY)
    serializer_class = AdvertisementSerializer

class AdvertisementPeriod(ListAPIView):
    queryset = Advertisement.objects.filter(Q(period_id__isnull=False), DISPLAY_QUERY)
    serializer_class = AdvertisementSerializer

class AdvertisementPeriodDetail(ListAPIView):
    def get_queryset(self):
        return Advertisement.objects.filter(Q(period_id=self.kwargs['pk']), DISPLAY_QUERY)
    serializer_class = AdvertisementSerializer

class AdvertisementEvent(ListAPIView):
    queryset = Advertisement.objects.filter(Q(event_id__isnull=False), DISPLAY_QUERY)
    serializer_class = AdvertisementSerializer

class AdvertisementEventFirstOnly(ListAPIView):
    queryset = Advertisement.objects.filter(Q(event_id__isnull=False), DISPLAY_QUERY, FIRST_LEVEL_AD_ONLY_QUERY)
    serializer_class = AdvertisementSerializer

class AdvertisementEventDetail(ListAPIView):
    def get_queryset(self):
        return Advertisement.objects.filter(Q(event_id=self.kwargs['pk']), DISPLAY_QUERY)
    serializer_class = AdvertisementSerializer

class AdvertisementRestaurant(ListAPIView):
    queryset = Advertisement.objects.filter(Q(restaurant_id__isnull=False), DISPLAY_QUERY)
    serializer_class = AdvertisementSerializer

class AdvertisementRestaurantFirstOnly(ListAPIView):
    queryset = Advertisement.objects.filter(Q(restaurant_id__isnull=False), DISPLAY_QUERY, FIRST_LEVEL_AD_ONLY_QUERY)
    serializer_class = AdvertisementSerializer

class AdvertisementRestaurantDetail(ListAPIView):
    def get_queryset(self):
        return Advertisement.objects.filter(Q(restaurant_id=self.kwargs['pk']), DISPLAY_QUERY)
    serializer_class = AdvertisementSerializer

class AdvertisementTransportation(ListAPIView):
    queryset = Advertisement.objects.filter(Q(transportation_id__isnull=False), DISPLAY_QUERY)
    serializer_class = AdvertisementSerializer

class AdvertisementTransportationFirstOnly(ListAPIView):
    queryset = Advertisement.objects.filter(Q(transportation_id__isnull=False), DISPLAY_QUERY, FIRST_LEVEL_AD_ONLY_QUERY)
    serializer_class = AdvertisementSerializer

class AdvertisementTransportationDetail(ListAPIView):
    def get_queryset(self):
        return Advertisement.objects.filter(Q(transportation_id=self.kwargs['pk']), DISPLAY_QUERY)
    serializer_class = AdvertisementSerializer

class AdvertisementRetail(ListAPIView):
    queryset = Advertisement.objects.filter(Q(retail_id__isnull=False), DISPLAY_QUERY)
    serializer_class = AdvertisementSerializer

class AdvertisementRetailFirstOnly(ListAPIView):
    queryset = Advertisement.objects.filter(Q(retail_id__isnull=False), DISPLAY_QUERY, FIRST_LEVEL_AD_ONLY_QUERY)
    serializer_class = AdvertisementSerializer

class AdvertisementRetailDetail(ListAPIView):
    def get_queryset(self):
        return Advertisement.objects.filter(Q(retail_id=self.kwargs['pk']), DISPLAY_QUERY)
    serializer_class = AdvertisementSerializer

class AdvertisementMining(ListAPIView):
    queryset = Advertisement.objects.filter(Q(mining_id__isnull=False), DISPLAY_QUERY)
    serializer_class = AdvertisementSerializer

class AdvertisementMiningFirstOnly(ListAPIView):
    queryset = Advertisement.objects.filter(Q(mining_id__isnull=False), DISPLAY_QUERY, FIRST_LEVEL_AD_ONLY_QUERY)
    serializer_class = AdvertisementSerializer

class AdvertisementMiningDetail(ListAPIView):
    def get_queryset(self):
        return Advertisement.objects.filter(Q(mining_id=self.kwargs['pk']), DISPLAY_QUERY)
    serializer_class = AdvertisementSerializer

class AdvertisementEssentialService(ListAPIView):
    queryset = Advertisement.objects.filter(Q(essentialservice_id__isnull=False), DISPLAY_QUERY)
    serializer_class = AdvertisementSerializer

class AdvertisementEssentialServiceFirstOnly(ListAPIView):
    queryset = Advertisement.objects.filter(Q(essentialservice_id__isnull=False), DISPLAY_QUERY,
                                            FIRST_LEVEL_AD_ONLY_QUERY)
    serializer_class = AdvertisementSerializer

class AdvertisementEssentialServiceDetail(ListAPIView):
    def get_queryset(self):
        return Advertisement.objects.filter(Q(essentialservice_id=self.kwargs['pk']), DISPLAY_QUERY)
    serializer_class = AdvertisementSerializer

class AdvertisementDestination(ListAPIView):
    queryset = Advertisement.objects.filter(Q(destination_id__isnull=False), DISPLAY_QUERY)
    serializer_class = AdvertisementSerializer

class AdvertisementDestinationFirstOnly(ListAPIView):
    queryset = Advertisement.objects.filter(Q(destination_id__isnull=False), DISPLAY_QUERY, FIRST_LEVEL_AD_ONLY_QUERY)
    serializer_class = AdvertisementSerializer

class AdvertisementDestinationDetail(ListAPIView):
    def get_queryset(self):
        return Advertisement.objects.filter(Q(destination_id=self.kwargs['pk']), DISPLAY_QUERY)
    serializer_class = AdvertisementSerializer

class AdvertisementActivity(ListAPIView):
    queryset = Advertisement.objects.filter(Q(activity_id__isnull=False), DISPLAY_QUERY)
    serializer_class = AdvertisementSerializer

class AdvertisementActivityDetail(ListAPIView):
    def get_queryset(self):
        return Advertisement.objects.filter(Q(activity_id=self.kwargs['pk']), DISPLAY_QUERY)
    serializer_class = AdvertisementSerializer

class AdvertisementActivityDestination(ListAPIView):
    queryset = Advertisement.objects.filter(Q(activityDestination_id__isnull=False), DISPLAY_QUERY)
    serializer_class = AdvertisementSerializer

class AdvertisementActivityDestinationFirstOnly(ListAPIView):
    queryset = Advertisement.objects.filter(Q(activityDestination_id__isnull=False), DISPLAY_QUERY,
                                            FIRST_LEVEL_AD_ONLY_QUERY)
    serializer_class = AdvertisementSerializer

class AdvertisementActivityDestinationDetail(ListAPIView):
    def get_queryset(self):
        return Advertisement.objects.filter(Q(activityDestination_id=self.kwargs['pk']), DISPLAY_QUERY)
    serializer_class = AdvertisementSerializer

class AdvertisementServiceType(ListAPIView):
    queryset = Advertisement.objects.filter(Q(serviceType_id__isnull=False), DISPLAY_QUERY)
    serializer_class = AdvertisementSerializer

class AdvertisementServiceTypeDetail(ListAPIView):
    def get_queryset(self):
        return Advertisement.objects.filter(Q(serviceType_id=self.kwargs['pk']), DISPLAY_QUERY)
    serializer_class = AdvertisementSerializer

class AdvertisementWithVideos(ListAPIView):
    def get_queryset(self):
        return Advertisement.objects.exclude(videoAdvertisement=None).filter(videoAdvertisement__isDisplayVideo=False)
    serializer_class = AdvertisementSerializer

class AdvertisementServicesFirstOnly(ListAPIView):
    def get_queryset(self):
        return Advertisement.objects.filter(
            Q(essentialservice_id__isnull=False) | Q(transportation_id__isnull=False) | Q(mining_id__isnull=False)
            | Q(retail_id__isnull=False),
            FIRST_LEVEL_AD_ONLY_QUERY, DISPLAY_QUERY
        )
    serializer_class = AdvertisementSerializer

class AdvertisementServices(ListAPIView):
    def get_queryset(self):
        return Advertisement.objects.filter(
            Q(essentialservice_id__isnull=False) | Q(transportation_id__isnull=False) | Q(mining_id__isnull=False)
            | Q(retail_id__isnull=False), DISPLAY_QUERY
        )
    serializer_class = AdvertisementSerializer

class AdvertisementTrivia(ListAPIView):
    queryset = Advertisement.objects.filter(Q(trivia_id__isnull=False), DISPLAY_QUERY)
    serializer_class = AdvertisementSerializer

class ActivityList(ListAPIView):
    queryset = Activity.objects.filter(DISPLAY_QUERY)
    serializer_class = ActivitySerializer

class ActivityDetail(RetrieveAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class ActivityPost(APIView):
    def get_object(self, pk):
        try:
            return Activity.objects.get(pk=pk)
        except Activity.DoesNotExist:
            return return_not_found()

    def post(self, request, pk, format=None):
        instance = self.get_object(pk)
        if not isinstance(instance, Activity):
            return instance
        instance.numberOfClicks += 1
        instance.save()
        return return_success()

class DestinationList(ListAPIView):
    queryset = Destination.objects.filter(DISPLAY_QUERY)
    serializer_class = DestinationSerializer

class DestinationAccomodationList(ListAPIView):
    queryset = Destination.objects.filter(DISPLAY_QUERY)
    serializer_class = DestinationAccomodationSerializer

class DestinationAccomodationHeaderList(ListAPIView):
    queryset = Destination.objects.filter(
        Q(display=DISPLAY_INDEFINITE) | Q(display=DISPLAY_SPECIFY) & Q(displayFrom__lte=date.today())
        & Q(displayTo__gte=date.today())
    )
    serializer_class = DestinationAccomodationHeaderSerializer

class DestinationDetail(RetrieveAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationDetailedSerializer

class DestinationPost(APIView):
    def get_object(self, pk):
        try:
            return Destination.objects.get(pk=pk)
        except Destination.DoesNotExist:
            return return_not_found()

    def post(self, request, pk, format=None):
        instance = self.get_object(pk)
        if not isinstance(instance, Destination):
            return instance
        instance.numberOfClicks += 1
        instance.save()
        return return_success()

class PeriodList(ListAPIView):
    queryset = Period.objects.filter(DISPLAY_QUERY)
    serializer_class = PeriodSerializer

class PeriodDetail(RetrieveAPIView):
    queryset = Period.objects.all()
    serializer_class = PeriodSerializer

class PeriodPost(APIView):
    def get_object(self, pk):
        try:
            return Period.objects.get(pk=pk)
        except Period.DoesNotExist:
            return return_not_found()

    def post(self, request, pk, format=None):
        instance = self.get_object(pk)
        if not isinstance(instance, Period):
            return instance
        instance.numberOfClicks += 1
        instance.save()
        return return_success()

class EventList(ListAPIView):
    queryset = Event.objects.filter(DISPLAY_QUERY)
    serializer_class = EventSerializer

class EventDetail(RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventPost(APIView):
    def get_object(self, pk):
        try:
            return Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            return return_not_found()

    def post(self, request, pk, format=None):
        instance = self.get_object(pk)
        if not isinstance(instance, Event):
            return instance
        instance.numberOfClicks += 1
        instance.save()
        return return_success()

class RestaurantList(ListAPIView):
    queryset = Restaurant.objects.filter(DISPLAY_QUERY)
    serializer_class = RestaurantSerializer

class RestaurantDetail(RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class RestaurantSimpleDetail(RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializerSimple

class RestaurantPost(APIView):
    def get_object(self, pk):
        try:
            return Restaurant.objects.get(pk=pk)
        except Restaurant.DoesNotExist:
            return return_not_found()

    def post(self, request, pk, format=None):
        instance = self.get_object(pk)
        if not isinstance(instance, Restaurant):
            return instance
        instance.numberOfClicks += 1
        instance.save()
        return return_success()

class TransportationList(ListAPIView):
    queryset = Transportation.objects.filter(DISPLAY_QUERY)
    serializer_class = TransportationSerializer

class TransportationDetail(RetrieveAPIView):
    queryset = Transportation.objects.all()
    serializer_class = TransportationSerializer

class TransportationSimpleDetail(RetrieveAPIView):
    queryset = Transportation.objects.all()
    serializer_class = TransportationSerializerSimple

class TransportationPost(APIView):
    def get_object(self, pk):
        try:
            return Transportation.objects.get(pk=pk)
        except Transportation.DoesNotExist:
            return return_not_found()

    def post(self, request, pk, format=None):
        instance = self.get_object(pk)
        if not isinstance(instance, Transportation):
            return instance
        instance.numberOfClicks += 1
        instance.save()
        return return_success()

class RetailList(ListAPIView):
    queryset = Retail.objects.filter(DISPLAY_QUERY)
    serializer_class = RetailSerializer

class RetailDetail(RetrieveAPIView):
    queryset = Retail.objects.all()
    serializer_class = RetailSerializer

class RetailSimpleDetail(RetrieveAPIView):
    queryset = Retail.objects.all()
    serializer_class = RetailSerializerSimple

class RetailPost(APIView):
    def get_object(self, pk):
        try:
            return Retail.objects.get(pk=pk)
        except Retail.DoesNotExist:
            return return_not_found()

    def post(self, request, pk, format=None):
        instance = self.get_object(pk)
        if not isinstance(instance, Retail):
            return instance
        instance.numberOfClicks += 1
        instance.save()
        return return_success()

class MiningList(ListAPIView):
    queryset = Mining.objects.filter(DISPLAY_QUERY)
    serializer_class = MiningSerializer

class MiningDetail(RetrieveAPIView):
    queryset = Mining.objects.all()
    serializer_class = MiningSerializer

class MiningSimpleDetail(RetrieveAPIView):
    queryset = Mining.objects.all()
    serializer_class = MiningSerializerSimple

class MiningPost(APIView):
    def get_object(self, pk):
        try:
            return Mining.objects.get(pk=pk)
        except Mining.DoesNotExist:
            return return_not_found()

    def post(self, request, pk, format=None):
        instance = self.get_object(pk)
        if not isinstance(instance, Mining):
            return instance
        instance.numberOfClicks += 1
        instance.save()
        return return_success()

class EssentialServiceList(ListAPIView):
    queryset = EssentialService.objects.filter(DISPLAY_QUERY)
    serializer_class = EssentialServiceSerializer

class EssentialServiceDetail(RetrieveAPIView):
    queryset = EssentialService.objects.all()
    serializer_class = EssentialServiceSerializer

class EssentialServiceSimpleDetail(RetrieveAPIView):
    queryset = EssentialService.objects.all()
    serializer_class = EssentialServiceSerializerSimple

class EssentialServicePost(APIView):
    def get_object(self, pk):
        try:
            return EssentialService.objects.get(pk=pk)
        except EssentialService.DoesNotExist:
            return return_not_found()

    def post(self, request, pk, format=None):
        instance = self.get_object(pk)
        if not isinstance(instance, EssentialService):
            return instance
        instance.numberOfClicks += 1
        instance.save()
        serializer = EssentialServiceSerializer(instance)
        return return_success()

class TourList(ListAPIView):
    queryset = Tour.objects.filter(DISPLAY_QUERY)
    serializer_class = TourSerializer

class TourDetail(RetrieveAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer

class TourPost(APIView):
    def get_object(self, pk):
        try:
            return Tour.objects.get(pk=pk)
        except Tour.DoesNotExist:
            return return_not_found()

    def post(self, request, pk, format=None):
        instance = self.get_object(pk)
        if not isinstance(instance, Tour):
            return instance
        instance.numberOfClicks += 1
        instance.save()
        return return_success()

class AccomodationList(ListAPIView):
    queryset = Accomodation.objects.filter(DISPLAY_QUERY)
    serializer_class = AccomodationSerializer

class AccomodationHeaderList(ListAPIView):
    queryset = Accomodation.objects.filter(DISPLAY_QUERY)
    serializer_class = AccomodationHeaderSerializer

class AccomodationDetail(RetrieveAPIView):
    queryset = Accomodation.objects.all()
    serializer_class = AccomodationSerializer

class AccomodationPost(APIView):
    def get_object(self, pk):
        try:
            return Accomodation.objects.get(pk=pk)
        except Accomodation.DoesNotExist:
            return return_not_found()

    def post(self, request, pk, format=None):
        instance = self.get_object(pk)
        if not isinstance(instance, Accomodation):
            return instance
        instance.numberOfClicks += 1
        instance.save()
        return return_success()

class ActivityDestinationList(ListAPIView):
    queryset = ActivityDestination.objects.filter(DISPLAY_QUERY)
    serializer_class = ActivityDestinationSerializer

class ActivityDestinationDetail(RetrieveAPIView):
    queryset = ActivityDestination.objects.all()
    serializer_class = ActivityDestinationSerializer

class ActivityDestinationSimpleDetail(RetrieveAPIView):
    queryset = ActivityDestination.objects.all()
    serializer_class = ActivityDestinationSerializerSimple

class ActivityDestinationPost(APIView):
    def get_object(self, pk):
        try:
            return ActivityDestination.objects.get(pk=pk)
        except ActivityDestination.DoesNotExist:
            return return_not_found()

    def post(self, request, pk, format=None):
        instance = self.get_object(pk)
        if not isinstance(instance, ActivityDestination):
            return instance
        instance.numberOfClicks += 1
        instance.save()
        return return_success()

class ServiceTypeCompleteList(ListAPIView):
    queryset = ServiceType.objects.filter(DISPLAY_QUERY)
    serializer_class = ServiceTypeCompleteSerializer

class ServiceTypeDetail(RetrieveAPIView):
    queryset = ServiceType.objects.all()
    serializer_class = ServiceTypeCompleteSerializer

class ServiceTypeTransportationList(ListAPIView):
    queryset = ServiceType.objects.exclude(transportationServiceType=None).filter(DISPLAY_QUERY)
    serializer_class = ServiceTypeTransportationSerializer

class ServiceTypeRetailList(ListAPIView):
    queryset = ServiceType.objects.exclude(retailServiceType=None).filter(DISPLAY_QUERY)
    serializer_class = ServiceTypeRetailSerializer

class ServiceTypeMiningList(ListAPIView):
    queryset = ServiceType.objects.exclude(miningServiceType=None).filter(DISPLAY_QUERY)
    serializer_class = ServiceTypeMiningSerializer

class ServiceTypeEssentialServiceList(ListAPIView):
    queryset = ServiceType.objects.exclude(essentialServiceServiceType=None).filter(DISPLAY_QUERY)
    serializer_class = ServiceTypeEssentialServiceSerializer

class ServiceTypePost(APIView):
    def get_object(self, pk):
        try:
            return ServiceType.objects.get(pk=pk)
        except ServiceType.DoesNotExist:
            return return_not_found()

    def post(self, request, pk, format=None):
        instance = self.get_object(pk)
        if not isinstance(instance, ServiceType):
            return instance
        instance.numberOfClicks += 1
        instance.save()
        return return_success()

class AirportDetail(RetrieveAPIView):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer

class TriviaList(ListAPIView):
    queryset = Trivia.objects.filter(DISPLAY_QUERY)
    serializer_class = TriviaSerializer

class TriviaPost(APIView):
    def get_object(self, pk):
        try:
            return Trivia.objects.get(pk=pk)
        except Trivia.DoesNotExist:
            return return_not_found()

    def post(self, request, pk, format=None):
        instance = self.get_object(pk)
        if not isinstance(instance, Trivia):
            return instance
        instance.numberOfClicks += 1
        instance.save()
        return return_success()

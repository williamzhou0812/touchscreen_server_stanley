from __future__ import unicode_literals
from django.db import models
from django.core.validators import RegexValidator
from datetime import datetime
from django.utils.safestring import mark_safe

phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))


class Activity(models.Model):
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
    title = models.CharField(max_length=200, blank=False)
    numberOfClicks = models.IntegerField(default=0, verbose_name="Number of clicks")

class Destination(models.Model):
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
    title = models.CharField(max_length=200, blank=False)
    numberOfClicks = models.IntegerField(default=0, verbose_name="Number of clicks")

class Period(models.Model):
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
    title = models.CharField(max_length=200, blank=False)
    numberOfClicks = models.IntegerField(default=0, verbose_name="Number of clicks")

class Event(models.Model):
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField(default='')
    fromEventDate = models.DateField(auto_now=False, auto_now_add=False, blank=False, default=datetime.now,
                                     verbose_name="From event date")
    untilEventDate = models.DateField(auto_now=False, auto_now_add=False, blank=False, default=datetime.now,
                                      verbose_name="Until event date")
    numberOfClicks = models.IntegerField(default=0, verbose_name="Number of clicks")
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='eventDestination')
    period = models.ForeignKey(Period, on_delete=models.CASCADE, related_name='eventPeriod')

class Restaurant(models.Model):
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField()
    address = models.CharField(max_length=300, blank=False)
    phone = models.CharField(max_length=16, validators=[phone_regex], blank=False)
    email = models.EmailField(max_length=100)
    logo = models.ImageField(upload_to='restaurant_logos/', blank=True, null=True)
    numberOfClicks = models.IntegerField(default=0, verbose_name="Number of clicks")
    order = models.IntegerField(blank=False, default=0, verbose_name="Restaurant order display")
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='restaurantDestination')
    def image_logo(self):
        return mark_safe('''<img src="%s" />''' % self.logo.url)
    image_logo.short_description = 'Restaurant Logo'

class Transportation(models.Model):
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField()
    address = models.CharField(max_length=300, blank=False)
    phone = models.CharField(max_length=16, validators=[phone_regex], blank=False)
    email = models.EmailField(max_length=100)
    logo = models.ImageField(upload_to='transportation_logos/', blank=True, null=True)
    numberOfClicks = models.IntegerField(default=0, verbose_name="Number of clicks")
    order = models.IntegerField(blank=False, default=0, verbose_name="Transportation order display")
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='transportationDestination')
    def image_logo(self):
        return mark_safe('''<img src="%s" />''' % self.logo.url)
    image_logo.short_description = 'Transportation Logo'
    class Meta:
        verbose_name = 'Car Hire & Transport'

class Retail(models.Model):
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField()
    address = models.CharField(max_length=300, blank=False)
    phone = models.CharField(max_length=16, validators=[phone_regex], blank=False)
    email = models.EmailField(max_length=100)
    logo = models.ImageField(upload_to='retail_logos/', blank=True, null=True)
    numberOfClicks = models.IntegerField(default=0, verbose_name="Number of clicks")
    order = models.IntegerField(blank=False, default=0, verbose_name="Retail order display")
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='retailDestination')
    def image_logo(self):
        return mark_safe('''<img src="%s" />''' % self.logo.url)
    image_logo.short_description = 'Retail Logo'

class Mining(models.Model):
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField()
    address = models.CharField(max_length=300, blank=False)
    phone = models.CharField(max_length=16, validators=[phone_regex], blank=False)
    email = models.EmailField(max_length=100)
    logo = models.ImageField(upload_to='mining_logos/', blank=True, null=True)
    numberOfClicks = models.IntegerField(default=0, verbose_name="Number of clicks")
    order = models.IntegerField(blank=False, default=0, verbose_name="Mining order display")
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='miningDestination')
    def image_logo(self):
        return mark_safe('''<img src="%s" />''' % self.logo.url)
    image_logo.short_description = 'Mining Logo'
    class Meta:
        verbose_name = 'Mining & Resource'

class EssentialService(models.Model):
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField()
    address = models.CharField(max_length=300, blank=False)
    phone = models.CharField(max_length=16, validators=[phone_regex], blank=False)
    email = models.EmailField(max_length=100)
    logo = models.ImageField(upload_to='retail_logos/', blank=True, null=True)
    numberOfClicks = models.IntegerField(default=0, verbose_name="Number of clicks")
    order = models.IntegerField(blank=False, default=0, verbose_name="Essential Service order display")
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='essentialServiceDestination')
    def image_logo(self):
        return mark_safe('''<img src="%s" />''' % self.logo.url)
    image_logo.short_description = 'Essential Service Logo'
    class Meta:
        verbose_name = 'Essential Service'

class Deal(models.Model):
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField()

class Tour(models.Model):
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
    title = models.CharField(max_length=200, blank=False)
    numberOfClicks = models.IntegerField(default=0)

class Accomodation(models.Model):
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField()
    address = models.CharField(max_length=300, blank=False)
    phone = models.CharField(max_length=16, validators=[phone_regex], blank=False)
    email = models.EmailField(max_length=100)
    logo = models.ImageField(upload_to='accomodation_logos/', blank=True, null=True)
    numberOfClicks = models.IntegerField(default=0, verbose_name="Number of clicks")
    order = models.IntegerField(blank=False, default=0, verbose_name="Accomodation order display")
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='accomodationDestination')
    def image_logo(self):
        return mark_safe('''<img src="%s" />''' % self.logo.url)
    image_logo.short_description = 'Accomodation Logo'


class Map(models.Model):
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
    title = models.CharField(max_length=200, blank=False)
    mapImage = models.ImageField(upload_to='maps/')
    
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='mapTour', blank=True, null=True)
    def is_tour_map(self):
        '''Checks whether this map instance is a tour map'''
        return self.tour is not None

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='mapRestaurant', blank=True, null=True)
    def is_restaurant_map(self):
        '''Checks whether this map instance is a restaurant map'''
        return self.restaurant is not None

    transportation = models.ForeignKey(Transportation, on_delete=models.CASCADE, related_name='mapTransportation',
                                       blank=True, null=True, verbose_name="Car Hire & Transportation")
    def is_transportation_map(self):
        '''Checks whether this map instance is a transportation map'''
        return self.transportation is not None

    retail = models.ForeignKey(Retail, on_delete=models.CASCADE, related_name='mapRetail', blank=True, null=True)
    def is_retail_map(self):
        '''Checks whether this map instance is a retail map'''
        return self.retail is not None

    mining = models.ForeignKey(Mining, on_delete=models.CASCADE, related_name='mapMining', blank=True, null=True,
                               verbose_name="Mining & Resources")
    def is_mining_map(self):
        '''Checks whether this map instance is a mining map'''
        return self.mining is not None

    essentialservice = models.ForeignKey(EssentialService, on_delete=models.CASCADE, related_name='mapEssentialService',
                                     blank=True, null=True, verbose_name='Essential Services')
    def is_essential_service_map(self):
        '''Checks whether this map instance is an essential service map'''
        return self.essentialservice is not None

    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='mapEvent', blank=True, null=True)
    def is_event_map(self):
        '''Checks whether this map instance is an event map'''
        return self.event is not None

    accomodation = models.ForeignKey(Accomodation, on_delete=models.CASCADE, related_name='mapAccomodation', blank=True, null=True)
    def is_accomodation_map(self):
        '''Checks whether this map instance is an accomodation map'''
        return self.accomodation is not None

    def map_preview(self):
        return mark_safe('''<img src="%s" />''' % self.mapImage.url)
    map_preview.short_description = 'Map preview'

class Advertisement(models.Model):
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
    title = models.CharField(max_length=200, blank=False)
    company = models.CharField(max_length=200, blank=False, default='')
    description = models.TextField()
    inTopDeal = models.BooleanField(blank=False, default=False, verbose_name="In top deals?", choices=BOOL_CHOICES)
    numberOfShows = models.IntegerField(default=0, verbose_name="Number of shows")
    numberOfClicks = models.IntegerField(default=0, verbose_name="Number of clicks")
    orderTopDeal = models.IntegerField(blank=False, default=0, verbose_name="Top deal order display")
    highlighted = models.BooleanField(blank=False, default=False, verbose_name="In featured ads?", choices=BOOL_CHOICES)
    
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='advertisementTour', blank=True, null=True)
    def is_tour_advertisement(self):
        '''Checks whether this advertisement instance is a tour advertisement'''
        return self.tour is not None

    accomodation = models.ForeignKey(Accomodation, on_delete=models.CASCADE, related_name='advertisementAccomodation', blank=True, null=True)
    def is_accomodation_advertisement(self):
        '''Checks whether this advertisement instance is an accomodation advertisement'''
        return self.accomodation is not None

    period = models.ForeignKey(Period, on_delete=models.CASCADE, related_name='advertisementPeriod', blank=True, null=True)
    def is_period_advertisement(self):
        '''Checks whether this advertisement instance is part of the event period advertisement'''
        return self.period is not None
    
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='advertisementEvent', blank=True, null=True)
    def is_event_advertisement(self):
        '''Checks whether this advertisement instance is an event advertisement'''
        return self.event is not None
    
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='advertisementRestaurant', blank=True, null=True)
    def is_restaurant_advertisement(self):
        '''Checks whether this advertisement instance is a restaurant advertisement'''
        return self.restaurant is not None

    transportation = models.ForeignKey(Transportation, on_delete=models.CASCADE, related_name='advertisementTransportation',
                                       blank=True, null=True, verbose_name='Car Hire & Transportation')
    def is_transportation_advertisement(self):
        '''Checks whether this advertisement instance is a transportation advertisement'''
        return self.transportation is not None

    retail = models.ForeignKey(Retail, on_delete=models.CASCADE, related_name='advertisementRetail', blank=True,
                               null=True)
    def is_retail_advertisement(self):
        '''Checks whether this advertisement instance is a advertisement image'''
        return self.retail is not None

    mining = models.ForeignKey(Mining, on_delete=models.CASCADE, related_name='advertisementMining', blank=True,
                               null=True, verbose_name='Mining & Resources')
    def is_mining_advertisement(self):
        '''Checks whether this advertisement instance is a mining advertisement'''
        return self.mining is not None

    essentialservice = models.ForeignKey(EssentialService, on_delete=models.CASCADE,
                                         related_name='advertisementEssentialService', blank=True, null=True,
                                         verbose_name='Essential Services')
    def is_essential_service_advertisement(self):
        '''Checks whether this advertisement instance is an essential service advertisement'''
        return self.essentialservice is not None

    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='advertisementDestination', blank=True, null=True)
    def is_destination_advertisement(self):
        '''Checks whether this advertisement instance is a destination advertisement'''
        return self.destination is not None

    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='advertisementActivity', blank=True, null=True)
    def is_activity_advertisement(self):
        '''Checks whether this advertisement instance is an activity advertisement'''
        return self.activity is not None

    ### Service Model still undefined / unclear ###
    # service = models.ForeignKey(Service, models.CASCADE, related_name='videoService', null=True)

class Video(models.Model):
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
    title = models.CharField(max_length=200, blank=False)
    videoFile = models.FileField(upload_to='videos/', blank=False, null=False)

    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='videoTour', blank=True, null=True)
    def is_tour_video(self):
        '''Checks whether this video instance is a tour video'''
        return self.tour is not None

    accomodation = models.ForeignKey(Accomodation, on_delete=models.CASCADE, related_name='videoAccomodation', blank=True, null=True)
    def is_accomodation_video(self):
        '''Checks whether this video instance is an accomodation video'''
        return self.accomodation is not None

    period = models.ForeignKey(Period, on_delete=models.CASCADE, related_name='videoPeriod', blank=True, null=True)
    def is_period_video(self):
        '''Checks whether this video instance is part of the event period video'''
        return self.period is not None
    
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='videoEvent', blank=True, null=True)
    def is_event_video(self):
        '''Checks whether this video instance is an event video'''
        return self.event is not None
    
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='videoRestaurant', blank=True, null=True)
    def is_restaurant_video(self):
        '''Checks whether this video instance is a restaurant video'''
        return self.restaurant is not None

    transportation = models.ForeignKey(Transportation, on_delete=models.CASCADE, related_name='videoTransportation',
                                       blank=True, null=True, verbose_name='Car Hire & Transportation')
    def is_transportation_video(self):
        '''Checks whether this video instance is a transportation video'''
        return self.transportation is not None

    retail = models.ForeignKey(Retail, on_delete=models.CASCADE, related_name='videoRetail', blank=True, null=True)
    def is_retail_video(self):
        '''Checks whether this video instance is a retail video'''
        return self.retail is not None

    mining = models.ForeignKey(Mining, on_delete=models.CASCADE, related_name='videoMining', blank=True, null=True,
                               verbose_name='Mining & Resources')
    def is_mining_video(self):
        '''Checks whether this video instance is a mining video'''
        return self.mining is not None

    essentialservice = models.ForeignKey(EssentialService, on_delete=models.CASCADE, related_name='videoEssentialService',
                                     blank=True, null=True, verbose_name='Essential Services')
    def is_essential_service_video(self):
        '''Checks whether this video instance is an essential service video'''
        return self.essentialservice is not None

    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='videoDestination', blank=True, null=True)
    def is_destination_video(self):
        '''Checks whether this video instance is a destination video'''
        return self.destination is not None
    
    ### Service Model still undefined / unclear ###
    # service = models.ForeignKey(Service, models.CASCADE, related_name='videoService', null=True)

    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE, related_name='videoAdvertisement', blank=True, null=True)
    def is_advertisement_video(self):
        '''Checks whether this video instance is an advertisement video'''
        return self.advertisement is not None

    def video_preview(self):
        return mark_safe('''<video src="%s" controls>Your browser does not support the video tag.</video>''' % self.videoFile.url)
    video_preview.short_description = 'Video preview'

class Image(models.Model):
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
    title = models.CharField(max_length=200, blank=False)
    imageFile = models.ImageField(upload_to='images/', blank=False, null=False)

    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='imageTour', blank=True, null=True)
    def is_tour_image(self):
        '''Checks whether this image instance is a tour image'''
        return self.tour is not None

    accomodation = models.ForeignKey(Accomodation, on_delete=models.CASCADE, related_name='imageAccomodation', blank=True, null=True)
    def is_accomodation_image(self):
        '''Checks whether this image instance is an accomodation image'''
        return self.accomodation is not None

    period = models.ForeignKey(Period, on_delete=models.CASCADE, related_name='imagePeriod', blank=True, null=True)
    def is_period_image(self):
        '''Checks whether this image instance is part of the events period image'''
        return self.accomodation is not None
    
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='imageEvent', blank=True, null=True)
    def is_event_image(self):
        '''Checks whether this image instance is an event image'''
        return self.event is not None
    
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='imageRestaurant', blank=True, null=True)
    def is_restaurant_image(self):
        '''Checks whether this image instance is a restaurant image'''
        return self.restaurant is not None

    transportation = models.ForeignKey(Transportation, on_delete=models.CASCADE, related_name='imageTransportation',
                                       blank=True,null=True, verbose_name='Car Hire & Transportation')
    def is_transportation_image(self):
        '''Checks whether this image instance is a transportation image'''
        return self.transportation is not None

    retail = models.ForeignKey(Retail, on_delete=models.CASCADE, related_name='imageRetail', blank=True, null=True)
    def is_retail_image(self):
        '''Checks whether this image instance is a retail image'''
        return self.retail is not None

    mining = models.ForeignKey(Mining, on_delete=models.CASCADE, related_name='imageMining', blank=True, null=True,
                               verbose_name='Mining & Resources')
    def is_mining_image(self):
        '''Checks whether this image instance is a mining image'''
        return self.mining is not None

    essentialservice = models.ForeignKey(EssentialService, on_delete=models.CASCADE, related_name='imageEssentialService',
                                         blank=True, null=True, verbose_name='Essential Services')
    def is_essential_service_image(self):
        '''Checks whether this image instance is an essential service image'''
        return self.essentialservice is not None

    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='imageDestination', blank=True, null=True)
    def is_destination_image(self):
        '''Checks whether this image instance is a destination image'''
        return self.destination is not None

    ### Service Model still undefined / unclear ###
    # service = models.ForeignKey(Service, models.CASCADE, related_name='videoService', null=True)

    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE, related_name='imageAdvertisement', blank=True, null=True)
    def is_advertisement_image(self):
        return self.advertisement is not None

    def image_preview(self):
        return mark_safe('''<img src="%s" />''' % self.imageFile.url)
    image_preview.short_description = 'Image preview'

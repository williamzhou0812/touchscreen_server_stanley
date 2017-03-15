from __future__ import unicode_literals
from django.db import models
from django.core.validators import RegexValidator
from datetime import datetime

phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

class Activity(models.Model):
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
    title = models.CharField(max_length=200, blank=False)
    numberOfClicks = models.IntegerField(default=0)

class Destination(models.Model):
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
    title = models.CharField(max_length=200, blank=False)
    numberOfClicks = models.IntegerField(default=0)

class Period(models.Model):
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
    title = models.CharField(max_length=200, blank=False)
    numberOfClicks = models.IntegerField(default=0)

class Event(models.Model):
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField(default='')
    fromEventDate = models.DateField(auto_now=False, auto_now_add=False, blank=False, default=datetime.now)
    untilEventDate = models.DateField(auto_now=False, auto_now_add=False, blank=False, default=datetime.now)
    numberOfClicks = models.IntegerField(default=0)
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
    numberOfClicks = models.IntegerField(default=0)
    order = models.IntegerField(blank=False, default=1)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='restaurantDestination')

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
    numberOfClicks = models.IntegerField(default=0)
    order = models.IntegerField(blank=False, default=1)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='accomodationDestination')

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
        return not self.tour is None

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='mapRestaurant', blank=True, null=True)
    def is_restaurant_map(self):
        '''Checks whether this map instance is a restaurant map'''
        return  not self.restaurant is None
    
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='mapEvent', blank=True, null=True)
    def is_event_map(self):
        '''Checks whether this map instance is an event map'''
        return not self.event is None

    accomodation = models.ForeignKey(Accomodation, on_delete=models.CASCADE, related_name='mapAccomodation', blank=True, null=True)
    def is_accomodation_map(self):
        '''Checks whether this map instance is an accomodation map'''
        return not self.accomodation is None

class Advertisement(models.Model):
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
    title = models.CharField(max_length=200, blank=False)
    company = models.CharField(max_length=200, blank=False, default='')
    description = models.TextField()
    inTopDeal = models.BooleanField(blank=False, default=False)
    numberOfShows = models.IntegerField(default=0)
    numberOfClicks = models.IntegerField(default=0)
    orderTopDeal = models.IntegerField(blank=False, default=1)
    highlighted = models.BooleanField(blank=False, default=False)
    
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='advertisementTour', blank=True, null=True)
    def is_tour_advertisement(self):
        '''Checks whether this advertisement instance is a tour advertisement'''
        return not self.tour is None

    accomodation = models.ForeignKey(Accomodation, on_delete=models.CASCADE, related_name='advertisementAccomodation', blank=True, null=True)
    def is_accomodation_advertisement(self):
        '''Checks whether this advertisement instance is an accomodation advertisement'''
        return not self.accomodation is None

    period = models.ForeignKey(Period, on_delete=models.CASCADE, related_name='advertisementPeriod', blank=True, null=True)
    def is_period_advertisement(self):
        '''Checks whether this advertisement instance is part of the event period advertisement'''
        return not self.period is None
    
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='advertisementEvent', blank=True, null=True)
    def is_event_advertisement(self):
        '''Checks whether this advertisement instance is an event advertisement'''
        return not self.event is None
    
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='advertisementRestaurant', blank=True, null=True)
    def is_restaurant_advertisement(self):
        '''Checks whether this advertisement instance is a restaurant advertisement'''
        return not self.restaurant is None

    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='advertisementDestination', blank=True, null=True)
    def is_destination_advertisement(self):
        '''Checks whether this advertisement instance is a destination advertisement'''
        return not self.destination is None

    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='advertisementActivity', blank=True, null=True)
    def is_activity_advertisement(self):
        '''Checks whether this advertisement instance is an activity advertisement'''
        return not self.activity is None

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
        return not self.tour is None

    accomodation = models.ForeignKey(Accomodation, on_delete=models.CASCADE, related_name='videoAccomodation', blank=True, null=True)
    def is_accomodation_video(self):
        '''Checks whether this video instance is an accomodation video'''
        return not self.accomodation is None

    period = models.ForeignKey(Period, on_delete=models.CASCADE, related_name='videoPeriod', blank=True, null=True)
    def is_period_video(self):
        '''Checks whether this video instance is part of the event period video'''
        return not self.period is None
    
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='videoEvent', blank=True, null=True)
    def is_event_video(self):
        '''Checks whether this video instance is an event video'''
        return not self.event is None
    
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='videoRestaurant', blank=True, null=True)
    def is_restaurant_video(self):
        '''Checks whether this video instance is a restaurant video'''
        return not self.restaurant is None
    
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='videoDestination', blank=True, null=True)
    def is_destination_video(self):
        '''Checks whether this video instance is a destination video'''
        return not self.destination is None
    
    ### Service Model still undefined / unclear ###
    # service = models.ForeignKey(Service, models.CASCADE, related_name='videoService', null=True)

    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE, related_name='videoAdvertisement', blank=True, null=True)
    def is_advertisement_video(self):
        '''Checks whether this video instance is an advertisement video'''
        return not self.advertisement is None

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
        return not self.tour is None

    accomodation = models.ForeignKey(Accomodation, on_delete=models.CASCADE, related_name='imageAccomodation', blank=True, null=True)
    def is_accomodation_image(self):
        '''Checks whether this image instance is an accomodation image'''
        return not self.accomodation is None

    period = models.ForeignKey(Period, on_delete=models.CASCADE, related_name='imagePeriod', blank=True, null=True)
    def is_period_image(self):
        '''Checks whether this image instance is part of the events period image'''
        return not self.accomodation is None
    
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='imageEvent', blank=True, null=True)
    def is_event_image(self):
        '''Checks whether this image instance is an event image'''
        return not self.event is None
    
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='imageRestaurant', blank=True, null=True)
    def is_restaurant_image(self):
        '''Checks whether this image instance is a restaurant image'''
        return not self.restaurant is None

    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='imageDestination', blank=True, null=True)
    def is_destination_image(self):
        '''Checks whether this image instance is a destination image'''
        return not self.destination is None

    ### Service Model still undefined / unclear ###
    # service = models.ForeignKey(Service, models.CASCADE, related_name='videoService', null=True)

    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE, related_name='imageAdvertisement', blank=True, null=True)
    def is_advertisement_image(self):
        return not self.advertisement is None

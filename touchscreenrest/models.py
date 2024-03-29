from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
from django.utils.safestring import mark_safe
import phonenumbers
from django.db.models.signals import post_delete
from django.dispatch.dispatcher import receiver


# phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))
DISPLAY_CHOICES = (('NOT_DISPLAY', 'DO NOT DISPLAY'), ('INDEFINITE', 'INDEFINITE'), ('SPECIFY', 'SPECIFY'))
DEFAULT_DISPLAY = 'INDEFINITE'

def validate_phone(value):
    #Allow emergency numbers
    if len(value) == 3:
        return

    #Check phone number not longer than 15 digits
    if len(value) > 15:
        raise ValidationError(
            _('Up to 15 digits allowed for phone numbers.')
        )

    #Check phone number is a valid PNG or AUS number
    png = phonenumbers.parse(value, "AU")
    aus = phonenumbers.parse(value, "PG")
    if phonenumbers.is_valid_number(png) or phonenumbers.is_valid_number(aus):
        return
    else:
        raise ValidationError(_('Incorrect phone number inputted'))


class Activity(models.Model):
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
    title = models.CharField(max_length=200, blank=False)
    numberOfClicks = models.IntegerField(default=0, verbose_name="Number of clicks")
    order = models.IntegerField(blank=False, default=0, verbose_name="Activity order display")
    display = models.CharField(max_length=11, default=DEFAULT_DISPLAY, choices=DISPLAY_CHOICES)
    displayFrom = models.DateField(blank=True, null=True, verbose_name="Start display from")
    displayTo = models.DateField(blank=True, null=True, verbose_name="Stop display from")
    icon = models.FileField(upload_to='activity_icons/', blank=True, null=True)
    class Meta:
        verbose_name = "Activity"
        verbose_name_plural = "Activities"
        ordering = ['order', 'pk']

class Destination(models.Model):
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
    title = models.CharField(max_length=200, blank=False)
    province = models.CharField(max_length=200, blank=False, default='')
    airport = models.CharField(max_length=200, blank=False, default='', verbose_name="Closest Airport")
    description = models.TextField()
    numberOfClicks = models.IntegerField(default=0, verbose_name="Number of clicks")
    order = models.IntegerField(blank=False, default=0, verbose_name="Destination order display")
    display = models.CharField(max_length=11, default=DEFAULT_DISPLAY, choices=DISPLAY_CHOICES)
    displayFrom = models.DateField(blank=True, null=True, verbose_name="Start display from")
    displayTo = models.DateField(blank=True, null=True, verbose_name="Stop display from")
    class Meta:
        ordering = ['order', 'pk']

class Period(models.Model):
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
    title = models.CharField(max_length=200, blank=False)
    numberOfClicks = models.IntegerField(default=0, verbose_name="Number of clicks")
    order = models.IntegerField(blank=False, default=0, verbose_name="Period order display")
    display = models.CharField(max_length=11, default=DEFAULT_DISPLAY, choices=DISPLAY_CHOICES)
    displayFrom = models.DateField(blank=True, null=True, verbose_name="Start display from")
    displayTo = models.DateField(blank=True, null=True, verbose_name="Stop display from")
    class Meta:
        ordering = ['order', 'pk']

class Event(models.Model):
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
    MONTH_CHOICES = (('JANUARY', 'JANUARY'), ('FEBRUARY', 'FEBRUARY'), ('MARCH', 'MARCH'), ('APRIL', 'APRIL'),
                     ('MAY', 'MAY'), ('JUNE', 'JUNE'), ('JULY', 'JULY'), ('AUGUST', 'AUGUST'), ('SEPTEMBER', 'SEPTEMBER'),
                     ('OCTOBER', 'OCTOBER'), ('NOVEMBER', 'NOVEMBER'), ('DECEMBER', 'DECEMBER'))
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField(default='')
    location = models.CharField(max_length=200, blank=True, null=True, verbose_name="Event Location")
    phone = models.CharField(max_length=16, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    eventDate = models.PositiveIntegerField(blank=True, null=True, verbose_name='Date of event')
    eventMonth = models.CharField(max_length=10, blank=True, null=True, verbose_name='Month of event', choices=MONTH_CHOICES)
    numberOfClicks = models.IntegerField(default=0, verbose_name="Number of clicks")
    order = models.IntegerField(blank=False, default=0, verbose_name="Events order display")
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='eventDestination')
    period = models.ForeignKey(Period, on_delete=models.CASCADE, related_name='eventPeriod', blank=True, null=True)
    display = models.CharField(max_length=11, default=DEFAULT_DISPLAY, choices=DISPLAY_CHOICES)
    displayFrom = models.DateField(blank=True, null=True, verbose_name="Start display from")
    displayTo = models.DateField(blank=True, null=True, verbose_name="Stop display from")
    class Meta:
        ordering = ['order', 'pk']

class Restaurant(models.Model):
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
    CHOICES = (('Yes', 'Yes'), ('No', 'No'), ('Other', 'Other'))
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField()
    address = models.CharField(max_length=300, blank=False)
    phone = models.CharField(max_length=16, blank=False)
    email = models.EmailField(max_length=100, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    cuisine = models.CharField(max_length=200, blank=True, null=True)
    cards = models.CharField(max_length=200, blank=True, null=True, verbose_name="Cards accepted")
    price = models.CharField(max_length=200, blank=True, null=True, verbose_name="Price Guide")
    takeaway = models.CharField(max_length=200, blank=True, null=True, default='')
    takeawayOther = models.CharField(max_length=200, blank=True, null=True, verbose_name='Take-away Additional Info')
    wifi = models.CharField(max_length=200, blank=True, null=True, verbose_name="Wi-Fi", default='')
    wifiOther = models.CharField(max_length=200, blank=True, null=True, verbose_name='Wi-Fi Additional Info')
    parking = models.CharField(max_length=200, blank=True, null=True, verbose_name="Secure Parking", default='')
    parkingOther = models.CharField(max_length=200, blank=True, null=True,
                                    verbose_name="Secure Parking Additional Info")
    courtesy = models.CharField(max_length=200, blank=True, null=True, verbose_name="Courtesy Transport", default='')
    courtesyOther = models.CharField(max_length=200, blank=True, null=True,
                                     verbose_name="Courtesy Transport Additional Info")

    logo = models.ImageField(upload_to='restaurant_logos/', blank=True, null=True)
    numberOfClicks = models.IntegerField(default=0, verbose_name="Number of clicks")
    order = models.IntegerField(blank=False, default=0, verbose_name="Restaurant order display")
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='restaurantDestination')
    display = models.CharField(max_length=11, default=DEFAULT_DISPLAY, choices=DISPLAY_CHOICES)
    displayFrom = models.DateField(blank=True, null=True, verbose_name="Start display from")
    displayTo = models.DateField(blank=True, null=True, verbose_name="Stop display from")
    onlyShowSpecificAds = models.BooleanField(blank=False, default=False,
                                              verbose_name="Only show Specific Advertisements?", choices=BOOL_CHOICES)
    def image_logo(self):
        return mark_safe('''<img src="%s" />''' % self.logo.url)
    image_logo.short_description = 'Restaurant Logo'
    class Meta:
        verbose_name = "Dining"
        verbose_name_plural = "Dining"
        ordering = ['order', 'pk']

@receiver(post_delete, sender=Restaurant)
def mymodel_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.logo.delete(False)

class ServiceType(models.Model):
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
    title = models.CharField(max_length=200, blank=False)
    numberOfClicks = models.IntegerField(default=0, verbose_name="Number of clicks")
    order = models.IntegerField(blank=False, default=0, verbose_name="Services Subsection 2 order display")
    display = models.CharField(max_length=11, default=DEFAULT_DISPLAY, choices=DISPLAY_CHOICES)
    displayFrom = models.DateField(blank=True, null=True, verbose_name="Start display from")
    displayTo = models.DateField(blank=True, null=True, verbose_name="Stop display from")
    icon = models.FileField(upload_to='service_type_icons/', blank=True, null=True)
    class Meta:
        verbose_name = "Services Subsection 2"
        verbose_name_plural = "Services Subsection 2"
        ordering = ['order', 'pk']

class Transportation(models.Model):
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=300, blank=True, null=True)
    phone = models.CharField(max_length=16, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    logo = models.ImageField(upload_to='transportation_logos/', blank=True, null=True)
    numberOfClicks = models.IntegerField(default=0, verbose_name="Number of clicks")
    order = models.IntegerField(blank=False, default=0, verbose_name="Transportation order display")
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='transportationDestination',
                                    blank=True, null=True)
    serviceType = models.ForeignKey(ServiceType, on_delete=models.CASCADE, related_name='transportationServiceType',
                                    verbose_name='Services Subsection 2', blank=True, null=True)
    display = models.CharField(max_length=11, default=DEFAULT_DISPLAY, choices=DISPLAY_CHOICES)
    displayFrom = models.DateField(blank=True, null=True, verbose_name="Start display from")
    displayTo = models.DateField(blank=True, null=True, verbose_name="Stop display from")
    onlyShowSpecificAds = models.BooleanField(blank=False, default=False,
                                              verbose_name="Only show Specific Advertisements?", choices=BOOL_CHOICES)
    def image_logo(self):
        return mark_safe('''<img src="%s" />''' % self.logo.url)
    image_logo.short_description = 'Transportation Logo'
    class Meta:
        verbose_name = 'Car Hire & Transport'
        verbose_name_plural = 'Car Hire & Transport'
        ordering = ['order', 'pk']

@receiver(post_delete, sender=Transportation)
def mymodel_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.logo.delete(False)

class Retail(models.Model):
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=300, blank=True, null=True)
    phone = models.CharField(max_length=16, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    logo = models.ImageField(upload_to='retail_logos/', blank=True, null=True)
    numberOfClicks = models.IntegerField(default=0, verbose_name="Number of clicks")
    order = models.IntegerField(blank=False, default=0, verbose_name="Retail order display")
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='retailDestination', blank=True,
                                    null=True)
    serviceType = models.ForeignKey(ServiceType, on_delete=models.CASCADE, related_name='retailServiceType',
                                    verbose_name='Services Subsection 2', blank=True, null=True)
    display = models.CharField(max_length=11, default=DEFAULT_DISPLAY, choices=DISPLAY_CHOICES)
    displayFrom = models.DateField(blank=True, null=True, verbose_name="Start display from")
    displayTo = models.DateField(blank=True, null=True, verbose_name="Stop display from")
    onlyShowSpecificAds = models.BooleanField(blank=False, default=False,
                                              verbose_name="Only show Specific Advertisements?", choices=BOOL_CHOICES)
    def image_logo(self):
        return mark_safe('''<img src="%s" />''' % self.logo.url)
    image_logo.short_description = 'Retail Logo'
    class Meta:
        verbose_name = 'Retail & Service'
        ordering = ['order', 'pk']

@receiver(post_delete, sender=Retail)
def mymodel_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.logo.delete(False)

class Mining(models.Model):
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=300, blank=True, null=True)
    phone = models.CharField(max_length=16, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    logo = models.ImageField(upload_to='mining_logos/', blank=True, null=True)
    numberOfClicks = models.IntegerField(default=0, verbose_name="Number of clicks")
    order = models.IntegerField(blank=False, default=0, verbose_name="Mining order display")
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='miningDestination', blank=True,
                                    null=True)
    serviceType = models.ForeignKey(ServiceType, on_delete=models.CASCADE, related_name='miningServiceType',
                                    verbose_name='Services Subsection 2', blank=True, null=True)
    display = models.CharField(max_length=11, default=DEFAULT_DISPLAY, choices=DISPLAY_CHOICES)
    displayFrom = models.DateField(blank=True, null=True, verbose_name="Start display from")
    displayTo = models.DateField(blank=True, null=True, verbose_name="Stop display from")
    onlyShowSpecificAds = models.BooleanField(blank=False, default=False,
                                              verbose_name="Only show Specific Advertisements?", choices=BOOL_CHOICES)
    def image_logo(self):
        return mark_safe('''<img src="%s" />''' % self.logo.url)
    image_logo.short_description = 'Mining Logo'
    class Meta:
        verbose_name = 'Mining & Resource'
        ordering = ['order', 'pk']

@receiver(post_delete, sender=Mining)
def mymodel_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.logo.delete(False)

class EssentialService(models.Model):
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=300, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    logo = models.ImageField(upload_to='essential_services_logos/', blank=True, null=True)
    numberOfClicks = models.IntegerField(default=0, verbose_name="Number of clicks")
    order = models.IntegerField(blank=False, default=0, verbose_name="Essential Service order display")
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='essentialServiceDestination',
                                    blank=True, null=True)
    serviceType = models.ForeignKey(ServiceType, on_delete=models.CASCADE, related_name='essentialServiceServiceType',
                                    verbose_name='Services Subsection 2', blank=True, null=True)
    display = models.CharField(max_length=11, default=DEFAULT_DISPLAY, choices=DISPLAY_CHOICES)
    displayFrom = models.DateField(blank=True, null=True, verbose_name="Start display from")
    displayTo = models.DateField(blank=True, null=True, verbose_name="Stop display from")
    onlyShowSpecificAds = models.BooleanField(blank=False, default=False,
                                              verbose_name="Only show Specific Advertisements?", choices=BOOL_CHOICES)
    def image_logo(self):
        return mark_safe('''<img src="%s" />''' % self.logo.url)
    image_logo.short_description = 'Essential Service Logo'
    class Meta:
        verbose_name = 'Essential Service'
        ordering = ['order', 'pk']

@receiver(post_delete, sender=EssentialService)
def mymodel_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.logo.delete(False)


class ActivityDestination(models.Model):
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField()
    numberOfClicks = models.IntegerField(default=0, verbose_name="Number of clicks")
    order = models.IntegerField(blank=False, default=0, verbose_name="Destination for Activity order display")
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='activityDestinationActivity',
                                 blank=True, null=True)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name="activityDestinationDestination",
                                    blank=True, null=True)
    display = models.CharField(max_length=11, default=DEFAULT_DISPLAY, choices=DISPLAY_CHOICES)
    displayFrom = models.DateField(blank=True, null=True, verbose_name="Start display from")
    displayTo = models.DateField(blank=True, null=True, verbose_name="Stop display from")
    onlyShowSpecificAds = models.BooleanField(blank=False, default=False,
                                              verbose_name="Only show Specific Advertisements?", choices=BOOL_CHOICES)
    class Meta:
        verbose_name = 'Destination for Activity'
        verbose_name_plural = 'Destination for Activities'
        ordering = ['order', 'pk']

class Tour(models.Model):
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=300, blank=True, null=True)
    phone = models.CharField(max_length=16, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    logo = models.ImageField(upload_to='tour_logos/', blank=True, null=True)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='tourActivity', blank=True, null=True)
    activityDestination = models.ForeignKey(ActivityDestination, on_delete=models.CASCADE,
                                            related_name='tourActivityDestination', blank=True, null=True,
                                            verbose_name='Destination for Activity')
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='tourDestination', blank=True,
                                    null=True)
    numberOfClicks = models.IntegerField(default=0)
    order = models.IntegerField(blank=False, default=0, verbose_name="Tour order display")
    display = models.CharField(max_length=11, default=DEFAULT_DISPLAY, choices=DISPLAY_CHOICES)
    displayFrom = models.DateField(blank=True, null=True, verbose_name="Start display from")
    displayTo = models.DateField(blank=True, null=True, verbose_name="Stop display from")
    class Meta:
        ordering = ['order', 'pk']

    def image_logo(self):
        return mark_safe('''<img src="%s" />''' % self.logo.url)
    image_logo.short_description = 'Tour Logo'

@receiver(post_delete, sender=Tour)
def mymodel_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.logo.delete(False)

class Accomodation(models.Model):
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField()
    address = models.CharField(max_length=300, blank=False)
    phone = models.CharField(max_length=16, blank=False)
    email = models.EmailField(max_length=100, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    logo = models.ImageField(upload_to='accomodation_logos/', blank=True, null=True)
    rating = models.FloatField(blank=False, default=0)
    numberOfClicks = models.IntegerField(default=0, verbose_name="Number of clicks")
    order = models.IntegerField(blank=False, default=0, verbose_name="Accommodation order display")
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='accomodationDestination')
    display = models.CharField(max_length=11, default=DEFAULT_DISPLAY, choices=DISPLAY_CHOICES)
    displayFrom = models.DateField(blank=True, null=True, verbose_name="Start display from")
    displayTo = models.DateField(blank=True, null=True, verbose_name="Stop display from")
    def image_logo(self):
        return mark_safe('''<img src="%s" />''' % self.logo.url)
    image_logo.short_description = 'Accomodation Logo'
    class Meta:
        verbose_name = "Accommodation"
        verbose_name_plural = "Accommodation"
        ordering = ['order', 'pk']

@receiver(post_delete, sender=Accomodation)
def mymodel_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.logo.delete(False)

class Trivia(models.Model):
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
    title = models.CharField(max_length=200, blank=False)
    order = models.IntegerField(blank=False, default=0, verbose_name="Trivia order display")
    numberOfClicks = models.IntegerField(default=0, verbose_name="Number of clicks")
    display = models.CharField(max_length=11, default=DEFAULT_DISPLAY, choices=DISPLAY_CHOICES)
    displayFrom = models.DateField(blank=True, null=True, verbose_name="Start display from")
    displayTo = models.DateField(blank=True, null=True, verbose_name="Stop display from")
    icon = models.FileField(upload_to='trivia_icons/', blank=True, null=True)
    class Meta:
        ordering = ['order', 'pk']

class Section(models.Model):
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
    title = models.CharField(max_length=200, blank=False)
    text = models.TextField(default="")
    order = models.IntegerField(blank=False, default=0, verbose_name="Section order display")
    numberOfClicks = models.IntegerField(default=0, verbose_name="Number of clicks")
    display = models.CharField(max_length=11, default=DEFAULT_DISPLAY, choices=DISPLAY_CHOICES)
    displayFrom = models.DateField(blank=True, null=True, verbose_name="Start display from")
    displayTo = models.DateField(blank=True, null=True, verbose_name="Stop display from")
    trivia = models.ForeignKey(Trivia, on_delete=models.CASCADE, related_name='sectionTrivia', blank=True, null=True)
    class Meta:
        ordering = ['order', 'pk']

class Map(models.Model):
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
    MAP_CHOICES = (('CITY', 'CITY MAP'), ('COUNTRY', 'COUNTRY MAP'))
    DEFAULT_MAP_CHOICE = 'COUNTRY'
    title = models.CharField(max_length=200, blank=False)
    mapImage = models.ImageField(upload_to='maps/')
    mapType = models.CharField(max_length=7, default=DEFAULT_MAP_CHOICE, choices=MAP_CHOICES, verbose_name="Map Type")
    
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

    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='mapDestination', blank=True,
                                    null=True)
    def is_destination_map(self):
        '''Checks whether this map instance is a destination map'''
        return self.accomodation is not None

    class Meta:
        ordering = ['pk']

    def map_preview(self):
        return mark_safe('''<img src="%s" />''' % self.mapImage.url)
    map_preview.short_description = 'Map preview'

@receiver(post_delete, sender=Map)
def mymodel_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.mapImage.delete(False)

class Advertisement(models.Model):
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
    title = models.CharField(max_length=200, blank=False)
    company = models.CharField(max_length=200, blank=False, default='')
    description = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=300, blank=True, null=True)
    phone = models.CharField(max_length=16, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    inTopDeal = models.BooleanField(blank=False, default=False, verbose_name="In top deals?", choices=BOOL_CHOICES)
    numberOfShows = models.IntegerField(default=0, verbose_name="Number of shows")
    numberOfClicks = models.IntegerField(default=0, verbose_name="Number of clicks")
    orderTopDeal = models.IntegerField(blank=False, default=0, verbose_name="Top deal order display")
    highlighted = models.BooleanField(blank=False, default=False, verbose_name="In featured ads?", choices=BOOL_CHOICES)
    display = models.CharField(max_length=11, default=DEFAULT_DISPLAY, choices=DISPLAY_CHOICES)
    displayFrom = models.DateField(blank=True, null=True, verbose_name="Start display from")
    displayTo = models.DateField(blank=True, null=True, verbose_name="Stop display from")
    firstLevelAd = models.BooleanField(blank=False, default=False, verbose_name="Is Level One Ad?", choices=BOOL_CHOICES)
    order = models.IntegerField(blank=False, default=0, verbose_name="Advertisement order display")
    redirectTo = models.CharField(max_length=200, blank=True, null=True, verbose_name="Redirect advertisement to")
    
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

    serviceType = models.ForeignKey(ServiceType, on_delete=models.CASCADE, related_name='advertisementServiceType',
                                    blank=True, null=True, verbose_name='Services Subsection 2')
    def is_service_type_advertisement(self):
        '''Checks whether this advertisement instance is a service type advertisement'''
        return self.serviceType is not None

    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='advertisementDestination', blank=True, null=True)
    def is_destination_advertisement(self):
        '''Checks whether this advertisement instance is a destination advertisement'''
        return self.destination is not None

    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='advertisementActivity', blank=True, null=True)
    def is_activity_advertisement(self):
        '''Checks whether this advertisement instance is an activity advertisement'''
        return self.activity is not None

    activityDestination = models.ForeignKey(ActivityDestination, on_delete=models.CASCADE,
                                            related_name='advertisementActivityDestination', blank=True, null=True,
                                            verbose_name='Destination for Activity')
    def is_activity_destination_advertisement(self):
        '''Checks whether this advertisement instance is an activity destination advertisement'''
        return self.activityDestination is not None

    trivia = models.ForeignKey(Trivia, on_delete=models.CASCADE, related_name='triviaAdvertisement', blank=True, null=True)
    def is_trivia_advertisement(self):
        '''Checks whether this advertisement instance is a trivia advertisement'''
        return self.trivia is not None

    class Meta:
        ordering = ['order', 'pk']

class Airport(models.Model):
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
    title = models.CharField(max_length=200, blank=False)
    header = models.TextField()
    description = models.TextField()
    logo = models.ImageField(upload_to='airport_logos/', blank=True, null=True)

    def image_logo(self):
        return mark_safe('''<img src="%s" />''' % self.logo.url)
    image_logo.short_description = 'Airport Logo'

class AirportContact(models.Model):
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
    title = models.CharField(max_length=200, blank=False)
    phone = models.CharField(max_length=16, blank=True, null=True)
    fax = models.CharField(max_length=16, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='airportAirportContact', blank=True,
                                null=True)

class Video(models.Model):
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
    title = models.CharField(max_length=200, blank=False)
    isDisplayVideo = models.BooleanField(blank=False, default=False, verbose_name="Is display Video?", choices=BOOL_CHOICES)
    videoFile = models.FileField(upload_to='videos/', blank=False, null=False)
    numberOfShows = models.IntegerField(default=0, verbose_name="Number of shows")

    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='videoActivity', blank=True, null=True)
    def is_activity_video(self):
        '''Checks whether this video instance is an activity video'''
        return self.activity is not None

    activityDestination = models.ForeignKey(ActivityDestination, on_delete=models.CASCADE,
                                            related_name='videoActivityDestination', blank=True, null=True,
                                            verbose_name='Destination for Activity')
    def is_activity_destination_video(self):
        '''Checks whether this video instance is an activity destination image'''
        return self.activityDestination is not None

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

    serviceType = models.ForeignKey(ServiceType, on_delete=models.CASCADE, related_name='videoServiceType',
                                    blank=True, null=True, verbose_name='Services Subsection 2')
    def is_service_type_video(self):
        '''Checks whether this video instance is a service type video'''
        return self.serviceType is not None

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

    airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='videoAirport', blank=True, null=True)
    def is_airport_video(self):
        '''Checks whether this video instance is an airport video'''
        return self.airport is not None

    class Meta:
        ordering = ['pk']

    def video_preview(self):
        return mark_safe('''<video src="%s" controls>Your browser does not support the video tag.</video>''' % self.videoFile.url)
    video_preview.short_description = 'Video preview'

@receiver(post_delete, sender=Video)
def mymodel_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.videoFile.delete(False)


class Image(models.Model):
    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title
    title = models.CharField(max_length=200, blank=False)
    imageFile = models.ImageField(upload_to='images/', blank=False, null=False)
    isHeaderImage = models.BooleanField(blank=False, default=False, verbose_name="Is Header Image?",
                                         choices=BOOL_CHOICES)

    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name='imageActivity', blank=True, null=True)
    def is_activity_image(self):
        '''Checks whether this image instance is an activity image'''
        return self.activity is not None

    activityDestination = models.ForeignKey(ActivityDestination, on_delete=models.CASCADE,
                                            related_name='imageActivityDestination', blank=True, null=True,
                                            verbose_name = 'Destination for Activity')
    def is_activity_destination_image(self):
        '''Checks whether this image instance is an activity destination image'''
        return self.activityDestination is not None

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

    serviceType = models.ForeignKey(ServiceType, on_delete=models.CASCADE, related_name='imageServiceType', blank=True,
                                    null=True, verbose_name='Services Subsection 2')
    def is_service_type_image(self):
        '''Checks whether this image instance is a service type image'''
        return self.serviceType is not None

    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='imageDestination', blank=True, null=True)
    def is_destination_image(self):
        '''Checks whether this image instance is a destination image'''
        return self.destination is not None

    ### Service Model still undefined / unclear ###
    # service = models.ForeignKey(Service, models.CASCADE, related_name='videoService', null=True)

    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE, related_name='imageAdvertisement', blank=True, null=True)
    def is_advertisement_image(self):
        return self.advertisement is not None

    airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='imageAirport', blank=True, null=True)
    def is_airport_image(self):
        '''Checks whether this image instance is an airport image'''
        return self.airport is not None

    trivia = models.ForeignKey(Trivia, on_delete=models.CASCADE, related_name='imageTrivia', blank=True, null=True)
    def is_trivia_image(self):
        '''Checks whether this image instance is a trivia image'''
        return self.trivia is not None

    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='imageSection', blank=True, null=True)
    def is_section_image(self):
        '''Checks whether this image isntance is a section image'''
        return self.section is not None

    class Meta:
        ordering = ['pk']

    def image_preview(self):
        return mark_safe('''<img src="%s" />''' % self.imageFile.url)
    image_preview.short_description = 'Image preview'

@receiver(post_delete, sender=Image)
def mymodel_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.imageFile.delete(False)
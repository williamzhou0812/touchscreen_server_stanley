from django.contrib import admin
from touchscreenrest.models import Activity, Destination, Period, Event,Restaurant, Tour, Accomodation, Map,\
    Advertisement, Image, Video

## Start of Accomodation Administration ##
class AccomodationImageInLine(admin.TabularInline):
    model = Image
    extra = 1
    exclude = ('tour', 'period', 'event', 'restaurant', 'destination', 'advertisement')

class AccomodationVideoInLine(admin.TabularInline):
    model = Video
    extra = 1
    exclude = ('tour', 'period', 'event', 'restaurant', 'destination', 'advertisement')

class AccomodationMapInLine(admin.TabularInline):
    model = Map
    extra = 1
    exclude = ('tour', 'restaurant', 'event')

class AccomodationAdvertisementInLine(admin.StackedInline):
    model = Advertisement
    extra = 1
    exclude = ('tour', 'period', 'event', 'restaurant', 'destination', 'activity')

class AccomodationAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Accomodation Information', {'fields': ['title', 'description', 'address', 'phone', 'email', 'logo']}),
        ('Other Settings', {'fields': ['numberOfClicks', 'order', 'destination']}),
    ]
    inlines = [AccomodationImageInLine, AccomodationVideoInLine, AccomodationMapInLine, AccomodationAdvertisementInLine]
    list_display = ('title', 'address', 'destination', 'phone', 'email')
    list_filter = ['title', 'destination']
    search_fields = ['title', 'address', 'destination__title']

    def get_title(self, obj):
        return obj.destination.title
    get_title.short_description = "title"

admin.site.register(Accomodation, AccomodationAdmin)
## End of Accomodation Administration ##

## Start of Activity Administration ##
class ActivityAdvertisementInLine(admin.StackedInline):
    model = Advertisement
    extra = 1
    exclude = ('tour', 'accomodation', 'period', 'event', 'restaurant', 'destination')

class ActivityAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Activity Information', {'fields': ['title']}),
        ('Other Settings', {'fields': ['numberOfClicks']}),
    ]
    inlines = [ActivityAdvertisementInLine]
    list_display = ('title', 'numberOfClicks')
    list_filter = ['title']
    search_fields = ['title']

admin.site.register(Activity, ActivityAdmin)
## End of Activity Administration ##

## Start of Destination Administration ##
class DestinationImageInLine(admin.TabularInline):
    model = Image
    extra = 1
    exclude = ('tour', 'period', 'event', 'restaurant', 'advertisement', 'accomodation')

class DestinationVideoInLine(admin.TabularInline):
    model = Video
    extra = 1
    exclude = ('tour', 'period', 'event', 'restaurant', 'advertisement', 'accomodation')

class PeriodEventInLine(admin.StackedInline):
    model = Event
    extra = 1

class DestinationAdvertisementInLine(admin.StackedInline):
    model = Advertisement
    extra = 1
    exclude = ('tour', 'period', 'event', 'restaurant', 'accomodation', 'activity')

class DestinationAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Destination Information', {'fields': ['title']}),
        ('Other Settings', {'fields': ['numberOfClicks']}),
    ]
    inlines = [DestinationImageInLine, DestinationVideoInLine, DestinationAdvertisementInLine]
    list_display = ('title', 'numberOfClicks')
    list_filter = ['title']
    search_fields = ['title']

admin.site.register(Destination, DestinationAdmin)
## End of Destination Administration ##

## Start of Period Administration ##
class PeriodImageInLine(admin.TabularInline):
    model = Image
    extra = 1
    exclude = ('tour', 'destination', 'event', 'restaurant', 'advertisement', 'accomodation')

class PeriodVideoInLine(admin.TabularInline):
    model = Video
    extra = 1
    exclude = ('tour', 'destination', 'event', 'restaurant', 'advertisement', 'accomodation')

class PeriodAdvertisementInLine(admin.StackedInline):
    model = Advertisement
    extra = 1
    exclude = ('tour', 'destination', 'event', 'restaurant', 'accomodation', 'activity')

class PeriodEventInLine(admin.StackedInline):
    model = Event
    extra = 1

class PeriodAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Period Information', {'fields': ['title']}),
        ('Other Settings', {'fields': ['numberOfClicks']}),
    ]
    inlines = [PeriodImageInLine, PeriodVideoInLine, PeriodEventInLine, PeriodAdvertisementInLine]
    list_display = ('title', 'numberOfClicks')
    list_filter = ['title']
    search_fields = ['title']

admin.site.register(Period, PeriodAdmin)
## End of Period Administration ##

## Start of Event Administration ##
class EventImageInLine(admin.TabularInline):
    model = Image
    extra = 1
    exclude = ('tour', 'destination', 'period', 'restaurant', 'advertisement', 'accomodation')

class EventVideoInLine(admin.TabularInline):
    model = Video
    extra = 1
    exclude = ('tour', 'destination', 'period', 'restaurant', 'advertisement', 'accomodation')

class EventMapInLine(admin.TabularInline):
    model = Map
    extra = 1
    exclude = ('tour', 'accomodation', 'restaurant')

class EventAdvertisementInLine(admin.StackedInline):
    model = Advertisement
    extra = 1
    exclude = ('tour', 'destination', 'period', 'restaurant', 'accomodation', 'activity')

class EventAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Period Information', {'fields': ['title', 'description', 'fromEventDate', 'untilEventDate', 'destination', 'period']}),
        ('Other Settings', {'fields': ['numberOfClicks']}),
    ]
    inlines = [EventImageInLine, EventVideoInLine, EventMapInLine, EventAdvertisementInLine]
    list_display = ('title', 'fromEventDate', 'untilEventDate', 'destination', 'period')
    list_filter = ['title', 'destination', 'period']
    search_fields = ['title', 'destination__title', 'period__title']

    def get_destination_title(self, obj):
        return obj.destination.title
    get_destination_title.short_description = "destinationTitle"

    def get_period_title(self, obj):
        return obj.period.title
    get_period_title.short_description = "periodTitle"

admin.site.register(Event, EventAdmin)
## End of Event Administration ##

## Start of Restaurant Administration ##
class RestaurantImageInLine(admin.TabularInline):
    model = Image
    extra = 1
    exclude = ('tour', 'period', 'event', 'accomodation', 'destination', 'advertisement')

class RestaurantVideoInLine(admin.TabularInline):
    model = Video
    extra = 1
    exclude = ('tour', 'period', 'event', 'accomodation', 'destination', 'advertisement')

class RestaurantMapInLine(admin.TabularInline):
    model = Map
    extra = 1
    exclude = ('tour', 'accomodation', 'event')

class RestaurantAdvertisementInLine(admin.StackedInline):
    model = Advertisement
    extra = 1
    exclude = ('tour', 'period', 'event', 'accomodation', 'destination', 'activity')

class RestaurantAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Restaurant Information', {'fields': ['title', 'description', 'address', 'phone', 'email', 'logo']}),
        ('Other Settings', {'fields': ['numberOfClicks', 'order', 'destination']}),
    ]
    inlines = [RestaurantImageInLine, RestaurantVideoInLine, RestaurantMapInLine, RestaurantAdvertisementInLine]
    list_display = ('title', 'address', 'destination', 'phone', 'email')
    list_filter = ['title', 'destination']
    search_fields = ['title', 'address', 'destination__title']

    def get_title(self, obj):
        return obj.destination.title
    get_title.short_description = "title"

admin.site.register(Restaurant, RestaurantAdmin)
## End of Restaurant Administration ##

## Start of Tour Administration ##
class TourImageInLine(admin.TabularInline):
    model = Image
    extra = 1
    exclude = ('period', 'destination', 'event', 'restaurant', 'advertisement', 'accomodation')

class TourVideoInLine(admin.TabularInline):
    model = Video
    extra = 1
    exclude = ('period', 'destination', 'event', 'restaurant', 'advertisement', 'accomodation')

class TourMapInLine(admin.TabularInline):
    model = Map
    extra = 1
    exclude = ('restaurant', 'accomodation', 'event')

class TourAdvertisementInLine(admin.StackedInline):
    model = Advertisement
    extra = 1
    exclude = ('period', 'destination', 'event', 'restaurant', 'accomodation', 'activity')

class TourAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Period Information', {'fields': ['title']}),
        ('Other Settings', {'fields': ['numberOfClicks']}),
    ]
    inlines = [TourImageInLine, TourVideoInLine, TourMapInLine, TourAdvertisementInLine]
    list_display = ('title', 'numberOfClicks')
    list_filter = ['title']
    search_fields = ['title']
admin.site.register(Tour, TourAdmin)
## End of Tour Administration ##

## Start of Map Administration ##
admin.site.register(Map)
## End of Map Administration ##

## Start of Advertisement Administration ##
admin.site.register(Advertisement)
## End of Advertisement Administration ##

## Start of Image Administration ##
admin.site.register(Image)
## End of Image Administration ##

## Start of Video Administration ##
admin.site.register(Video)
## End of Event Administration ##

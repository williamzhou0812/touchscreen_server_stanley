from django.contrib import admin
from forms import AdvertisementForm
from django.utils.safestring import mark_safe
from touchscreenrest.models import Activity, ActivityDestination, Destination, Period, Event, Restaurant,\
    Transportation, Retail, Mining, EssentialService, Tour, Accomodation, Map, Advertisement, Image, Video

IMAGE_SRC = '''<img src="%s" />'''
VIDEO_SRC = '''<video src="%s" controls>Your browser does not support the video tag.</video>'''
## Start of Accomodation Administration ##
class AccomodationImageInLine(admin.TabularInline):
    model = Image
    extra = 1
    fields = ('title', 'imageFile', 'render_image')
    readonly_fields = ('render_image',)
    exclude = ('activity', 'activityDestination', 'tour', 'period', 'event', 'restaurant', 'transportation', 'retail',
               'mining', 'essentialservice', 'destination', 'advertisement')
    def render_image(self, obj):
        return mark_safe(IMAGE_SRC % obj.imageFile.url)
    render_image.short_description = 'Image preview'

class AccomodationVideoInLine(admin.TabularInline):
    model = Video
    extra = 1
    fields = ('title', 'videoFile', 'render_video')
    readonly_fields = ('render_video',)
    exclude = ('activity', 'activityDestination', 'tour', 'period', 'event', 'restaurant',
               'transportation', 'retail', 'mining', 'essentialservice', 'destination', 'advertisement')
    def render_video(self, obj):
        return mark_safe(VIDEO_SRC % obj.videoFile.url)
    render_video.short_description = 'Video preview'

class AccomodationMapInLine(admin.TabularInline):
    model = Map
    extra = 1
    fields = ('title', 'mapImage', 'render_image')
    readonly_fields = ('render_image',)
    exclude = ('tour', 'restaurant', 'transportation', 'retail', 'mining', 'essentialservice', 'event',
               'destination')
    def render_image(self, obj):
        return mark_safe(IMAGE_SRC % obj.mapImage.url)
    render_image.short_description = 'Map preview'

class AccomodationAdvertisementInLine(admin.StackedInline):
    model = Advertisement
    extra = 1
    exclude = ('tour', 'period', 'event', 'restaurant', 'transportation', 'retail', 'mining', 'essentialservice',
               'destination', 'activity', 'activityDestination')
    form = AdvertisementForm

class AccomodationAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Accomodation Information', {'fields': ['title', 'description', 'address', 'phone', 'email', 'logo', 'image_logo']}),
        ('Other Settings', {'fields': ['numberOfClicks', 'order', 'destination']}),
    ]
    inlines = [AccomodationImageInLine, AccomodationVideoInLine, AccomodationMapInLine, AccomodationAdvertisementInLine]
    readonly_fields = ('image_logo',)
    list_display = ('title', 'address', 'destination', 'phone', 'email')
    list_filter = ['title', 'destination']
    search_fields = ['title', 'address', 'destination__title']

    def get_title(self, obj):
        return obj.destination.title
    get_title.short_description = "title"

admin.site.register(Accomodation, AccomodationAdmin)
## End of Accomodation Administration ##

## Start of Activity Administration ##
class ActivityImageInLine(admin.TabularInline):
    model = Image
    extra = 1
    exclude = ('destination', 'activityDestination', 'tour', 'period', 'event', 'restaurant', 'transportation',
               'retail', 'mining', 'essentialservice', 'advertisement', 'accomodation')
    fields = ('title', 'imageFile', 'render_image')
    readonly_fields = ('render_image',)

    def render_image(self, obj):
        return mark_safe(IMAGE_SRC % obj.imageFile.url)
    render_image.short_description = 'Image preview'

class ActivityVideoInLine(admin.TabularInline):
    model = Video
    extra = 1
    fields = ('title', 'videoFile', 'render_video')
    readonly_fields = ('render_video',)
    exclude = ('destination', 'activityDestination', 'tour', 'period', 'event', 'restaurant', 'transportation',
               'retail', 'mining', 'essentialservice', 'advertisement', 'accomodation')

    def render_video(self, obj):
        return mark_safe(VIDEO_SRC % obj.videoFile.url)
    render_video.short_description = 'Video preview'

class ActivityDestinationInLine(admin.StackedInline):
    model = ActivityDestination
    extra = 1

class ActivityTourInLine(admin.StackedInline):
    model = Tour
    extra = 1

class ActivityAdvertisementInLine(admin.StackedInline):
    model = Advertisement
    extra = 1
    exclude = ('tour', 'period', 'event', 'restaurant', 'transportation', 'mining', 'retail', 'accomodation',
               'destination', 'essentialservice', 'activityDestination')
    form = AdvertisementForm

class ActivityAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Activity Information', {'fields': ['title']}),
        ('Other Settings', {'fields': ['numberOfClicks']}),
    ]
    inlines = [ActivityImageInLine, ActivityVideoInLine, ActivityDestinationInLine, ActivityTourInLine,
               ActivityAdvertisementInLine]
    list_display = ('title', 'numberOfClicks')
    list_filter = ['title']
    search_fields = ['title']

admin.site.register(Activity, ActivityAdmin)
## End of Activity Administration ##

## Start of Destination Administration ##
class DestinationImageInLine(admin.TabularInline):
    model = Image
    extra = 1
    exclude = ('activity', 'activityDestination', 'tour', 'period', 'event', 'restaurant', 'transportation', 'retail',
               'mining', 'essentialservice', 'advertisement', 'accomodation')
    fields = ('title', 'imageFile', 'render_image')
    readonly_fields = ('render_image',)

    def render_image(self, obj):
        return mark_safe(IMAGE_SRC % obj.imageFile.url)
    render_image.short_description = 'Image preview'


class DestinationVideoInLine(admin.TabularInline):
    model = Video
    extra = 1
    fields = ('title', 'videoFile', 'render_video')
    readonly_fields = ('render_video',)
    exclude = ('activity', 'activityDestination', 'tour', 'period', 'event', 'restaurant', 'transportation', 'retail',
               'mining', 'essentialservice','advertisement', 'accomodation')

    def render_video(self, obj):
        return mark_safe(VIDEO_SRC % obj.videoFile.url)
    render_video.short_description = 'Video preview'

class DestinationMapInLine(admin.TabularInline):
    model = Map
    extra = 1
    fields = ('title', 'mapImage', 'render_image')
    readonly_fields = ('render_image',)
    exclude = ('tour', 'restaurant', 'transportation', 'retail', 'mining', 'essentialservice', 'event',
               'accomodation')
    def render_image(self, obj):
        return mark_safe(IMAGE_SRC % obj.mapImage.url)
    render_image.short_description = 'Map preview'

class DestinationAdvertisementInLine(admin.StackedInline):
    model = Advertisement
    extra = 1
    exclude = ('tour', 'period', 'event', 'restaurant', 'transportation', 'retail', 'mining', 'essentialservice',
               'accomodation', 'activity', 'activityDestination')
    form = AdvertisementForm

class DestinationAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Destination Information', {'fields': ['title', 'description']}),
        ('Other Settings', {'fields': ['numberOfClicks']}),
    ]
    inlines = [DestinationImageInLine, DestinationVideoInLine, DestinationMapInLine,
               DestinationAdvertisementInLine]
    list_display = ('title', 'numberOfClicks')
    list_filter = ['title']
    search_fields = ['title']

admin.site.register(Destination, DestinationAdmin)
## End of Destination Administration ##

## Start of Period Administration ##
class PeriodImageInLine(admin.TabularInline):
    model = Image
    extra = 1
    fields = ('title', 'imageFile', 'render_image')
    readonly_fields = ('render_image',)
    exclude = ('activity', 'activityDestination', 'tour', 'destination', 'event', 'restaurant', 'transportation',
               'retail', 'mining', 'essentialservice','advertisement', 'accomodation')

    def render_image(self, obj):
        return mark_safe(IMAGE_SRC % obj.imageFile.url)
    render_image.short_description = 'Image preview'

class PeriodVideoInLine(admin.TabularInline):
    model = Video
    extra = 1
    fields = ('title', 'videoFile', 'render_video')
    readonly_fields = ('render_video',)
    exclude = ('activity', 'activityDestination', 'tour', 'destination', 'event', 'restaurant', 'transportation',
               'retail', 'mining', 'essentialservice', 'advertisement', 'accomodation')

    def render_video(self, obj):
        return mark_safe(VIDEO_SRC % obj.videoFile.url)
    render_video.short_description = 'Video preview'

class PeriodAdvertisementInLine(admin.StackedInline):
    model = Advertisement
    extra = 1
    exclude = ('tour', 'destination', 'event', 'restaurant', 'transportation', 'retail', 'mining', 'essentialservice',
               'accomodation', 'activity', 'activityDestination')
    form = AdvertisementForm

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
    fields = ('title', 'imageFile', 'render_image')
    readonly_fields = ('render_image',)
    exclude = ('activity', 'activityDestination', 'tour', 'destination', 'period', 'restaurant', 'transportation',
               'retail', 'mining', 'essentialservice', 'advertisement', 'accomodation')

    def render_image(self, obj):
        return mark_safe(IMAGE_SRC % obj.imageFile.url)
    render_image.short_description = 'Image preview'

class EventVideoInLine(admin.TabularInline):
    model = Video
    extra = 1
    fields = ('title', 'videoFile', 'render_video')
    readonly_fields = ('render_video',)
    exclude = ('activity', 'activityDestination', 'tour', 'destination', 'period', 'restaurant', 'transportation',
               'retail', 'mining', 'essentialservice', 'advertisement', 'accomodation')

    def render_video(self, obj):
        return mark_safe(VIDEO_SRC % obj.videoFile.url)
    render_video.short_description = 'Video preview'

class EventMapInLine(admin.TabularInline):
    model = Map
    extra = 1
    fields = ('title', 'mapImage', 'render_image')
    readonly_fields = ('render_image',)
    exclude = ('tour', 'accomodation', 'restaurant', 'transportation', 'retail', 'mining', 'essentialservice',
               'destination')

    def render_image(self, obj):
        return mark_safe(IMAGE_SRC % obj.mapImage.url)
    render_image.short_description = 'Map preview'

class EventAdvertisementInLine(admin.StackedInline):
    model = Advertisement
    extra = 1
    exclude = ('tour', 'destination', 'period', 'restaurant', 'transportation', 'retail', 'mining', 'essentialservice',
               'accomodation', 'activity', 'activityDestination')
    form = AdvertisementForm

class EventAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Event Information', {'fields': ['title', 'description', 'fromEventDate', 'untilEventDate', 'destination', 'period']}),
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
    fields = ('title', 'imageFile', 'render_image')
    readonly_fields = ('render_image',)
    exclude = ('activity', 'activityDestination', 'tour', 'period', 'event', 'transportation', 'retail', 'mining',
               'essentialservice', 'accomodation', 'destination', 'advertisement')

    def render_image(self, obj):
        return mark_safe(IMAGE_SRC % obj.imageFile.url)
    render_image.short_description = 'Image preview'

class RestaurantVideoInLine(admin.TabularInline):
    model = Video
    extra = 1
    fields = ('title', 'videoFile', 'render_video')
    readonly_fields = ('render_video',)
    exclude = ('activity', 'activityDestination', 'tour', 'period', 'event', 'transportation', 'retail', 'mining',
               'essentialservice', 'accomodation', 'destination', 'advertisement')

    def render_video(self, obj):
        return mark_safe(VIDEO_SRC % obj.videoFile.url)
    render_video.short_description = 'Video preview'

class RestaurantMapInLine(admin.TabularInline):
    model = Map
    extra = 1
    fields = ('title', 'mapImage', 'render_image')
    readonly_fields = ('render_image',)
    exclude = ('tour', 'accomodation', 'event', 'transportation', 'retail', 'mining', 'essentialservice',
               'destination')

    def render_image(self, obj):
        return mark_safe(IMAGE_SRC % obj.mapImage.url)
    render_image.short_description = 'Map preview'

class RestaurantAdvertisementInLine(admin.StackedInline):
    model = Advertisement
    extra = 1
    exclude = ('tour', 'period', 'event', 'transportation', 'retail', 'mining', 'essentialservice', 'accomodation',
               'destination', 'activity', 'activityDestination')
    form = AdvertisementForm

class RestaurantAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Restaurant Information', {'fields': ['title', 'description', 'address', 'phone', 'email', 'logo', 'image_logo']}),
        ('Other Settings', {'fields': ['numberOfClicks', 'order', 'destination']}),
    ]
    inlines = [RestaurantImageInLine, RestaurantVideoInLine, RestaurantMapInLine, RestaurantAdvertisementInLine]
    readonly_fields = ('image_logo',)
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
    fields = ('title', 'imageFile', 'render_image')
    readonly_fields = ('render_image',)
    exclude = ('activity', 'activityDestination', 'period', 'destination', 'event', 'restaurant', 'transportation',
               'retail', 'mining', 'essentialservice', 'advertisement', 'accomodation')

    def render_image(self, obj):
        return mark_safe(IMAGE_SRC % obj.imageFile.url)
    render_image.short_description = 'Image preview'

class TourVideoInLine(admin.TabularInline):
    model = Video
    extra = 1
    fields = ('title', 'videoFile', 'render_video')
    readonly_fields = ('render_video',)
    exclude = ('activity', 'activityDestination', 'period', 'destination', 'event', 'restaurant', 'transportation',
               'retail', 'mining', 'essentialservice', 'advertisement', 'accomodation')

    def render_video(self, obj):
        return mark_safe(VIDEO_SRC % obj.videoFile.url)
    render_video.short_description = 'Video preview'

class TourMapInLine(admin.TabularInline):
    model = Map
    extra = 1
    fields = ('title', 'mapImage', 'render_image')
    readonly_fields = ('render_image',)
    exclude = ('restaurant', 'transportation', 'retail', 'mining', 'essentialservice', 'accomodation', 'event',
               'destination')

    def render_image(self, obj):
        return mark_safe(IMAGE_SRC % obj.mapImage.url)
    render_image.short_description = 'Map preview'

class TourAdvertisementInLine(admin.StackedInline):
    model = Advertisement
    extra = 1
    exclude = ('period', 'destination', 'event', 'restaurant', 'transportation', 'retail', 'mining', 'essentialservice',
               'accomodation', 'activity', 'activityDestination')
    form = AdvertisementForm

class TourAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Tour Information', {'fields': ['title', 'description', 'address', 'phone', 'email', 'logo', 'image_logo']}),
        ('Other Settings', {'fields': ['numberOfClicks', 'activity', 'activityDestination', 'destination']}),
    ]
    inlines = [TourImageInLine, TourVideoInLine, TourMapInLine, TourAdvertisementInLine]
    readonly_fields = ('image_logo',)
    list_display = ('title', 'address', 'phone', 'email', 'activity', 'numberOfClicks')
    list_filter = ['title', 'activity', 'activityDestination']
    search_fields = ['title', 'activity__title', 'activityDestination__title']

admin.site.register(Tour, TourAdmin)
## End of Tour Administration ##

## Start of Map Administration ##
class MapAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Map Information', {'fields': ['title', 'mapImage', 'map_preview']}),
        ('Where to Show Map', {'fields': ['tour', 'restaurant', 'transportation', 'retail', 'mining',
                                          'essentialservice', 'event', 'accomodation', 'destination']}
         ),
    ]
    readonly_fields = ('map_preview',)
admin.site.register(Map, MapAdmin)
## End of Map Administration ##

## Start of Advertisement Administration ##
class AdvertisementImageInLine(admin.TabularInline):
    model = Image
    extra = 1
    fields = ('title', 'imageFile', 'render_image')
    readonly_fields = ('render_image',)
    exclude = ('period', 'destination', 'event', 'restaurant', 'transportation', 'retail', 'mining', 'essentialservice',
               'activity', 'activityDestination', 'tour', 'accomodation')

    def render_image(self, obj):
        return mark_safe(IMAGE_SRC % obj.imageFile.url)
    render_image.short_description = 'Image preview'

class AdvertisementVideoInLine(admin.TabularInline):
    model = Video
    extra = 1
    fields = ('title', 'videoFile', 'render_video')
    readonly_fields = ('render_video',)
    exclude = ('period', 'destination', 'event', 'restaurant', 'transportation', 'retail', 'mining', 'essentialservice',
               'activity', 'activityDestination', 'tour', 'accomodation')

    def render_video(self, obj):
        return mark_safe(VIDEO_SRC % obj.videoFile.url)
    render_video.short_description = 'Video preview'

class AdvertisementAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Advertisement Information', {'fields': ['title', 'company', 'description']}),
        ('Other Settings', {'fields': ['inTopDeal', 'orderTopDeal', 'numberOfShows', 'numberOfClicks', 'highlighted']}),
        ('Where to Show Advertisement', {'fields': ['activity', 'activityDestination', 'tour', 'accomodation', 'period',
                                                    'event', 'restaurant', 'transportation', 'retail', 'mining',
                                                    'essentialservice', 'destination']}
         ),
    ]
    inlines = [AdvertisementImageInLine, AdvertisementVideoInLine]
    list_display = ('title', 'company')
    list_filter = ['title', 'company']
    search_fields = ['title', 'company']
    form = AdvertisementForm

admin.site.register(Advertisement, AdvertisementAdmin)
## End of Advertisement Administration ##

## Start of Image Administration ##
class ImageAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Image Information', {'fields': ['title', 'imageFile', 'image_preview']}),
        ('Where to Show Image', {'fields': ['activity', 'activityDestination', 'tour', 'accomodation', 'period', 'event',
                                            'restaurant', 'transportation', 'retail', 'mining', 'essentialservice',
                                            'destination', 'advertisement']}
         ),
    ]
    readonly_fields = ('image_preview',)
admin.site.register(Image, ImageAdmin)
## End of Image Administration ##

## Start of Video Administration ##
class VideoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Video Information', {'fields': ['title', 'videoFile', 'video_preview']}),
        ('Where to Show Video', {'fields': ['activity', 'activityDestination', 'tour', 'accomodation', 'period', 'event',
                                            'restaurant', 'transportation', 'retail', 'mining', 'essentialservice',
                                            'destination','advertisement']}
         ),
    ]
    readonly_fields = ('video_preview',)
admin.site.register(Video, VideoAdmin)
## End of Event Administration ##

## Start of Transportation Administration ##
class TransportationImageInLine(admin.TabularInline):
    model = Image
    extra = 1
    fields = ('title', 'imageFile', 'render_image')
    readonly_fields = ('render_image',)
    exclude = ('activity', 'activityDestination', 'tour', 'period', 'event', 'restaurant', 'retail', 'mining',
               'essentialservice', 'accomodation', 'destination', 'advertisement')

    def render_image(self, obj):
        return mark_safe(IMAGE_SRC % obj.imageFile.url)
    render_image.short_description = 'Image preview'

class TransportationVideoInLine(admin.TabularInline):
    model = Video
    extra = 1
    fields = ('title', 'videoFile', 'render_video')
    readonly_fields = ('render_video',)
    exclude = ('activity', 'activityDestination', 'tour', 'period', 'event', 'restaurant', 'retail', 'mining',
               'essentialservice', 'accomodation', 'destination', 'advertisement')

    def render_video(self, obj):
        return mark_safe(VIDEO_SRC % obj.videoFile.url)
    render_video.short_description = 'Video preview'

class TransportationMapInLine(admin.TabularInline):
    model = Map
    extra = 1
    fields = ('title', 'mapImage', 'render_image')
    readonly_fields = ('render_image',)
    exclude = ('tour', 'accomodation', 'event', 'restaurant', 'retail', 'mining', 'essentialservice',
               'destination')

    def render_image(self, obj):
        return mark_safe(IMAGE_SRC % obj.mapImage.url)
    render_image.short_description = 'Map preview'

class TransportationAdvertisementInLine(admin.StackedInline):
    model = Advertisement
    extra = 1
    exclude = ('tour', 'period', 'event', 'restaurant', 'retail', 'mining', 'essentialservice', 'accomodation',
               'destination', 'activity', 'activityDestination')
    form = AdvertisementForm

class TransportationAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Car Hire & Transportation Information', {'fields': ['title', 'description', 'address', 'phone', 'email',
                                                              'logo', 'image_logo']}),
        ('Other Settings', {'fields': ['numberOfClicks', 'order', 'destination']}),
    ]
    inlines = [TransportationImageInLine, TransportationVideoInLine, TransportationMapInLine,
               TransportationAdvertisementInLine]
    readonly_fields = ('image_logo',)
    list_display = ('title', 'address', 'destination', 'phone', 'email')
    list_filter = ['title', 'destination']
    search_fields = ['title', 'address', 'destination__title']

    def get_title(self, obj):
        return obj.destination.title
    get_title.short_description = "title"

admin.site.register(Transportation, TransportationAdmin)
## End of Transportation Administration ##

## Start of Retail Administration ##
class RetailImageInLine(admin.TabularInline):
    model = Image
    extra = 1
    fields = ('title', 'imageFile', 'render_image')
    readonly_fields = ('render_image',)
    exclude = ('activity', 'activityDestination', 'tour', 'period', 'event', 'restaurant', 'transportation', 'mining',
               'essentialservice', 'accomodation', 'destination', 'advertisement')

    def render_image(self, obj):
        return mark_safe(IMAGE_SRC % obj.imageFile.url)
    render_image.short_description = 'Image preview'

class RetailVideoInLine(admin.TabularInline):
    model = Video
    extra = 1
    fields = ('title', 'videoFile', 'render_video')
    readonly_fields = ('render_video',)
    exclude = ('activity', 'activityDestination', 'tour', 'period', 'event', 'restaurant', 'transportation', 'mining',
               'essentialservice', 'accomodation', 'destination', 'advertisement')

    def render_video(self, obj):
        return mark_safe(VIDEO_SRC % obj.videoFile.url)
    render_video.short_description = 'Video preview'

class RetailMapInLine(admin.TabularInline):
    model = Map
    extra = 1
    fields = ('title', 'mapImage', 'render_image')
    readonly_fields = ('render_image',)
    exclude = ('tour', 'accomodation', 'event', 'restaurant', 'transportation', 'mining', 'essentialservice',
               'destination')

    def render_image(self, obj):
        return mark_safe(IMAGE_SRC % obj.mapImage.url)
    render_image.short_description = 'Map preview'

class RetailAdvertisementInLine(admin.StackedInline):
    model = Advertisement
    extra = 1
    exclude = ('tour', 'period', 'event', 'restaurant', 'transportation', 'mining', 'essentialservice', 'accomodation',
               'destination', 'activity', 'activityDestination')
    form = AdvertisementForm

class RetailAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Retail Information', {'fields': ['title', 'description', 'address', 'phone', 'email', 'logo', 'image_logo']}),
        ('Other Settings', {'fields': ['numberOfClicks', 'order', 'destination']}),
    ]
    inlines = [RetailImageInLine, RetailVideoInLine, RetailMapInLine, RetailAdvertisementInLine]
    readonly_fields = ('image_logo',)
    list_display = ('title', 'address', 'destination', 'phone', 'email')
    list_filter = ['title', 'destination']
    search_fields = ['title', 'address', 'destination__title']

    def get_title(self, obj):
        return obj.destination.title
    get_title.short_description = "title"

admin.site.register(Retail, RetailAdmin)
## End of Retail Administration ##

## Start of Mining Administration ##
class MiningImageInLine(admin.TabularInline):
    model = Image
    extra = 1
    fields = ('title', 'imageFile', 'render_image')
    readonly_fields = ('render_image',)
    exclude = ('activity', 'activityDestination', 'tour', 'period', 'event', 'restaurant', 'transportation', 'retail',
               'essentialservice', 'accomodation', 'destination', 'advertisement')

    def render_image(self, obj):
        return mark_safe(IMAGE_SRC % obj.imageFile.url)
    render_image.short_description = 'Image preview'

class MiningVideoInLine(admin.TabularInline):
    model = Video
    extra = 1
    fields = ('title', 'videoFile', 'render_video')
    readonly_fields = ('render_video',)
    exclude = ('activity', 'activityDestination', 'tour', 'period', 'event', 'restaurant', 'transportation', 'retail',
               'essentialservice', 'accomodation', 'destination', 'advertisement')

    def render_video(self, obj):
        return mark_safe(VIDEO_SRC % obj.videoFile.url)
    render_video.short_description = 'Video preview'

class MiningMapInLine(admin.TabularInline):
    model = Map
    extra = 1
    fields = ('title', 'mapImage', 'render_image')
    readonly_fields = ('render_image',)
    exclude = ('tour', 'accomodation', 'event', 'restaurant', 'transportation', 'retail', 'essentialservice',
               'destination')

    def render_image(self, obj):
        return mark_safe(IMAGE_SRC % obj.mapImage.url)
    render_image.short_description = 'Map preview'

class MiningAdvertisementInLine(admin.StackedInline):
    model = Advertisement
    extra = 1
    exclude = ('tour', 'period', 'event', 'restaurant', 'transportation', 'retail', 'essentialservice', 'accomodation',
               'destination', 'activity', 'activityDestination')
    form = AdvertisementForm

class MiningAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Mining Information', {'fields': ['title', 'description', 'address', 'phone', 'email', 'logo', 'image_logo']}),
        ('Other Settings', {'fields': ['numberOfClicks', 'order', 'destination']}),
    ]
    inlines = [MiningImageInLine, MiningVideoInLine, MiningMapInLine, MiningAdvertisementInLine]
    readonly_fields = ('image_logo',)
    list_display = ('title', 'address', 'destination', 'phone', 'email')
    list_filter = ['title', 'destination']
    search_fields = ['title', 'address', 'destination__title']

    def get_title(self, obj):
        return obj.destination.title
    get_title.short_description = "title"

admin.site.register(Mining, MiningAdmin)
## End of Mining Administration ##

## Start of Essential Services Administration ##
class EssentialServiceImageInLine(admin.TabularInline):
    model = Image
    extra = 1
    fields = ('title', 'imageFile', 'render_image')
    readonly_fields = ('render_image',)
    exclude = ('activity', 'activityDestination', 'tour', 'period', 'event', 'restaurant', 'transportation', 'mining',
               'retail', 'accomodation', 'destination', 'advertisement')

    def render_image(self, obj):
        return mark_safe(IMAGE_SRC % obj.imageFile.url)
    render_image.short_description = 'Image preview'

class EssentialServiceVideoInLine(admin.TabularInline):
    model = Video
    extra = 1
    fields = ('title', 'videoFile', 'render_video')
    readonly_fields = ('render_video',)
    exclude = ('activity', 'activityDestination', 'tour', 'period', 'event', 'restaurant', 'transportation', 'mining',
               'retail', 'accomodation', 'destination', 'advertisement')

    def render_video(self, obj):
        return mark_safe(VIDEO_SRC % obj.videoFile.url)
    render_video.short_description = 'Video preview'

class EssentialServiceMapInLine(admin.TabularInline):
    model = Map
    extra = 1
    fields = ('title', 'mapImage', 'render_image')
    readonly_fields = ('render_image',)
    exclude = ('tour', 'accomodation', 'event', 'restaurant', 'transportation', 'mining', 'retail', 'destination')

    def render_image(self, obj):
        return mark_safe(IMAGE_SRC % obj.mapImage.url)
    render_image.short_description = 'Map preview'

class EssentialServiceAdvertisementInLine(admin.StackedInline):
    model = Advertisement
    extra = 1
    exclude = ('tour', 'period', 'event', 'restaurant', 'transportation', 'mining', 'retail', 'accomodation',
               'destination', 'activity', 'activityDestination')
    form = AdvertisementForm

class EssentialServiceAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Essential Service Information', {'fields': ['title', 'description', 'address', 'phone', 'email', 'logo',
                                                       'image_logo']}),
        ('Other Settings', {'fields': ['numberOfClicks', 'order', 'destination']}),
    ]
    inlines = [EssentialServiceImageInLine, EssentialServiceVideoInLine, EssentialServiceMapInLine,
               EssentialServiceAdvertisementInLine]
    readonly_fields = ('image_logo',)
    list_display = ('title', 'address', 'destination', 'phone', 'email')
    list_filter = ['title', 'destination']
    search_fields = ['title', 'address', 'destination__title']

    def get_title(self, obj):
        return obj.destination.title
    get_title.short_description = "title"

admin.site.register(EssentialService, EssentialServiceAdmin)
## End of Essential Services Administration ##


## Start of Activity Destination Administration ##
class ActivityDestinationImageInLine(admin.TabularInline):
    model = Image
    extra = 1
    exclude = ('destination', 'activity', 'tour', 'period', 'event', 'restaurant', 'transportation',
               'retail', 'mining', 'essentialservice', 'advertisement', 'accomodation')
    fields = ('title', 'imageFile', 'render_image')
    readonly_fields = ('render_image',)

    def render_image(self, obj):
        return mark_safe(IMAGE_SRC % obj.imageFile.url)
    render_image.short_description = 'Image preview'

class ActivityDestinationVideoInLine(admin.TabularInline):
    model = Video
    extra = 1
    fields = ('title', 'videoFile', 'render_video')
    readonly_fields = ('render_video',)
    exclude = ('destination', 'activity', 'tour', 'period', 'event', 'restaurant', 'transportation',
               'retail', 'mining', 'essentialservice', 'advertisement', 'accomodation')

    def render_video(self, obj):
        return mark_safe(VIDEO_SRC % obj.videoFile.url)
    render_video.short_description = 'Video preview'

class ActivityDestinationTourInLine(admin.StackedInline):
    model = Tour
    extra = 1

class ActivityDestinationAdvertisementInLine(admin.StackedInline):
    model = Advertisement
    extra = 1
    exclude = ('tour', 'period', 'event', 'restaurant', 'transportation', 'mining', 'retail', 'accomodation',
               'destination', 'activity', 'essentialservices')
    form = AdvertisementForm

class ActivityDestinationAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Activity Information', {'fields': ['title']}),
        ('Other Settings', {'fields': ['numberOfClicks', 'activity']}),
    ]
    inlines = [ActivityDestinationImageInLine, ActivityDestinationVideoInLine, ActivityDestinationTourInLine,
               ActivityDestinationAdvertisementInLine]
    list_display = ('title', 'numberOfClicks')
    list_filter = ['title', 'activity']
    search_fields = ['title', 'activity__title']

admin.site.register(ActivityDestination, ActivityDestinationAdmin)
## End of Activity Destination Administration ##
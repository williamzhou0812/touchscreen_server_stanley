from django.contrib import admin
from forms import AdvertisementForm
from django.utils.safestring import mark_safe
from touchscreenrest.models import Activity, Destination, Period, Event,Restaurant, Tour, Accomodation, Map,\
    Advertisement, Image, Video

IMAGE_SRC = '''<img src="%s" />'''
VIDEO_SRC = '''<video src="%s" controls>Your browser does not support the video tag.</video>'''
## Start of Accomodation Administration ##
class AccomodationImageInLine(admin.TabularInline):
    model = Image
    extra = 1
    fields = ('title', 'imageFile', 'render_image')
    readonly_fields = ('render_image',)
    exclude = ('tour', 'period', 'event', 'restaurant', 'destination', 'advertisement')
    def render_image(self, obj):
        return mark_safe(IMAGE_SRC % obj.imageFile.url)
    render_image.short_description = 'Image preview'

class AccomodationVideoInLine(admin.TabularInline):
    model = Video
    extra = 1
    fields = ('title', 'videoFile', 'render_video')
    readonly_fields = ('render_video',)
    exclude = ('tour', 'period', 'event', 'restaurant', 'destination', 'advertisement')
    def render_video(self, obj):
        return mark_safe(VIDEO_SRC % obj.videoFile.url)
    render_video.short_description = 'Video preview'

class AccomodationMapInLine(admin.TabularInline):
    model = Map
    extra = 1
    fields = ('title', 'mapImage', 'render_image')
    readonly_fields = ('render_image',)
    exclude = ('tour', 'restaurant', 'event')
    def render_image(self, obj):
        return mark_safe(IMAGE_SRC % obj.mapImage.url)
    render_image.short_description = 'Map preview'

class AccomodationAdvertisementInLine(admin.StackedInline):
    model = Advertisement
    extra = 1
    exclude = ('tour', 'period', 'event', 'restaurant', 'destination', 'activity')
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
class ActivityAdvertisementInLine(admin.StackedInline):
    model = Advertisement
    extra = 1
    exclude = ('tour', 'accomodation', 'period', 'event', 'restaurant', 'destination')
    form = AdvertisementForm

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
    exclude = ('tour', 'period', 'event', 'restaurant', 'advertisement', 'accomodation')

    def render_video(self, obj):
        return mark_safe(VIDEO_SRC % obj.videoFile.url)
    render_video.short_description = 'Video preview'

class DestinationAdvertisementInLine(admin.StackedInline):
    model = Advertisement
    extra = 1
    exclude = ('tour', 'period', 'event', 'restaurant', 'accomodation', 'activity')
    form = AdvertisementForm

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
    fields = ('title', 'imageFile', 'render_image')
    readonly_fields = ('render_image',)
    exclude = ('tour', 'destination', 'event', 'restaurant', 'advertisement', 'accomodation')

    def render_image(self, obj):
        return mark_safe(IMAGE_SRC % obj.imageFile.url)
    render_image.short_description = 'Image preview'

class PeriodVideoInLine(admin.TabularInline):
    model = Video
    extra = 1
    fields = ('title', 'videoFile', 'render_video')
    readonly_fields = ('render_video',)
    exclude = ('tour', 'destination', 'event', 'restaurant', 'advertisement', 'accomodation')

    def render_video(self, obj):
        return mark_safe(VIDEO_SRC % obj.videoFile.url)
    render_video.short_description = 'Video preview'

class PeriodAdvertisementInLine(admin.StackedInline):
    model = Advertisement
    extra = 1
    exclude = ('tour', 'destination', 'event', 'restaurant', 'accomodation', 'activity')
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
    exclude = ('tour', 'destination', 'period', 'restaurant', 'advertisement', 'accomodation')

    def render_image(self, obj):
        return mark_safe(IMAGE_SRC % obj.imageFile.url)
    render_image.short_description = 'Image preview'

class EventVideoInLine(admin.TabularInline):
    model = Video
    extra = 1
    fields = ('title', 'videoFile', 'render_video')
    readonly_fields = ('render_video',)
    exclude = ('tour', 'destination', 'period', 'restaurant', 'advertisement', 'accomodation')

    def render_video(self, obj):
        return mark_safe(VIDEO_SRC % obj.videoFile.url)
    render_video.short_description = 'Video preview'

class EventMapInLine(admin.TabularInline):
    model = Map
    extra = 1
    fields = ('title', 'mapImage', 'render_image')
    readonly_fields = ('render_image',)
    exclude = ('tour', 'accomodation', 'restaurant')

    def render_image(self, obj):
        return mark_safe(IMAGE_SRC % obj.mapImage.url)
    render_image.short_description = 'Map preview'

class EventAdvertisementInLine(admin.StackedInline):
    model = Advertisement
    extra = 1
    exclude = ('tour', 'destination', 'period', 'restaurant', 'accomodation', 'activity')
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
    exclude = ('tour', 'period', 'event', 'accomodation', 'destination', 'advertisement')

    def render_image(self, obj):
        return mark_safe(IMAGE_SRC % obj.imageFile.url)
    render_image.short_description = 'Image preview'

class RestaurantVideoInLine(admin.TabularInline):
    model = Video
    extra = 1
    fields = ('title', 'videoFile', 'render_video')
    readonly_fields = ('render_video',)
    exclude = ('tour', 'period', 'event', 'accomodation', 'destination', 'advertisement')

    def render_video(self, obj):
        return mark_safe(VIDEO_SRC % obj.videoFile.url)
    render_video.short_description = 'Video preview'

class RestaurantMapInLine(admin.TabularInline):
    model = Map
    extra = 1
    fields = ('title', 'mapImage', 'render_image')
    readonly_fields = ('render_image',)
    exclude = ('tour', 'accomodation', 'event')

    def render_image(self, obj):
        return mark_safe(IMAGE_SRC % obj.mapImage.url)
    render_image.short_description = 'Map preview'

class RestaurantAdvertisementInLine(admin.StackedInline):
    model = Advertisement
    extra = 1
    exclude = ('tour', 'period', 'event', 'accomodation', 'destination', 'activity')
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
    exclude = ('period', 'destination', 'event', 'restaurant', 'advertisement', 'accomodation')

    def render_image(self, obj):
        return mark_safe(IMAGE_SRC % obj.imageFile.url)
    render_image.short_description = 'Image preview'

class TourVideoInLine(admin.TabularInline):
    model = Video
    extra = 1
    fields = ('title', 'videoFile', 'render_video')
    readonly_fields = ('render_video',)
    exclude = ('period', 'destination', 'event', 'restaurant', 'advertisement', 'accomodation')

    def render_video(self, obj):
        return mark_safe(VIDEO_SRC % obj.videoFile.url)
    render_video.short_description = 'Video preview'

class TourMapInLine(admin.TabularInline):
    model = Map
    extra = 1
    fields = ('title', 'mapImage', 'render_image')
    readonly_fields = ('render_image',)
    exclude = ('restaurant', 'accomodation', 'event')

    def render_image(self, obj):
        return mark_safe(IMAGE_SRC % obj.mapImage.url)
    render_image.short_description = 'Map preview'

class TourAdvertisementInLine(admin.StackedInline):
    model = Advertisement
    extra = 1
    exclude = ('period', 'destination', 'event', 'restaurant', 'accomodation', 'activity')
    form = AdvertisementForm

class TourAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Tour Information', {'fields': ['title']}),
        ('Other Settings', {'fields': ['numberOfClicks']}),
    ]
    inlines = [TourImageInLine, TourVideoInLine, TourMapInLine, TourAdvertisementInLine]
    list_display = ('title', 'numberOfClicks')
    list_filter = ['title']
    search_fields = ['title']
admin.site.register(Tour, TourAdmin)
## End of Tour Administration ##

## Start of Map Administration ##
class MapAdmin(admin.ModelAdmin):
    fields = ('title', 'mapImage', 'map_preview', 'tour', 'restaurant', 'event', 'accomodation')
    readonly_fields = ('map_preview',)
admin.site.register(Map, MapAdmin)
## End of Map Administration ##

## Start of Advertisement Administration ##
class AdvertisementImageInLine(admin.TabularInline):
    model = Image
    extra = 1
    fields = ('title', 'imageFile', 'render_image')
    readonly_fields = ('render_image',)
    exclude = ('period', 'destination', 'event', 'restaurant', 'tour', 'accomodation')

    def render_image(self, obj):
        return mark_safe(IMAGE_SRC % obj.imageFile.url)
    render_image.short_description = 'Image preview'

class AdvertisementVideoInLine(admin.TabularInline):
    model = Video
    extra = 1
    fields = ('title', 'videoFile', 'render_video')
    readonly_fields = ('render_video',)
    exclude = ('period', 'destination', 'event', 'restaurant', 'tour', 'accomodation')

    def render_video(self, obj):
        return mark_safe(VIDEO_SRC % obj.videoFile.url)
    render_video.short_description = 'Video preview'

class AdvertisementAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Advertisement Information', {'fields': ['title', 'company', 'description']}),
        ('Other Settings', {'fields': ['inTopDeal', 'orderTopDeal', 'numberOfShows', 'numberOfClicks', 'highlighted']}),
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
    fields = ('title', 'imageFile', 'image_preview','tour', 'accomodation', 'period', 'event', 'restaurant', 'destination',
              'advertisement')
    readonly_fields = ('image_preview',)
admin.site.register(Image, ImageAdmin)
## End of Image Administration ##

## Start of Video Administration ##
class VideoAdmin(admin.ModelAdmin):
    fields = ('title', 'videoFile', 'video_preview', 'tour', 'accomodation', 'period', 'event', 'restaurant', 'destination',
              'advertisement')
    readonly_fields = ('video_preview',)
admin.site.register(Video, VideoAdmin)
## End of Event Administration ##

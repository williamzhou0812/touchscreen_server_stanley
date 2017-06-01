from django.contrib import admin
from django.contrib.auth.models import Group
from forms import AdvertisementForm, VideoForm, RestaurantForm, ImageForm
from django.utils.safestring import mark_safe
from touchscreenrest.models import Activity, ActivityDestination, Destination, Period, Event, Restaurant,\
    Transportation, Retail, Mining, EssentialService, Tour, Accomodation, Map, Advertisement, Image, Video, ServiceType
import nested_admin

IMAGE_SRC = '''<img src="%s" />'''
VIDEO_SRC = '''<video src="%s" controls>Your browser does not support the video tag.</video>'''

## Start of Custom Actions ##
def reset_number_of_clicks(modeladmin, request, queryset):
    queryset.update(numberOfClicks=0)
reset_number_of_clicks.short_description = "Reset number of clicks back to zero"
### End of Custom Actions ###

## Start of Accomodation Administration ##
class AccomodationImageInLine(admin.TabularInline):
    model = Image
    extra = 1
    fields = ('title', 'imageFile', 'isHeaderImage')
    form = ImageForm
    exclude = ('activity', 'activityDestination', 'tour', 'period', 'event', 'restaurant', 'transportation', 'retail',
               'mining', 'essentialservice', 'destination', 'advertisement', 'serviceType')
    classes = ['collapse']
    def render_image(self, obj):
        return mark_safe(IMAGE_SRC % obj.imageFile.url)
    render_image.short_description = 'Image preview'

class AccomodationVideoInLine(admin.TabularInline):
    model = Video
    extra = 1
    fields = ('title', 'videoFile')
    exclude = ('activity', 'activityDestination', 'tour', 'period', 'event', 'restaurant',
               'transportation', 'retail', 'mining', 'essentialservice', 'destination', 'advertisement',
               'isDisplayVideo', 'serviceType')
    classes = ['collapse']
    def render_video(self, obj):
        return mark_safe(VIDEO_SRC % obj.videoFile.url)
    render_video.short_description = 'Video preview'

class AccomodationMapInLine(admin.TabularInline):
    model = Map
    extra = 1
    fields = ('title', 'mapImage')
    exclude = ('tour', 'restaurant', 'transportation', 'retail', 'mining', 'essentialservice', 'event',
               'destination')
    classes = ['collapse']
    def render_image(self, obj):
        return mark_safe(IMAGE_SRC % obj.mapImage.url)
    render_image.short_description = 'Map preview'

class AccomodationAdvertisementInLine(admin.StackedInline):
    model = Advertisement
    extra = 1
    exclude = ('tour', 'period', 'event', 'restaurant', 'transportation', 'retail', 'mining', 'essentialservice',
               'destination', 'activity', 'activityDestination', 'serviceType', 'display', 'displayFrom', 'displayTo')
    form = AdvertisementForm
    classes = ['collapse']

class AccomodationAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Accommodation Title', {'fields': ['title']}),
        ('Display Settings', {'fields': ['display', 'displayFrom', 'displayTo']}),
        ('Accommodation Detail', {'fields': ['description', 'address', 'phone', 'email', 'website', 'logo','image_logo']}),
        ('Other Settings', {'fields': ['numberOfClicks', 'order', 'destination']}),

    ]
    inlines = [AccomodationImageInLine, AccomodationVideoInLine, AccomodationMapInLine]
    readonly_fields = ('image_logo',)
    list_display = ('title', 'address', 'destination', 'phone', 'email', 'website')
    list_filter = ['title', 'destination']
    search_fields = ['title', 'address', 'destination__title']
    actions = [reset_number_of_clicks]

    def get_title(self, obj):
        return obj.destination.title
    get_title.short_description = "title"
    class Media:
        js = ('https://code.jquery.com/jquery-1.12.4.min.js', 'admin-script.js',)

admin.site.register(Accomodation, AccomodationAdmin)
## End of Accomodation Administration ##

## Start of Activity Administration ##
class ActivityImageInLine(nested_admin.NestedTabularInline):
    model = Image
    extra = 1
    exclude = ('destination', 'activityDestination', 'tour', 'period', 'event', 'restaurant', 'transportation',
               'retail', 'mining', 'essentialservice', 'advertisement', 'accomodation', 'serviceType')
    fields = ('title', 'imageFile', 'isHeaderImage')
    form = ImageForm
    classes = ['collapse']
    def render_image(self, obj):
        return mark_safe(IMAGE_SRC % obj.imageFile.url)
    render_image.short_description = 'Image preview'

class ActivityVideoInLine(nested_admin.NestedTabularInline):
    model = Video
    extra = 1
    fields = ('title', 'videoFile')
    exclude = ('destination', 'activityDestination', 'tour', 'period', 'event', 'restaurant', 'transportation',
               'retail', 'mining', 'essentialservice', 'advertisement', 'accomodation', 'isDisplayVideo', 'serviceType')
    classes = ['collapse']
    def render_video(self, obj):
        return mark_safe(VIDEO_SRC % obj.videoFile.url)
    render_video.short_description = 'Video preview'

class ActivityTourInLine(admin.StackedInline):
    model = Tour
    extra = 1

class ActivityAdvertisementInLine(admin.StackedInline):
    model = Advertisement
    extra = 1
    exclude = ('tour', 'period', 'event', 'restaurant', 'transportation', 'mining', 'retail', 'accomodation',
               'destination', 'essentialservice', 'activityDestination', 'serviceType', 'display', 'displayFrom',
               'displayTo')
    form = AdvertisementForm
    classes = ['collapse']

###START OF ACTIVITY TOUR INLINE###
class TourImageNestedInLine(nested_admin.NestedTabularInline):
    model = Image
    extra = 1
    fields = ('title', 'imageFile')
    exclude = ('activity', 'activityDestination', 'period', 'destination', 'event', 'restaurant', 'transportation',
               'retail', 'mining', 'essentialservice', 'advertisement', 'accomodation', 'serviceType')
    classes = ['collapse']

class TourVideoNestedInLine(nested_admin.NestedTabularInline):
    model = Video
    extra = 1
    fields = ('title', 'videoFile')
    exclude = ('activity', 'activityDestination', 'period', 'destination', 'event', 'restaurant', 'transportation',
               'retail', 'mining', 'essentialservice', 'advertisement', 'accomodation', 'isDisplayVideo', 'serviceType')
    classes = ['collapse']

class TourMapNestedInLine(nested_admin.NestedTabularInline):
    model = Map
    extra = 1
    fields = ('title', 'mapImage')
    exclude = ('restaurant', 'transportation', 'retail', 'mining', 'essentialservice', 'accomodation', 'event',
               'destination')
    classes = ['collapse']

class TourInLine(nested_admin.NestedStackedInline):
    model = Tour
    inlines = [TourImageNestedInLine, TourVideoNestedInLine, TourMapNestedInLine]
    classes = ['collapse']
    exclude = ('display', 'displayFrom', 'displayTo')
    extra = 1
###END OF ACTIVITY TOUR INLINE###

###START OF ACTIVITY DESTINATION INLINE###
class ActivityDestinationImageInLine(nested_admin.NestedTabularInline):
    model = Image
    extra = 1
    exclude = ('destination', 'activity', 'tour', 'period', 'event', 'restaurant', 'transportation',
               'retail', 'mining', 'essentialservice', 'advertisement', 'accomodation', 'serviceType')
    fields = ('title', 'imageFile')
    classes = ['collapse']
    def render_image(self, obj):
        return mark_safe(IMAGE_SRC % obj.imageFile.url)
    render_image.short_description = 'Image preview'

class ActivityDestinationVideoInLine(nested_admin.NestedTabularInline):
    model = Video
    extra = 1
    fields = ('title', 'videoFile')
    exclude = ('destination', 'activity', 'tour', 'period', 'event', 'restaurant', 'transportation',
               'retail', 'mining', 'essentialservice', 'advertisement', 'accomodation', 'isDisplayVideo', 'serviceType')
    classes = ['collapse']
    def render_video(self, obj):
        return mark_safe(VIDEO_SRC % obj.videoFile.url)
    render_video.short_description = 'Video preview'

class ActivityDestinationTourInLine(nested_admin.NestedStackedInline):
    model = Tour
    extra = 1
    classes = ['collapse']

class ActivityDestinationInLine(nested_admin.NestedStackedInline):
    model = ActivityDestination
    exclude = ('display', 'displayFrom', 'displayTo')
    inlines = [ActivityDestinationImageInLine, ActivityDestinationVideoInLine, ActivityDestinationTourInLine]
    classes = ['collapse']
    extra = 1

class ActivityAdmin(nested_admin.NestedModelAdmin):
    fieldsets = [
        ('Activity Information', {'fields': ['title']}),
        ('Display Settings', {'fields': ['display', 'displayFrom', 'displayTo']}),
        ('Other Settings', {'fields': ['numberOfClicks']}),
    ]
    inlines = [ActivityImageInLine, ActivityVideoInLine, ActivityDestinationInLine, TourInLine]
    list_display = ('title', 'numberOfClicks')
    list_filter = ['title']
    search_fields = ['title']
    actions = [reset_number_of_clicks]
    class Media:
        js = ('https://code.jquery.com/jquery-1.12.4.min.js', 'admin-script.js',)

admin.site.register(Activity, ActivityAdmin)
## End of Activity Administration ##

## Start of Destination Administration ##
class DestinationImageInLine(admin.TabularInline):
    model = Image
    extra = 1
    exclude = ('activity', 'activityDestination', 'tour', 'period', 'event', 'restaurant', 'transportation', 'retail',
               'mining', 'essentialservice', 'advertisement', 'accomodation', 'serviceType')
    fields = ('title', 'imageFile', 'isHeaderImage')
    form = ImageForm
    classes = ['collapse']
    def render_image(self, obj):
        return mark_safe(IMAGE_SRC % obj.imageFile.url)
    render_image.short_description = 'Image preview'


class DestinationVideoInLine(admin.TabularInline):
    model = Video
    extra = 1
    fields = ('title', 'videoFile')
    exclude = ('activity', 'activityDestination', 'tour', 'period', 'event', 'restaurant', 'transportation', 'retail',
               'mining', 'essentialservice','advertisement', 'accomodation', 'isDisplayVideo', 'serviceType')
    classes = ['collapse']
    def render_video(self, obj):
        return mark_safe(VIDEO_SRC % obj.videoFile.url)
    render_video.short_description = 'Video preview'

class DestinationMapInLine(admin.TabularInline):
    model = Map
    extra = 1
    fields = ('title', 'mapImage')
    exclude = ('tour', 'restaurant', 'transportation', 'retail', 'mining', 'essentialservice', 'event',
               'accomodation')
    classes = ['collapse']
    def render_image(self, obj):
        return mark_safe(IMAGE_SRC % obj.mapImage.url)
    render_image.short_description = 'Map preview'

class DestinationAdvertisementInLine(admin.StackedInline):
    model = Advertisement
    extra = 1
    exclude = ('tour', 'period', 'event', 'restaurant', 'transportation', 'retail', 'mining', 'essentialservice',
               'accomodation', 'activity', 'activityDestination', 'serviceType', 'display', 'displayFrom', 'displayTo')
    classes = ['collapse']
    form = AdvertisementForm

class DestinationAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Destination Information', {'fields': ['title',]}),
        ('Display Settings', {'fields': ['display', 'displayFrom', 'displayTo']}),
        ('Destination Detail', {'fields': ['province', 'airport', 'description']}),
        ('Other Settings', {'fields': ['numberOfClicks']}),
    ]
    inlines = [DestinationImageInLine, DestinationVideoInLine, DestinationMapInLine]
    list_display = ('title', 'numberOfClicks')
    list_filter = ['title']
    search_fields = ['title']
    actions = [reset_number_of_clicks]
    class Media:
        js = ('https://code.jquery.com/jquery-1.12.4.min.js', 'admin-script.js',)

admin.site.register(Destination, DestinationAdmin)
## End of Destination Administration ##

## Start of Period Administration ##
class PeriodImageInLine(admin.TabularInline):
    model = Image
    extra = 1
    fields = ('title', 'imageFile', 'isHeaderImage')
    exclude = ('activity', 'activityDestination', 'tour', 'destination', 'event', 'restaurant', 'transportation',
               'retail', 'mining', 'essentialservice','advertisement', 'accomodation', 'serviceType')
    form = ImageForm
    classes = ['collapse']
    def render_image(self, obj):
        return mark_safe(IMAGE_SRC % obj.imageFile.url)
    render_image.short_description = 'Image preview'

class PeriodVideoInLine(admin.TabularInline):
    model = Video
    extra = 1
    fields = ('title', 'videoFile')
    exclude = ('activity', 'activityDestination', 'tour', 'destination', 'event', 'restaurant', 'transportation',
               'retail', 'mining', 'essentialservice', 'advertisement', 'accomodation', 'isDisplayVideo', 'serviceType')
    classes = ['collapse']
    def render_video(self, obj):
        return mark_safe(VIDEO_SRC % obj.videoFile.url)
    render_video.short_description = 'Video preview'

class PeriodAdvertisementInLine(admin.StackedInline):
    model = Advertisement
    extra = 1
    exclude = ('tour', 'destination', 'event', 'restaurant', 'transportation', 'retail', 'mining', 'essentialservice',
               'accomodation', 'activity', 'activityDestination', 'serviceType', 'display', 'displayFrom', 'displayTo')
    form = AdvertisementForm
    classes = ['collapse']

class PeriodEventInLine(admin.StackedInline):
    model = Event
    extra = 1
    classes = ['collapse']

class PeriodAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Period Information', {'fields': ['title']}),
        ('Display Settings', {'fields': ['display', 'displayFrom', 'displayTo']}),
        ('Other Settings', {'fields': ['numberOfClicks']}),
    ]
    inlines = [PeriodImageInLine, PeriodVideoInLine]
    list_display = ('title', 'numberOfClicks')
    list_filter = ['title']
    search_fields = ['title']
    actions = [reset_number_of_clicks]
    class Media:
        js = ('https://code.jquery.com/jquery-1.12.4.min.js', 'admin-script.js',)

admin.site.register(Period, PeriodAdmin)
## End of Period Administration ##

## Start of Event Administration ##
class EventImageInLine(admin.TabularInline):
    model = Image
    extra = 1
    fields = ('title', 'imageFile')
    exclude = ('activity', 'activityDestination', 'tour', 'destination', 'period', 'restaurant', 'transportation',
               'retail', 'mining', 'essentialservice', 'advertisement', 'accomodation', 'serviceType')
    classes = ['collapse']
    def render_image(self, obj):
        return mark_safe(IMAGE_SRC % obj.imageFile.url)
    render_image.short_description = 'Image preview'

class EventVideoInLine(admin.TabularInline):
    model = Video
    extra = 1
    fields = ('title', 'videoFile')
    exclude = ('activity', 'activityDestination', 'tour', 'destination', 'period', 'restaurant', 'transportation',
               'retail', 'mining', 'essentialservice', 'advertisement', 'accomodation', 'isDisplayVideo', 'serviceType')
    classes = ['collapse']
    def render_video(self, obj):
        return mark_safe(VIDEO_SRC % obj.videoFile.url)
    render_video.short_description = 'Video preview'

class EventMapInLine(admin.TabularInline):
    model = Map
    extra = 1
    fields = ('title', 'mapImage')
    exclude = ('tour', 'accomodation', 'restaurant', 'transportation', 'retail', 'mining', 'essentialservice',
               'destination')
    classes = ['collapse']
    def render_image(self, obj):
        return mark_safe(IMAGE_SRC % obj.mapImage.url)
    render_image.short_description = 'Map preview'

class EventAdvertisementInLine(admin.StackedInline):
    model = Advertisement
    extra = 1
    exclude = ('tour', 'destination', 'period', 'restaurant', 'transportation', 'retail', 'mining', 'essentialservice',
               'accomodation', 'activity', 'activityDestination', 'serviceType', 'display', 'displayFrom', 'displayTo')
    form = AdvertisementForm
    classes = ['collapse']

class EventAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Event Information', {'fields': ['title',]}),
        ('Display Settings', {'fields': ['display', 'displayFrom', 'displayTo']}),
        ('Event Detail', {'fields': ['description', 'location', 'phone', 'email', 'website', 'eventDate', 'eventMonth',
                                     'destination', 'period']}),
        ('Other Settings', {'fields': ['numberOfClicks']}),
    ]
    inlines = [EventImageInLine, EventVideoInLine, EventMapInLine]
    list_display = ('title', 'destination', 'period')
    list_filter = ['title', 'destination', 'period']
    search_fields = ['title', 'destination__title', 'period__title']
    actions = [reset_number_of_clicks]

    def get_destination_title(self, obj):
        return obj.destination.title
    get_destination_title.short_description = "destinationTitle"

    def get_period_title(self, obj):
        return obj.period.title
    get_period_title.short_description = "periodTitle"

    class Media:
        js = ('https://code.jquery.com/jquery-1.12.4.min.js', 'admin-script.js',)

admin.site.register(Event, EventAdmin)
## End of Event Administration ##

## Start of Restaurant Administration ##
class RestaurantImageInLine(admin.TabularInline):
    model = Image
    extra = 1
    fields = ('title', 'imageFile')
    exclude = ('activity', 'activityDestination', 'tour', 'period', 'event', 'transportation', 'retail', 'mining',
               'essentialservice', 'accomodation', 'destination', 'advertisement', 'serviceType')
    classes = ['collapse']
    def render_image(self, obj):
        return mark_safe(IMAGE_SRC % obj.imageFile.url)
    render_image.short_description = 'Image preview'

class RestaurantVideoInLine(admin.TabularInline):
    model = Video
    extra = 1
    fields = ('title', 'videoFile')
    exclude = ('activity', 'activityDestination', 'tour', 'period', 'event', 'transportation', 'retail', 'mining',
               'essentialservice', 'accomodation', 'destination', 'advertisement', 'isDisplayVideo', 'serviceType')
    classes = ['collapse']
    def render_video(self, obj):
        return mark_safe(VIDEO_SRC % obj.videoFile.url)
    render_video.short_description = 'Video preview'

class RestaurantMapInLine(admin.TabularInline):
    model = Map
    extra = 1
    fields = ('title', 'mapImage')
    exclude = ('tour', 'accomodation', 'event', 'transportation', 'retail', 'mining', 'essentialservice',
               'destination')
    classes = ['collapse']
    def render_image(self, obj):
        return mark_safe(IMAGE_SRC % obj.mapImage.url)
    render_image.short_description = 'Map preview'

class RestaurantAdvertisementInLine(admin.StackedInline):
    model = Advertisement
    extra = 1
    exclude = ('tour', 'period', 'event', 'transportation', 'retail', 'mining', 'essentialservice', 'accomodation',
               'destination', 'activity', 'activityDestination', 'serviceType', 'display', 'displayFrom', 'displayTo')
    form = AdvertisementForm
    classes = ['collapse']

class RestaurantAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Restaurant Information', {'fields': ['title',]}),
        ('Display Settings', {'fields': ['display', 'displayFrom', 'displayTo']}),
        ('Restaurant Detail', {'fields': ['description', 'address', 'phone', 'email', 'website', 'logo', 'image_logo']}),
        ('Restaurant Guide', {'fields': ['cuisine', 'takeaway', 'takeawayOther', 'wifi', 'wifiOther', 'parking',
                                         'parkingOther', 'courtesy', 'courtesyOther', 'cards', 'price']}),
        ('Other Settings', {'fields': ['numberOfClicks', 'order', 'destination']}),
    ]
    inlines = [RestaurantImageInLine, RestaurantVideoInLine, RestaurantMapInLine]
    readonly_fields = ('image_logo',)
    form = RestaurantForm
    list_display = ('title', 'address', 'destination', 'phone', 'email', 'website')
    list_filter = ['title', 'destination']
    search_fields = ['title', 'address', 'destination__title']
    actions = [reset_number_of_clicks]

    def get_title(self, obj):
        return obj.destination.title
    get_title.short_description = "title"

    class Media:
        js = ('https://code.jquery.com/jquery-1.12.4.min.js', 'admin-script.js',)

admin.site.register(Restaurant, RestaurantAdmin)
## End of Restaurant Administration ##

## Start of Tour Administration ##
class TourImageInLine(admin.TabularInline):
    model = Image
    extra = 1
    fields = ('title', 'imageFile')
    exclude = ('activity', 'activityDestination', 'period', 'destination', 'event', 'restaurant', 'transportation',
               'retail', 'mining', 'essentialservice', 'advertisement', 'accomodation', 'serviceType')
    classes = ['collapse']
    def render_image(self, obj):
        return mark_safe(IMAGE_SRC % obj.imageFile.url)
    render_image.short_description = 'Image preview'

class TourVideoInLine(admin.TabularInline):
    model = Video
    extra = 1
    fields = ('title', 'videoFile')
    exclude = ('activity', 'activityDestination', 'period', 'destination', 'event', 'restaurant', 'transportation',
               'retail', 'mining', 'essentialservice', 'advertisement', 'accomodation', 'isDisplayVideo', 'serviceType')
    classes = ['collapse']
    def render_video(self, obj):
        return mark_safe(VIDEO_SRC % obj.videoFile.url)
    render_video.short_description = 'Video preview'

class TourMapInLine(admin.TabularInline):
    model = Map
    extra = 1
    fields = ('title', 'mapImage')
    exclude = ('restaurant', 'transportation', 'retail', 'mining', 'essentialservice', 'accomodation', 'event',
               'destination')
    classes = ['collapse']
    def render_image(self, obj):
        return mark_safe(IMAGE_SRC % obj.mapImage.url)
    render_image.short_description = 'Map preview'

class TourAdvertisementInLine(admin.StackedInline):
    model = Advertisement
    extra = 1
    exclude = ('period', 'destination', 'event', 'restaurant', 'transportation', 'retail', 'mining', 'essentialservice',
               'accomodation', 'activity', 'activityDestination', 'serviceType', 'display', 'displayFrom', 'displayTo')
    form = AdvertisementForm
    classes = ['collapse']

class TourAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Tour Information', {'fields': ['title',]}),
        ('Display Settings', {'fields': ['display', 'displayFrom', 'displayTo']}),
        ('Tour Detail', {'fields': ['description', 'address', 'phone', 'email', 'website', 'logo', 'image_logo']}),
        ('Other Settings', {'fields': ['numberOfClicks', 'activity', 'activityDestination', 'destination']}),
    ]
    inlines = [TourImageInLine, TourVideoInLine, TourMapInLine]
    readonly_fields = ('image_logo',)
    list_display = ('title', 'address', 'phone', 'email', 'website', 'activity', 'numberOfClicks')
    list_filter = ['title', 'activity', 'activityDestination']
    search_fields = ['title', 'activity__title', 'activityDestination__title']
    actions = [reset_number_of_clicks]
    class Media:
        js = ('https://code.jquery.com/jquery-1.12.4.min.js', 'admin-script.js',)

admin.site.register(Tour, TourAdmin)
## End of Tour Administration ##

## Start of Map Administration ##
class MapAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Map Information', {'fields': ['title', 'mapImage']}),
        ('Where to Show Map', {'fields': ['tour', 'restaurant', 'transportation', 'retail', 'mining',
                                          'essentialservice', 'event', 'accomodation', 'destination']}
         ),
    ]
admin.site.register(Map, MapAdmin)
## End of Map Administration ##

## Start of Advertisement Administration ##
class AdvertisementImageInLine(admin.TabularInline):
    model = Image
    extra = 1
    fields = ('title', 'imageFile')
    exclude = ('period', 'destination', 'event', 'restaurant', 'transportation', 'retail', 'mining', 'essentialservice',
               'activity', 'activityDestination', 'tour', 'accomodation', 'serviceType')
    classes = ['collapse']
    def render_image(self, obj):
        return mark_safe(IMAGE_SRC % obj.imageFile.url)
    render_image.short_description = 'Image preview'

class AdvertisementVideoInLine(admin.TabularInline):
    model = Video
    extra = 1
    fields = ('title', 'videoFile')
    exclude = ('period', 'destination', 'event', 'restaurant', 'transportation', 'retail', 'mining', 'essentialservice',
               'activity', 'activityDestination', 'tour', 'accomodation', 'isDisplayVideo', 'serviceType')
    classes = ['collapse']
    def render_video(self, obj):
        return mark_safe(VIDEO_SRC % obj.videoFile.url)
    render_video.short_description = 'Video preview'

class AdvertisementAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Advertisement Information', {'fields': ['title',]}),
        ('Display Settings', {'fields': ['display', 'displayFrom', 'displayTo']}),
        ('Advertisement Detail', {'fields': ['company', 'description', 'address', 'phone', 'email', 'website']}),
        ('Other Settings', {'fields': ['inTopDeal', 'orderTopDeal', 'numberOfShows', 'numberOfClicks', 'highlighted']}),
        ('Where to Show Advertisement', {'fields': ['activity', 'activityDestination', 'tour', 'accomodation', 'period',
                                                    'event', 'restaurant', 'transportation', 'retail', 'mining',
                                                    'essentialservice', 'destination', 'serviceType']}
         ),
    ]
    inlines = [AdvertisementImageInLine, AdvertisementVideoInLine]
    list_display = ('title', 'company')
    list_filter = ['title', 'company']
    search_fields = ['title', 'company']
    actions = [reset_number_of_clicks]
    form = AdvertisementForm
    class Media:
        js = ('https://code.jquery.com/jquery-1.12.4.min.js', 'admin-script.js',)

admin.site.register(Advertisement, AdvertisementAdmin)
## End of Advertisement Administration ##

## Start of Image Administration ##
class ImageAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Image Information', {'fields': ['title', 'imageFile', 'isHeaderImage']}),
        ('Where to Show Image', {'fields': ['activity', 'activityDestination', 'tour', 'accomodation', 'period', 'event',
                                            'restaurant', 'transportation', 'retail', 'mining', 'essentialservice',
                                            'destination', 'advertisement', 'serviceType']}
         ),
    ]
    form = ImageForm
admin.site.register(Image, ImageAdmin)
## End of Image Administration ##

## Start of Video Administration ##
class VideoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Video Information', {'fields': ['title', 'isDisplayVideo', 'videoFile']}),
        ('Where to Show Video', {'fields': ['activity', 'activityDestination', 'tour', 'accomodation', 'period', 'event',
                                            'restaurant', 'transportation', 'retail', 'mining', 'essentialservice',
                                            'destination','advertisement', 'serviceType']}
         ),
    ]
    form = VideoForm
admin.site.register(Video, VideoAdmin)
## End of Event Administration ##

## Start of Transportation Administration ##
class TransportationImageInLine(admin.TabularInline):
    model = Image
    extra = 1
    fields = ('title', 'imageFile', 'isHeaderImage')
    exclude = ('activity', 'activityDestination', 'tour', 'period', 'event', 'restaurant', 'retail', 'mining',
               'essentialservice', 'accomodation', 'destination', 'advertisement', 'serviceType')
    form = ImageForm
    classes = ['collapse']
    def render_image(self, obj):
        return mark_safe(IMAGE_SRC % obj.imageFile.url)
    render_image.short_description = 'Image preview'

class TransportationVideoInLine(admin.TabularInline):
    model = Video
    extra = 1
    fields = ('title', 'videoFile')
    exclude = ('activity', 'activityDestination', 'tour', 'period', 'event', 'restaurant', 'retail', 'mining',
               'essentialservice', 'accomodation', 'destination', 'advertisement', 'isDisplayVideo', 'serviceType')
    classes = ['collapse']
    def render_video(self, obj):
        return mark_safe(VIDEO_SRC % obj.videoFile.url)
    render_video.short_description = 'Video preview'

class TransportationMapInLine(admin.TabularInline):
    model = Map
    extra = 1
    fields = ('title', 'mapImage')
    exclude = ('tour', 'accomodation', 'event', 'restaurant', 'retail', 'mining', 'essentialservice',
               'destination')
    classes = ['collapse']
    def render_image(self, obj):
        return mark_safe(IMAGE_SRC % obj.mapImage.url)
    render_image.short_description = 'Map preview'

class TransportationAdvertisementInLine(admin.StackedInline):
    model = Advertisement
    extra = 1
    exclude = ('tour', 'period', 'event', 'restaurant', 'retail', 'mining', 'essentialservice', 'accomodation',
               'destination', 'activity', 'activityDestination', 'serviceType', 'display', 'displayFrom', 'displayTo')
    form = AdvertisementForm
    classes = ['collapse']

class TransportationAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Car Hire & Transportation Information', {'fields': ['title',]}),
        ('Display Settings', {'fields': ['display', 'displayFrom', 'displayTo']}),
        ('Car Hire & Transportation Detail', {'fields': ['description', 'address', 'phone', 'email', 'website', 'logo',
                                                         'image_logo']}),
        ('Other Settings', {'fields': ['numberOfClicks', 'order', 'destination', 'serviceType']}),
    ]
    inlines = [TransportationImageInLine, TransportationVideoInLine, TransportationMapInLine]
    readonly_fields = ('image_logo',)
    list_display = ('title', 'address', 'destination', 'phone', 'email', 'website')
    list_filter = ['title', 'destination']
    search_fields = ['title', 'address', 'destination__title']
    actions = [reset_number_of_clicks]

    def get_title(self, obj):
        return obj.destination.title
    get_title.short_description = "title"

    class Media:
        js = ('https://code.jquery.com/jquery-1.12.4.min.js', 'admin-script.js',)

admin.site.register(Transportation, TransportationAdmin)
## End of Transportation Administration ##

## Start of Retail Administration ##
class RetailImageInLine(admin.TabularInline):
    model = Image
    extra = 1
    fields = ('title', 'imageFile', 'isHeaderImage')
    exclude = ('activity', 'activityDestination', 'tour', 'period', 'event', 'restaurant', 'transportation', 'mining',
               'essentialservice', 'accomodation', 'destination', 'advertisement', 'serviceType')
    form = ImageForm
    classes = ['collapse']
    def render_image(self, obj):
        return mark_safe(IMAGE_SRC % obj.imageFile.url)
    render_image.short_description = 'Image preview'

class RetailVideoInLine(admin.TabularInline):
    model = Video
    extra = 1
    fields = ('title', 'videoFile')
    exclude = ('activity', 'activityDestination', 'tour', 'period', 'event', 'restaurant', 'transportation', 'mining',
               'essentialservice', 'accomodation', 'destination', 'advertisement', 'isDisplayVideo', 'serviceType')
    classes = ['collapse']
    def render_video(self, obj):
        return mark_safe(VIDEO_SRC % obj.videoFile.url)
    render_video.short_description = 'Video preview'

class RetailMapInLine(admin.TabularInline):
    model = Map
    extra = 1
    fields = ('title', 'mapImage')
    exclude = ('tour', 'accomodation', 'event', 'restaurant', 'transportation', 'mining', 'essentialservice',
               'destination')
    classes = ['collapse']
    def render_image(self, obj):
        return mark_safe(IMAGE_SRC % obj.mapImage.url)
    render_image.short_description = 'Map preview'

class RetailAdvertisementInLine(admin.StackedInline):
    model = Advertisement
    extra = 1
    exclude = ('tour', 'period', 'event', 'restaurant', 'transportation', 'mining', 'essentialservice', 'accomodation',
               'destination', 'activity', 'activityDestination', 'serviceType', 'display', 'displayFrom', 'displayTo')
    form = AdvertisementForm
    classes = ['collapse']

class RetailAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Retail Information', {'fields': ['title',]}),
        ('Display Settings', {'fields': ['display', 'displayFrom', 'displayTo']}),
        ('Retail Detail', {'fields': ['description', 'address', 'phone', 'email', 'website', 'logo', 'image_logo']}),
        ('Other Settings', {'fields': ['numberOfClicks', 'order', 'destination', 'serviceType']}),
    ]
    inlines = [RetailImageInLine, RetailVideoInLine, RetailMapInLine]
    readonly_fields = ('image_logo',)
    list_display = ('title', 'address', 'destination', 'phone', 'email', 'website')
    list_filter = ['title', 'destination']
    search_fields = ['title', 'address', 'destination__title']
    actions = [reset_number_of_clicks]

    def get_title(self, obj):
        return obj.destination.title
    get_title.short_description = "title"

    class Media:
        js = ('https://code.jquery.com/jquery-1.12.4.min.js', 'admin-script.js',)

admin.site.register(Retail, RetailAdmin)
## End of Retail Administration ##

## Start of Mining Administration ##
class MiningImageInLine(admin.TabularInline):
    model = Image
    extra = 1
    fields = ('title', 'imageFile', 'isHeaderImage')
    exclude = ('activity', 'activityDestination', 'tour', 'period', 'event', 'restaurant', 'transportation', 'retail',
               'essentialservice', 'accomodation', 'destination', 'advertisement', 'serviceType')
    form = ImageForm
    classes = ['collapse']
    def render_image(self, obj):
        return mark_safe(IMAGE_SRC % obj.imageFile.url)
    render_image.short_description = 'Image preview'

class MiningVideoInLine(admin.TabularInline):
    model = Video
    extra = 1
    fields = ('title', 'videoFile')
    exclude = ('activity', 'activityDestination', 'tour', 'period', 'event', 'restaurant', 'transportation', 'retail',
               'essentialservice', 'accomodation', 'destination', 'advertisement', 'isDisplayVideo', 'serviceType')
    classes = ['collapse']
    def render_video(self, obj):
        return mark_safe(VIDEO_SRC % obj.videoFile.url)
    render_video.short_description = 'Video preview'

class MiningMapInLine(admin.TabularInline):
    model = Map
    extra = 1
    fields = ('title', 'mapImage')
    exclude = ('tour', 'accomodation', 'event', 'restaurant', 'transportation', 'retail', 'essentialservice',
               'destination')
    classes = ['collapse']
    def render_image(self, obj):
        return mark_safe(IMAGE_SRC % obj.mapImage.url)
    render_image.short_description = 'Map preview'

class MiningAdvertisementInLine(admin.StackedInline):
    model = Advertisement
    extra = 1
    exclude = ('tour', 'period', 'event', 'restaurant', 'transportation', 'retail', 'essentialservice', 'accomodation',
               'destination', 'activity', 'activityDestination', 'serviceType', 'display', 'displayFrom', 'displayTo')
    form = AdvertisementForm
    classes = ['collapse']

class MiningAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Mining Information', {'fields': ['title',]}),
        ('Display Settings', {'fields': ['display', 'displayFrom', 'displayTo']}),
        ('Mining Detail', {'fields': ['description', 'address', 'phone', 'email', 'website', 'logo', 'image_logo']}),
        ('Other Settings', {'fields': ['numberOfClicks', 'order', 'destination', 'serviceType']}),
    ]
    inlines = [MiningImageInLine, MiningVideoInLine, MiningMapInLine]
    readonly_fields = ('image_logo',)
    list_display = ('title', 'address', 'destination', 'phone', 'email', 'website')
    list_filter = ['title', 'destination']
    search_fields = ['title', 'address', 'destination__title']
    actions = [reset_number_of_clicks]

    def get_title(self, obj):
        return obj.destination.title
    get_title.short_description = "title"

    class Media:
        js = ('https://code.jquery.com/jquery-1.12.4.min.js', 'admin-script.js',)

admin.site.register(Mining, MiningAdmin)
## End of Mining Administration ##

## Start of Essential Services Administration ##
class EssentialServiceImageInLine(admin.TabularInline):
    model = Image
    extra = 1
    fields = ('title', 'imageFile', 'isHeaderImage')
    exclude = ('activity', 'activityDestination', 'tour', 'period', 'event', 'restaurant', 'transportation', 'mining',
               'retail', 'accomodation', 'destination', 'advertisement', 'serviceType')
    form = ImageForm
    classes = ['collapse']
    def render_image(self, obj):
        return mark_safe(IMAGE_SRC % obj.imageFile.url)
    render_image.short_description = 'Image preview'

class EssentialServiceVideoInLine(admin.TabularInline):
    model = Video
    extra = 1
    fields = ('title', 'videoFile')
    exclude = ('activity', 'activityDestination', 'tour', 'period', 'event', 'restaurant', 'transportation', 'mining',
               'retail', 'accomodation', 'destination', 'advertisement', 'isDisplayVideo', 'serviceType')
    classes = ['collapse']
    def render_video(self, obj):
        return mark_safe(VIDEO_SRC % obj.videoFile.url)
    render_video.short_description = 'Video preview'

class EssentialServiceMapInLine(admin.TabularInline):
    model = Map
    extra = 1
    fields = ('title', 'mapImage')
    exclude = ('tour', 'accomodation', 'event', 'restaurant', 'transportation', 'mining', 'retail', 'destination')
    classes = ['collapse']
    def render_image(self, obj):
        return mark_safe(IMAGE_SRC % obj.mapImage.url)
    render_image.short_description = 'Map preview'

class EssentialServiceAdvertisementInLine(admin.StackedInline):
    model = Advertisement
    extra = 1
    exclude = ('tour', 'period', 'event', 'restaurant', 'transportation', 'mining', 'retail', 'accomodation',
               'destination', 'activity', 'activityDestination', 'serviceType', 'display', 'displayFrom', 'displayTo')
    form = AdvertisementForm
    classes = ['collapse']

class EssentialServiceAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Essential Service Information', {'fields': ['title',]}),
        ('Display Settings', {'fields': ['display', 'displayFrom', 'displayTo']}),
        ('Essential Service Detail', {'fields': [ 'description', 'address', 'phone', 'email', 'website', 'logo',
                                                  'image_logo']}),
        ('Other Settings', {'fields': ['numberOfClicks', 'order', 'destination', 'serviceType']}),
    ]
    inlines = [EssentialServiceImageInLine, EssentialServiceVideoInLine, EssentialServiceMapInLine]
    readonly_fields = ('image_logo',)
    list_display = ('title', 'address', 'destination', 'phone', 'email', 'website')
    list_filter = ['title', 'destination']
    search_fields = ['title', 'address', 'destination__title']
    actions = [reset_number_of_clicks]

    def get_title(self, obj):
        return obj.destination.title
    get_title.short_description = "title"

    class Media:
        js = ('https://code.jquery.com/jquery-1.12.4.min.js', 'admin-script.js',)

admin.site.register(EssentialService, EssentialServiceAdmin)
## End of Essential Services Administration ##


## Start of Activity Destination Administration ##
class ActivityDestinationImageInLine(admin.TabularInline):
    model = Image
    extra = 1
    exclude = ('destination', 'activity', 'tour', 'period', 'event', 'restaurant', 'transportation',
               'retail', 'mining', 'essentialservice', 'advertisement', 'accomodation', 'serviceType')
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
               'retail', 'mining', 'essentialservice', 'advertisement', 'accomodation', 'isDisplayVideo', 'serviceType')

    def render_video(self, obj):
        return mark_safe(VIDEO_SRC % obj.videoFile.url)
    render_video.short_description = 'Video preview'

class ActivityDestinationAdvertisementInLine(admin.StackedInline):
    model = Advertisement
    extra = 1
    exclude = ('tour', 'period', 'event', 'restaurant', 'transportation', 'mining', 'retail', 'accomodation',
               'destination', 'activity', 'essentialservices', 'serviceType', 'display', 'displayFrom', 'displayTo')
    form = AdvertisementForm

class ActivityDestinationAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Activity Information', {'fields': ['title', 'description']}),
        ('Display Settings', {'fields': ['display', 'displayFrom', 'displayTo']}),
        ('Other Settings', {'fields': ['numberOfClicks', 'activity', 'destination']}),
    ]
    inlines = [ActivityDestinationImageInLine, ActivityDestinationVideoInLine]
    list_display = ('title', 'numberOfClicks')
    list_filter = ['title', 'activity']
    search_fields = ['title', 'activity__title']
    actions = [reset_number_of_clicks]
    class Media:
        js = ('https://code.jquery.com/jquery-1.12.4.min.js', 'admin-script.js',)

admin.site.register(ActivityDestination, ActivityDestinationAdmin)
## End of Activity Destination Administration ##
admin.site.unregister(Group)

## Start of Service Type Administration ##
class ServiceTypeImageInLine(admin.TabularInline):
    model = Image
    extra = 1
    exclude = ('destination', 'activity', 'tour', 'period', 'event', 'restaurant', 'transportation',
               'retail', 'mining', 'essentialservice', 'advertisement', 'accomodation', 'activityDestination')
    fields = ('title', 'imageFile', 'isHeaderImage')
    classes = ['collapse']
    form = ImageForm
    def render_image(self, obj):
        return mark_safe(IMAGE_SRC % obj.imageFile.url)
    render_image.short_description = 'Image preview'

class ServiceTypeVideoInLine(admin.TabularInline):
    model = Video
    extra = 1
    fields = ('title', 'videoFile')
    exclude = ('destination', 'activity', 'tour', 'period', 'event', 'restaurant', 'transportation',
               'retail', 'mining', 'essentialservice', 'advertisement', 'accomodation', 'isDisplayVideo',
               'activityDestination')
    classes = ['collapse']
    def render_video(self, obj):
        return mark_safe(VIDEO_SRC % obj.videoFile.url)
    render_video.short_description = 'Video preview'

class ServiceTypeAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Activity Information', {'fields': ['title']}),
        ('Display Settings', {'fields': ['display', 'displayFrom', 'displayTo']}),
        ('Other Settings', {'fields': ['numberOfClicks']}),
    ]
    inlines = [ServiceTypeImageInLine, ServiceTypeVideoInLine]
    list_display = ('title', 'numberOfClicks')
    list_filter = ['title']
    search_fields = ['title']
    actions = [reset_number_of_clicks]
    class Media:
        js = ('https://code.jquery.com/jquery-1.12.4.min.js', 'admin-script.js',)

admin.site.register(ServiceType, ServiceTypeAdmin)
## End of Service Type Administration ##

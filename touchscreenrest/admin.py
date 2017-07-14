from django.contrib import admin
from django.contrib.auth.models import Group
from forms import AdvertisementForm, VideoForm, RestaurantForm, ImageForm, ActivityDestinationForm, EssentialServiceForm, \
    MiningForm, TransportationForm, RetailForm, MapForm
from django.utils.safestring import mark_safe
from touchscreenrest.models import Activity, ActivityDestination, Destination, Period, Event, Restaurant,\
    Transportation, Retail, Mining, EssentialService, Tour, Accomodation, Map, Advertisement, Image, Video, ServiceType, \
    Airport, AirportContact, Trivia, Section
import nested_admin
from reversion.admin import VersionAdmin
import csv
from django.http import HttpResponse


IMAGE_SRC = '''<img src="%s" />'''
VIDEO_SRC = '''<video src="%s" controls>Your browser does not support the video tag.</video>'''

## Start of Custom Actions ##
def reset_number_of_clicks(modeladmin, request, queryset):
    queryset.update(numberOfClicks=0)
reset_number_of_clicks.short_description = "Reset number of clicks back to zero"

def reset_number_of_shows(modeladmin, request, queryset):
    queryset.update(numberOfShows=0)
reset_number_of_clicks.short_description = "Reset number of shows back to zero"

def export_as_csv_action(description="Export selected objects as CSV file",
                         fields=None, exclude=None, header=True):
    """
    This function returns an export csv action
    'fields' and 'exclude' work like in django ModelForm
    'header' is whether or not to output the column names as the first row
    """
    def export_as_csv(modeladmin, request, queryset):
        """
        Generic csv export admin action.
        based on http://djangosnippets.org/snippets/1697/
        """
        opts = modeladmin.model._meta
        field_names = set([field.name for field in opts.fields])
        if fields:
            fieldset = set(fields)
            field_names = field_names & fieldset
        elif exclude:
            excludeset = set(exclude)
            field_names = field_names - excludeset

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=%s.csv' % unicode(opts).replace('.', '_')

        writer = csv.writer(response)
        if header:
            writer = csv.DictWriter(response,fields)
            writer.writeheader()
        for obj in queryset:
            writer.writerow(dict(zip(fields,[unicode(getattr(obj, field)).encode("utf-8","replace") for field in fields])))
        return response
    export_as_csv.short_description = description
    return export_as_csv

### End of Custom Actions ###

## Start of Accomodation Administration ##
class AccomodationImageInLine(admin.TabularInline):
    model = Image
    extra = 1
    fields = ('title', 'imageFile', 'isHeaderImage')
    form = ImageForm
    exclude = ('activity', 'activityDestination', 'tour', 'period', 'event', 'restaurant', 'transportation', 'retail',
               'mining', 'essentialservice', 'destination', 'advertisement', 'serviceType', 'airport', 'trivia',
               'section')
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
               'isDisplayVideo', 'serviceType', 'airport')
    classes = ['collapse']
    def render_video(self, obj):
        return mark_safe(VIDEO_SRC % obj.videoFile.url)
    render_video.short_description = 'Video preview'

class AccomodationMapInLine(admin.TabularInline):
    model = Map
    extra = 1
    fields = ('title', 'mapImage', 'mapType')
    exclude = ('tour', 'restaurant', 'transportation', 'retail', 'mining', 'essentialservice', 'event',
               'destination')
    classes = ['collapse']
    form = MapForm
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

class AccomodationAdmin(VersionAdmin):
    fieldsets = [
        ('Accommodation Title', {'fields': ['title']}),
        ('Display Settings', {'fields': ['display', 'displayFrom', 'displayTo']}),
        ('Order Settings', {'fields': ['order']}),
        ('Accommodation Detail', {'fields': ['description', ('address', 'phone', 'email'), 'website', 'logo','image_logo',
                                             'rating']}),
        ('Other Settings', {'fields': [('numberOfClicks', 'destination'),]}),

    ]
    inlines = [AccomodationImageInLine, AccomodationVideoInLine, AccomodationMapInLine]
    readonly_fields = ('image_logo',)
    list_display = ('order', 'title', 'destination', 'phone', 'email', 'numberOfClicks')
    list_filter = ['title', 'destination']
    search_fields = ['title', 'address', 'destination__title']
    actions = [reset_number_of_clicks,
               export_as_csv_action("Export selected accommodations as CSV", fields=['id', 'title', 'destination',
                                                                                     'phone', 'email', 'numberOfClicks'
                                                                                     ])]
    def get_title(self, obj):
        return obj.destination.title
    get_title.short_description = "title"

    def __init__(self, *args, **kwargs):
        super(AccomodationAdmin, self).__init__(*args, **kwargs)
        self.list_display_links = ('title',)

    class Media:
        js = ('https://code.jquery.com/jquery-1.12.4.min.js', 'admin-script.js',)
        css = {
            'all': ('admin-style.css',)
        }

admin.site.register(Accomodation, AccomodationAdmin)
## End of Accomodation Administration ##

## Start of Activity Administration ##
class ActivityImageInLine(nested_admin.NestedTabularInline):
    model = Image
    extra = 1
    exclude = ('destination', 'activityDestination', 'tour', 'period', 'event', 'restaurant', 'transportation',
               'retail', 'mining', 'essentialservice', 'advertisement', 'accomodation', 'serviceType', 'airport')
    fields = ('title', 'imageFile', 'isHeaderImage', 'trivia', 'section')
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
               'retail', 'mining', 'essentialservice', 'advertisement', 'accomodation', 'isDisplayVideo', 'serviceType',
               'airport')
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
               'retail', 'mining', 'essentialservice', 'advertisement', 'accomodation', 'serviceType', 'airport')
    classes = ['collapse']

class TourVideoNestedInLine(nested_admin.NestedTabularInline):
    model = Video
    extra = 1
    fields = ('title', 'videoFile')
    exclude = ('activity', 'activityDestination', 'period', 'destination', 'event', 'restaurant', 'transportation',
               'retail', 'mining', 'essentialservice', 'advertisement', 'accomodation', 'isDisplayVideo', 'serviceType',
               'airport')
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
               'retail', 'mining', 'essentialservice', 'advertisement', 'accomodation', 'serviceType', 'airport',
               'trivia', 'section')
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
               'retail', 'mining', 'essentialservice', 'advertisement', 'accomodation', 'isDisplayVideo', 'serviceType',
               'airport')
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
    form = ActivityDestinationForm
    extra = 1

class ActivityAdmin(nested_admin.NestedModelAdmin, VersionAdmin):
    fieldsets = [
        ('Activity Information', {'fields': ['title', 'icon']}),
        ('Display Settings', {'fields': ['display', 'displayFrom', 'displayTo']}),
        ('Order Settings', {'fields': ['order']}),
        ('Other Settings', {'fields': ['numberOfClicks']}),
    ]
    inlines = [ActivityImageInLine, ActivityVideoInLine, ActivityDestinationInLine, TourInLine]
    list_display = ('order', 'title', 'numberOfClicks')
    list_filter = ['title']
    search_fields = ['title']
    actions = [reset_number_of_clicks, export_as_csv_action("Export selected activities as CSV",
                                                            fields=['id', 'title', 'numberOfClicks'])]

    def __init__(self, *args, **kwargs):
        super(ActivityAdmin, self).__init__(*args, **kwargs)
        self.list_display_links = ('title',)

    class Media:
        js = ('https://code.jquery.com/jquery-1.12.4.min.js', 'admin-script.js',)

admin.site.register(Activity, ActivityAdmin)
## End of Activity Administration ##

## Start of Destination Administration ##
class DestinationImageInLine(admin.TabularInline):
    model = Image
    extra = 1
    exclude = ('activity', 'activityDestination', 'tour', 'period', 'event', 'restaurant', 'transportation', 'retail',
               'mining', 'essentialservice', 'advertisement', 'accomodation', 'serviceType', 'airport', 'trivia',
               'section')
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
               'mining', 'essentialservice','advertisement', 'accomodation', 'isDisplayVideo', 'serviceType', 'airport')
    classes = ['collapse']
    def render_video(self, obj):
        return mark_safe(VIDEO_SRC % obj.videoFile.url)
    render_video.short_description = 'Video preview'

class DestinationMapInLine(admin.TabularInline):
    model = Map
    extra = 1
    fields = ('title', 'mapImage', 'mapType')
    exclude = ('tour', 'restaurant', 'transportation', 'retail', 'mining', 'essentialservice', 'event',
               'accomodation')
    classes = ['collapse']
    form = MapForm
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

class DestinationAdmin(VersionAdmin):
    fieldsets = [
        ('Destination Information', {'fields': ['title',]}),
        ('Display Settings', {'fields': ['display', 'displayFrom', 'displayTo']}),
        ('Order Settings', {'fields': ['order']}),
        ('Destination Detail', {'fields': [('province', 'airport'), 'description']}),
        ('Other Settings', {'fields': ['numberOfClicks']}),
    ]
    inlines = [DestinationImageInLine, DestinationVideoInLine, DestinationMapInLine]
    list_display = ('order', 'title', 'numberOfClicks')
    list_filter = ['title']
    search_fields = ['title']
    actions = [reset_number_of_clicks, export_as_csv_action("Export selected destinations as CSV",
                                                            fields=['id', 'title', 'province', 'airport',
                                                                    'numberOfClicks'])]

    def __init__(self, *args, **kwargs):
        super(DestinationAdmin, self).__init__(*args, **kwargs)
        self.list_display_links = ('title',)

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
               'retail', 'mining', 'essentialservice','advertisement', 'accomodation', 'serviceType', 'airport',
               'trivia', 'section')
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
               'retail', 'mining', 'essentialservice', 'advertisement', 'accomodation', 'isDisplayVideo', 'serviceType',
               'airport')
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

class PeriodAdmin(VersionAdmin):
    fieldsets = [
        ('Period Information', {'fields': ['title']}),
        ('Display Settings', {'fields': ['display', 'displayFrom', 'displayTo']}),
        ('Order Settings', {'fields': ['order']}),
        ('Other Settings', {'fields': ['numberOfClicks']}),
    ]
    inlines = [PeriodImageInLine, PeriodVideoInLine]
    list_display = ('order', 'title', 'numberOfClicks')
    list_filter = ['title']
    search_fields = ['title']
    actions = [reset_number_of_clicks, export_as_csv_action("Export selected periods as CSV",
                                                            fields=['id', 'title', 'numberOfClicks'])]

    def __init__(self, *args, **kwargs):
        super(PeriodAdmin, self).__init__(*args, **kwargs)
        self.list_display_links = ('title',)

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
               'retail', 'mining', 'essentialservice', 'advertisement', 'accomodation', 'serviceType', 'airport',
               'trivia', 'section')
    classes = ['collapse']
    def render_image(self, obj):
        return mark_safe(IMAGE_SRC % obj.imageFile.url)
    render_image.short_description = 'Image preview'

class EventVideoInLine(admin.TabularInline):
    model = Video
    extra = 1
    fields = ('title', 'videoFile')
    exclude = ('activity', 'activityDestination', 'tour', 'destination', 'period', 'restaurant', 'transportation',
               'retail', 'mining', 'essentialservice', 'advertisement', 'accomodation', 'isDisplayVideo', 'serviceType',
               'airport')
    classes = ['collapse']
    def render_video(self, obj):
        return mark_safe(VIDEO_SRC % obj.videoFile.url)
    render_video.short_description = 'Video preview'

class EventMapInLine(admin.TabularInline):
    model = Map
    extra = 1
    fields = ('title', 'mapImage', 'mapType')
    exclude = ('tour', 'accomodation', 'restaurant', 'transportation', 'retail', 'mining', 'essentialservice',
               'destination')
    classes = ['collapse']
    form = MapForm
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

class EventAdmin(VersionAdmin):
    fieldsets = [
        ('Event Information', {'fields': ['title',]}),
        ('Display Settings', {'fields': ['display', 'displayFrom', 'displayTo']}),
        ('Order Settings', {'fields': ['order']}),
        ('Event Detail', {'fields': ['description', ('location', 'phone', 'email'), 'website',
                                     'eventDate', 'eventMonth', ('destination', 'period')]}),
        ('Other Settings', {'fields': ['numberOfClicks']}),
    ]
    inlines = [EventImageInLine, EventVideoInLine, EventMapInLine]
    list_display = ('order', 'title', 'destination', 'period', 'numberOfClicks')
    list_filter = ['title', 'destination', 'period']
    search_fields = ['title', 'destination__title', 'period__title']
    actions = [reset_number_of_clicks, export_as_csv_action("Export selected events as CSV",
                                                            fields=['id', 'title', 'period', 'destination',
                                                                    'numberOfClicks'])]

    def get_destination_title(self, obj):
        return obj.destination.title
    get_destination_title.short_description = "destinationTitle"

    def get_period_title(self, obj):
        return obj.period.title
    get_period_title.short_description = "periodTitle"

    def __init__(self, *args, **kwargs):
        super(EventAdmin, self).__init__(*args, **kwargs)
        self.list_display_links = ('title',)

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
               'essentialservice', 'accomodation', 'destination', 'advertisement', 'serviceType', 'airport', 'trivia',
               'section')
    classes = ['collapse']
    def render_image(self, obj):
        return mark_safe(IMAGE_SRC % obj.imageFile.url)
    render_image.short_description = 'Image preview'

class RestaurantVideoInLine(admin.TabularInline):
    model = Video
    extra = 1
    fields = ('title', 'videoFile')
    exclude = ('activity', 'activityDestination', 'tour', 'period', 'event', 'transportation', 'retail', 'mining',
               'essentialservice', 'accomodation', 'destination', 'advertisement', 'isDisplayVideo', 'serviceType',
               'airport')
    classes = ['collapse']
    def render_video(self, obj):
        return mark_safe(VIDEO_SRC % obj.videoFile.url)
    render_video.short_description = 'Video preview'

class RestaurantMapInLine(admin.TabularInline):
    model = Map
    extra = 1
    fields = ('title', 'mapImage', 'mapType')
    exclude = ('tour', 'accomodation', 'event', 'transportation', 'retail', 'mining', 'essentialservice',
               'destination')
    classes = ['collapse']
    form = MapForm
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

class RestaurantAdmin(VersionAdmin):
    fieldsets = [
        ('Restaurant Information', {'fields': ['title',]}),
        ('Display Settings', {'fields': ['display', 'displayFrom', 'displayTo']}),
        ('Order Settings', {'fields': ['order']}),
        ('Restaurant Detail', {'fields': ['description', ('address', 'phone', 'email'), 'website', 'logo', 'image_logo']}),
        ('Restaurant Guide', {'fields': ['cuisine', ('takeaway', 'takeawayOther'), ('wifi', 'wifiOther'), ('parking',
                                         'parkingOther'), ('courtesy', 'courtesyOther'), ('cards', 'price')]}),
        ('Other Settings', {'fields': [('numberOfClicks', 'onlyShowSpecificAds'), ('order', 'destination')]}),
    ]
    inlines = [RestaurantImageInLine, RestaurantVideoInLine, RestaurantMapInLine]
    readonly_fields = ('image_logo',)
    form = RestaurantForm
    list_display = ('order', 'title', 'destination', 'phone', 'email', 'numberOfClicks')
    list_filter = ['title', 'destination']
    search_fields = ['title', 'address', 'destination__title']
    actions = [reset_number_of_clicks, export_as_csv_action("Export selected restaurants as CSV",
                                                            fields=['id', 'title', 'destination', 'phone', 'email',
                                                                    'numberOfClicks'])]

    def get_title(self, obj):
        return obj.destination.title
    get_title.short_description = "title"

    def __init__(self, *args, **kwargs):
        super(RestaurantAdmin, self).__init__(*args, **kwargs)
        self.list_display_links = ('title',)

    class Media:
        js = ('https://code.jquery.com/jquery-1.12.4.min.js', 'admin-script.js',)
        css = {
            'all': ('admin-style.css',)
        }

admin.site.register(Restaurant, RestaurantAdmin)
## End of Restaurant Administration ##

## Start of Tour Administration ##
class TourImageInLine(admin.TabularInline):
    model = Image
    extra = 1
    fields = ('title', 'imageFile')
    exclude = ('activity', 'activityDestination', 'period', 'destination', 'event', 'restaurant', 'transportation',
               'retail', 'mining', 'essentialservice', 'advertisement', 'accomodation', 'serviceType', 'airport',
               'trivia', 'section')
    classes = ['collapse']
    def render_image(self, obj):
        return mark_safe(IMAGE_SRC % obj.imageFile.url)
    render_image.short_description = 'Image preview'

class TourVideoInLine(admin.TabularInline):
    model = Video
    extra = 1
    fields = ('title', 'videoFile')
    exclude = ('activity', 'activityDestination', 'period', 'destination', 'event', 'restaurant', 'transportation',
               'retail', 'mining', 'essentialservice', 'advertisement', 'accomodation', 'isDisplayVideo', 'serviceType',
               'airport')
    classes = ['collapse']
    def render_video(self, obj):
        return mark_safe(VIDEO_SRC % obj.videoFile.url)
    render_video.short_description = 'Video preview'

class TourMapInLine(admin.TabularInline):
    model = Map
    extra = 1
    fields = ('title', 'mapImage', 'mapType')
    exclude = ('restaurant', 'transportation', 'retail', 'mining', 'essentialservice', 'accomodation', 'event',
               'destination')
    classes = ['collapse']
    form = MapForm
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

class TourAdmin(VersionAdmin):
    fieldsets = [
        ('Tour Information', {'fields': ['title',]}),
        ('Display Settings', {'fields': ['display', 'displayFrom', 'displayTo']}),
        ('Order Settings', {'fields': ['order']}),
        ('Tour Detail', {'fields': ['description', ('address', 'phone', 'email'), 'website', 'logo', 'image_logo']}),
        ('Other Settings', {'fields': ['numberOfClicks', 'activity', ('activityDestination', 'destination')]}),
    ]
    inlines = [TourImageInLine, TourVideoInLine, TourMapInLine]
    readonly_fields = ('image_logo',)
    list_display = ('order', 'title', 'phone', 'email', 'activity', 'numberOfClicks')
    list_filter = ['title', 'activity', 'activityDestination']
    search_fields = ['title', 'activity__title', 'activityDestination__title']
    actions = [reset_number_of_clicks, export_as_csv_action("Export selected tours as CSV",
                                                            fields=['id', 'title', 'phone', 'email', 'activity',
                                                                    'numberOfClicks'])]

    def __init__(self, *args, **kwargs):
        super(TourAdmin, self).__init__(*args, **kwargs)
        self.list_display_links = ('title',)

    class Media:
        js = ('https://code.jquery.com/jquery-1.12.4.min.js', 'admin-script.js')
        css = {
            'all': ('admin-style.css',)
        }

admin.site.register(Tour, TourAdmin)
## End of Tour Administration ##

## Start of Map Administration ##
class MapAdmin(VersionAdmin):
    fieldsets = [
        ('Map Information', {'fields': ['title', 'mapImage', 'mapType']}),
        ('Where to Show Map', {'fields': ['tour', 'restaurant', 'transportation', 'retail', 'mining',
                                          'essentialservice', 'event', 'accomodation', 'destination']}
         ),
    ]
    form = MapForm
admin.site.register(Map, MapAdmin)
## End of Map Administration ##

## Start of Advertisement Administration ##
class AdvertisementImageInLine(admin.TabularInline):
    model = Image
    extra = 1
    fields = ('title', 'imageFile')
    exclude = ('period', 'destination', 'event', 'restaurant', 'transportation', 'retail', 'mining', 'essentialservice',
               'activity', 'activityDestination', 'tour', 'accomodation', 'serviceType', 'airport', 'trivia', 'section')
    classes = ['collapse']
    def render_image(self, obj):
        return mark_safe(IMAGE_SRC % obj.imageFile.url)
    render_image.short_description = 'Image preview'

class AdvertisementVideoInLine(admin.TabularInline):
    model = Video
    extra = 1
    fields = ('title', 'videoFile')
    exclude = ('period', 'destination', 'event', 'restaurant', 'transportation', 'retail', 'mining', 'essentialservice',
               'activity', 'activityDestination', 'tour', 'accomodation', 'isDisplayVideo', 'serviceType', 'airport')
    classes = ['collapse']
    def render_video(self, obj):
        return mark_safe(VIDEO_SRC % obj.videoFile.url)
    render_video.short_description = 'Video preview'

class AdvertisementAdmin(VersionAdmin):
    fieldsets = [
        ('Advertisement Information', {'fields': ['title',]}),
        ('Display Settings', {'fields': ['display', 'displayFrom', 'displayTo']}),
        ('Order Settings', {'fields': ['order']}),
        ('Advertisement Detail', {'fields': ['company', 'description', ('address', 'phone', 'email'), 'website']}),
        ('Other Settings', {'fields': ['numberOfShows', 'numberOfClicks', 'highlighted']}),
        ('Where to Show Advertisement', {'fields': ['activityDestination', 'accomodation', 'event', 'restaurant',
                                                    'destination', 'essentialservice', 'transportation', 'retail',
                                                    'mining', 'trivia']}
         ),
        ('Where to Redirect Advertisement (in Touchscreen SPA)', {'fields': ['redirectTo']})
    ]
    inlines = [AdvertisementImageInLine, AdvertisementVideoInLine]
    list_display = ('title', 'company', 'numberOfShows', 'numberOfClicks')
    list_filter = ['title', 'company']
    search_fields = ['title', 'company']
    actions = [reset_number_of_shows ,reset_number_of_clicks,
               export_as_csv_action("Export selected advertisements as CSV", fields=['id', 'title', 'company',
                                                                                     'numberOfShows', 'numberOfClicks'])
               ]
    form = AdvertisementForm
    class Media:
        js = ('https://code.jquery.com/jquery-1.12.4.min.js', 'admin-script.js',)

admin.site.register(Advertisement, AdvertisementAdmin)
## End of Advertisement Administration ##

## Start of Image Administration ##
class ImageAdmin(VersionAdmin):
    fieldsets = [
        ('Image Information', {'fields': ['title', 'imageFile', 'isHeaderImage']}),
        ('Where to Show Image', {'fields': ['activity', 'activityDestination', 'tour', 'accomodation', 'period', 'event',
                                            'restaurant', 'transportation', 'retail', 'mining', 'essentialservice',
                                            'destination', 'advertisement', 'serviceType', 'airport', 'section',
                                            'trivia']}
         ),
    ]
    form = ImageForm
admin.site.register(Image, ImageAdmin)
## End of Image Administration ##

## Start of Video Administration ##
class VideoAdmin(VersionAdmin):
    fieldsets = [
        ('Video Information', {'fields': ['title', 'isDisplayVideo', 'videoFile', 'numberOfShows']}),
        ('Where to Show Video', {'fields': ['activity', 'activityDestination', 'tour', 'accomodation', 'period', 'event',
                                            'restaurant', 'transportation', 'retail', 'mining', 'essentialservice',
                                            'destination','advertisement', 'serviceType', 'airport']}
         ),
    ]
    form = VideoForm
    actions = [reset_number_of_shows,
               export_as_csv_action("Export selected videos as CSV", fields=['id', 'title', 'isDisplayVideo',
                                                                             'numberOfShows'])
               ]
    list_display = ('id', 'title', 'isDisplayVideo', 'numberOfShows')
    list_filter = ['title']
    search_fields = ['title']

    def __init__(self, *args, **kwargs):
        super(VideoAdmin, self).__init__(*args, **kwargs)
        self.list_display_links = ('title',)
admin.site.register(Video, VideoAdmin)
## End of Event Administration ##

## Start of Transportation Administration ##
class TransportationImageInLine(admin.TabularInline):
    model = Image
    extra = 1
    fields = ('title', 'imageFile', 'isHeaderImage')
    exclude = ('activity', 'activityDestination', 'tour', 'period', 'event', 'restaurant', 'retail', 'mining',
               'essentialservice', 'accomodation', 'destination', 'advertisement', 'serviceType', 'airport', 'trivia',
               'section')
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
               'essentialservice', 'accomodation', 'destination', 'advertisement', 'isDisplayVideo', 'serviceType',
               'airport')
    classes = ['collapse']
    def render_video(self, obj):
        return mark_safe(VIDEO_SRC % obj.videoFile.url)
    render_video.short_description = 'Video preview'

class TransportationMapInLine(admin.TabularInline):
    model = Map
    extra = 1
    fields = ('title', 'mapImage', 'mapType')
    exclude = ('tour', 'accomodation', 'event', 'restaurant', 'retail', 'mining', 'essentialservice',
               'destination')
    classes = ['collapse']
    form = MapForm
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

class TransportationAdmin(VersionAdmin):
    fieldsets = [
        ('Car Hire & Transportation Information', {'fields': ['title',]}),
        ('Display Settings', {'fields': ['display', 'displayFrom', 'displayTo']}),
        ('Order Settings', {'fields': ['order']}),
        ('Car Hire & Transportation Detail', {'fields': ['description', ('address', 'phone', 'email'), 'website', 'logo',
                                                         'image_logo']}),
        ('Other Settings', {'fields': [('numberOfClicks', 'onlyShowSpecificAds'), ('destination', 'serviceType')]}),
    ]
    form = TransportationForm
    inlines = [TransportationImageInLine, TransportationVideoInLine, TransportationMapInLine]
    readonly_fields = ('image_logo',)
    list_display = ('order', 'title', 'destination', 'phone', 'email', 'numberOfClicks')
    list_filter = ['title', 'destination']
    search_fields = ['title', 'address', 'destination__title']
    actions = [reset_number_of_clicks, export_as_csv_action("Export selected car hire & transportation services as CSV",
                                                            fields=['id', 'title', 'destination', 'phone', 'email',
                                                                    'numberOfClicks'])]

    def get_title(self, obj):
        return obj.destination.title
    get_title.short_description = "title"

    def __init__(self, *args, **kwargs):
        super(TransportationAdmin, self).__init__(*args, **kwargs)
        self.list_display_links = ('title',)

    class Media:
        js = ('https://code.jquery.com/jquery-1.12.4.min.js', 'admin-script.js',)
        css = {
            'all': ('admin-style.css',)
        }

admin.site.register(Transportation, TransportationAdmin)
## End of Transportation Administration ##

## Start of Retail Administration ##
class RetailImageInLine(admin.TabularInline):
    model = Image
    extra = 1
    fields = ('title', 'imageFile', 'isHeaderImage')
    exclude = ('activity', 'activityDestination', 'tour', 'period', 'event', 'restaurant', 'transportation', 'mining',
               'essentialservice', 'accomodation', 'destination', 'advertisement', 'serviceType', 'airport', 'trivia',
               'section')
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
               'essentialservice', 'accomodation', 'destination', 'advertisement', 'isDisplayVideo', 'serviceType',
               'airport')
    classes = ['collapse']
    def render_video(self, obj):
        return mark_safe(VIDEO_SRC % obj.videoFile.url)
    render_video.short_description = 'Video preview'

class RetailMapInLine(admin.TabularInline):
    model = Map
    extra = 1
    fields = ('title', 'mapImage', 'mapType')
    exclude = ('tour', 'accomodation', 'event', 'restaurant', 'transportation', 'mining', 'essentialservice',
               'destination')
    classes = ['collapse']
    form = MapForm
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

class RetailAdmin(VersionAdmin):
    fieldsets = [
        ('Retail Information', {'fields': ['title',]}),
        ('Display Settings', {'fields': ['display', 'displayFrom', 'displayTo']}),
        ('Order Settings', {'fields': ['order']}),
        ('Retail Detail', {'fields': ['description', ('address', 'phone', 'email', 'website'), 'logo', 'image_logo']}),
        ('Other Settings', {'fields': [('numberOfClicks', 'onlyShowSpecificAds'), ('destination', 'serviceType')]}),
    ]
    form = RetailForm
    inlines = [RetailImageInLine, RetailVideoInLine, RetailMapInLine]
    readonly_fields = ('image_logo',)
    list_display = ('order', 'title', 'destination', 'phone', 'email', 'numberOfClicks')
    list_filter = ['title', 'destination']
    search_fields = ['title', 'address', 'destination__title']
    actions = [reset_number_of_clicks, export_as_csv_action("Export selected retail services as CSV",
                                                            fields=['id', 'title', 'destination', 'phone', 'email',
                                                                    'numberOfClicks'])]

    def get_title(self, obj):
        return obj.destination.title
    get_title.short_description = "title"

    def __init__(self, *args, **kwargs):
        super(RetailAdmin, self).__init__(*args, **kwargs)
        self.list_display_links = ('title',)

    class Media:
        js = ('https://code.jquery.com/jquery-1.12.4.min.js', 'admin-script.js',)
        css = {
            'all': ('admin-style.css',)
        }

admin.site.register(Retail, RetailAdmin)
## End of Retail Administration ##

## Start of Mining Administration ##
class MiningImageInLine(admin.TabularInline):
    model = Image
    extra = 1
    fields = ('title', 'imageFile', 'isHeaderImage')
    exclude = ('activity', 'activityDestination', 'tour', 'period', 'event', 'restaurant', 'transportation', 'retail',
               'essentialservice', 'accomodation', 'destination', 'advertisement', 'serviceType', 'airport', 'trivia',
               'section')
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
               'essentialservice', 'accomodation', 'destination', 'advertisement', 'isDisplayVideo', 'serviceType',
               'airport')
    classes = ['collapse']
    def render_video(self, obj):
        return mark_safe(VIDEO_SRC % obj.videoFile.url)
    render_video.short_description = 'Video preview'

class MiningMapInLine(admin.TabularInline):
    model = Map
    extra = 1
    fields = ('title', 'mapImage', 'mapType')
    exclude = ('tour', 'accomodation', 'event', 'restaurant', 'transportation', 'retail', 'essentialservice',
               'destination')
    form = MapForm
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

class MiningAdmin(VersionAdmin):
    fieldsets = [
        ('Mining Information', {'fields': ['title',]}),
        ('Display Settings', {'fields': ['display', 'displayFrom', 'displayTo']}),
        ('Order Settings', {'fields': ['order']}),
        ('Mining Detail', {'fields': ['description', ('address', 'phone', 'email'), 'website', 'logo', 'image_logo']}),
        ('Other Settings', {'fields': [('numberOfClicks', 'onlyShowSpecificAds'), ('destination', 'serviceType')]}),
    ]
    form = MiningForm
    inlines = [MiningImageInLine, MiningVideoInLine, MiningMapInLine]
    readonly_fields = ('image_logo',)
    list_display = ('order', 'title', 'address', 'destination', 'phone', 'email', 'numberOfClicks')
    list_filter = ['title', 'destination']
    search_fields = ['title', 'address', 'destination__title']
    actions = [reset_number_of_clicks, export_as_csv_action("Export selected mining & resource services as CSV",
                                                            fields=['id', 'title', 'destination', 'phone', 'email',
                                                                    'numberOfClicks'])]

    def get_title(self, obj):
        return obj.destination.title
    get_title.short_description = "title"

    def __init__(self, *args, **kwargs):
        super(MiningAdmin, self).__init__(*args, **kwargs)
        self.list_display_links = ('title',)

    class Media:
        js = ('https://code.jquery.com/jquery-1.12.4.min.js', 'admin-script.js',)
        css = {
            'all': ('admin-style.css',)
        }

admin.site.register(Mining, MiningAdmin)
## End of Mining Administration ##

## Start of Essential Services Administration ##
class EssentialServiceImageInLine(admin.TabularInline):
    model = Image
    extra = 1
    fields = ('title', 'imageFile', 'isHeaderImage')
    exclude = ('activity', 'activityDestination', 'tour', 'period', 'event', 'restaurant', 'transportation', 'mining',
               'retail', 'accomodation', 'destination', 'advertisement', 'serviceType', 'airport', 'trivia', 'section')
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
               'retail', 'accomodation', 'destination', 'advertisement', 'isDisplayVideo', 'serviceType', 'airport')
    classes = ['collapse']
    def render_video(self, obj):
        return mark_safe(VIDEO_SRC % obj.videoFile.url)
    render_video.short_description = 'Video preview'

class EssentialServiceMapInLine(admin.TabularInline):
    model = Map
    extra = 1
    fields = ('title', 'mapImage', 'mapType')
    exclude = ('tour', 'accomodation', 'event', 'restaurant', 'transportation', 'mining', 'retail', 'destination')
    classes = ['collapse']
    form = MapForm
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

class EssentialServiceAdmin(VersionAdmin):
    fieldsets = [
        ('Essential Service Information', {'fields': ['title',]}),
        ('Display Settings', {'fields': ['display', 'displayFrom', 'displayTo']}),
        ('Order Settings', {'fields': ['order']}),
        ('Essential Service Detail', {'fields': [ 'description', ('address', 'phone', 'email'), 'website', 'logo',
                                                  'image_logo']}),
        ('Other Settings', {'fields': [('numberOfClicks', 'onlyShowSpecificAds'), ('destination', 'serviceType')]}),
    ]
    form = EssentialServiceForm
    inlines = [EssentialServiceImageInLine, EssentialServiceVideoInLine, EssentialServiceMapInLine]
    readonly_fields = ('image_logo',)
    list_display = ('order', 'title', 'destination', 'phone', 'email', 'numberOfClicks')
    list_filter = ['title', 'destination']
    search_fields = ['title', 'address', 'destination__title']
    actions = [reset_number_of_clicks, export_as_csv_action("Export selected essential services as CSV",
                                                            fields=['id', 'title', 'destination', 'phone', 'email',
                                                                    'numberOfClicks'])]

    def get_title(self, obj):
        return obj.destination.title
    get_title.short_description = "title"

    def __init__(self, *args, **kwargs):
        super(EssentialServiceAdmin, self).__init__(*args, **kwargs)
        self.list_display_links = ('title',)

    class Media:
        js = ('https://code.jquery.com/jquery-1.12.4.min.js', 'admin-script.js',)
        css = {
            'all': ('admin-style.css',)
        }

admin.site.register(EssentialService, EssentialServiceAdmin)
## End of Essential Services Administration ##


## Start of Activity Destination Administration ##
class ActivityDestinationImageInLine(admin.TabularInline):
    model = Image
    extra = 1
    exclude = ('destination', 'activity', 'tour', 'period', 'event', 'restaurant', 'transportation',
               'retail', 'mining', 'essentialservice', 'advertisement', 'accomodation', 'serviceType', 'airport',
               'trivia', 'section')
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
               'retail', 'mining', 'essentialservice', 'advertisement', 'accomodation', 'isDisplayVideo', 'serviceType',
               'airport')

    def render_video(self, obj):
        return mark_safe(VIDEO_SRC % obj.videoFile.url)
    render_video.short_description = 'Video preview'

class ActivityDestinationAdvertisementInLine(admin.StackedInline):
    model = Advertisement
    extra = 1
    exclude = ('tour', 'period', 'event', 'restaurant', 'transportation', 'mining', 'retail', 'accomodation',
               'destination', 'activity', 'essentialservices', 'serviceType', 'display', 'displayFrom', 'displayTo')
    form = AdvertisementForm

class ActivityDestinationAdmin(VersionAdmin):
    fieldsets = [
        ('Activity Information', {'fields': ['title', 'description']}),
        ('Display Settings', {'fields': ['display', 'displayFrom', 'displayTo']}),
        ('Order Settings', {'fields': ['order']}),
        ('Other Settings', {'fields': [('numberOfClicks', 'onlyShowSpecificAds'), ('activity', 'destination')]}),
    ]
    form = ActivityDestinationForm
    inlines = [ActivityDestinationImageInLine, ActivityDestinationVideoInLine]
    list_display = ('order', 'title', 'numberOfClicks')
    list_filter = ['title', 'activity']
    search_fields = ['title', 'activity__title']
    actions = [reset_number_of_clicks, export_as_csv_action("Export selected destinations for activities as CSV",
                                                            fields=['id', 'title', 'numberOfClicks'])]

    def __init__(self, *args, **kwargs):
        super(ActivityDestinationAdmin, self).__init__(*args, **kwargs)
        self.list_display_links = ('title',)

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
               'retail', 'mining', 'essentialservice', 'advertisement', 'accomodation', 'activityDestination', 'airport',
               'trivia', 'section')
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
               'activityDestination', 'airport')
    classes = ['collapse']
    def render_video(self, obj):
        return mark_safe(VIDEO_SRC % obj.videoFile.url)
    render_video.short_description = 'Video preview'

class ServiceTypeAdmin(VersionAdmin):
    fieldsets = [
        ('Service Subsection 2 Title', {'fields': ['title', 'icon']}),
        ('Display Settings', {'fields': ['display', 'displayFrom', 'displayTo']}),
        ('Order Settings', {'fields': ['order']}),
        ('Other Settings', {'fields': ['numberOfClicks']}),
    ]
    inlines = [ServiceTypeImageInLine, ServiceTypeVideoInLine]
    list_display = ('order', 'title', 'numberOfClicks')
    list_filter = ['title']
    search_fields = ['title']
    actions = [reset_number_of_clicks, export_as_csv_action("Export selected Service Types as CSV",
                                                            fields=['id', 'title', 'numberOfClicks'])]

    def __init__(self, *args, **kwargs):
        super(ServiceTypeAdmin, self).__init__(*args, **kwargs)
        self.list_display_links = ('title',)

    class Media:
        js = ('https://code.jquery.com/jquery-1.12.4.min.js', 'admin-script.js',)

admin.site.register(ServiceType, ServiceTypeAdmin)
## End of Service Type Administration ##

## Start of Airport Administration ##
class AirportImageInLine(admin.TabularInline):
    model = Image
    extra = 1
    exclude = ('destination', 'activity', 'tour', 'period', 'event', 'restaurant', 'transportation',
               'retail', 'mining', 'essentialservice', 'advertisement', 'accomodation', 'activityDestination',
               'serviceType', 'trivia', 'section')
    fields = ('title', 'imageFile', 'isHeaderImage')
    classes = ['collapse']
    form = ImageForm

class AirportVideoInLine(admin.TabularInline):
    model = Video
    extra = 1
    fields = ('title', 'videoFile')
    exclude = ('destination', 'activity', 'tour', 'period', 'event', 'restaurant', 'transportation',
               'retail', 'mining', 'essentialservice', 'advertisement', 'accomodation', 'isDisplayVideo',
               'activityDestination', 'serviceType')
    classes = ['collapse']

class AirportContactInLine(admin.TabularInline):
    model = AirportContact
    extra = 1
    clases = ['collapse']

class AirportAdmin(VersionAdmin):
    fieldsets = [
        ('Airport Information', {'fields': ['title', 'header', 'description', 'logo', 'image_logo']}),
    ]
    inlines = [AirportContactInLine, AirportImageInLine, AirportVideoInLine]
    readonly_fields = ('image_logo',)
    list_display = ('id', 'title')

    def __init__(self, *args, **kwargs):
        super(AirportAdmin, self).__init__(*args, **kwargs)
        self.list_display_links = ('title',)

    class Media:
        css = {
            'all': ('admin-style.css',)
        }

admin.site.register(Airport, AirportAdmin)
## End of Airport Administration ##

## Start of Trivia Administration ##
class TriviaImageInLine(admin.TabularInline):
    model = Image
    extra = 1
    exclude = ('destination', 'activity', 'tour', 'period', 'event', 'restaurant', 'transportation',
               'retail', 'mining', 'essentialservice', 'advertisement', 'accomodation', 'activityDestination',
               'serviceType', 'airport')
    fields = ('title', 'imageFile')
    classes = ['collapse']
    form = ImageForm

class TriviaAdmin(VersionAdmin):
    fieldsets = [
        ('Trivia Title', {'fields': ['title', 'icon', 'numberOfClicks']}),
        ('Display Settings', {'fields': ['display', 'displayFrom', 'displayTo']}),
        ('Order Settings', {'fields': ['order']}),
    ]
    inlines = [TriviaImageInLine]
    list_display = ('id', 'title', 'numberOfClicks')
    actions = [reset_number_of_clicks, export_as_csv_action("Export selected Trivia as CSV",
                                                            fields=['id', 'title', 'order', 'numberOfClicks'])]
    def __init__(self, *args, **kwargs):
        super(TriviaAdmin, self).__init__(*args, **kwargs)
        self.list_display_links = ('title',)

    class Media:
        js = ('https://code.jquery.com/jquery-1.12.4.min.js', 'admin-script.js',)

admin.site.register(Trivia, TriviaAdmin)
## End of Trivia Administration ##

## Start of Section Administration ##
class SectionImageInLine(admin.TabularInline):
    model = Image
    extra = 1
    exclude = ('destination', 'activity', 'tour', 'period', 'event', 'restaurant', 'transportation',
               'retail', 'mining', 'essentialservice', 'advertisement', 'accomodation', 'activityDestination',
               'serviceType', 'airport', 'trivia')
    fields = ('title', 'imageFile')
    classes = ['collapse']
    form = ImageForm

class SectionAdmin(VersionAdmin):
    fieldsets = [
        ('Section Title & Text', {'fields': ['title', 'text', 'trivia']}),
        ('Display Settings', {'fields': ['display', 'displayFrom', 'displayTo']}),
        ('Order Settings', {'fields': ['order']}),
    ]
    inlines = [TriviaImageInLine]
    list_display = ('id', 'title')
    def __init__(self, *args, **kwargs):
        super(SectionAdmin, self).__init__(*args, **kwargs)
        self.list_display_links = ('title',)

    class Media:
        js = ('https://code.jquery.com/jquery-1.12.4.min.js', 'admin-script.js',)

admin.site.register(Section, SectionAdmin)
## End of Section Administration ##
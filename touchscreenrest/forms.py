from django import forms
from django.forms import RadioSelect
from models import Advertisement, Video, Restaurant, Image, Transportation, Retail, Mining, EssentialService, \
    ActivityDestination, Map
class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        exclude = ('',)
        widgets = {
            'inTopDeal': RadioSelect,
            'highlighted': RadioSelect,
        }

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        exclude = ('',)
        widgets = {
            'isDisplayVideo': RadioSelect,
        }

class RestaurantForm (forms.ModelForm):
    takeaway = forms.ChoiceField(choices=Restaurant.CHOICES, required=False, widget=RadioSelect(), label="Take-away")
    wifi = forms.ChoiceField(choices=Restaurant.CHOICES, required=False, widget=RadioSelect(), label="Wi-Fi")
    parking = forms.ChoiceField(choices=Restaurant.CHOICES, required=False, widget=RadioSelect(), label="Secure Parking")
    courtesy = forms.ChoiceField(choices=Restaurant.CHOICES, required=False, widget=RadioSelect(), label="Courtesy Transport")
    class Meta:
        model = Restaurant
        exclude = (''),
        widgets = {
            'onlyShowSpecificAds': RadioSelect,
        }

class ImageForm (forms.ModelForm):
    class Meta:
        model = Image
        exclude = (''),
        widgets = {
            'isHeaderImage': RadioSelect,
        }

class MapForm (forms.ModelForm):
    class Meta:
        model = Map
        exclude = (''),
        widgets = {
            'mapType': RadioSelect,
        }

class TransportationForm (forms.ModelForm):
    class Meta:
        model = Transportation
        exclude = (''),
        widgets = {
            'onlyShowSpecificAds': RadioSelect
        }

class RetailForm (forms.ModelForm):
    class Meta:
        model = Retail
        exclude = (''),
        widgets = {
            'onlyShowSpecificAds': RadioSelect
        }

class MiningForm (forms.ModelForm):
    class Meta:
        model = Mining
        exclude = (''),
        widgets = {
            'onlyShowSpecificAds': RadioSelect
        }

class EssentialServiceForm (forms.ModelForm):
    class Meta:
        model = EssentialService
        exclude = (''),
        widgets = {
            'onlyShowSpecificAds': RadioSelect
        }

class ActivityDestinationForm (forms.ModelForm):
    class Meta:
        model = ActivityDestination
        exclude = (''),
        widgets = {
            'onlyShowSpecificAds': RadioSelect
        }
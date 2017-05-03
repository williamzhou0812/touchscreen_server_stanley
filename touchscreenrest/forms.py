from django import forms
from django.forms import RadioSelect
from models import Advertisement, Video, Restaurant, Image
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

class ImageForm (forms.ModelForm):
    class Meta:
        model = Image
        exclude = (''),
        widgets = {
            'isHeaderImage': RadioSelect,
        }
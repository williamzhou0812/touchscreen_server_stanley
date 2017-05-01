from django import forms
from models import Advertisement, Video, Restaurant
class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        exclude = ('',)
        widgets = {
            'inTopDeal': forms.RadioSelect,
            'highlighted': forms.RadioSelect,
        }

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        exclude = ('',)
        widgets = {
            'isDisplayVideo': forms.RadioSelect,
        }

class RestaurantForm (forms.ModelForm):
    class Meta:
        model = Restaurant
        exclude = (''),
        widgets = {
            'takeaway': forms.RadioSelect,
            'wifi': forms.RadioSelect,
            'parking': forms.RadioSelect,
            'courtesy': forms.RadioSelect,
        }
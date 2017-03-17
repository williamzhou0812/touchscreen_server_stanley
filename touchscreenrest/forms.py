from django import forms
from models import Advertisement
class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        exclude = ('',)
        widgets = {
            'inTopDeal': forms.RadioSelect,
            'highlighted': forms.RadioSelect,
        }
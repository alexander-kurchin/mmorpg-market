from django import forms
from .models import AdvertModel


class AdvertForm(forms.ModelForm):
    ...

    class Meta:
        model = AdvertModel
        fields = []

from django import forms
from .models import AdvertModel
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class AdvertForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = AdvertModel
        fields = ['category', 'title', 'content']

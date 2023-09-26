from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from .models import AdvertModel, ReplyModel


class AdvertForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = AdvertModel
        fields = ['category', 'title', 'content']


class ReplyForm(forms.ModelForm):
    class Meta:
        model = ReplyModel
        fields = ['text']

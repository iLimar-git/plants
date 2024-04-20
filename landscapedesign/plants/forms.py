from django import forms
from .models import Plant
from .models import Image
from django.forms import ModelForm

class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ['name', 'color', 'height', 'description', 'date']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'image')
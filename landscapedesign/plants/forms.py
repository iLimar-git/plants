from django import forms
from .models import Plant
from django.forms import ModelForm

class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ['name', 'color', 'height', 'description', 'date']
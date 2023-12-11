
from xml.etree.ElementTree import Comment
from django import forms
from django.core.exceptions import ValidationError

from .models import Game, Speedrun, Platform

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('title', 'description', 'image', 'platforms')
        labels = {
            "description": "Please Enter a Description"
        }

class SpeedrunForm(forms.ModelForm):
    seconds = forms.IntegerField(min_value=0)
    class Meta:
        model = Speedrun
        fields = ('time_in_seconds', 'video_link')
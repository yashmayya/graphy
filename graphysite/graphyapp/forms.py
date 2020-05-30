"""Django forms module"""

from django import forms
from .models import ImageStory, VideoStory


class ImageStoryForm(forms.ModelForm):
    """Form for Image Stories"""
    class Meta:
        """Meta class"""
        model = ImageStory
        fields = ["story_name", "grapher_name", "story_description", "story_image"]


class VideoStoryForm(forms.ModelForm):
    """Form for Video Stories"""
    class Meta:
        """Meta class"""
        model = VideoStory
        fields = ["story_name", "grapher_name", "story_description", "story_video"]

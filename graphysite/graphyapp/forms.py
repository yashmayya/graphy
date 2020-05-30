from django import forms
from .models import ImageStory, VideoStory

class ImageStoryForm(forms.ModelForm):
	class Meta:
		model = ImageStory
		fields = ["story_name", "grapher_name", "story_description", "story_image"]


class VideoStoryForm(forms.ModelForm):
	class Meta:
		model = VideoStory
		fields = ["story_name", "grapher_name", "story_description", "story_video"]
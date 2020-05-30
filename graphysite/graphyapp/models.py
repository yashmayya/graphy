from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.

class ImageStory(models.Model):
	story_name = models.CharField(max_length=200)
	grapher_name = models.CharField(max_length=200)
	created_time = models.DateTimeField(auto_now_add=True)
	story_description = models.TextField()
	story_image = models.ImageField(upload_to='storyimages')

	def __str__(self):
		return self.story_name

	def get_cname(self):
	    class_name = "ImageStory"
	    return class_name


class VideoStory(models.Model):
	story_name = models.CharField(max_length=200)
	grapher_name = models.CharField(max_length=200)
	created_time = models.DateTimeField(auto_now_add=True)
	story_description = models.TextField()
	story_video = models.FileField(upload_to='storyvideos', validators=[FileExtensionValidator(allowed_extensions=['mp4', 'avi'])])

	def __str__(self):
		return self.story_name

	def get_cname(self):
	    class_name = "VideoStory"
	    return class_name
"""Django models module"""

from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.

class ImageStory(models.Model):
    """Model for image stories"""
    story_name = models.CharField(max_length=200)
    grapher_name = models.CharField(max_length=200)
    created_time = models.DateTimeField(auto_now_add=True)
    story_description = models.TextField()
    story_image = models.ImageField(upload_to='storyimages')

    def __str__(self):
        """Custom str representation"""
        return str(self.story_name)

    def get_cname(self):
        """Get class name to distinguish objects of ImageStory and VideoStory in templates"""
        class_name = "ImageStory"
        return class_name


class VideoStory(models.Model):
    """Model for video stories"""
    story_name = models.CharField(max_length=200)
    grapher_name = models.CharField(max_length=200)
    created_time = models.DateTimeField(auto_now_add=True)
    story_description = models.TextField()
    story_video = models.FileField(upload_to='storyvideos', validators=[FileExtensionValidator(
        allowed_extensions=['mp4', 'avi'])])

    def __str__(self):
        """Custom str representation"""
        return str(self.story_name)

    def get_cname(self):
        """Get class name to distinguish objects of ImageStory and VideoStory in templates"""
        class_name = "VideoStory"
        return class_name

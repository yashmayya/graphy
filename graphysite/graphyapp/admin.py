"""Django admin module"""

from django.contrib import admin
from .models import ImageStory, VideoStory
# Register your models here.

admin.site.register(ImageStory)
admin.site.register(VideoStory)

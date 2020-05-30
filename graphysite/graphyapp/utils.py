"""Utils"""

from PIL import Image
from .models import ImageStory


def resize_image(image_story):
    """Util to resize image for ImageStory object"""
    image = Image.open(image_story.story_image)
    image.thumbnail((1200, 600))
    image.save(image_story.story_image)
    image_story.save()

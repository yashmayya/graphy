from .models import ImageStory
from PIL import Image

def resize_image(image_story):
	image = Image.open(image_story.story_image)
	image.thumbnail((1200, 600))
	image.save(image_story.story_image)
	image_story.save()
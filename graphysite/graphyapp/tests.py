from django.test import TestCase
from django.urls import reverse
from .models import ImageStory, VideoStory


class ImageStoryModelTests(TestCase):
	def test_timestamp_created(self):
		img_story = ImageStory(story_name='test_story', grapher_name='yash', story_description='this is a story')
		img_story.save()
		self.assertIsNotNone(img_story.created_time)


class VideoStoryModelTests(TestCase):
	def test_timestamp_created(self):
		img_story = VideoStory(story_name='test_story', grapher_name='yash', story_description='this is a story')
		img_story.save()
		self.assertIsNotNone(img_story.created_time)



class StoryViewTests(TestCase):
	def test_no_stories(self):
		"""If no stories exist, appropriate message displayed"""
		response = self.client.get(reverse('graphyapp:stories'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "No stories created yet.")
		self.assertQuerysetEqual(response.context['stories'], [])


	def test_one_story(self):
		"""If at least one story exists, context should have the list of stories.
		   Also check custom __str__ representation for model """

		img_story = ImageStory(story_name='test_story', grapher_name='yash', story_description='this is a story', story_image="test")
		img_story.save()
		response = self.client.get(reverse('graphyapp:stories'))
		self.assertQuerysetEqual(response.context['stories'], ['<ImageStory: test_story>'])


	def test_story_order(self):
		"""If multiple image and video stories exist, the list of stories should be ordered by timestamp"""
		img_story = ImageStory(story_name='test_story', grapher_name='yash', story_description='this is a story', story_image="test")
		img_story.save()
		img_story2 = ImageStory(story_name='test_story2', grapher_name='yash', story_description='this is a story', story_image="test2")
		img_story2.save()
		video_story = VideoStory(story_name='test_story', grapher_name='yash', story_description='this is a story', story_video="test_vid")
		video_story.save()
		response = self.client.get(reverse('graphyapp:stories'))
		stories = response.context['stories']
		sorted_stories = sorted(stories, key=lambda inst: inst.created_time, reverse=True)

		self.assertEqual(stories, sorted_stories)
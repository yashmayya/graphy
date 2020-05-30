from itertools import chain

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import ImageStory, VideoStory
from .forms import ImageStoryForm, VideoStoryForm
# Create your views here.

def index(request):
    return HttpResponse("Hello, world.")


def stories(request):
	stories_list = ImageStory.objects.all().order_by('-created_time')
	videos_list = VideoStory.objects.all().order_by('-created_time')
	stories = sorted(chain(stories_list, videos_list), key=lambda inst: inst.created_time, reverse=True)
	context = {'stories':stories}
	return render(request, 'graphyapp/stories.html', context)


def create_image_story(request):
	form = ImageStoryForm(request.POST or None, request.FILES or None)

	if request.method=="POST":
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('graphyapp:stories'))

	context = {}
	context['form'] = form
	return render(request, "graphyapp/create_image_story.html", context)


def create_video_story(request):
	form = VideoStoryForm(request.POST or None, request.FILES or None)

	if request.method=="POST":
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('graphyapp:stories'))

	context = {}
	context['form'] = form
	return render(request, "graphyapp/create_video_story.html", context)
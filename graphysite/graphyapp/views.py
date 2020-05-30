"""Django views module"""

from itertools import chain
# import threading

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import ImageStory, VideoStory
from .forms import ImageStoryForm, VideoStoryForm
from .utils import resize_image
# Create your views here.


def stories_view(request):
    """Stories view- homepage"""
    stories_list = ImageStory.objects.all().order_by('-created_time')
    videos_list = VideoStory.objects.all().order_by('-created_time')
    stories = sorted(chain(stories_list, videos_list), key=lambda inst: inst.created_time,
                     reverse=True)
    context = {'stories': stories}
    return render(request, 'graphyapp/stories.html', context)


def create_image_story(request):
    """View for creating image stories"""
    form = ImageStoryForm(request.POST or None, request.FILES or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            # t = threading.Thread(target=resize_image, args=[image_story])
            # t.setDaemon(True)
            # t.start()
            return HttpResponseRedirect(reverse('graphyapp:stories'))

    context = {'form': form}

    return render(request, "graphyapp/create_image_story.html", context)


def create_video_story(request):
    """View for creating video stories"""
    form = VideoStoryForm(request.POST or None, request.FILES or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('graphyapp:stories'))

    context = {'form': form}
    context['form'] = form
    return render(request, "graphyapp/create_video_story.html", context)

"""Django URLs module for graphyapp"""

from django.urls import path

from . import views

app_name = 'graphyapp'
urlpatterns = [
    path('', views.stories_view, name='stories'),
    path('create/image', views.create_image_story, name='create_image'),
    path('create/video', views.create_video_story, name='create_video'),
]

from django.urls import path
from . import views

urlpatterns = [
    path("", views.text_to_speech_view, name='text_to_speech_view'),
]
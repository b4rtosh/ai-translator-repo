from django.urls import path
from . import views

urlpatterns = [
    path("", views.speech_to_speech_view, name='speech_to_speech_view'),
]
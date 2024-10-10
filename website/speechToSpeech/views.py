from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def speech_to_speech_view(request):
    return render(request, 'speechToSpeech/translate_sound_sound.html')

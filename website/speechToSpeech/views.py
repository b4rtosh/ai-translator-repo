from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def speech_to_speech_view(request):
    return HttpResponse('Welcome to the speech to speech translation page')

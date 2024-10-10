from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def speech_to_text_view(request):
    return render(request, 'speechToText/translate_sound.html')

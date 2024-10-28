from django.shortcuts import render
import azure.cognitiveservices.speech as speechsdk
from . import utils

def text_to_speech_view(request):
    if request.method == 'POST':
        text_input = request.POST.get('text_input')
        try:
            speech_result = utils.generate_speech(text_input)
            return render(request, 'textToSpeech/generate_speech.html',
                          {'audio_stream': speech_result, 'text-input': text_input})
        except Exception as e:
            print(e)
            return render(request, 'textToSpeech/generate_speech.html', {'error': e, 'text_input': text_input})
    return render(request, 'textToSpeech/generate_speech.html')


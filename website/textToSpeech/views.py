import base64
from django.shortcuts import render
from . import utils

def text_to_speech_view(request):
    if request.method == 'POST':
        text_input = request.POST.get('text-input')
        try:
            audio_path = utils.generate_speech(text_input)
            with open(audio_path, 'rb') as audio_file:
                audio_data = base64.b64encode(audio_file.read()).decode('utf-8')
            return render(request, 'textToSpeech/generate_speech.html',
                          {'audio': audio_data, 'text_input': text_input})
        except Exception as e:
            print(e)
            return render(request, 'textToSpeech/generate_speech.html', {'error': e, 'text_input': text_input})
    return render(request, 'textToSpeech/generate_speech.html')


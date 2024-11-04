import base64
from django.shortcuts import render
from requests.packages import target

from . import utils as speech_utils
from textToText import utils, translator


def find_speech_by_code(code, speeches):
    for speech in speeches:
        if speech['Code'] == code:
            return speech
    return None


def text_to_speech_view(request):
    languages = utils.get_supported_languages()
    speeches = speech_utils.load_speeches()
    if request.method == 'POST':
        text_input = request.POST.get('text-input')
        target_language = request.POST.get('language-target')
        print(target_language)
        target_language_speech = find_speech_by_code(target_language, speeches)
        try:
            print(target_language[0:2])
            translation = translator.translateToFrom('auto', target_language[0:2], text_input)
            source_language = translation[0]['detectedLanguage']['language']
            translation = translation[0]['translations'][0]['text']
            print(target_language_speech['Speech'])
            audio_path = speech_utils.generate_speech(translation, target_language_speech['Speech'])
            with open(audio_path, 'rb') as audio_file:
                audio_data = base64.b64encode(audio_file.read()).decode('utf-8')
            return render(request, 'textToSpeech/generate_speech.html',
                          {'audio': audio_data, 'text_input': text_input, 'speeches': speeches,
                           'selected_language_before': source_language, 'selected_language_after': target_language,
                           'languages': languages})
        except Exception as e:
            print(e)
            return render(request, 'textToSpeech/generate_speech.html', {'error': e,
                                                                         'text_input': text_input,
                                                                         'speeches': speeches})
    return render(request, 'textToSpeech/generate_speech.html', {'speeches': speeches})

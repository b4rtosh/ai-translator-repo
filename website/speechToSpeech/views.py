import base64
import os
import tempfile
from django.shortcuts import render
from speechToText import utils as transcribe_utils
from textToSpeech import utils as speech_utils
from textToText import utils, translator


def find_speech_by_code(code, speeches):
    for speech in speeches:
        if speech['Code'] == code:
            return speech
    return None


def speech_to_speech_view(request):
    languages = utils.get_supported_languages()
    speeches = speech_utils.load_speeches()
    if request.method == 'POST':
        catalog = request.FILES['uploaded-file']
        temp_dir = tempfile.gettempdir()
        audio_file_path = os.path.join(temp_dir, catalog.name)
        with open(audio_file_path, 'wb') as f:
            for chunk in catalog.chunks():
                f.write(chunk)
        print(audio_file_path)

        target_language = request.POST.get('language-target')
        target_language_speech = find_speech_by_code(target_language, speeches)
        transcribed = transcribe_utils.recognize_speech_from_audio(audio_file_path)
        try:
            print(target_language[0:2])
            translation = translator.translateToFrom('auto', target_language[0:2], transcribed)
            source_language = translation[0]['detectedLanguage']['language']
            translation = translation[0]['translations'][0]['text']
            print(target_language_speech['Speech'])
            new_audio_path = speech_utils.generate_speech(translation, target_language_speech['Speech'])
            with open(new_audio_path, 'rb') as audio_file:
                audio_data = base64.b64encode(audio_file.read()).decode('utf-8')
            return render(request, 'speechToSpeech/translate_sound_sound.html',
                          {'audio': audio_data, 'speeches': speeches,
                           'selected_langauge_before': source_language, 'selected_language_after':target_language,
                           'languages': languages})
        except Exception as e:
            print(e)
            return render(request, 'speechToSpeech/translate_sound_sound.html',
                          {'error': e, 'speeches': speeches})
    return render(request, 'speechToSpeech/translate_sound_sound.html', {'speeches': speeches})


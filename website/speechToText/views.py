import os
import tempfile
from django.shortcuts import render
from . import speechToText
from textToText import translator, utils


# Create your views here.
def speech_to_text_view(request):
    languages = utils.get_supported_languages()
    if request.method == 'POST':
        catalog = request.FILES['uploaded-file']

        # save temporarily the file and get the path
        temp_dir = tempfile.gettempdir()
        audio_file_path = os.path.join(temp_dir, catalog.name)
        with open(audio_file_path, 'wb') as f:
            for chunk in catalog.chunks():
                f.write(chunk)
        print(audio_file_path)
        # source_language = request.POST.get('language-source')
        target_language = request.POST.get('language-target')
        print(target_language)
        transcribed = speechToText.recognize_speech_from_audio(audio_file_path)
        print(transcribed)
        translation = transcribed
        # if source_language != target_language:
        #     translation = translator.translateToFrom(source_language, target_language, transcribed)
        #     if source_language == 'auto':
        #         source_language = translation[0]['detectedLanguage']['language']
        #     translation = translation[0]['translations'][0]['text']
        translation = translator.translateToFrom('auto', target_language, transcribed)
        source_language = translation[0]['detectedLanguage']['language']
        translation = translation[0]['translations'][0]['text']
        os.remove(audio_file_path)
        return render(request, 'speechToText/translate_sound.html',
                      {'languages': languages, 'selected_language_before': source_language,
                       'selected_language_after': target_language, 'translated_text': translation})
    return render(request, 'speechToText/translate_sound.html', {'languages': languages})

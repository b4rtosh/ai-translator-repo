from idlelib.pyparse import trans

from django.shortcuts import render
from . import speechToText
from textToText import translator, utils


# Create your views here.
def speech_to_text_view(request):
    languages = utils.get_supported_languages()
    if request.method == 'POST':
        catalog = request.FILES['uploaded-file']
        file_content = catalog.read()
        source_language = request.POST.get('language-source')
        print(source_language)
        target_language = request.POST.get('language-target')
        print(target_language)
        transcribed = speechToText.recognize_speech_from_audio(file_content)
        print(transcribed)
        translation = translator.translateToFrom(source_language, target_language, transcribed)
        if source_language == 'auto':
            source_language = translation[0]['detectedLanguage']['language']
        translation = translation[0]['translations'][0]['text']
        return render(request, 'speechToText/translate_sound.html',
                      {'languages': languages, 'selected_language_before': source_language,
                       'selected_language_after': target_language, 'translated_text': translation})
    return render(request, 'speechToText/translate_sound.html', {'languages': languages})

from django.shortcuts import render
from . import translator, utils


# Create your views here.
def text_to_text_view(request):
    languages = utils.get_supported_languages()
    if request.method == 'POST':
        input_text = request.POST.get('input-text')
        print(input_text)
        source_language = request.POST.get('language-source')
        print(source_language)
        target_language = request.POST.get('language-target')
        print(target_language)
        if source_language != target_language:
            translated_text = translator.translateToFrom(source_language, target_language, input_text)
            if source_language == 'auto':
                source_language = translated_text[0]['detectedLanguage']['language']
            translated_text = translated_text[0]['translations'][0]['text']
        else:
            translated_text = input_text
        return render(request, 'textToText/translate_text.html',
                      {'input_text': input_text, 'selected_language_before': source_language,
                       'selected_language_after': target_language, 'translated_text': translated_text,
                       'languages': languages})
    return render(request, 'textToText/translate_text.html', {'languages': languages})


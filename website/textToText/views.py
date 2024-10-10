from django.shortcuts import render
from django.http import HttpResponse
from . import translator

from .forms import TextInputForm


# Create your views here.
def text_to_text_view(request):
    if request.method == 'POST':
        input_text = request.POST.get('input_text')
        print(input_text)
        source_language = request.POST.get('source_language')
        print(source_language)
        target_language = request.POST.get('target_language')
        print(target_language)
        translated_text = translator.translateToFrom(source_language, target_language, input_text)
        return render(request, 'textToText/translate_text.html', {'input_text': input_text, 'source_language': source_language, 'target_language': target_language, 'translated_text': translated_text})
    return render(request, 'textToText/translate_text.html')


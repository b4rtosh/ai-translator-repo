from django.shortcuts import render
from django.http import HttpResponse
from . import translator

from .forms import TextInputForm


# Create your views here.
def text_to_text_view(request):
    if request.method == 'POST':
        form = TextInputForm(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data['user_input']

            translation = translator.translateToFrom('pl', 'en', user_input)
            print(translation)
            return render(request, 'textToText/result.html', {'api_data': translation})
    else:
        form = TextInputForm()
    return render(request, 'textToText/input.html', {'form': form})

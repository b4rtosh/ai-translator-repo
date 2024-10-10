from django.shortcuts import render
from django.http import HttpResponse
from . import translator

from .forms import TextInputForm


# Create your views here.
def text_to_text_view(request):
    return render(request, 'textToText/translate_text.html')
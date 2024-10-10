from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from googletrans import Translator  # Do tłumaczenia
from django.http import JsonResponse

# Ekran powitalny
def home(request):
    return render(request, 'home.html')

# Strona tłumaczenia tekstu
def translate_text(request):
    translated_text = None
 #Tu jakiś placeholder niedziałający algorytm
    if request.method == 'POST':
        input_text = request.POST.get('input_text')
        source_language = request.POST.get('source_language', 'auto')
        target_language = request.POST.get('target_language')

        # Wywołanie funkcji tłumaczącej z backendu
        translated_text = translate_text_backend(input_text, source_language, target_language)

    return render(request, 'translate_text.html', {
        'translated_text': translated_text
    })
# Strona tłumaczenia dźwięku (placeholder, ni ma żadnej funkcjonalności)
def translate_sound(request):
    return render(request, 'translate_sound.html')
# Strona do tłumaczenia z dźwięku na dźwięk
def translate_sound_sound(request):
    return render(request, 'translate_sound_sound.html')
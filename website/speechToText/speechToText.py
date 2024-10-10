import os
from pydub import AudioSegment
import azure.cognitiveservices.speech as speechsdk
from moviepy.editor import VideoFileClip

# Konwersja MP3 do WAV
def convert_mp3_to_wav(mp3_path, wav_path):
    audio = AudioSegment.from_mp3(mp3_path)
    audio.export(wav_path, format="wav")

# Rozpoznawanie mowy za pomocą Azure Speech Service
def recognize_speech_from_audio(wav_path, speech_key, service_region):
    # Tworzenie konfiguracji dla usługi Azure Speech
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    audio_input = speechsdk.AudioConfig(filename=wav_path)

    # Tworzenie obiektu rozpoznawania mowy
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)

    print("Rozpoczynanie rozpoznawania mowy...")

    # Wywołanie synchronizujące na rozpoznanie mowy (zwraca po zakończeniu rozpoznawania)
    result = speech_recognizer.recognize_once()

    # Obsługa wyników
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Rozpoznany tekst:", result.text)
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("Nie rozpoznano żadnej mowy.")
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print(f"Rozpoznawanie anulowane: {cancellation_details.reason}")
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print(f"Błąd: {cancellation_details.error_details}")

# Ścieżki do pliku MP3 i docelowego pliku WAV
video_path = "film.mp4"
mp3_path = 'audio.mp3'  # Podaj ścieżkę do swojego pliku MP3
wav_path = 'plik.wav'  # Tymczasowy plik WAV

# Klucz API i region Azure Speech Service
speech_key = "84d3af67396442ddaec8c499ff208bfd"  # Zamień na swój klucz API Azure
service_region = "westeurope"  # Region np. "westeurope"

# Konwertujemy MP3 do WAV
convert_mp3_to_wav(mp3_path, wav_path)

# Rozpoznawanie mowy
recognize_speech_from_audio(wav_path, speech_key, service_region)


import os
from pydub import AudioSegment
import azure.cognitiveservices.speech as speechsdk
from dotenv import load_dotenv


# Konwersja MP3 do WAV
def convert_mp3_to_wav(mp3_path, wav_path):
    audio = AudioSegment.from_mp3(mp3_path)
    audio.export(wav_path, format="wav")


def recognize_speech_from_audio(audio_path):
    load_dotenv()
    speech_key = os.getenv('API_KEY_SPEECH')
    service_region = os.getenv('API_LOCATION')

    # Create configuration for Azure Speech Service
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

    audio_input = speechsdk.AudioConfig(filename=audio_path)

    # Create the speech recognizer
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)

    print("Starting speech recognition...")

    # Synchronously call the speech recognizer (returns after recognition completes)
    result = speech_recognizer.recognize_once()

    # Handle results
    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Success")
        return result.text
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized.")
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print(f"Speech recognition canceled: {cancellation_details.reason}")
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print(f"Error: {cancellation_details.error_details}")
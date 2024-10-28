import os
import tempfile

import azure.cognitiveservices.speech as speechsdk
import dotenv


def generate_speech(text):
    # Load environment variables from .env file
    dotenv.load_dotenv()

    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
    speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('API_KEY_SPEECH'), region=os.environ.get('API_LOCATION'))
    print(os.environ.get('API_KEY_SPEECH'), os.environ.get('API_LOCATION'))
    # create a file to store the audio
    temp_dir = tempfile.gettempdir()
    audio_file_path = os.path.join(temp_dir, 'audio.wav')

    audio_config = speechsdk.audio.AudioOutputConfig(filename=audio_file_path)
    # The neural multilingual voice can speak different languages based on the input text.
    speech_config.speech_synthesis_voice_name='en-US-AvaMultilingualNeural'

    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

    if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        return audio_file_path
    else:
        raise Exception(f"Speech synthesis failed: {speech_synthesis_result.reason}")

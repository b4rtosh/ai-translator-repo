import os
import azure.cognitiveservices.speech as speechsdk
import dotenv


def generate_speech(text):
    # Load environment variables from .env file
    dotenv.load_dotenv()

    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
    speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('API_KEY_SPEECH'), region=os.environ.get('API_LOCATION'))
    # create stream to push audio data to
    push_stream = speechsdk.audio.AudioOutputStream()
    audio_config = speechsdk.audio.AudioOutputConfig(stream=push_stream)
    # audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
    # The neural multilingual voice can speak different languages based on the input text.
    speech_config.speech_synthesis_voice_name='en-US-AvaMultilingualNeural'

    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    # Get text from the console and synthesize to the default speaker.
    print("Enter some text that you want to speak >")

    speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

    if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        audio_data = speech_synthesis_result
        return audio_data
    elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_synthesis_result.cancellation_details
        return Exception("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                return Exception("Error details: {}".format(cancellation_details.error_details))
    return Exception("Unknown error: {}".format(speech_synthesis_result.reason))

import os
import tempfile
import azure.cognitiveservices.speech as speechsdk
import dotenv

dotenv.load_dotenv()


def generate_speech(text, speech='en-US-AvaMultilingualNeural'):
    speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('API_KEY_SPEECH'),
                                           region=os.environ.get('API_LOCATION'))
    print(os.environ.get('API_KEY_SPEECH'), os.environ.get('API_LOCATION'))
    # create a file to store the audio
    temp_dir = tempfile.gettempdir()
    audio_file_path = os.path.join(temp_dir, 'audio.wav')
    print("Speech: ", speech)
    audio_config = speechsdk.audio.AudioOutputConfig(filename=audio_file_path)
    # The neural multilingual voice can speak different languages based on the input text.
    speech_config.speech_synthesis_voice_name = speech

    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

    if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        return audio_file_path
    else:
        raise Exception(f"Speech synthesis failed: {speech_synthesis_result.reason}")


def load_speeches():
    return [
        {"Code": "ar-EG", "Language": "Arabic (Egypt)", "Speech": "ar-EG-ShakirNeural"},
        {"Code": "bg-BG", "Language": "Bulgarian (Bulgaria)", "Speech": "bg-BG-BorislavNeural"},
        {"Code": "cs-CZ", "Language": "Czech (Czechia)", "Speech": "cs-CZ-AntoninNeural"},
        {"Code": "de-DE", "Language": "German (Germany)", "Speech": "de-DE-KatjaNeural"},
        {"Code": "el-GR", "Language": "Greek (Greece)", "Speech": "el-GR-AthinaNeural"},
        {"Code": "en-GB", "Language": "English (United Kingdom)", "Speech": "en-GB-SoniaNeural"},
        {"Code": "es-ES", "Language": "Spanish (Spain)", "Speech": "es-ES-ElviraNeural"},
        {"Code": "fa-IR", "Language": "Persian (Iran)", "Speech": "fa-IR-FaridNeural"},
        {"Code": "fi-FI", "Language": "Finnish (Finland)", "Speech": "fi-FI-SelmaNeural"},
        {"Code": "fr-FR", "Language": "French (France)", "Speech": "fr-FR-DeniseNeural"},
        {"Code": "he-IL", "Language": "Hebrew (Israel)", "Speech": "he-IL-AvriNeural"},
        {"Code": "hr-HR", "Language": "Croatian (Croatia)", "Speech": "hr-HR-GabrijelaNeural"},
        {"Code": "hu-HU", "Language": "Hungarian (Hungary)", "Speech": "hu-HU-TamasNeural"},
        {"Code": "it-IT", "Language": "Italian (Italy)", "Speech": "it-IT-ElsaNeural"},
        {"Code": "ja-JP", "Language": "Japanese (Japan)", "Speech": "ja-JP-KeitaNeural"},
        {"Code": "kn-IN", "Language": "Kannada (India)", "Speech": "kn-IN-SapnaNeural"},
        {"Code": "ko-KR", "Language": "Korean (Korea)", "Speech": "ko-KR-SunHiNeural"},
        {"Code": "pl-PL", "Language": "Polish (Poland)", "Speech": "pl-PL-AgnieszkaNeural"},
        {"Code": "pt-BR", "Language": "Portuguese (Brazil)", "Speech": "pt-BR-FranciscaNeural"},
        {"Code": "ru-RU", "Language": "Russian (Russia)", "Speech": "ru-RU-DmitryNeural"},
        {"Code": "sv-SE", "Language": "Swedish (Sweden)", "Speech": "sv-SE-SofieNeural"},
        {"Code": "th-TH", "Language": "Thai (Thailand)", "Speech": "th-TH-PremwadeeNeural"},
        {"Code": "zh-CN", "Language": "Chinese (Mandarin, Simplified)", "Speech": "zh-CN-XiaoxiaoNeural"}
    ]

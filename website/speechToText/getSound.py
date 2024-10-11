import os
from moviepy.editor import VideoFileClip
from pydub import AudioSegment

video_path = "film.mp4"
audio_path = "audio.mp3"

if not os.path.exists(video_path):
    print("Plik wideo nie istnieje!")
else:
    try:
        video = VideoFileClip(video_path)
        audio = video.audio
        audio.write_audiofile(audio_path)
        audio.close()
        video.close()

    except Exception as e:
        print(f"Wystąpił błąd: {e}")


audioConvertion = AudioSegment.from_mp3("audio.mp3")
audioConvertion.export("audioPoKonwersji.wav", format="wav")
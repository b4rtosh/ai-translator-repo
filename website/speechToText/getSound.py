from pydub import AudioSegment

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
        print("Ekstrakcja dźwięku zakończona sukcesem.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")

audioConvertion = AudioSegment.from_mp3("audio.mp3")

audioConvertion.export("plik.wav", format="wav")


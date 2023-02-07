from gtts import gTTS
import playsound
def criando_audio(audio):
    tts = gTTS(audio, lang='pt-br')
    tts.save('audios/audio.mp3')
    print("Aprendendo oque você está falando.")
    playsound('audios/audio.mp3')
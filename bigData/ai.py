import speech_recognition as sr
from pathlib import Path
from pygame import mixer

def rec(rate=16000):
    r = sr.Recognizer()
    with sr.Microphone(sample_rate=rate) as source:
        print("please say something")
        audio =  r.listen(source)

    au = "recoding.mp3"
    f = Path(au).absolute()
    with f.open("wb") as f:
        f.write(audio.get_wav_data())
    return f
def playsound(file):

    mixer.init()
    mixer.music.load(str(file))
    mixer.music.play()
    while mixer.music.get_busy():
        pass

    mixer.music.stop()

def main():

    text = rec()
    playsound(text)
if __name__ == '__main__':
    main()
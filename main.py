import pyttsx3 as pt
import speech_recognition as speach

sr = speach.Recognizer()
engine = pt.init()

# Set the speed and volume of the voice
engine.setProperty('rate', 150)  # 150 words per minute
engine.setProperty('volume', 1)  # 80% volume


with speach.Microphone() as mic:
    while True:
        sr.adjust_for_ambient_noise(source=mic)

        print(">>>")
        audio = sr.listen(mic, timeout=0.8, phrase_time_limit=10, )
        text = sr.recognize_google(audio_data=audio, language="ru-RU").lower()

        print(text)
        engine.say(text=text)
        engine.runAndWait()

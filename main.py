import speech_recognition as sr

r = sr.Recognizer()

def hello():
    return "Привет"

with sr.Microphone() as mic:
    r.adjust_for_ambient_noise(source=mic)

    audio = r.listen(mic)
    mec = r.recognize_google(audio_data=audio, language="RU-ru",).lower()

print(mec)

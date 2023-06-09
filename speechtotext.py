import speech_recognition as sr
import time

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Silahkan bicara')
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language="id-ID")
        print('{}'.format(text))
        time.sleep(100.0)

    except:
        print('error')
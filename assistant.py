import speech_recognition as sr
from gtts import gTTS
import os
import time
import sys

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        print("You said: " + r.recognize_google(audio))
        amanda(r.recognize_google(audio))
    except sr.UnknownValueError:
        say("Could you repeat that?")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

def say(audio):
    print(audio)
    tts = gTTS(text=audio, lang='en')
    tts.save("audio.mp3")
    os.system("mpg123 audio.mp3")

def amanda(command):
    if command == 'time':
        respose = "It's " + time.ctime()
        say(respose)
    elif command == 'goodbye':
        say(command)
        sys.exit(0)

say("Hi, how can I help you today?")

while 1:
    command = listen()


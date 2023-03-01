#!/usr/local/bin/python3
import speech_recognition as sr
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser

engine = pyttsx3.init()
engine.say("Hello world")

print("Hello world")
# engine.setProperty('voice', voices[1].id)
# recognizer = sr.Recognizer()
# def cmd():
#     with sr.Microphone as source:
#         print('Clearing background noise please wait...')
#         recognizer.adjust_for_ambient_noise(source, duration=0.5)
#         print('Ask me anything')
#         recordedaudio = recognizer.listen(source)
#         print("Your message:", format(command))
        
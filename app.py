import speech_recognition  as sr
import pyttsx3 
import streamlit as st


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text) 
    engine.runAndWait()

def get_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognizer_google(voice)
            command = command.lower()
            print(command)
    except:
        pass


def start():
    command = get_command()

    if('Hello' in command):
        talk("Hello boss")
        talk("What can I do for you")
    else:
        talk("Talk something boss")


btn = st.button('start')

 
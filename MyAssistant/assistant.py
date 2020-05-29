import os;
import webbrowser;
import sys;
import pyttsx3;
import speech_recognition as recog;
import smtplib;
from datetime import datetime;
import wikipedia;

engine = pyttsx3.init('sapi5');
voices = engine.getProperty('voices');
engine.setProperty('voice',voices[0].id);

def speech(audio):
    engine.say(audio);
    engine.runAndWait();

def takeRequest():
    recognizer = recog.Recognizer();
    with recog.Microphone() as source:
        print('What can I Do....');
        recognizer.pause_threshold = 1;
        audio = recognizer.listen(source);
        
    try:
        print('Getting....');
        query = recognizer.recognize_google(audio,'en-in');
        print(query);
    except Exception as e:
        print('Say that again please');
        return 'None';

    return query;

def greet():
    greetings = None;
    timeNow = datetime.now().hour;
    if timeNow>20 or timeNow<4:
        greetings = 'Good Morning';
    elif timeNow>5 and timeNow<12:
        greetings = 'Good Night';
    else:
        greetings = 'God Day'
    speech(f'Hello! {greetings}, I thought you must be a programmer.');

if __name__ == "__main__":
    greet();
    while True:
        takeRequest();
        break;
# /i have a upgraded verion of it
# i think you will like it and you need to change some paths according to paths described in your pc
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import smtplib
import pyautogui

chrome = False
music = False
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour = int(datetime.datetime.now().hour)  
    if hour>0 and hour<12:
        speak('Good morning sir')
    elif hour>=12 and hour<18:
        speak('Good afternoon sir')
    else:
        speak('Good evening sir')
    speak('I am prajna sir. Please tell me how may i help you')
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listneing...')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('recognizing...')
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}")
    except Exception as e:
        # print(e)
        print('plz say it again...')
        return 'none'
    return query
def sendemail(to,content):
    youremail="xxxxxxxx"
    yourpass = "xxxxxxx"
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo
    server.starttls()
    server.login(youremail,yourpass)
    server.sendmail(youremail,to,content)
def closeprogramm(app):
    os.system(f"TASKKILL /F /IM {app}.exe")
screenshots = 1
def takescreenshoot():
    img = pyautogui.screenshot()
    img.save(f"E:\\webpage programmming\\screenshot{random.randint(0,4854658)}.png")
    speak('screenshot taken and saved to decribed location') 
if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        # main logic building
        if 'wikipedia' in query:
            speak('searching on wiki...')
            query = query.replace('wikipedia',"")
            try:
                results = wikipedia.summary(query,sentences = 2)
                print('According to wikipedia')
                speak("According to wikipedia")
                print(results)
                speak(results)
            except ValueError:
                print('NO! results found..')
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak('opening youtube')
            youtube = True
        elif 'take screenshot' in query:
            takescreenshoot()    
        elif 'open google' in query:
            webbrowser.open("google.com",chrome,)
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir = 'E:\\MY MUSIC'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[random.randint(0,len(songs)-1)]))
            music =True
        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir , the time is{strtime}")
        elif 'open vs code' in query:
            codepath = "C:\\Users\\Win8.1\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif 'what is your name'in query :
            speak('sir , how you forgot my name i am prajna')
        elif 'what are you doing' in query:
            speak('nothing much just waiting for your command sir')
        elif 'open chrome' in query:
            chromepath = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            os.startfile(chromepath)
            chrome = True
        elif 'quit chrome' or 'exit chrome' in query: 
            if chrome == True:
                closeprogramm('chrome')
                chrome = False
        elif 'close music' in query:
            speak('closing music')
            closeprogramm('wmplayer')
        
        elif 'send email to gopal' in query:
            try:
                speak('what should i send')
                content = takecommand()
                to = 'xxxxxxxx'
                sendemail(to,content)
                speak('email has been sent')
            except Exception as e:
                print(e)
                speak('Sorry! sir due to some system default email has been not sent')
        elif 'quit buddy' in query:
            speak('quitting myself')
            exit()

import pyttsx3
import datetime 
import speech_recognition as sr
import wikipedia
import webbrowser
import pywhatkit
from os import startfile
from pyautogui import click
import keyboard
from time import sleep
# from selenium import webdriver

# chrome_path = "C:\Program Files (x86)\chromedriver.exe"
# driver= webdriver.Chrome()
engine= pyttsx3.init('sapi5') # sapi5- Used for taking voices (inbuilt windows voices)
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
        print("Good Morning!\n")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
        print("Good Afternoon!\n")

    else:
        speak("Good Evening!")
        print("Good Evening!\n")
    speak("Hello!!! I am Artemis. How can I be at your service?")
    print("Hello!!! I am Artemis. How can I be at your service?\n")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def Whatsapp_cmd(receiver,txt):
    startfile("C:\\Users\\anjalee\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(20)
    click(x=89, y=113)
    sleep(2)
    keyboard.write(receiver)
    sleep(2)
    keyboard.press('enter')
    sleep(2)
    click(x=538, y=694)
    sleep(2)
    keyboard.write(txt)
    keyboard.press('enter')
    sleep(5)
    click(x=1350, y=12)



if __name__=="__main__":
     wishMe()
     while True:
        query = takeCommand().lower()
        #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia')
            query= query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube'in query:
            speak("Opening youtube")
            webbrowser.open("youtube.com")
        
        elif 'open google'in query:
            speak("Opening google")
            webbrowser.open("google.com")
        
        elif 'open hackerrank'in query:
            speak("Opening hackerrank")
            webbrowser.open("hackerrank.com")

        elif 'open linkedin'in query:
            speak("Opening linkedin")
            webbrowser.open("linkedin.com")

        elif 'open facebook'in query:
            speak("Opening facebook")
            webbrowser.open("facebook.com")

        elif 'open instagram'in query:
            speak("Opening instagram")
            webbrowser.open("instagram.com")

        elif 'the time' in query:
            strtime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Maam, The time is {strtime}")

        elif 'play song' in query:
            s=query.split("song ")
            song=s[1]
            print(song)
            speak(f"Playing song {song}")
            pywhatkit.playonyt(f"{song}") 

        elif 'whatsapp' in query:
            speak("Whom would you like to send a text ma'am")
            receiver=takeCommand().lower()
            speak("What should I text")
            txt=takeCommand().lower()
            speak(f"Sending text to {receiver} on whatsapp")
            Whatsapp_cmd(receiver,txt) 

        elif 'quit' in query :
            speak("Thank you for using Artemis. Signing off now")
            exit()

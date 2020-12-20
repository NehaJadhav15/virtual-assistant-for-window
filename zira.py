import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import subprocess
#import ecapture as ec
import wolframalpha
import json
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak ("Good Morning")

    elif hour >=12 and hour<18:
        speak ("Good aFternoon")
    else:
        speak("good Evening")
    speak ("I am zira mam please tell me How may i help you")
 
def myCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening......")
        r.pause_threshold = 1
        audio= r.listen(source)
    try:
        print("recognizing.....")
        query= r.recognize_google(audio, language='en-in')
        print(f"User said:,{query}\n")
        speak(f":,{query}\n")
    except Exception as e:
         #print(e)
         print("say that again please....")
         speak("say that again please....")
         return "none"
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('https://mail.google.com/mail/u/0/#inbox', 587)
    server.ehlo()
    server.starttls()
    server.login('neha.jadhav19@vit.edu', 'Neha@1501')
    server.sendmail('neha.jadhav19@vit.edu', to, content)
    server.close()


if __name__ == '__main__':
    speak("hii..")
    wishMe()
    while True:
        query = myCommand().lower()
        if 'wikipedia' in query:
            speak ('searching Wikipedia....')
            query = query.replace("wikipedia","")
            results= wikipedia.summary(query,sentences=6)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com/")

        elif 'open web whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")

        elif 'latest news' in query:
            webbrowser.open("https://timesofindia.indiatimes.com")

        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com/")
        
        
        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com/")

        elif 'open linknden' in query:
            webbrowser.open("https://www.facebook.com/")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'play music' in query:
            music_dir = 'C:\\Users\\admin\\Desktop\\zira\\fvt song'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"mam, the time is {strTime}")
        

        elif 'open code' in query:
            codePath ='C:\\Users\\admin\\Desktop\\zira'
            os.startfile(codePath)

        elif 'email to zira' in query:
            try:
                speak("What should I say?")
                content = myCommand()
                to = "nehabjadhav1501@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend zira. I am not able to send this email")

    
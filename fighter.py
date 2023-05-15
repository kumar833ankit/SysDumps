import datetime
import json
import os
import random
import re
import smtplib
import subprocess
import sys
import time
import webbrowser

import pyautogui
import pyttsx3  # pip install pyttsx3
import requests
import speech_recognition as sr  # pip install speechRecognition
import wikipedia  # pip install wikipedia
import wolframalpha
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def start():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("who are you") 
        r.pause_threshold = 6
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        speak("comnfirmed access")    
        quer = r.recognize_google(audio, language='en-in')
        print(f"sir: {quer}\n")

    except Exception as e:
        # print(e)    
        print("sorry sir stranger not allowed")  
        return "None"
    return quer   

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("  Good Morning ! sir ")

    elif hour>=12 and hour<18:
        speak(" Good Afternoon ! sir")   

    else:
        speak(" Good Evening ! sir ")  

    speak("jarvis online ")  

    stMsgs = ['how are you sir? ', 'Hope you are having a nice time ', 'at your command ', 'how can I help you sir ' , 'working on improvement' , 'having completed all previous task ' , 'glad to see you working boss' , 'pleased with your work boss' , 'installed all required data files '] 
    speak(random.choice(stMsgs))

    speak("  ") 
    speak(" ") 

    stMsgs = ['calibrated data file  ', 'connected to data servers  ', 'restablizied utilities', 'ready sir' , ] 
    speak(random.choice(stMsgs))
       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("hmmmmm")
        r.pause_threshold = 6
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        speak("searching for  resources")    
        query = r.recognize_google(audio, language='en-in')
        print(f"sir: {query}\n")

    except Exception as e:
        # print(e)    
        print("sorry sir again please ")  
        return "None"
    return query


def search_web():
    driver =  webdriver.Chrome(r'C:\Users\B&O\Downloads\chromedriver (2).exe')
    





def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
   
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query or  'who ' in query or  'how ' in query or  'why ' in query or  'when ' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=8)
            speak("According to Wikipedia")
            page = wikipedia.page(query)
            print(page.images[0])
            print(results)
            speak(results)


        
        
            
        elif  'youtube' in query :
            speak('Opening ')
            indx = query.split().index('youtube')
            quer = query.split()[indx+1:]
            driver =  webdriver.Chrome(r'C:\Users\B&O\Downloads\chromedriver (2).exe')
            driver.maximize_window()
            driver.get("http://www.youtube.com/results?search_query=" + '+'.join(quer))
            pyautogui.click(370, 328)
             
        


        elif 'open facebook' in query:
            webbrowser.open("facebook.com")    

        elif 'google' in query or  'show information regarding ' in query  :
           indx1 = query.split().index('google')
           quer1 = query.split()[indx1+1:]
           driver =  webdriver.Chrome(r'C:\Users\B&O\Downloads\chromedriver (2).exe')
           driver.maximize_window()    
           driver.get("https://www.google.com/search?q=" + '+'.join(quer1))
           pyautogui.click(1271, 51) 

        elif 'close the web' in query:
            pyautogui.click(1354, 17)

        elif 'open xda' in query:
            webbrowser.open("forum.xda-developers.com")
               

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = 'C:\\Users\\rames\\Desktop\\ani\\aa'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "G:\\old\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'pubg' in query:
            codePath = "C:\\Program Files\\txgameassistant\\ui\\AndroidEmulator.exe"
            os.startfile(codePath)    

        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "harryyourEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry . I am not able to send this email")    

        elif ' play endgame' in query:
            codePath = "C:\\Users\\rames\\Desktop\\Avengers Endgame (2019) Dual Audio Hindi 720p HDCAM NEW MovieMAD.mkv"
            os.startfile(codePath)  

        elif 'ok done ' in query:
          speak("bye sir")  
          sys.exit()

        elif 'open notepad' in query:
            codePath = "G:\\old\\danger\\notepad.bat"
            os.startfile(codePath)  

        elif 'shut down the system' in query:
            codePath = "G:\\old\\danger\\shutdown.bat"
            os.startfile(codePath) 

        elif 'news' in query:
            codePath = "G:\\old\\AI\\news.py"
            os.startfile(codePath) 

        elif 'start timer' in query:
            codePath = "G:\\old\\danger\\timer.bat"
            os.startfile(codePath) 
       
        elif 'pc status' in query:
            codePath = "G:\\old\\danger\\sign.bat"
            os.startfile(codePath) 


        elif 'where is ' in query:
           query = query.split(" ") 
           location = query[2]
           speak("looking for  " + location + " sir " )
           os.system("chromium-browser http://www.google.nl/maps/place/" + location + "/&amp;")

        elif "calculate" in query:
            app_id= "K62LAE-GKW95R2TJR"
            client = wolframalpha.Client(app_id)

            indx = query.split().index('calculate')
            quer = query.split()[indx + 1:]
            res = client.query(' '.join(quer))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)

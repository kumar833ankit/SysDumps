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
#import pyjokes
#import tkinter 
import operator 
#import winshell 
#import feedparser 
import ctypes 
import shutil 
#from twilio.rest import Client 
#from clint.textui import progress 
#from ecapture import ecapture as ec 
from bs4 import BeautifulSoup 
import win32com.client as wincl 
from urllib.request import urlopen
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
    print("                     I only have access to these only               ")
    print("************************************************************************************************")
    print("")
    print("")
    print("           WIKI  YOUTUBE FACEBOOK GOOGLE TAB SWITCH ACTIVE CHROME CAMERA CAPTURE FOLDER XDA STACKOVERFLOW   ")
    print("************************************************************************************************")
    print("          MUSIC TIME VS EMAIL EXIT NOTEPAD SHUTDOWN NEWS TIMER PC STATUS LOCATION CALCULATE")
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("  Good Morning sir ")

    elif hour>=12 and hour<18:
        speak(" Good Afternoon sir")   

    else:
        speak(" Good Evening sir ")  

    speak("I am online ")  

    stMsgs = ['how are you today? ', 'Hope you are having a nice time ', 'at your command ', 'how can I help you sir ' , 'working on improvement' , 'having completed all previous task ' , 'glad to see you working boss' , 'pleased with your work sir' , 'installed all required data files '] 
    speak(random.choice(stMsgs))

    speak("  ") 
    speak(" ") 

    stMsgs = ['calibrated data file  ', 'connected to data servers  ', 'restablizied utilities',  ] 
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
    driver =  webdriver.Chrome(r'D:\python\AI1\chromedriver.exe')
   # "D:\python\AI1\chromedriver.exe"
    





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
            driver =  webdriver.Chrome(r'D:\python\AI1\chromedriver.exe')
            driver.maximize_window()
            driver.get("http://www.youtube.com/results?search_query=" + '+'.join(quer))
            pyautogui.click(370, 328)
             
        


        elif 'open facebook' in query:
            speak('Opening ')
            webbrowser.open("facebook.com")

        elif 'change background' in query: 
            ctypes.windll.user32.SystemParametersInfoW(20,  
                                                       0,  
                                                       "Location of wallpaper", 
                                                       0) 
            speak("Background changed succesfully") 


        elif 'news' in query: 
              
            try:  
                jsonObj = urlopen('''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =018d28bad6844700ab73069a07c92fbe''') 
                data = json.load(jsonObj) 
                i = 1
                  
                speak('here are some top news from the times of india') 
                print('''=============== TIMES OF INDIA ============'''+ '\n') 
                  
                for item in data['articles']: 
                      
                    print(str(i) + '. ' + item['title'] + '\n') 
                    print(item['description'] + '\n') 
                    speak(str(i) + '. ' + item['title'] + '\n') 
                    i += 1
            except Exception as e: 
                  
                print(str(e))         

           


        elif 'google' in query or  'show information regarding ' in query  :
           speak('Opening ')
           indx1 = query.split().index('google')
           quer1 = query.split()[indx1+1:]
           driver =  webdriver.Chrome(r'D:\python\AI1\chromedriver.exe')
           driver.maximize_window()    
           driver.get("https://www.google.com/search?q=" + '+'.join(quer1))
           pyautogui.click(1271, 51) 

        elif 'close the web' in query:
            pyautogui.click(1354, 17)

        elif 'lock window' in query: 
                speak("locking the device") 
                ctypes.windll.user32.LockWorkStation() 
  
        elif 'shutdown system' in query: 
                speak("Hold On a Sec ! Your system is on its way to shut down") 
                subprocess.call('shutdown / p /f') 
                  
        elif 'empty recycle bin' in query: 
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True) 
            speak("Recycle Bin Recycled") 
  
        elif "don't listen" in query or "stop listening" in query: 
            speak("for how much time you want to stop jarvis from listening commands") 
            a = int(takeCommand()) 
            time.sleep(a) 
            print(a)   

        elif "camera" in query or "take a photo" in query: 
            ec.capture(0, "Jarvis Camera ", "img.jpg") 


        elif "restart" in query: 
            subprocess.call(["shutdown", "/r"]) 
              
        elif "hibernate" in query or "sleep" in query: 
            speak("Hibernating") 
            subprocess.call("shutdown / h") 
  
        elif "log off" in query or "sign out" in query: 
            speak("Make sure all the application are closed before sign-out") 
            time.sleep(5) 
            subprocess.call(["shutdown", "/l"])        


        elif 'first tab ' in query:
            speak(' yes')
            pyautogui.click(170, 13)  
        
        elif 'close first tab' in query:
            speak(' yes')
            pyautogui.click(175, 13)     
        
        elif 'close second tab' in query:
            speak(' yes')
            pyautogui.click(360, 13)

































        elif 'open second  tab' in query:
            speak(' yes')
            pyautogui.click(365, 13)












        elif 'active chrome ' in query:
            speak(' yes')
            pyautogui.click(624, 751)  

        elif 'camera' in query:
            speak(' yes')
            pyautogui.click(552, 752)      
        
        elif 'capture' in query:
            speak(' yes')
            pyautogui.click(1314, 376) 
      
        elif 'open my folder ' in query:
            speak(' yes')
            pyautogui.click(0, 29)
            pyautogui.click(1041, 351)  
            pyautogui.click(1201, 218) 

        elif 'open xda' in query:
            speak(' right away')
            webbrowser.open("forum.xda-developers.com")


        elif "write a note" in query: 
            speak("What should i write, sir") 
            note = takeCommand() 
            file = open('jarvis.txt', 'w') 
            speak("Sir, Should i include date and time") 
            snfm = takeCommand() 
            if 'yes' in snfm or 'sure' in snfm: 
                strTime = datetime.datetime.now().strftime("% H:% M:% S") 
                file.write(strTime) 
                file.write(" :- ") 
                file.write(note) 
            else: 
                file.write(note) 
          
        elif "show note" in query: 
            speak("Showing Notes") 
            file = open("jarvis.txt", "r")  
            print(file.read()) 
            speak(file.read(6))    
               

        elif 'open stackoverflow' in query:
            speak(' straight away ')
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            speak(' on my way sir')
            music_dir = 'C:\\Users\\rames\\Desktop\\ani\\aa'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[1]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "G:\\old\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'pubg' in query:
            codePath = "C:\\Program Files\\txgameassistant\\ui\\AndroidEmulator.exe"
            os.startfile(codePath)   

        elif 'joke' in query: 
            speak(pyjokes.get_joke())      

        elif 'email to a' in query:
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
            speak(' yes ')
            codePath = "G:\\old\\danger\\notepad.bat"
            os.startfile(codePath)  

        elif 'shut down the system' in query:
            speak('bye sir ')
            codePath = "G:\\old\\danger\\shutdown.bat"
            os.startfile(codePath) 

        elif 'news' in query:
            speak('fetching latest news sir ')
            codePath = "G:\\old\\AI\\news.py"
            os.startfile(codePath) 

        elif 'weather' in query or ' todays weather' in query:
            codePath = "G:\\old\\AI\\weather.py"
            os.startfile(codePath)    

        elif 'start timer' in query:
            codePath = "G:\\old\\danger\\timer.bat"
            os.startfile(codePath) 
       
        elif 'pc status' in query:
            codePath = "G:\\old\\danger\\sign.bat"
            os.startfile(codePath) 


        elif "weather" in query: 
              
            # Google Open weather website 
            # to get API of Open weather  
            api_key = "Api key" 
            base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
            speak(" City name ") 
            print("City name : ") 
            city_name = takeCommand() 
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name 
            response = requests.get(complete_url)  
            x = response.json()  
              
            if x["cod"] != "404":  
                y = x["main"]  
                current_temperature = y["temp"]  
                current_pressure = y["pressure"]  
                current_humidiy = y["humidity"]  
                z = x["weather"]  
                weather_description = z[0]["description"]  
                print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))  
              
            else:  
                speak(" City Not Found ")    


        elif 'where is ' in query:
           query = query.split(" ") 
           location = query[2]
           speak("looking for  " + location + " sir " )
           os.system("chromium-browser http://www.google.nl/maps/place/" + location + "/&amp;")


        

        elif "Good Morning" in query: 
            speak("A warm" +query) 
            speak("How are you Mister") 
            speak(assname)            

        elif "calculate" in query:
            app_id= "K62LAE-GKW95R2TJR"
            client = wolframalpha.Client(app_id)

            indx = query.split().index('calculate')
            quer = query.split()[indx + 1:]
            res = client.query(' '.join(quer))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)




        elif "what is" in query or "who is" in query: 
              
            # Use the same API key  
            # that we have generated earlier 
            client = wolframalpha.Client("API_ID") 
            res = client.query(query) 
              
            try: 
                print (next(res.results).text) 
                speak (next(res.results).text) 
            except StopIteration: 
                print ("No results")     

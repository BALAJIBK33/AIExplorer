import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import psutil
import pywhatkit
import pyautogui
import smtplib
import pyjokes
import wolframalpha
import requests
from bs4 import BeautifulSoup 


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning sir")
    elif hour>=12 and hour<18:
        speak("good afternoon sir")
    else:
        speak("good evening sir")
    speak("I  Am  Bruce ,,  how  may  I  help  you")

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing...") 
        query=r.recognize_google(audio,language='en-in')
        print("user said", query)
        



    except Exception as e:
        print(e)
        speak("say that again please")
        query="nothing"
    return query 

   

def sendemail(to, subject, content):
    server = smtplib.SMTP('smpt.gmail.com', 587)
    server.ehlo
    server.starttls()
    server.login("bkking3328@gamil.com","123test")
    server.sendmail("balajisarask@gmail.com", to, content)
    server.close()

   

if __name__=="__main__":
    wishme()
    while True:
        query = takecommand().lower()
        if "turn on" in query:
            speak("I am on,, please tell me what can i do for you sir")
            while True:
                query = takecommand().lower()


                if 'wikipedia' in query:
                    speak("searching in wikipedia")
                    query=query.replace("wikipedia","")
                    results=wikipedia.summary(query,sentences=2)
                    speak("according to wikipedia")
                    speak(results)
                    print(results)


                elif 'open youtube' in query:
                    speak("opening youtube sir")
                    webbrowser.open("youtube.com")

                elif 'open google' in query:
                    speak("on the way sir")
                    webbrowser.open("google.com")

                elif 'open amazon' in query:
                    speak("opening sir")
                    webbrowser.open("amazon.com")

                elif 'open flipkart' in query:
                    speak("opening sir")
                    webbrowser.open("flipkart.com") 

                elif 'open panimalar' in query:
                    speak("opening website sir")
                    webbrowser.open("panimalar.ac.in")

                elif 'open instagram' in query:
                    speak("As per your wish sir")
                    webbrowser.open("instagram.com")

                elif 'open mail' in query:
                    speak("As per your wish sir")
                    webbrowser.open("gmail.com")

                elif 'play music' in query:
                    speak("playing music sir")
                    musicdir="A:\\MUSIC"
                    songs=os.listdir(musicdir)
                    print(songs)
                    os.startfile(os.path.join(musicdir,songs[0]))

                elif 'play video' in query:
                    speak("playing video sir")
                    musicdir="A:\\MOVIES\\VIDEOS"
                    songs=os.listdir(musicdir)
                    print(songs)
                    os.startfile(os.path.join(musicdir,songs[19]))

                elif 'play batman movie' in query:
                    speak("playing movie sir")
                    musicdir="A:\\MOVIES\\THE BATMAN 2022"
                    songs=os.listdir(musicdir)
                    print(songs)
                    os.startfile(os.path.join(musicdir,songs[1]))

                elif 'play series' in query:
                    speak("playing video sir")
                    musicdir="A:\\MOVIES\\SERIES"
                    songs=os.listdir(musicdir)
                    print(songs)
                    os.startfile(os.path.join(musicdir,songs[5]))



                elif 'open game' in query:
                    speak("welcome back sir,,  all   system   for   gaming   will   be   prepared   in   few   minutes")
                    codepath="B:\\GAMES\\Batman - Arkham Knight\\Binaries\Win64\\BatmanAK.exe"
                    os.startfile(codepath)

                elif 'open devour' in query:
                    speak("welcome back sir,,  all   system   for   gaming   will   be   prepared   in   few   minutes")
                    codepath1="B:\GAMES\DEVOUR.v3.2.2\DEVOUR.v3.2.2\DEVOUR.exe"
                    os.startfile(codepath1)


                elif 'open fps' in query:
                    codepath2="C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Fraps\Fraps.lnk"
                    os.startfile(codepath2)

                elif 'the time' in query:
                    time=datetime.datetime.now().strftime("%H:%M")
                    speak(time)

                elif 'battery percentage' in query:
                    battery =psutil.sensors_battery()
                    percent=battery.percent
                    speak("the Battery percentage is" + str(percent))

                elif 'how are you' in query:
                    speak("i am fine sir,,  thank you ")
                    speak(" how are you sir")

                elif 'who are you' in query:
                    speak(" let me introduce my self,,  im Bruce,,  a  virtual   Artificial  intelligence,,  im  here  to   assist  you  with  the  varity    of  tasks   as   best as   i   can  24   hours   a   day,,   seven   days   week ,,  systems   are   now  fully  operational")

                elif 'good' in query or 'fine' in query:
                    speak("its good to know that you are fine")

                elif 'search youtube' in query:
                    speak("searching youtube sir")
                    result = query.replace("search youtube for","")
                    webbrowser.open("https://www.youtube.com/results?search_query="+result)
                    speak("found,, what you have searched for")
                    pywhatkit.playonyt(result)
                    speak("playing video sir")
                
                elif 'search google' in query:
                    import wikipedia as googleScrap
                    speak("searching google sir")
                    result=query.replace("search google for","")
                    webbrowser.open("https://www.bing.com/search?q="+result)
                    speak("I got the information sir")
                    result = googleScrap.summary(result,2)
                    speak(result)
                    print(result)

                
                elif 'search amazon' in query:
                    speak("searching amazon sir")
                    result=query.replace("search googlefor","")
                    webbrowser.open("https://www.amazon.in/s?k="+result)
                    speak(" sir, I found what you have searched for ") 

                elif 'stop' in query:
                    pyautogui.press("k")
                    speak("video paused")

                elif 'play' in query:
                    pyautogui.press("k")
                    speak("video played")

                elif 'mute video'in query:
                    pyautogui.press("m")
                    speak("video muted")


                elif 'volume up' in query:
                    speak("increasing volume sir")
                    pyautogui.press("volumeup")

                elif 'volume down' in query:
                    speak("decreasing volume sir")
                    pyautogui.press("volumedown")

                elif 'jokes' in query:
                    results = (pyjokes.get_joke())
                    speak(results)
                    print(results)


                elif "temperature" in query:
                    app = wolframalpha.Client("LPPQ5A-U9WPHJA6RY")
                    result = app.query(query)
                    speak(next(result.results).text)
                    print(result)

                elif 'calculate' in query:
                    app = wolframalpha.Client("LPPQ5A-U9WPHJA6RY")
                    speak("what should I calculate?")
                    gh = takecommand().lower()
                    result = app.query(gh)
                    speak(next(result.results).text)
                    print(next(result.results).text)

                elif "take screenshot" in query:
                    speak("please sir hold the screen for few seconds, I am taking screenshot")
                    img = pyautogui.screenshot()
                    img.save("screenshot.png")
                    speak(" I am done sir, the screenshot is saved in our main folder")


                elif "open" in query:
                    speak("opening sir")
                    query = query.replace("open","")
                    query = query.replace("app","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(1)
                    pyautogui.press("enter")


                elif "close notepad" in query:
                    speak("okay sir, closing notepad")
                    os.system("taskkill /f /im notepad.exe")

                elif "close discord" in query:
                    speak("okay sir, closing")
                    os.system("taskkill /f /im discord.exe")

                elif "close fps" in query:
                    speak("okay sir, closing")
                    os.system("taskkill /f /im fraps.exe")

                elif "close game" in query:
                    speak("okay sir, closing")
                    os.system("taskkill /f /im BatmanAK.exe")

                elif "close telegram" in query:
                    speak("okay sir, closing")
                    os.system("taskkill /f /im telegram.exe")


                elif "click my picture" in query:
                    speak(" wait, I am opening camera")
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("smile sir, i am taking picture")
                    pyautogui.press("enter") 


                elif "shutdown" in query or "shutdown system" in query:
                    speak("shutdowning system sir")
                    os.system("shutdown /s /t 1")
                    
                    
                elif "logout" in query or "logout system" in query:
                    speak("logging out system sir")
                    os.system("shutdown /1")
                    

                elif "restart" in query or "restart system" in query:
                    speak("restarting system sir")
                    os.system("shutdown /r")

                                                     
                elif 'quit' in query:
                    speak("quitting sir")
                    break

                elif 'exit' in query:
                    speak("exitting sir,,  have a nice day")
                    exit()
                
                

                elif "send email" in query:
                    try:
                        speak("what should I say?")
                        content =  takecommand()
                        to = "balajisarask@gmail.com"
                        sendemail(to, content)
                        speak(" sir, Email has been sent sucessfully")
                        
                    except Exception as e:
                        speak("sorry email cannot be sent")
                        print(e)

                

                

                
                


                
        

                               

                
                    


                        








               



                        

               






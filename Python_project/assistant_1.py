
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import time
import webbrowser
import os
import random
import smtplib
from ecapture import ecapture as ec
import requests

# this is the dictionary for email . assistant will take user name then this returns their gmail.
dict1={"deepak":"dipakrajsharma@gmail.com","dipesh":"techtwins001@gmail.com"}

#this select the voice for our asssistant
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#this function return the value in speech when called
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


#this wish whether it is morning,afternoon,or evening
def wishme():
    hour = int(datetime.datetime.now().hour)

    if hour==0 and hour<12:
        if hour>6 and hour>7:
            print("Good morning sir!!!")
            speak("Good morning sir!!!")

    
    elif hour==12 and hour<18:
        print("Good Afternoon sir !!!")
        speak("Good afternoon sir!!!")

    else:
        print("Good evening sir!!!")
        speak("Good evening sir !!!")
    
    print("your personal assistant is ready to help you")
    speak("your personal assistant is ready to help you")

#this takes input from user and return strings
def takeCommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 0.5
        r.energy_threshold=3000
        audio = r.listen(source)
    #this will try to take user voice
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    # if it didnot recognize then except will work
    except Exception as e:
        print("say again please...")
        #speak("say again please...")
        return "None"   # this is not a string

    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('www.pandit1234567890@gmail.com','Diwas@123')
    server.sendmail('www.pandit1234567890@gmail.com',to,content)
    server.close()



if __name__ == "__main__":
    wishme()
    while True:
    #if 1:
        query = takeCommand().lower()

    # logic foor extracting tasks based oon query
            
            
        if "open youtube" in query:
            webbrowser.open("www.youtube.com")
            print("youtube is open now")
            speak("youtube is now open")
            time.sleep(5)

        elif "close youtube" in query:
            os.system("taskkill /f /im " + "brave.exe")
            print("your browser has been closed")
            speak("your browser has been closed")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")
            print("facebook is open now")
            speak("facebook is open now")
            time.sleep(5)

        elif "close facebook" in query:
            os.system("taskkill /f /im " + "brave.exe")
            print("your facebook has been closed")
            speak("your facebook has been closed")

        # elif "search" in query or "shots" in query:
        #     query= query.replace("search"," ")
        #     webbrowser.open(query)
        #     time.sleep(5)

        # elif "close search" in query or "close shots":
        #     os.system("taskkill /f /im " + "brave.exe")
        #     print("your browsing has been closed")
        #     speak("your browsing has been closed")

        elif "open stackoverflow" in query or "open stack overflow" in query:
            webbrowser.open("www.stackoverflow.com")
            print("stackoverflow is now open")
            speak("stackoverflow is now open")
            time.sleep(5)

        elif "close stackoverflow" in query or "close stack overflow" in query:
            os.system("taskkill /f /im " + "brave.exe")
            print("your stackoverflow has been closed")
            speak("your stackoverflow has been closed")

        elif "open gmail" in query:
            webbrowser.open("www.gmail.com")
            print("gmail is open now")
            speak("gmail is open now")
            time.sleep(5)

        elif "close gamil" in query:
            os.system("taskkill /f /im " + "brave.exe")
            print("your gmail has been closed")
            speak("your gmail has been closed")


        elif "play music" in query:
            music_dir = 'C:\\Users\\Sunil Aryal\\Desktop\\music'
            songs = os.listdir(music_dir)
            #print(songs)
            #this give any random number
            random_num= random.randint(0,98)
            print(f"Song number {random_num} is playing....")
            speak(f"Song number {random_num} is playing....")
            os.startfile(os.path.join(music_dir,songs[random_num]))
            time.sleep(5)

        elif "close music" in query or "stop music" in query:
            os.system("taskkill /f /im " + "vlc.exe")
            print("your music has been closed")
            speak("your music has been closed")

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"sir, the time is {strTime}")
            speak(f"sir, the time is {strTime}")

        elif "open vscode" in query:
            codePath = "C:\\Users\\Sunil Aryal\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            print("vscode is now open")
            speak("vscode is now open")
            time.sleep(5)

        elif "close vscode" in query:
            os.system("taskkill /f /im " + "code.exe")
            print("your vscode has been closed")
            speak("your vscode has been closed")

        elif "how are you" in query:
            print("i am fine and what about yours")
            speak("i am fine and what about yours")

        elif "i am fine" in query or "i am also fine" in query:
            print("that's good. how can i help you ?")
            speak("that's good. how can i help you ?")

        elif "send email" in query:
            try:
                speak("to whom you want to send email")
                content1 = takeCommand()
                print(content1)
                
                #to = dict1.values(content1)
                to = dict1[content1.lower()]
                speak("what should i say")
                content = takeCommand()
                print(content)
                sendEmail(to,content)
                speak("email has been sent!!")

            except Exception as e:
                print(e)
                speak("sorry i could not send due to some error")

        elif "open camera" in query:
            print("your photo is being captured")
            speak("your photo is being captured")
            speak("your photo has been captured")
            ec.capture(0,"robo camera","img.jpg")

        elif "open filmora" in query or "open filmmora" in query:
            codePath ="C:\\Program Files\\Wondershare\\Wondershare Filmora\\Wondershare Filmora X.exe"
            os.startfile(codePath)
            print("filmora x is now open")
            speak("filmora x is now open")
            time.sleep(10)

        # elif "close filmora" in query or "close filmmora" in query:
        #     filmora="C:\\Program Files\Wondershare\Wondershare Filmora\Wondershare Filmora X.exe"
        #     os.system("taskkill /f /im " + filmora)
        #     print("your filmora has been closed")
        #     speak("your filmora has been closed")

        elif "who are you" in query or "what can you do" in query:
            print(" i am personal assistant. i am programmed for minor tasks like opening youtube,gmail and stackoverflow ,say current time,take a photo,search wikipedia, send email, and much more ")
            speak(" i am personal assistant. i am programmed for minor tasks like opening youtube,gmail and stackoverflow ,say current time,take a photo,search wikipedia, send email, and much more ")
            

        elif "who made you" in query or "who created you" in query or "who discovered you" in query:
            print("i was built by DD Twins")
            speak("i was built by DD Twins")

        elif "who is rishav" in query or "who is rishabh" in query:
            speak("rishav is a khate.. stupied and careless man... but he is handsome too.")
            
        elif 'wikipedia' in query or "who is" in query or "where is" in query:
            speak("Searching wikipedia")
            query= query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "close wikipedia" in query:
            os.system("taskkill /f /im " + "brave.exe")
            print("your wikipedia has been closed")
            speak("your wikipedia has been closed")

        #elif "who are you"

        elif "quit" in query or "exit" in query:
            print("your assistant is turning off!!")
            speak("your assistant is turning off!!")
            exit()

        elif "shutdown pc" in query or "shutdown computer" in query:
            os.system("shutdown /s /t 10")

        else:
            print("something error")
            

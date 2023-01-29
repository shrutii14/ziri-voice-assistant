from tkinter.tix import MAIN
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import smtplib


engine = pyttsx3.init('sapi5')        #to accept voice
voices = engine.getProperty('voices') 
print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)        #abhi ka time hour mei mil jaega
    if hour<=0 and hour >=12:
         speak("Good Morning")

    elif hour<=12 and hour>=18:
         speak("Good Afternoon")

    else:
         speak("Good Night")

    speak("I am Ziri. Nice to meeet you. How may I help you")  

def takeCommand():                                  #take input from microphone   
        r = sr.Recognizer
        with sr.Microphone as source:
            print("Listening.......")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print('Recognizing.....')
            query = r.recognize_google(audio, Language= 'en') 
            print("User said: {query}\n")   

        except Exception as e:
            #print(e)
            print("Say that again, Please.....")
            return "None"
        return query

def sendEmail(to, content):
    server = smtplib.SMTP('smntp.gmail.com, 586')
    server.ehlo()
    server.starttls()
    server.login('apnaemail@gmail.com', 'apna-password')
    server.sendemail('apnaemail@gmail.com', to, content)
    server.close()


if _name_ == "_main_":
    speak("Embrace your awesomeness.")
    wishMe()
    if 1:
          query = takeCommand().lower()

          if 'wikipedia' in query:
             speak('Searching Wikipedia...')
             query = query.replace("wikipedia", "")
             results = wikipedia.summary(query, sentences = 2)
             speak("According to wikipedia")
             speak(results)

          elif 'open youtube' in query:
             webbrowser.open("youtube.com")

          elif 'open google' in query:
            webbrowser.open("google.com")   

          elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

          elif 'email to me' in query:
            try:
                speak("What should I say")
                content = takeCommand()
                to = "shrutianand1492@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                    print("email not sent")

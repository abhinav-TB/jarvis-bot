import pyttsx3
import datetime
import speech_recognition as sr

engine=pyttsx3.init()



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time =datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)

def date():
    year =int(datetime.datetime.now().year)
    month =int(datetime.datetime.now().month)
    date =int(datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("welcome back sir")
    speak("the current time is")
    time()
    speak("the current date is")
    date()
    hour =datetime.datetime.now().hour
    if hour>= 6 and  hour<12:
        speak("good morning sir")
    elif hour >=12 and hour<18:
        speak("good afternoon sir")
    elif hour >=18 and hour<24:
        speak("good evening sir")
    else:
        speak("good night sir")
    speak("jarvis at your service please tell me how can i help you")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening")
        r.pause_threshold =1
        audio =r.listen(source)

    try:
        print("recognizing..")
        query = r.recognize_google(audio, language="en-in")
        print(query)

    except Exception as e:
        print(e)
        speak("say that again please")

        return "none"

    return query

takeCommand()

        




import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
engine=pyttsx3.init()



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time =datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)

def date():
    year =int(datetime.datetime.now().year)
    month =int(datetime.datetime.now().month)
    date =int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("welcome back sir")
    time()
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
    
def sendEmail(to,content):
    server =smtplib.SMTP('smtp.gamil.com')
    server.echo()
    server.starttls()
    server.login("abhinavelenthikara@gmail.com","holygrace123")
    server.sendmail("abhinavelenthikara@gmail.com",to,content)


if __name__ == "__main__":
    wishme()
    while True:
        query =takeCommand().lower()

        if 'time' in query:
            time()
        elif 'date' in query:
            date()   
        elif 'offline' in query:
            quit()
        elif 'wikipedia' in query:
            speak("Searching..")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)
        elif "send email" in query :
            try:
                speak("what should i say?")
                content =takeCommand()
                to="abhinavtb@gmail.com"
                sendEmail(to,content)
                speak("email send")
            except Exception as e:
                print(e)
                speak("unable to send the email")

        elif "chrome" in query :
            speak("what should i search for")
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search =takeCommand.lower()
            wb.get(chrome_path).open_new_tab(search+'.com')

        

        




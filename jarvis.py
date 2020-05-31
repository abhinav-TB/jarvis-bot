import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import psutil
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
    # time()
    # date()
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

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # r.pause_threshold = 1
        audio = r.listen(source)
        print("hello")

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        # query=r.recognize_wit(audio)
        print(f"AK47 Said:{query}\n")

    except Exception as e:
        print(e)
        print("Say that again Please...")
        speak("Say that again Please...")
        return "None"
    return query

    
def sendEmail(to,content):
    server =smtplib.SMTP('smtp.gamil.com')
    server.echo()
    server.starttls()
    server.login("email","password")
    server.sendmail("email",to,content)

def cpu():
    usage =str(psutil.cpu_percent())
    speak("CPU usage is"+usage)
    battery=psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)


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
            search =takeCommand().lower()
            wb.get(chrome_path).open_new_tab(search+'.com')

        elif "play songs" in query:
            songs_dir="" 
            songs =os.litdir(songs_dir)
            os.startfile(os.path.join(songs_dir,songs[0]))

        elif "remember" in query:
            speak("what should i remember")
            data=takeCommand()
            speak("you asked me to remember"+data)
            remember =open("data.txt",'w')
            remember.write(data)
            remember.close()
        elif "do you know anything" in query:
            remember=open("data.txt")
            speak("you said me to rember that"+remember.read())
        
        elif "cpu" in query:
            cpu()
        
        

        

        




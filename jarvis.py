import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib,ssl
import webbrowser as wb
import os,sys
import psutil
from wit import Wit

client = Wit('H6MW36R46P6E6QQJTK3PJ36B2G5YSB6Q')
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
    # speak("welcome back sir")
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
    speak("welcome back ")
    speak("jarvis at your service please tell me how can i help you")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # r.pause_threshold = 1
        audio = r.listen(source,phrase_time_limit=5)
        # print("hello")

    try:
      
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        # query = r.recognize_wit(audio, key = "H6MW36R46P6E6QQJTK3PJ36B2G5YSB6Q")

        # query=r.recognize_wit(audio)
        print(f"AK47 Said:{query}\n")
        res=client.message(query)
        intent=list(res['intents'])[0]['name']
        print(list(res['intents'])[0]['name'])

    except Exception as e:
      
        print(e)
        print("Say that again Please...")
        speak("Say that again Please...")
        return "None","None"
    return intent,query

    
def sendEmail(content):
    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    
    speak("to whom should i send the message")
    reciever_email = input("recievers email:")
    sender_email="your email"
    password = "your password"

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:

        server = smtplib.SMTP(smtp_server,port)
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email,reciever_email,content)
    except Exception as e:

        # Print any error messages to stdout
        print(e)
    finally:
        server.quit() 

def cpu():
    usage =str(psutil.cpu_percent())
    speak("CPU usage is"+usage)
    battery=psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)

def get_message():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # r.pause_threshold = 1
        audio = r.listen(source,phrase_time_limit=5)
        # print("hello")

    try:
      
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"AK47 Said:{query}\n")
     
    except Exception as e:
      
        print(e)
        print("Say that again Please...")
        speak("Say that again Please...")
        return "None"
    return query



if __name__ == "__main__":
    wishme()
    while True:
        res,query =takeCommand()
        
        
        
        if ('time' in query or 'time' in res):
            time()
        elif 'date' in query or 'date' in res:
            date()   
        elif 'offline' in query or 'offline' in res:
            quit()
        elif 'wikipedia' in query or'wiki' in res:
            speak("Searching..")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)
        elif "email" in res or "email" in query :
            try:
                speak("what should i say?")
                content =get_message()
                to="abhinavtb@gmail.com"
                sendEmail(content)
                speak("email send")
            except Exception as e:
                print(e)
                speak("unable to send the email")

        elif "chrome" in query or "chrome" in res:
            speak("what should i search for")
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search =get_message().lower()
            wb.get(chrome_path).open_new_tab(search+'.com')

        elif "music" in res or "song" in query:
            songs_dir="C:/Users/abhin/OneDrive/Desktop/songs" 
            songs =os.listdir(songs_dir)
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
        
        

        

        




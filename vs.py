import pyttsx3  
import speech_recognition as sr  
import datetime
import wikipedia 
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def ask(audio):
    engine.say(audio)
    engine.runAndWait()


def askMe():
    hours = int(datetime.datetime.now().hour)
    if hours>=0 and hours<12:
        ask("Good Morning Sir!")

    elif hours>=12 and hours<18:
        ask("Good Afternoon Sir!")   

    else:
        ask("Good Evening Sir!")  

    ask("I am Your Voice Assistant Sir. Please tell me how may I help you")   

def listener():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query.lower()
    except Exception as e:
        print("Say that again, please...")
        return "None"    

def commands():
     
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
            
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    askMe()
    while True:
     if 1:
        query = commands().lower()

        
        if 'wikipedia' in query:
            ask('Searching Wikipedia...')
            query = listener()
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            ask("According to Wikipedia")
            print(results.encode('utf-8', errors='ignore').decode('utf-8'))
            ask(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")  

        elif 'open teams' in query:
            webbrowser.open("microsoft.com") 

        elif 'open github' in query:
            webbrowser.open("github.com")

        elif 'open linkedin' in query:
            webbrowser.open("linkedin.com")

        elif 'play music' in query:
            webbrowser.open("open.spotify.com")

        elif 'open whatsapp' in query:
            webbrowser.open("whatsapp.com")

        elif 'exit' in query: 
            ask("Exiting the program.")
            break  

         


        
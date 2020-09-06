import pyttsx3
import datetime 
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        speak("Good morning!")
    elif hour >= 12  and hour<18:
        speak("Good afternoon!")
    else:
        speak("Good evening Sir!")    
    speak("\n I am Your Desktop Assistant \n Please tell me how may I help you")

def takeCommand():
    #it takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except Exception as e:
        print("Couldn't recognize....Say that again please...")
        return "None"
    return query

def sendEmail(to , content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('abcdefg@gmail.com','abcdefg')
    server.sendmail('abcdefg@gmail.com',to,content)
    server.quit()

def writeText(voice_text):
    text_dir = 'C:/Users/User1/Desktop/assistant.doc'
    speak("Opening written file")
    a = open(text_dir,'w')
    a.write(voice_text)
    a.close()
    #assistant_text = os.listdir(text_dir)
    os.startfile(text_dir)
    


    
if __name__ == "__main__":
    wishMe()  

    while True:
        query = takeCommand().lower()
        
        # logic for executing tasks based on query

        if 'wikipedia' in query:
            speak("Searching wikipedia.....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences = 2)
            speak("According to wikipedia: ")
            print(results)
            speak(results)

        elif 'open website' in query:
            speak('Tell the name of website')
            a = takeCommand().lower()
            webbrowser.open("https://www.{}.com".format(a)) 

        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com")
            speak("opening youtube")

        elif "open google" in query:
            webbrowser.open("https://www.google.co.in")
            speak("opening google")

        elif ("open whatsapp" or 'whats app') in query:
            webbrowser.open("https://web.whatsapp.com")
            speak("opening whatsapp") 

        elif "open stackoverflow" in query:
            webbrowser.open("https://stackoverflow.com")
            speak("opening stackoverflow")  
        
        elif "play python tutorial" in query:              
            py_dir = 'C:\\Users\\User1\\Desktop\\python' 
            tutorial = os.listdir(py_dir) 
            speak("playing python tutorial") 
            os.startfile(os.path.join(py_dir, tutorial[0])) 

        elif "play breaking bad" in query:             
            py_dir2 = 'C:\\Users\\User1\\Desktop\\breaking bad\\BB SEASON 1' 
            tutorial1 = os.listdir(py_dir2) 
            speak("playing breaking bad") 
            os.startfile(os.path.join(py_dir2, tutorial1[0]))        
        
        elif "the time" in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {strtime} ")
            
        elif "open vscode" in query:     
            code_path = "F:\\Microsoft VS Code\\Code.exe"
            speak("opening vscode")
            os.startfile(code_path)

        elif "open amazon" in query:
            webbrowser.open("https://www.amazon.in")
            speak("opening amazon")    

        elif 'send email' in query:
            try:
                speak("opening ur email\n")
                speak("What should I send?")
                content = takeCommand()
                to = "xyxyxyxyx@gmail.com"
                sendEmail(to , content)
                speak("Email has been sent to xyxyxyxyx!")

            except Exception as e:
                print(e)
                speak("Oops!\nSomething went wrong \n I'm not able to send mail to xyxyxyxyx")
                
        elif ('quit' or 'sleep' or 'close') in query:
            speak("Ok sir have a nice day")
            break 

        elif 'write text' in query:
            speak('Sir\n,PLease tell me What to write in the file')
            voice_text = takeCommand()
            writeText(voice_text)
        


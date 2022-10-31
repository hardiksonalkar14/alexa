import pyttsx3 # to convert text to speech
import speech_recognition as sr  # for speech recognition
import datetime # to get date and time
import wikipedia # for getting information from wikepidia
import webbrowser # # for getting information from google
import os # for opening the code path
import pywhatkit # to play songs 
import pyjokes # for jokes

engine = pyttsx3.init('sapi5') #sapi 5 is to take voices(inbuilt)
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Alex Sir. Please tell me how may I help you")     
    
def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 #second of non-speaking audio before a phrase is considered complete
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak('Opening youtube')
            webbrowser.open("youtube.com")
            
        elif 'open google' in query:
            speak('Opening google')
            webbrowser.open("google.com")

        elif 'open instagram' in query:
            speak('Opening instagram')
            webbrowser.open("instagram.com")
 
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'vs code' in query:
            speak('Opening Vs code')
            codePath = "C:\\Users\\HARDIK SONALKAR\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)    

        elif 'play' in query:
              song = query.replace('play','')
              speak('playing '+song)
              pywhatkit.playonyt(song)

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'are you single' in query:
            speak('I am in a relationship with myself')    

        elif 'hello' in query:
            speak('Hello sir how are you')

        elif 'how are you doing' in query:
            speak('I am doing good! Thanks for asking!')  

        elif 'how are you feeling today' in query:
            speak('I am feeling good, what about you?')  

        elif "goodbye" in query:
            speak("Bye sir. Come Back later on!")
            exit()    

   
              
   

          

        
       
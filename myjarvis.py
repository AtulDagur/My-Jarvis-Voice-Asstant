import datetime
import wikipedia
import pyttsx3
import speech_recognition as sr
import webbrowser

engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices') #getting details of current voice

engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',140)
engine.setProperty("languages",'hi')

def speak(audio):

    engine.say(audio)

    engine.runAndWait()

def wishme():
    hour =int(datetime.datetime.now().hour)
    period=""
    #Good Morning
    #Good Evening
    if hour >= 00 and hour < 12:
        period=("Good Morning")
    if hour >= 12 and hour < 16:
        period=("Good AfterNoon")
    if hour >= 16 and hour < 24:
        period=("Good Evening")
    speak(period)
    speak("I am Bot. What's your name")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")#User query will be printed.

    except Exception as e:
        # print(e)
        print("Say that again please...")   #Say that again will be printed in case of improper voice
        return "None" #None string will be returned
    return query
if __name__=="__main__" :

    speak("Hii")
    wishme()
    while True:
        query=takecommand().lower()

        if 'about' in query:  #if wikipedia found in the query then this block will be executed
            query = query.replace("about", "")
            speak(f'Searching About {query}...')

            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        if 'search' in query:  #if wikipedia found in the query then this block will be executed
            query= query .replace("search", "")
            webbrowser.open(f"https://www.google.com/search?q={query}")
        if 'current time' in query:  #if wikipedia found in the query then this block will be executed
            timec=str(datetime.datetime.now())
            ntime=timec.replace(":"," ")
            speak(timec)

        if 'play' in query:  #if wikipedia found in the query then this block will be executed
            query = query.replace("play", "")
            if(query):
                webbrowser.open(f"https://www.youtube.com/")
            webbrowser.open(f"https://www.youtube.com/search?q={query}")
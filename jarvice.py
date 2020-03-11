import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishME():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak("good morning boss. had u breakfast?")

        elif hour>=12 and hour<=18: 
            speak("good afternoon")

        else:
            speak("good evening") 

        speak("tell me how can help you")

def takeCommand():
    #it takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recogizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")
    except Exception as e:
        #print(e)    
        print("sai that again please")
        return "None"
    return query
if __name__ == "__main__":
    wishME()
    takeCommand()
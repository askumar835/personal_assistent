import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
from boltiot import Bolt
import pyautogui


api_key="XXXXXXXXXXXXXXXXX"
device_id="xxxxxxxxx"
mybolt= Bolt(api_key,device_id)



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()




def wiseMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")


    speak("I am jarvis. please tell me how may I help you")

def takeCommand():

    #It takes microphone input from the user and returns string output

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
         #print(e)
         print("say that again please...")
         return "None"

    return query



if __name__ == '__main__':
    wiseMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            webbrowser.open("https://www.youtube.com/watch?v=_oyDybJiNlQ")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")

        elif 'open pycharm' in query:
            pyPath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.1\\bin\\pycharm64.exe"
            os.startfile(pyPath)

        elif 'led on' in query:
            speak("turning lights on")
            response = mybolt.digitalWrite('0', 'HIGH')


        elif 'led off' in query:
            speak("turning lights off")
            response = mybolt.digitalWrite('0', 'LOW')

        elif 'close' in query:
            pyautogui.press('Alt'+'F4')



        # elif 'switch on the fan' in query:
        #     speak("Fan on")
        #     response = mybolt.digitalWrite('', 'HIGH')
        #
        #
        # elif 'switch off the fan' in query:
        #     speak("fan off")
        #     response = mybolt.digitalWrite('', 'LOW')


        # elif 'ring the bell' in query:
        #     speak("turning Buzzer onn")
        #     response = mybolt.digitalWrite('1', 'HIGH')
        #
        # elif 'switch off the bell' in query:
        #     speak("closing Buzzer")
        #     response = mybolt.digitalWrite('1', 'LOW')

        elif 'temperature' in query:
            response = mybolt.analogRead('A0')
            temp = (int(response[11:14]))//10.34
            speak(f"the Temperature of your room is{temp} degree centigrate ")



















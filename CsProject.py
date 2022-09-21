import datetime
from pyttsx3 import engine
import pyjokes
import pywhatkit
import speech_recognition as freddy
import wikipedia
from serpapi import GoogleSearch

while True:
    def talk(text1):
        engine.say(text1)
        engine.runAndWait()

    def initialization():
        try:
            with freddy.Microphone() as input:
                print("Listening...")
                voice = listener.listen(input)
                text = listener.recognize_google(voice)
                text = text.lower()
                if 'alexa' in text:
                    text = text.replace("alexa", "")
                    talk(text)


        except:
            pass
        return text
    text=initialization()
    print(text)
    if 'play' in text:

        song = text.replace('play', '')
        talk('playing' + song)
        print("Playing", song)
        pywhatkit.playonyt(song)
    elif 'time' in text:
        time = datetime.datetime.now().strftime("%I:%M %p")
        talk("Current time is " + time)
        print(time)
    elif 'search1' in text:
        search = text.replace("search", '')
        info = wikipedia.summary(search, 1)
        print(info)
        talk(info)
    elif 'joke' in text:
        talk(pyjokes.get_joke())
    elif 'search' in text:
        text1 = text.replace("search", '')
        search1 = GoogleSearch({"q": text1, "api_key": "secretkey"})
        result = search1.get_dict()
    else:
        talk("Pls tell the command again")









#commands: play <song name>, search <something>, tell me about <someone>, tell me a joke...
import datetime
import os

try:
    import tkinter
except ImportError:
    os.system('pip install tk')
    import tkinter
try:
    import pyttsx3
except:
    os.system('pip install pyttsx3')
    import pyttsx3
try:
    import pyjokes
except ImportError:
    os.system('pip install pyjokes')
    import pyjokes
try:
    import pywhatkit
except ImportError:
    os.system('pip install pywhatkit')
    import pywhatkit
try:
    import speech_recognition as freddy
except ImportError:
    os.system('pip install speech-recognition-python')
    import speech_recognition as freddy
try:
    import pyaudio
except ImportError:
    os.system('pip install PyAudio')
    import pyaudio
try:
    from neuralintents import GenericAssistant
except ImportError:
    os.system('pip install neuralintents')
    from neuralintents import GenericAssistant
try:
    import nltk
except ImportError:
    os.system('pip install nltk')
    import nltk
import subprocess
import threading
import tkinter
import sys

os.system('python -m nltk.downloader -d /usr/local/share/nltk_data all')
engine = pyttsx3.init()
listener = freddy.Recognizer()
nltk.download('omw-1.4')


def talk(text2):
    global engine
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[1].id)
    engine.say(text2)
    engine.runAndWait()


talk("I'm ready")
engine.runAndWait()


def playing():
    global listener
    done = False
    text1 = ''
    while not done:
        try:
            with freddy.Microphone() as mic:
                listener.adjust_for_ambient_noise(mic)
                voice = listener.listen(mic)
                text = listener.recognize_google(voice)
                for i in text:
                    text1 += i.lower()
            song = text1.replace('play', '')
            talk('playing' + song)
            engine.runAndWait()
            print('playing' + song)
            pywhatkit.playonyt(song)
            done = True
        except freddy.UnknownValueError:
            listener = freddy.Recognizer()
            talk('I did not understand please try again')
            engine.runAndWait()


def time():
    global listener
    done = False
    text1 = ''
    while not done:
        try:
            with freddy.Microphone() as mic:
                listener.adjust_for_ambient_noise(mic)
                voice = listener.listen(mic)
                text = listener.recognize_google(voice)
                for i in text:
                    text1 += i.lower()
            time = datetime.datetime.now().strftime("%I:%M %p")
            talk(time)
            engine.runAndWait()
            print(time)
            done = True
        except freddy.UnknownValueError:
            listener = freddy.Recognizer()
            talk('I did not understand please try again')
            engine.runAndWait()


def wiki():
    global listener
    done = False
    text1 = ''
    while not done:
        try:
            with freddy.Microphone() as mic:
                listener.adjust_for_ambient_noise(mic)
                voice = listener.listen(mic)
                text = listener.recognize_google(voice)
                for i in text:
                    text1 += i.lower()
            wiki = text1.replace("tell me about", '')
            print(pywhatkit.info(wiki, lines=5))
            talk(pywhatkit.info(wiki, lines=5))
            engine.runAndWait()
            done = True
        except freddy.UnknownValueError:
            listener = freddy.Recognizer()
            talk('I did not understand please try again')
            engine.runAndWait()


def joke():
    global listener
    done = False
    text1 = ''
    while not done:
        try:
            with freddy.Microphone() as mic:
                listener.adjust_for_ambient_noise(mic)
                voice = listener.listen(mic)
                text = listener.recognize_google(voice)
                for i in text:
                    text1 += i.lower()
            talk(pyjokes.get_joke())
            engine.runAndWait()
            print(pyjokes.get_joke())
            done = True
        except freddy.UnknownValueError:
            listener = freddy.Recognizer()
            talk('I did not understand please try again')
            engine.runAndWait()


def search():
    global listener
    done = False
    text1 = ''
    while not done:
        try:
            with freddy.Microphone() as mic:
                listener.adjust_for_ambient_noise(mic)
                voice = listener.listen(mic)
                text = listener.recognize_google(voice)
                for i in text:
                    text1 += i.lower()
            text3 = text1.replace("search", '')
            print('Opening Google')
            talk('opening google')
            engine.runAndWait()
            pywhatkit.search(text3)
            done = True
        except freddy.UnknownValueError:
            listener = freddy.Recognizer()
            talk('I did not understand please try again')
            engine.runAndWait()


def open_app():
    global listener
    done = False
    text1 = ''
    while not done:
        try:
            with freddy.Microphone() as mic:
                listener.adjust_for_ambient_noise(mic)
                voice = listener.listen(mic)
                text = listener.recognize_google(voice)
                for i in text:
                    text1 += i.lower()
            open = text1.replace('open', '')
            app = open + '.exe'
            subprocess.call(app)
            done = True
        except freddy.UnknownValueError:
            listener = freddy.Recognizer()
            talk('I did not understand please try again')
            engine.runAndWait()


def hello():
    talk("Hello sir. What can I do for you?")
    engine.runAndWait()


def quit():
    talk("Bye")
    engine.runAndWait()
    sys.exit(0)


mappings = {
    "greeting": hello,
    "goodbye": quit,
    "play": playing,
    "about": wiki,
    "joke": joke,
    "search": search,
    "open": open_app
}
assistant = GenericAssistant("intents.json", intent_methods=mappings)
assistant.train_model()

while True:
    try:
        with freddy.Microphone() as mic:
            text1 = ''
            listener.adjust_for_ambient_noise(mic)
            voice = listener.listen(mic)
            text = listener.recognize_google(voice)
            for i in text:
                text1 += i.lower()
        assistant.request(text)
    except freddy.UnknownValueError:
        listener = freddy.Recognizer()

import datetime
import os
try:
    import pyttsx3
except ImportError:
    os.system('pip install tk')
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

import subprocess
import threading
import tkinter

engine = pyttsx3.init()
listener = freddy.Recognizer()
root = tkinter.Tk()
root.geometry('200x200')

listen = tkinter.Label(root, text='Listening')
listen.pack()


def loop(t=0):
    if t<12:
        listen.configure(text='Listening' + '.' * (t%3 + 1))
        root.after(500, loop, t+1)


loop()


def listening():
    def talk(text2):
        engine.say(text2)
        engine.runAndWait()

    def initialization(listener):
        with freddy.Microphone() as mic:
            voice = listener.listen(mic)
            listener.adjust_for_ambient_noise(mic)
            try:
                text1 = listener.recognize_google(voice)
                text1 = text1.lower()
                if 'alexa' in text1:
                    text1 = text1.replace("alexa", "")
                    talk(text1)
            except freddy.UnknownValueError:
                print('')

        return text1
    wake = 'alexa'
    while True:
        text = initialization(listener)
        talk("I'm Ready")
        if 'play' in text:
            song = text.replace('play', '')
            talk('playing' + song)
            button = tkinter.Label(root,text="Playing"+ song)
            button.pack()
            pywhatkit.playonyt(song)
        elif 'time' in text:
            time = datetime.datetime.now().strftime("%I:%M %p")
            talk("Current time is " + time)
            button1 = tkinter.Label(root,text=time)
            button1.pack()
        elif 'tell me about' in text:
            wiki = text.replace("tell me about", '')
            button2 = tkinter.Label(root,text=pywhatkit.info(wiki, lines=5))
            button2.pack()
            talk(pywhatkit.info(wiki, lines=5))
        elif 'joke' in text:
            talk(pyjokes.get_joke())
            button3 = tkinter.Label(root,text=pyjokes.get_joke())
            button3.pack()
        elif 'search' in text:
            text3 = text.replace("search", '')
            button4 = tkinter.Label(root, text='Opening Google')
            button4.pack()
            pywhatkit.search(text3)
        elif 'open' in text:
            open = text.replace('open','')
            app = open + '.exe'
            subprocess.call(app)
        else:
            talk("Please tell the command again")


listening()


root.mainloop()










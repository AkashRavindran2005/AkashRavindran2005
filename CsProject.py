import datetime
import os
try:
    import pyttsx3
except ImportError:
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
    import requests
except ImportError:
    os.system('pip install requests')
    import requests
try:
    import bs4
except ImportError:
    os.system('pip install bs4')
    import bs4
engine = pyttsx3.init()
listener = freddy.Recognizer()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate', 150)

def talk(text2):
    global engine
    engine.say(text2)
    engine.runAndWait()
talk('How can I help you sir? ')
done = False
while not done:
    try:
        with freddy.Microphone() as mic:
            voice = listener.listen(mic)
            listener.adjust_for_ambient_noise(mic)
            text1 = listener.recognize_google(voice)
            text1 = text1.lower()
            if 'alexa' in text1:
                text1 = text1.replace('alexa','')
                if 'play' in text1:
                    talk('Opening youtube')
                    song = text1.replace('play', '')
                    talk('playing' + song)
                    print("Playing" + song)
                    pywhatkit.playonyt(song)
                elif 'time' in text1:
                    time = datetime.datetime.now().strftime("%I:%M %p")
                    talk("Current time is " + time)
                    print(time)
                elif 'tell me about' in text1:
                    talk('Here you go sir')
                    wiki = text1.replace("tell me about", '')
                    print(pywhatkit.info(wiki, lines=5))
                    talk(pywhatkit.info(wiki, lines=5))
                elif 'joke' in text1:
                    talk('This might be cringy but here you go sir')
                    talk(pyjokes.get_joke())
                    print(pyjokes.get_joke())
                elif 'search' in text1:
                    talk('Opening google')
                    text3 = text1.replace("search", '')
                    print('Opening Google')
                    pywhatkit.search(text3)
                elif 'open' in text1:
                    talk('Here you go sir')
                    open = text1.replace('open', '')
                    print('Opening' + open)
                    os.system(open)
                elif 'news' in text1:
                    url = 'https://www.bbc.com/news'
                    response = requests.get(url)
                    soup = BeautifulSoup(response.text, 'html.parser')
                    headlines = soup.find('body').find_all('h3')
                    for x in headlines:
                        talk(x.text.strip())
                        print(x.text.strip())
                elif 'quit' in text1 or 'bye' in text1:
                    done = True
    except freddy.UnknownValueError:
        listener = freddy.Recognizer()
        talk('I did not understand please try again')

"""
pip install playsound==1.2.2
pip install googlesearch-python
pip install newspaper3k
pip install gtts
pip install SpeechRecognition
pip install pipwin
pipwin install pyaudio
"""

from googlesearch import search
import speech_recognition as sr
from newspaper import Article
from gtts import gTTS
import playsound

r = sr.Recognizer()
wd = 'smart'

TLD = "com"
lang = 'en'
num = 1

def searcher():
    try:
        with sr.Microphone() as source:
            print("listening...\n")
            audio = r.listen(source)

        query = r.recognize_google(audio)
        query = query.lower()
        print(query + "\n")

        if wd in query:
            query = query.replace(wd, "")
            print("Query: " + query)

            for j in search(query, tld=TLD, lang=lang, num=num, stop=num, pause=0):
                URL = j

            print("URL: " + URL + "\n")

            article = Article(URL)
            article.download()

            article.parse()
            text = article.text

            print("Text:\n" + text)

            myobj = gTTS(text=text, lang=lang, slow=False)
            myobj.save("Content.mp3")

            playsound.playsound('Content.mp3', True)

        elif wd not in query:
            print("Please add the Wake-Word while searching!\n")

        else:
            searcher()

    except sr.UnknownValueError:
        print("Couldn't hear anything...\nspeak again!\n\n")
        searcher()

    except AssertionError:
        print("Error! No text in page\n\n")
        searcher()


print("Ready!\n\n")
while True:
    searcher()
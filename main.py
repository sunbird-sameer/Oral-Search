from googlesearch import search
import speech_recognition as sr
from newspaper import Article
from gtts import gTTS
import playsound

r = sr.Recognizer()

TLD = "com"
lang = 'en'
num = 1

with sr.Microphone() as source:
    print("Ready!")
    playsound.playsound('Ready.mp3', True)
    audio = r.listen(source)

query = r.recognize_google(audio)
print(query)

for j in search(query, tld=TLD, lang = lang, num = num, stop = num, pause = 0):
    URL = j

print(URL)

article = Article(URL)
article.download()

article.parse()
text = article.text

print(text)

myobj = gTTS(text=text, lang=lang, slow=False)
myobj.save("Content.mp3")
playsound.playsound('Content.mp3', True)
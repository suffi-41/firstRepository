import json

import requests as re
from win32com.client import Dispatch as dis

def Speak(json):
    speak = dis("SAPI.SpVoice")
    speak.speak(json)

def Request(url):
    request = re.get(url)
    print(request.status_code)
    return request.json()

def save(file , text):
    with open(file, 'w') as f:
        f.write(text)
    f.close()

if __name__ == '__main__':

    url = "https://newsapi.org/v2/everything?q=tesla&from=2023-06-27&sortBy=publishedAt&apiKey=4fb4794aa362497e8103bdcac11096a5"
    text = Request(url)
    print(text)
    #save("index.html", text)


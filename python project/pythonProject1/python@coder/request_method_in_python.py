import requests as req
from win32com.client import Dispatch as disp

def Speak(string):
    speak = disp("SAPI.SpVoice")
    speak.speak(string)

if __name__ == '__main__':
    url = 'https://kandi.openweaver.com/search?q=request%20%20method%20in%20pyhon'
    request = req.get(url)
    print(request.text)
    print(request.request)
    print(request.status_code)
    Speak(request.status_code)

    Speak("Mohammad Sufiyan , thank you so much for created the code! ")

    data = {
        'password': '9598960497@',
        'user name': 'suffii_41'
    }

    post = req.get(url=url, data=data)
    Speak(post.text )
    Speak(post.url)
    Speak(post.status_code)
    print(post.text, post.url)

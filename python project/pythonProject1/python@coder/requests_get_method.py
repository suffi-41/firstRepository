import requests as req
from win32com.client import Dispatch
from abc import ABC,abstractmethod
import json

def Speak(string):
    speak = Dispatch("SAPI.SpVoice")
    speak.speak(string)


def save(file_name, text):
    with open(file_name, 'w', encoding="utf-8" ) as file:
        file.write(text)
    file.close()

    Speak("saved data")


def send_request(url):
    re = req.get(url)
    return re.text

def find_link(string):
    link = string.fineAll('href')
    print(link)


if __name__ == "__main__":
    print('geting the data')
    _url = "https://www.amazon.in/Python-Programming-Beginners-Learn-Fundamentals-ebook/dp/B071JBYPPW/ref=sr_1_4?crid=3UVVD8Q8VVZ3X&keywords=python+book&qid=1688307429&sprefix=python+boo%2Caps%2C414&sr=8-4"
    url = "https://www.amazon.in/Yamaha-2022-MT-03-ABS-Colour-Black/dp/B0BVZNN353/ref=sr_1_1_sspa?brr=1&qid=1688306606&rd=1&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGZfYnJvd3Nl&psc=1"
    text = send_request(url)
    new_text = send_request(_url)
    save('index.html', text)
    save('python_data.html', new_text)
    find_link(text)


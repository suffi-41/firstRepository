import requests
from win32com.client import Dispatch
import json


def Speak(string):
    speak = Dispatch("SAPI.SpVoice")
    speak.speak(string)



if __name__ == '__main__':



 re=requests.get('https://w3schools.com/python/demopage.htm')
 print(re.text)
 print(re.status_code)


 url='https://w3schools.com/python/demopage.htm'
 data = {
    'name':'sufiyan',
    'password':9598960497
 }
 re_post = requests.post(url=url, data=data)
 Speak(re_post.text)
 print(re_post.status_code)
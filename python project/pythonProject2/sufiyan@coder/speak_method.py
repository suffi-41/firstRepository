from win32com.client import Dispatch


def Speak(string):
    speak = Dispatch("SAPI.SpVoice")
    speak.speak(string)



if __name__ == '__main__':

  lis = ['sufiyan', 'arman', 'aman khan', 'papa, I love you so much', 'mummy , I love so much']
  # Speak(name)
  # Speak(str(lis))
  name = input("Enter your name:")

  if name.__eq__('mummy'):
      Speak(name)

  elif name.__eq__("papa"):
      Speak(name)

  else:
      Speak(name)
      Speak("Thank you so much"+name)



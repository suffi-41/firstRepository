from win32com.client import Dispatch as disp


def Speak(string):
    speak = disp("SAPI.SpVoice")
    speak.speak(string)


if __name__ == "__main__":
    name = input("Enter your name:")
    Speak(name)


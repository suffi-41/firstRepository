import time
from functools import reduce
from win32com.client import Dispatch

def first_function(function):
    def second_function():
        print("before executing!")
        function()
        print("after executing!")
    return second_function
@first_function
def third_function():
    print("third function executing now!")

def take_input_from_user(function):
    def new_function():
      name=input("Enter your name:")
      function()
      print(name)
    return new_function

@take_input_from_user
def print_details():
    print("I am sufiyan from varanasi!")

def decorator_function(function):
    def sum_of_function():
        print(3+5)
        function()
    return sum_of_function

@decorator_function
def squre_function():
    print(6*6)

def Speak(name, father_name , mother_name, role):
    speak = Dispatch("SAPI.SpVoice")
    speak.speak(f" My name is {name}, My father name is {father_name}, My mother name is {mother_name}, I am {role}")

if __name__=='__main__':
   squre_function()
   print_details()
   third_function()
   Speak('Mohammad Sufiyan', 'Mohammad Shabbar', 'Shabname khatun', ' programmer')
from abc import ABC , abstractmethod
from win32com.client import Dispatch
from functools import reduce
import time
import random
import math

class Abstract(ABC):
     @abstractmethod
     def print_data(self):
         return 0

     @abstractmethod
     def print_my_data(self):
         return 0



class Employee(Abstract):
    def __init__(self, name, id):
        self.name=name
        self.id=id

    def print_my_data(self):
        return 'mohd sufiyan from varansi!'

    def print_data(self):
        return f"Employee name is:{self.name}, his id is {self.id}"

    def __repr__(self):
        return f"Employee data is ({self.name} ,{self.id})"

    def __str__(self):
        return f"Employee name is:{self.name}, his id is {self.id}"

    def __add__(self, other):
        return self.id + other.id

    def __truediv__(self, other):
        return 567

    @classmethod
    def cunstructure(cls, data):
        return cls(*data.split('-'))

    @staticmethod
    def print_maths_data(angle):
        print(math.sin(angle))
        print(math.cos(angle))
        print(math.tan(angle))


    def Speak_data(self):
        speak=Dispatch("SAPI.SpVoice")
        speak.speak(f"Employee name is {self.name}, His id is {self.id}")

if __name__ == '__main__':
    sufiyan=Employee.cunstructure('Mohd sufiyan-22DPCS041HY')
    aman=Employee.cunstructure('Aman khan-4140')
    print(sufiyan +aman )
    print(sufiyan/aman)
    aman.Speak_data()
    sufiyan.Speak_data()

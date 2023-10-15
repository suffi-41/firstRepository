import math
import time
import random
from functools import reduce
from win32com.client import Dispatch
from abc import ABC, abstractmethod
import requests

class abstract_function(ABC):
    @abstractmethod
    def print_data(self):
        return

    @abstractmethod
    def take_data(self):
        return


class Student(abstract_function):
    def __init__(self, name, id, role):
        self.name = name
        self.id = id
        self.role = role


    def print_data(self):
        return f"Student name is {self.name} , his id is {self.id} and role is {self.role}"

    def take_data(self):
        print('sufiyan')

    def __str__(self):
        return f"Student name is {self.name} , his id is {self.id} and role is {self.role}"

    def __repr__(self):
        return f"{self.name}, {self.id}, {self.role}"

    @classmethod
    def constructor(cls, string):
        return
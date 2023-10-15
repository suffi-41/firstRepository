import time
import random
import math
from abc import ABC, abstractmethod
from functools import reduce

class Abstract:
    @abstractmethod
    def yahoo(self):
        return 0

    @abstractmethod
    def print_data(self):
        return 0


class Yahoo_property(Abstract):
    def __init__(self, first_name, last_name):
        self.first_name=first_name
        self.last_name=last_name

    @property
    def yahoo(self):
        if self.first_name == None or self.last_name == None:
            return f"Yahoo email is invalid , please set if using setter!"

        else:
            return f"{self.first_name}.{self.last_name}@yahoo.com"


    @yahoo.setter
    def yahoo(self, string):
        print("Setting now...")
        name = string.split('@')[0]
        new_name = name.split('.')
        first_name = name[0]
        last_name = name[1]

    @yahoo.deleter
    def yahoo(self):
        print('deleting now...')
        self.first_name = None
        self.last_name = None


    @classmethod
    def constructure(cls, string):
        return cls(*string.split('-'))

    def __str__(self):
        return f"first name is {self.first_name}, last name is {self.last_name}"

    def __repr__(self):
        return f"name is :{self.first_name} {self.last_name}"

    def __add__(self, other):
        return self.first_name + other.last_name

    def __truediv__(self, other):
        return 3450

    def print_data(self):
        print(self.first_name, self.last_name)


if __name__ == '__main__':
    sufiyan = Yahoo_property.constructure('sufiyan-si')
    print(sufiyan.yahoo)
    sufiyan.yahoo='mohdbin.shibban@yahoo.com'
    print(sufiyan.yahoo)
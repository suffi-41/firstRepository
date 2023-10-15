import time
import random
import math
from abc import ABC, abstractmethod
from functools import reduce

class Abstract:
    @abstractmethod
    def email(self):
        return 0

class Empolyee(Abstract):
    def __init__(self,first_name, last_name):
        self.first_name=first_name
        self.last_name=last_name

    def __str__(self):
        return f"Employee first name is {self.first_name}, and last name is {self.last_name}"

    @property
    def email(self):
        if self.first_name == None or self.last_name == None:
            return f"Email is not valid , please set if using setter"

        else:
          return f"{self.first_name}.{self.last_name}@gmail.com"


    @email.setter
    def email(self, string):
        print('sitting now.....')
        name=string.split('@')[0]
        new_name=name.split('.')
        first_name=new_name[0]
        last_name=new_name[1]
        print('Email is set')


    @email.deleter
    def email(self):
        print('deleting now........')
        self.first_name=None
        self.last_name=None
        print('Email is deteled')


    @classmethod
    def constructure(cls, string):
        return cls(*string.split('-'))


if __name__ == '__main__':
    sufiyan=Empolyee.constructure('Mohd-sufiyan')
    aman=Empolyee.constructure('Aman-khan')
    print(aman.email)
    aman.email='Aman.khan@gmail.com'
    print(aman.email)
    del aman.email
    print(aman.email)
    sufiyan.first_name='mohd'
    sufiyan.last_name='sufiyan'
    sufiyan.email='mohdbin.sufiyan@gmail.com'
    print(sufiyan.email)
    del sufiyan.email
    print(sufiyan.email)








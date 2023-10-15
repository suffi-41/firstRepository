import time
import random
from functools import reduce
from abc import ABC,abstractmethod
import math
import Abstract_method_and_class

class Abstract(ABC):
    @abstractmethod
    def print_data(self):
        return 0

    @abstractmethod
    def take_imput(self):
        return 0



class Student(Abstract):
    def __init__(self, name , id , father_name, mother_name):
        self.name=name
        self.id=id
        self.father_name=father_name
        self.mother_name=mother_name

    def take_imput(self):
        opiniun=input("shere your opiniun:")
        print(opiniun)

    def print_data(self):
        print(f"{self.name},{self.id},{self.father_name},{self.mother_name}")

    def __str__(self):
            return f"I am {self.name}, My id is {self.id}, My  father name is {self.father_name}, and mother name is {self.mother_name}"

    def __repr__(self):
        return f"{self.name},{self.id},{self.father_name},{self.mother_name}"

    def __add__(self, other):
        return self.id+other.id

    def __truediv__(self, other):
        return 34

    @classmethod
    def constructor(cls, string):
        return cls(*string.split('-'))

    @classmethod
    def constructor_(cls, string):
        new_data=string.split('-')
        return cls( new_data[0], new_data[1], new_data[2], new_data[3])

    @staticmethod
    def print_details(hody, name):
        print(f"{name},{hody}")


if __name__ == '__main__':

    arman=Student.constructor('sufiyan - 41 - mohd shabbar - shabnam khatun')
    print(arman)
    print(repr(arman))
    print(arman+arman)
    print(arman/arman)
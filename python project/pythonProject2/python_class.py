import time
from functools import reduce
import random

class Student:
    no_of_leave=8


if __name__ == '__main__':

    sufiyan=Student()
    sufiyan.name="sufiyan"
    sufiyan.roll=41
    sufiyan.cgp=9.8
    sufiyan.list=['sufiyan','sufiyan ahmad','junaid','farhan']
    sufiyan.dictionary={
        'java':'java language is very femous language!',
        'python':'python is also very populor language!'
    }
    Student.no_of_leave=40
    print(sufiyan.name,sufiyan.roll,sufiyan.cgp,sufiyan.list)
    print(sufiyan.dictionary,sufiyan.no_of_leave)
    print(Student.no_of_leave)

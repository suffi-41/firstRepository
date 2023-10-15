import time
import json
import random
import requests
import pickle
import python_class
from functools import reduce
from win32com.client import Dispatch as dispatch


class Registrstion_form:
    def __init__(self, name, age, phone_no, email, gander):
        self.name = name
        self.age = age
        self.phone_no = phone_no
        self.email = email
        self.gander = gander

    def __repr__(self):
        return f"Name : {self.name}, Age : {self.age}, Phone no : {self.phone_no}, Email : {self.email}, Gander : {self.gander}, this is a repr"

    def __str__(self):
        return f"Name : {self.name}, Age : {self.age}, Phone no : {self.phone_no}, Email : {self.email}, Gander : {self.gander} this is a str "

    def submit_form(self):
        return f"Thank your for submit this {self.name}"

    def cancel_from(self):
        return f"Form is canceled !"

    @classmethod
    def constructor(cls, string):
        return cls(*string.split("-"))

    @classmethod
    def second_constructor(cls, string):
        new_string = string.split("-")
        return cls(new_string[0], new_string[1], new_string[2], new_string[3], new_string[4])

    @staticmethod
    def satatic_method(name):
        return f"{name}, this is a static method"


    @staticmethod
    def Save(file, data):
        with open(file, "w")as f:
           f.write(data)
        f.close()


class Libarary:
    def __init__(self, name):
        self.book = []
        self.name = name

    def add_book(self, book):
        self.book.append(book)
        print(book +' has been added!')

    def show_book(self):
        for available_book in self.book:
            if available_book == None:
                continue
            else:
                print(available_book)

    def issu_book(self, book):
        for i in range(len(self.book)):
            if self.book[i] is  book:
                print(book + ' has been issued !')
                self.book[i] = None
                return

            elif self.book is  book:
                print(book + " is not available")
                break
    def retrun_book(self, book):
        self.book.append(book)
        print(book + ' has been return!')

class Email:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def email(self):
        if self.first_name is None or self.last_name is None:
            print("Please enter the first name and last name!")
        else:
            return f"{self.first_name}.{self.last_name}@sufiyan.com"

    @email.setter
    def email(self, string):
        print("email is setting...")
        name = string.split('@')[0]
        self.first_name = name.split('.')[0]
        self.last_name = name.split('.')[1]
        print('Email is setted')

    @email.deleter
    def email(self):
        print('Email is deleting...')
        self.first_name = None
        self.last_name = None
        print("Email is deleted successfully!")

    @classmethod
    def constructor(cls, string):
        return cls(*string.split('-'))





if __name__ == '__main__':

    name = '["sufiyan", "rehan", "aman", "faizan"]'
    print(name)
    new_name = json.loads(name)
    print(new_name[3])
    print(new_name)
    name_dumps = json.dumps(new_name)
    print(name_dumps)



    aman = Email.constructor('mohdbin-sufiyan')
    print(aman.email)
    aman.email = 'sufiyan.ahamd@sufiyan.com'
    print(aman.email)
    del aman.email
    print(aman.email)


    sufiyan = Registrstion_form.constructor("sufiyan-17-6307874140-mohdbinsufiyan@gmail.com-male")
    data = str(sufiyan)
    sufiyan.Save("save.txt", data)
    print(sufiyan.submit_form())
    print(sufiyan.satatic_method('rehan'))
    print(sufiyan.cancel_from())

    rehan = Libarary('sufiyan')
    rehan.add_book('Python')
    rehan.add_book('java')
    rehan.add_book("javascript")
    rehan.add_book('css book')
    rehan.show_book()
    rehan.issu_book('Python')
    rehan.issu_book('css book')
    rehan.show_book()
    rehan.retrun_book('python')
    rehan.retrun_book('css book')
    rehan.show_book()







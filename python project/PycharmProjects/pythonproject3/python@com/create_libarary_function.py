from abc import ABC, abstractmethod
from functools import reduce
from win32com.client import Dispatch as dispatch


class Libarary:

    def __init__(self):
        self.libarary = []

    def add_book(self, book):
        self.libarary.append(book)
        print("Book has been added!")

    def show_book(self):
        print('Available book!')
        for available_book in self.libarary:
            if(available_book == None):
              continue

            else:
                print(available_book)

    def issue_book(self, book):
        for index, available_book in enumerate(self.libarary):
            if(available_book[index] == book):
                print('Book has been issued')
                available_book[index] = None
                return

            else:
                print("Book is not available!")

    def return_book(self):
        pass




class Email:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


    @property
    def email(self):
        if(self.first_name == None  and  self.last_name == None):
            print("please enter the first and last name , you have not entered the first and last name!")
        else:
            return f"{self.first_name}.{self.last_name}@gmail.com"

    @email.setter
    def email(self , string):
        email = string.split('@')[0]
        name = email.split('.')
        self.first_name = name[0]
        self.last_name = name[1]

    @email.deleter
    def email(self):
        self.first_name = None
        self.last_name = None

    @classmethod
    def constructor(cls, string):
        return cls(*string.split('-'))

    @staticmethod
    def save(file, email):
        with open('file', 'w')as f:
            f.write(email)
            sufiyan.Speak(f"save {email}")
        f.close()

    @staticmethod
    def Speak(email):
        speak = dispatch('SAPI.SpVoice')
        speak.speak(email)


if __name__ == '__main__':
    sufiyan = Email("mohd", 'sufiyan')
    rehan = Email.constructor('rehan-alam')
    print(rehan.email)
    print(sufiyan.email)
    sufiyan.email = 'sufiyan.ahmad@gmail.com'
    del sufiyan.email
    sufiyan.email = 'mohdbin.sufiyan@gmail.com'
    print(sufiyan.email)
    sufiyan.Speak(sufiyan.email)
    sufiyan.save('save.txt', sufiyan.email)
    rehan.save('save.txt', rehan.email)








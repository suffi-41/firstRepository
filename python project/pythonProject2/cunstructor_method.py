import time
from functools import reduce
import random


class Employee:
    no_of_leave = 8
    name = "sufiyan"

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def print_details(self):
        print(f"Employee name is: {self.name} , Employee salary is :{self.salary} and Employee role is: {self.role}")
        return f"I am {self.name} from varanasi!"

    @classmethod
    def change_leave(cls, new_leave):
        cls.no_of_leave = new_leave

    @classmethod
    def change_name(cls, name):
        cls.name = name


class Employee1:
    def __init__(self, name, hoby, salary):
        self.name = name
        self.hoby = hoby
        self.salary = salary

    def print_data(self):
        return f"Employee name is:{self.name}, his salary is {self.salary}, and role is {self.hoby}"

    @classmethod
    def employee_data(cls, new_string):
        string=new_string.split(",")
        return cls(string[0],int(string[1]),string[2])




if __name__ == '__main__':
  sufiyan = Employee(" sufiyan ", 3456, "Employee worker")
  sufiyan.change_leave(9)
  sufiyan.change_name('rehan')
  details = sufiyan.print_details()
  print(details, sufiyan.name, sufiyan.no_of_leave)

  arman = Employee1.employee_data("sufiyan ,2345 ,programmer")
  print(arman.print_data())
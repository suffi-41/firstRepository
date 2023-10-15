import time
import math
from functools import reduce
import random
import inheritance_method


class Employee:
    __name='mohd sufiyan'
    __id=41

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def print_employee_data(self):
        return f"Employee name is: {self.name}, his id salary: {self.salary}"

    @classmethod
    def cunstructor_value(cls, data):
        new_data=data.split('-')
        return cls(new_data[0], new_data[1])







class Programmer(Employee):
    __employee='Arman'

    def __init__(self, name, salary, programmer_name):
        super().__init__(name,salary)
        self.programmer_name=programmer_name

    def print_programmer_details(self):
        return f"Programmer name is: {self.programmer_name} ,and  employee_name is {self.name} "

    @classmethod
    def programmer_cunstructure_value(cls, programmer_data):
        data=programmer_data.split('-')
        return cls(data[0], data[1], data[2])

class Software_company(Programmer):
    _company_name="pylo"

    def __init__(self, name, salary, programmer_name):
        super().__init__(name, salary, programmer_name)


    @staticmethod
    def print_about_company(name):
        print(name)

    @classmethod
    def constructure_value_Of_company(cls, data):
         new_data=data.split('-')
         return cls(data[0], data[1], data[2])



if __name__ == '__main__':
    sufiyan=Software_company.constructure_value_Of_company('Adnan-4568-mohd sufiyan')
    sufiyan.print_about_company("hell9")
    print(sufiyan.print_programmer_details())
    print(sufiyan.print_employee_data())

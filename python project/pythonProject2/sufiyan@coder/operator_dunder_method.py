import time
import math
import random
from functools import reduce



class Employee:
    def __init__(self, name, salary, role):
        self.name=name
        self.salary=salary
        self.role=role

    def Return_Employee_data(self):
        return f"Employee name is:{self.name}, His salary is {self.name}, and his role is :{self.role}"

    @classmethod
    def cunstructure(cls, data):
        return cls(*data.split('-'))

    def __repr__(self):
        return f"Employee data is :({self.name}, {self.salary}, {self.role})"

    def __str__(self):
        return f"Employee name is:{self.name}, His salary is {self.name}, and his role is :{self.role}"

    def __add__(self, other):
       return self.salary+other.salary

    def __truediv__(self, other):
        return 78400

if __name__ == '__main__':
    sufiyan=Employee.cunstructure('sufiyan-4200000-programmer')
    aman=Employee.cunstructure('aman khan-780000-police officer')
    print(repr(sufiyan),repr(aman))
    print(str(sufiyan),str(aman))
    print(sufiyan+aman)
    print(sufiyan/aman)

from abc import ABC , abstractmethod
from functools import reduce

class abstract(ABC):
    @abstractmethod
    def print_data(self):
        return

    @abstractmethod
    def constructor(self, string):
        return


class Python_class(abstract):

    name = 'sufiyan'

    def __init__(self, name, salary, address):
        self.name = name
        self.salary = salary
        self.address = address

    def print_data(self):
        return f"student name is {self.name}, his salary is {self.salary} , he is belong to {self.address}"


    def __str__(self):
       return f"student name is {self.name}, his salary is {self.salary} , he is belong to {self.address}"

    def __repr__(self):
       return f"{self.name}, {self.salary}, {self.address}"

    @classmethod
    def constructor(cls, string):
        return cls(*string.split('-'))

    @classmethod
    def constructor_method(cls, string):
        new_string = string.split('-')
        return cls(new_string[0], new_string[1], new_string[2])

    @classmethod
    def change_name(cls, new_name):
         cls.name = new_name


    @staticmethod
    def print_my_data(name, hoby):
        return f"{name}, {hoby}"

    def __add__(self, other):
        return self.salary + other.salary

    def __truediv__(self, other):
        return 34


class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __str__(self):
        return f"Employee name is {self.name}, his id is {self.id}"

class Worker(Employee):
    def __init__(self, name, id, worker_name, worker_id):
        super().__init__(name, id)
        self.worker_name = worker_name
        self.worker_id = worker_id

    def __repr__(self):
        return f"worker name is {self.worker_name}, his is id {self.worker_id}"

    @classmethod
    def construtor(cls, string):
        return cls(*string.split('-'))

    @classmethod
    def constructor_method(cls, string):
        value = string.split('-')
        return cls(value[0], value[1], value[2], value[3])

if __name__ == '__main__':

    rehan = Worker.construtor('sufiyan-41-rehan-34')
    print(rehan, repr(rehan))


    sufiyan = Python_class.constructor('sufiyan-2347585-A39/301')
    print(sufiyan)
    print(sufiyan.print_my_data('sufiyan', 'i want to become a software engineering'))
    print(repr(sufiyan))
    print(sufiyan.print_data())
    sufiyan.change_name('rehan')
    print(sufiyan.name)
    print(sufiyan+sufiyan)
    print(sufiyan/sufiyan)


    name = ['sufiyan', 'shibban', 'arman', 'rehan', 'adnan', 'kulsoom']
    number = [3, 5, 64, 3, 54, 34, 33 , 23, 45]

    new_name = list(filter(lambda item: item.endswith('n'), name))
    print(new_name)
    new_number = list(filter(lambda x: x % 2 == 0, number))
    print(new_number)

    m = list(map(lambda x: str(x), number))
    mul = list(map(lambda x: x*x, number))
    print(m, mul)

    red = reduce(lambda x, y: x*y, number)
    print(red)
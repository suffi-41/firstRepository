import cunstructor_method
import inspect

class Employee:
    def __init__(self, name, id):
        self.name=name
        self.id=id

    def print_data(self):
        return f"Employee name is {self.name} ,and his id is {self.id}"


    @classmethod
    def constructure_value_of_employee_class(cls, string):
        new_value=string.split('-')
        return cls(new_value[0], new_value[1])



    @staticmethod
    def print_my_data(string):
        return "Mohd "+string


class Programmer(Employee):
    def __init__(self, name, id, programmer_name, programmer_id):
        super().__init__(name, id)
        self.progarammer_name=programmer_name
        self.programmer_id=programmer_id

    def print_programmer_data(self):
        return f"Programmer name is {self.progarammer_name} ,and programmer id is {self.programmer_id}"

    def print_hello(self, string):
        print("hello",string)

    @classmethod
    def __cotur__(cls, string):
        new_string=string.split('-')
        return cls(new_string[0], new_string[1], new_string[2], new_string[3])




if __name__ == '__main__':
    sufiyan=Programmer.__cotur__("Adnan-42-Sufiyan-41")
    print(sufiyan.print_programmer_data())
    print(sufiyan.print_data())
    print(sufiyan.print_my_data("I am sufiyan from varansi!"))
    sufiyan.print_hello("brother")


    print(inspect.getmembers(sufiyan))
    print(type(sufiyan))
    print(dir(sufiyan))
    print(id(sufiyan))

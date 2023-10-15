import cunstructor_method
import time
import math
from functools import reduce

class Math:
    def __init__(self,angle_of_sin, angle_of_cos, angle_of_tan):
        self.angle_of_sin=angle_of_sin
        self.angle_of_cos=angle_of_cos
        self.angle_of_tan=angle_of_tan

    def value_of_trignomatric(self):
        return f"value od sin30 is {math.sin(int(self.angle_of_sin))} , value of cos30 is:{math.cos(int(self.angle_of_cos))} and value of tan30 is {math.tan(int(self.angle_of_tan))}"


    @classmethod
    def pass_of_angel(cls, angle):
        new_angle=angle.split("-")
        return cls(new_angle[0],new_angle[1],new_angle[2])

    @classmethod
    def second_value_pass_of_angle(cls,angle):
       new_angle=angle.split("-")
       return cls(new_angle[0], new_angle[1], new_angle[2])

    @staticmethod
    def print_string(string):
        print(string)


if __name__ == '__main__':

    sufiyan = Math.second_value_pass_of_angle("30-30-30")
    print(sufiyan.value_of_trignomatric())
    print(sufiyan.print_string("sufiyan"))

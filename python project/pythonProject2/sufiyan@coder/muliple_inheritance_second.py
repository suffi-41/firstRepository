import multiple_inheritance_method


class A:
    def print_a(self):
        print("class A!")

class B(A):
    def print_b(self):
        print("class B!")

class C(A):
    def print_c(self):
        print("class C")

class D(B,C):
    def print_d(self):
        print("class D")

if __name__ == '__main__':
    sufiyan=D()
    sufiyan.print_a()
    sufiyan.print_c()
    sufiyan.print_b()
    sufiyan.print_d()


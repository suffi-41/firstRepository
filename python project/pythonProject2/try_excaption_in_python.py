import time



if __name__=='__main__':
    first_num=int(input("Enter the first number:"))
    second_num=int(input("Enter the second number:"))
    try:
       print("The sum of two number:",first_num+second_num)
       divide=first_num/second_num

    except ArithmeticError as e:
        print(e)
        print("we failled of division!")
    except Exception as except1:
        print(except1)

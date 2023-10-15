import time

def recusion(n):
    if n==0 or n==1:
        return 1

    else:
      return n*recusion(n-1)

def recusion_sum(n):
    if n==0 or n==1:
        return n
    else:
        return n+recusion_sum(n-1)

def fibinachu(n):

    if n==0 or n==1:
        return n

    else:
        num=fibinachu(n-1)+fibinachu(n-2)
        return num


def itreter_sum(n):
    sum=0
    for i in range(n):
        sum+=i
    return sum


if __name__ == '__main__':
    print(recusion(4))
    print(recusion_sum(10))
    print(itreter_sum(11))
    for i in range(10):
     print(fibinachu(i))

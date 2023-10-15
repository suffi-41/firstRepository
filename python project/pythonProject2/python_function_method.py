import time

def sum():
    """ hello brother ,I am sufiyan from varansi"""
    return 3+5

def list_name(lis):
    sum=0
    for item in range(len(lis)):
        sum+=lis[item]
        """Return of sum of ilst item"""
    return sum

if __name__== '__main__':
    print(sum())
    print(sum.__doc__)
    lis1=[]
    for i in range(3):
     item=int(input("Enter the multiple number:"))
     lis1.append(item)
    print(list_name(lis1),list_name.__doc__)


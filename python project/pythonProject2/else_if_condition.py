import time


if __name__=='__main__':
 lis=['sufiyan',"arman","aman khan"]
 name=input("Enter your name:")
 if name in lis:
    print("It's present in list !")

 elif name not in lis:
     print("it's not present in list!")

 else:
     print("thank you!")

 lis1=[1,2,3,4,5,67,89,65,54,3,4,3,0,7,4,2,2,1,5]
 bool=False
 item=int(input("Enter the number:"))
 if item in lis1:
     print("It's present!")

 elif item  not in lis1:
     print(item," It's not present!")

 print(lis1)

 dis={
     'sufiyan':'I want to become a programmer!',
     'rehan':'He want to become hafiz! ',
     'farhan':'he want to become computer engineering!',
     'sufiyan ahmad':'he want to become codder!'
 }
 new_name=input("Enter your name:")
 print(dis.get(new_name))
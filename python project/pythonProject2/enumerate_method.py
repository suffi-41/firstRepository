import time

if __name__=='__main__':
    l=['aloo','tamato','patato','pees']
    number=[6,3,4,5,6,7,3,2,8,64,3,21,23,56,22,56]

    i=0
    for item in l:
        if i%2==0:
          print(f"second item is:{item}")

        i+=1


    for index,item in enumerate(l):
        if index%2==0:
          print(f"second item is:{item}")
        else:
            print(f"{item}")

    for position,item in enumerate(number):
        if position%3==0:
            print(f"{item}")

        elif position%2!=0:
            print(f"{item}")

    for index,item in enumerate(number):
        if index%2==0:
            continue
        elif index%3==0:
             item*item
        else:
            print(item)
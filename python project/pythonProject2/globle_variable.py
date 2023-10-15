import time

g=4 #globl variable
name="sufiyan" #Global variable

def number():
    l=7 #local variable
    global g
    global name
    name+=" ahmad"
    g+=l  #change of the value of global variable

    print(g,name) #print the global  value
    print(l)  #print the local value
if __name__=='__main__':
    number()
    print(g,name)



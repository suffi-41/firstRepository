import time
#write mmode
f=open("python.txt","w")
f.write("helllo ")
f.write("hididd ")
f.write("I am sufiyan from varanasi\n")
f.close()
#append mode
f=open("python.txt","a")
f.write("Hi brother, How are you/n")
f.write("I am a progarammer!/n")
f.close()

#read mode
f=open("python.txt","r")
print(f.readline())
f.close()

#read mode
f=open("python.txt")
print(f.read())
f.close()
#read mode
f=open("python.txt","r")
print(f.readline())
f.close()

#read mode and write mode
f=open("python.txt","r+")
print(f.readline())
f.write("Thank you!\n")
f.close()




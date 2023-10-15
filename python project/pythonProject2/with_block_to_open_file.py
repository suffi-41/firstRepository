import time

with open("sufiyan.txt","r+")as f:
 for i in range(10):
  f.write("Hello ,I am sufiyan from varanasi!\n")
 f.tell()
 f.seek(8)
 print(f.readline())
f.close()

with open("python.txt","r+")as f:
    print(f.readline())
f.close()

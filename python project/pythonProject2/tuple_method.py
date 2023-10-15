import time

time=time.asctime(time.localtime(time.time()))
str(time);
print(time)

tupl=("sufiyan",'arman','rehan','aman khan')
print(type(tupl),tupl)
print(tupl[0])
print(tupl.count('sufiyan'))
print(tupl[0].__eq__('sufiyan'))

import time

t=time.localtime(time.time())
time=time.asctime(t)
print(time)

lis=['sufiyan','arman','rehan','kashfi','aman khan']
print(lis[0])
print(lis[:5]);
print(lis[::-1])
print(lis[-6:-1])
print(lis.index('sufiyan'))
lis[0]="shibban"
lis.insert(2,"mummy")
lis.append("papa")
new_name=lis.copy()
print(new_name)
lis.remove('arman')
lis.clear()
print(lis)
print(type(lis))
print(new_name)
print(len(new_name))
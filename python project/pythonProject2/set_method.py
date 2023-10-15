import time
time=time.asctime(time.localtime(time.time()))



if __name__=='__main__':
    print(time)

s={1,2,3,4,2,4,3,}
s.add(4)
s.add(100)
s.remove(100)
print(len(s),max(s),min(s))
print(s,type(s))

lis=['name','name','name','papa','mummy']
se=set(lis)
print(se)

sd=s.union({1,2,3,4,6,})
print(sd)
sd=s.intersection({1,2,3,})
print(sd)
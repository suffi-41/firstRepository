import time

def squre_function(x):
    return x*x

def qube_function(x):
    return x*x*x


if __name__=='__main__':
 #map method using here
 #what is map ,map is python method which is using the updating of data ,for examle!
 string_list=["2","5","7","9"]
 print(string_list)
 change_int_list=list(map(lambda x:int(x),string_list))
 print(change_int_list)
 lis=[2,5,7,3,5,0,57,9]
 new_list=list(map(lambda x:x*x,lis))
 print(new_list)
 print(lis)

 string=["sufiyan","aman khan","rehan"]

 string=list(map(lambda name:"Mohd "+name, string))
 print(string)

 func=[squre_function,qube_function]

 for number in range(100):
  value=list(map(lambda x:x(number),func))
  print(value)



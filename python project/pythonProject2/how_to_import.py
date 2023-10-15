import python_function_method
import globle_variable
import time

if __name__=='__main__':
 time.asctime(time.localtime(time.time()))
 lis=[1,4,6,7,9]
 print(python_function_method.sum())
 sum=python_function_method.list_name(lis)
 print(sum)
 print(time)
 globle_variable.number()
 name=['sufiyan','farhan','rehan']
 new_name=' and'.join(name)
 print(new_name)

 for index,item in enumerate(lis):
    if index%2==0:
       print(item)
       print("Thanks!")
import time
import map_filter_reduce_method
import filter_method
from functools import reduce


if __name__=='__main__':
 list_number=[21,8,8,49,4,8,4,8,4,8,1,8]
 name=['sufiyan ','adnan',' farhan', 'shibban']
 sm_of_array=reduce(lambda x,y:x+y,list_number)
 print(sm_of_array)
 number=reduce(lambda x,y:x*y ,list_number)
 print(number)

 string_name=reduce(lambda first_name, next_name: first_name+next_name,name)
 print(string_name)
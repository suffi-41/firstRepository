import time
import map_filter_reduce_method

if __name__=='__main__':
 name_list=['sufiyan','shibban','shabber','adnan','aman khhan']
 number_list=[23,45,78,89,45,75,564,445,3,4,53,34,3,43,33]
 name_=list(filter(lambda item:item.endswith('n'),name_list))
 print(name_)
 new_name=list(filter(lambda nam:nam.startswith('s'),name_list))
 print(new_name)

 new_number_list=list(filter(lambda x:x%3!=0,number_list))
 print(new_number_list)
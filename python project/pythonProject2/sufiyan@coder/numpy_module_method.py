import numpy as np
from win32com.client import Dispatch as dp
import json as js

def Speak(string):
    speak = dp("SAPI.SpVoice")
    speak.speak(string)



if __name__ == '__main__':
 name = np.array(['sufiyan', 'farhan' , 'junaid', 'rehan', 'shibban' , ' adnan'])
 names = np.array([[1, 2, 3, 4, 5, 4], [ 2, 3, 4, 57, 7, 5]])
 print(names[0:2])
 print(names, names.ndim)
 print(name)
 list = np.array([2,3,5,6,7,8,8])
 print(name, list)
 print(name[:])
 print(name[2:4], name[:-1])
 name[0]= "mohammdsufiyan"
 print(name)
 x=name.copy() # copy fuction use here, name data is copy in x variable
 print(x)
 print(x[0])
 print(name.shape) # shape method is define the numpy array shape

 print(names.shape)
 print(name.reshape(3,2)) # reshape method is change the numpy array shape, but it's not chage the original numpy array
 print(name)

 new_arr=np.array_split([3,4,5,7,5,2,1,1,46,76,67,9,7], 5)
 print(new_arr)
 print(np.array_split(name, 3))

 print(np.concatenate((list, list)))
 join = np.concatenate((list, list ))

 for x in list:
  print(x)

 for  odd in list:
  if odd %2 != 0:
   print('odd number in list ', odd)
  else:
   print('Even number', odd)

 for index , item in enumerate(list):
    if index% 2!= 0:
     print( 'even number' ,item)

    elif index %3 != 0:
     print(item)

    else:
     print(item)


 search = np.array([3,4,5,67,8,989,54,3,3,3]) # search method use here
 new_numpy = np.where(search == 53)
 print(new_numpy)

 print(np.short(list)) # short method ude here

 print("filter method")
 new_list =np.array ([2, 3, 5, 41 ,46, 75])
 filter_arr=[True, False, True, False, True, False]  #filter method is used here!

 print(new_list[filter_arr])

 print('new filter')
 filter_arr=np.array([2, 3, 4,  5, 6, 7, 87, 9, 44, 32, 56])
 filter = []

 for x in filter_arr:
  if x%2 == 0:
   print('Even index!')
   filter.append(True)

  else:
   print('Odd index!')
   filter.append(False)
 new_filter = filter_arr[filter]
 print(new_filter)





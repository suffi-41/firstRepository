import json
from win32com.client import Dispatch
from functools import reduce
import time
import math
import pickle
from abc import ABC, abstractmethod



lis='["name" ,"rool" ,"est"]' # this is a json string ,json.laods methis is used to convert json string to python object
print(lis)
print(lis[2])
new_json = json.loads(lis)
print(new_json)
print(type(new_json))
print(new_json[2])        # this is converted python object



#json.load => method is used to read the file

name={                     # it's python object
    "name":"sufiyan",
    "roll":"22DPCS041HY",
    "enrolment_no":"A221070"
}

new_name = json.dumps(name) # json.dumps is used to convert python object to json
print(new_name)
print(type(new_name)) # it's json string



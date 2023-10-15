import numpy
import numpy as np
import requests
import json
import time
import random
import pickle
from functools import reduce
from win32com.client import Dispatch as dp
from abc import ABC , abstractmethod
import math

if __name__ == '__main__':
    list = np.array([34,56,23,56,34])
    print(type(list))
    name = list.copy()
    split = np.array_split(list, 3)
    concatenate = np.concatenate((list, list))
    shape = list.shape


    print(name, split, concatenate, shape)

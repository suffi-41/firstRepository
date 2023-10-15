

import numpy as np
import json as js
from win32com.client import Dispatch as dp
from functools import reduce


if __name__ == '__main__':
    filter_list=np.array([2,3,45,34,67,89,56,5])
    filter_string=np.array(['sufiyan', 'shibban', 'shabbar', 'adnam', 'aman khan'])
    filter = []
    second_filter = []

    for i in filter_string:
        if str(i).startswith('s'):
            filter.append(True)
        else:
            filter.append(False)

    new_filter_string=filter_string[filter]
    print(new_filter_string)

    for x in filter_list:
        if x ==x%2 == 0:
            second_filter.append(True)

        elif x < x == x%10 == 0:
            second_filter.append(False)

        elif x >= x+x%1 == x%3 == 0:
            second_filter.append(False)

    new_filter_list = filter_list[second_filter]
    print(new_filter_list)
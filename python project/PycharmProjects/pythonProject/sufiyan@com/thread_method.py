import time
import threading
from concurrent.futures import ThreadPoolExecutor


def function(second):
    print(f'function is sleeping for {second} second')
    time.sleep(second)
    print(f'function is run')


def concurrentFiture():
    with ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(function, 4)
        print(future.result())

        future = executor.submit(function, 3)
        print(future.result())

        future = executor.submit(function, 1)
        print(future.result())

concurrentFiture()

def poolDemo():
    with ThreadPoolExecutor() as executer:
        lis = [2,3,4,5,6,2,1,1]
        results = executer.map(function, lis )
        for result in results:
            print(result)




# function(4)
# function(2)
# function(1)

t1 = threading.Thread(target=function, args=[3])
t2 = threading.Thread(target=function, args=[2])
t3 = threading.Thread(target=function, args=[1])

t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
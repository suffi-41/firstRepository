import time

x = lambda x, y: x+y

print_array=lambda name:print(name)

def first(s):
    return s[1]

if __name__=='__main__':
    print_array("sufiyan")

    a=[ [2,3],[3,6],[4,5]]
    a.sort(key=lambda x:x[1])
    print(a)
    a.sort(key=first)
    print(a)



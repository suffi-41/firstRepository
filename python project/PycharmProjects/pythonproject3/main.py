name = 'sufiya n'
print(len(name))
print(name.lower())
print(name.upper())
print(name.startswith("s"))
print(name.endswith("yan"))
print(name.count("0"))
print(name.capitalize())
print(name.isupper())
print(name.split(' '))
print(name[3:4])
print(name[:])
print(name[::-1])
print(name[0:4:-1])

li = ['sufiyan', 'rehan', 'shibban', 'adnan', 'kulsoom']
print(li)
print(len(li))
print(li[2:4])
li.reverse()

li.append('sufiyan amna')
li.pop()
li.insert(2, 'amna')
print(li)

new_list = [3, 5, 6, 5, 6, 2, 4, 5]
for index, item in enumerate(new_list):
    if index %2 ==0:
        print(item, "item")





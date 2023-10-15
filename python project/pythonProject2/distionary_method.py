import time
time=time.asctime(time.localtime(time.time()))

roll_no={
    'rehan':41,
    'sufiyan':31,
    'shibban':78,
     'papa':{ 'name':'shabbar', 'brother':3, 'sister':3},
     'mummy':{
         'name':"shabnam khatun", 'charectare':"my mummy"
     }
}
print(roll_no)
roll_no['rehan']='papa'
print(roll_no['rehan'])
print(roll_no['papa']['name'])
print(roll_no['mummy']['name'])
roll_no.update({"sufiyan":5})
print(roll_no.get("sufiyan"))
print(roll_no.items())
print(roll_no.keys())
print(roll_no.__len__())
print(roll_no.values())

print(roll_no)

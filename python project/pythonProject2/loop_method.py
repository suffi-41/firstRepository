import time


if __name__=='__main__':
    name=['sufiyan','sufiyan ahmad','farhan','junaid','rehan']
    item=0
    for item in range(len(name)):
        print(name[item])
        item+=1

    lis=[['name','sufiyab'],['roll','22dpcs041hy'],['Enrollment no','A221070']]
    for item,v in lis:
      print(item,v)

    i=0
    while i<10:
     print(i)
     if i==5 or i==6 or i==7:
      break
     i+=1

    list_roll_no=[1,2,3,4,5,6,7,8,9,10]
    for x in list_roll_no:
     if x==3 or x==5 or x==8:
       print('roll No',x, 'not present!')
       continue
     print(x)

    print('hello')if 2==3 else print('goodbye!')


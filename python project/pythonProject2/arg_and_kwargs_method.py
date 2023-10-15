import time

def function_args_kwargs(normal, *args, **kwargs):
    print(normal)
    for item in args:
        print(item)

    for key ,value in kwargs.items():
      print(f"{key} and {value}")

def second_function_args_kwargs(dis,*lis,**diss) :
    for item in dis:
        print(dis)
    sum=0
    for number in range(len(lis)):
        sum+=number
    print(f"sum is {sum} of list")

    for key ,value in diss.items():
        print(f"{key} {value}")



if __name__=='__main__':
    string="I am sufiyan from varanasi!"

    list=["sufiyan","amna khan","Rehan","papa","mummy"]

    dis={
        "name":"sufiyan",
        "roll no":"22DPCS041HY"
    }

    function_args_kwargs(string,*list,**dis)

    dis_number={
        2: 4,
        4: 7,
        5: 5

    }
    lis_number=[2, 3, 4, 6, 8]
    dis_kwargs={
        "java":"System.out.println()",
        "python":"print()",
        "javascript":"console.log()"
    }

    second_function_args_kwargs(dis_number,*lis_number,**dis_kwargs)

    initial_time=time.time()
    i=0
    while i<=10:
        print(i)
        i+=1

    while_loop_time=time.time()-initial_time
    print(while_loop_time)
    time.sleep(2)
    second_intial_time=time.time()

    for i in range(11):
        print(i)
    for_loop_time=time.time()-second_intial_time
    print(for_loop_time)

    if while_loop_time > for_loop_time:
        print("while loop time is more ")
    elif while_loop_time==for_loop_time:
        print("both loop time is equal!")

    else:
        print("for loop time is more")


import asyncio
import time
import requests

async def function1():
    await asyncio.sleep(2)
    print('function1')

async def function2():
    await asyncio.sleep(1)
    print("function2")

async def function3():
    await asyncio.sleep(3)
    print("function3")

# async def main():
#     task = asyncio.create_task(function1())
#     # await function1()
#     await function2()
#     await function3()

async def main():
    new_functiom = await asyncio.gather(
        function1(),
        function2(),
        function3()
    )
    print(new_functiom)

asyncio.run(main())


async def Download():
    url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-fff2lftqIE077pFAKU1Mhbcj8YFvBbMvpA&usqp=CAU"
    response = requests.get(url)
    open("image.jpg", "wb").write(response.content)


async def main1():
    task = asyncio.gather(Download())

asyncio.run(main1())




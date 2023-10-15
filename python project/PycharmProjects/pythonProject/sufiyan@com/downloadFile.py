import asyncio
import requests
import time
import random
from win32com.client import Dispatch as dis
from functools import reduce
from abc import ABC, abstractmethod
import async_function

async def DownloadFirst(url):
    responce = requests.get(url)
    open('downloadFirstImage.jpg', "wb").write(responce.content)
    return f'FirstFile is downloaded!'

async def DownloadSecond(url):
    responce = requests.get(url)
    open("DownloadSecondImage.jpg", 'wb').write(responce.content)
    return f'SecondFile is downloaded!'

async def DownloadThird(url):
    responce = requests.get(url)
    open("DownloadThirdImage.jpg", 'wb').write(responce.content)
    return f"ThirdFile is downloaded!"

async def main(url1, url2, url3):
    download = asyncio.gather(
        DownloadFirst(url1),
        DownloadSecond(url2),
        DownloadThird(url3)
    )
    print(download)

async def async_function():
    print('first function is running...')



async def async_function_second():
    print('Second function is running...')



async def async_function_third():
    print('Third function is running...')




# async def main1():
#    await  async_function()
#    await  async_function_second()
#    await  async_function_third()

async def main1():
    let = asyncio.gather(
        async_function(),
        async_function_second(),
        async_function_third()
    )
    print(let)
    # task = asyncio.create_task(async_function())
    # await async_function_second()
    # await async_function_third()



if __name__ == '__main__':
    url1 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTUV81C4dx_7ItbSlobhs9D7liWFSTR6eZXOg&usqp=CAU"
    url2 = "https://images.pexels.com/photos/265152/pexels-photo-265152.jpeg?cs=srgb&dl=pexels-pixabay-265152.jpg&fm=jpg"
    url3 = "https://www.techquintal.com/wp-content/uploads/2021/05/Information-Technology.jpg"
    asyncio.run((main(url1, url2, url3)))
    asyncio.run(main1())
